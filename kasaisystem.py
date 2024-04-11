import RPi.GPIO as GPIO
import time
import board
import adafruit_dht
import paho.mqtt.client as mqtt
import json
from datetime import datetime
import pytz
import boto3

# AWS SNS 設定
sns_region = 'ap-northeast-1'  # SNS リージョン設定
sns_topic_arn = 'SNSトピックARNをここに入力'  # SNS トピックARN設定

sns_client = boto3.client('sns', region_name=sns_region)  # SNSクライアント初期化

# 日本のタイムゾーン設定
japan_timezone = pytz.timezone('Asia/Tokyo')

def get_japan_time():
    # 現在の日本時間を取得する関数
    japan_time = datetime.now(japan_timezone)
    return japan_time.strftime('%Y-%m-%d %H:%M:%S')

# AWS IoT 証明書ファイルのパス
root_ca_path = "rootCA.pem" #セキュリティ上の理由により任意設定
certificate_path = "/certificate.pem.crt" #セキュリティ上の理由により任意設定
private_key_path = "/private.pem.key" #セキュリティ上の理由により任意設定

# AWS IoT 設定
mqtt_endpoint = ".iot.ap-northeast-1.amazonaws.com"  #セキュリティ上の理由により任意設定
client_id = "iotconsole"  #セキュリティ上の理由により任意設定
topic = "kasai3"  #

# MQTTクライアントの初期化と設定
mqtt_client = mqtt.Client(client_id)
mqtt_client.tls_set(root_ca_path, certfile=certificate_path, keyfile=private_key_path)
mqtt_client.connect(mqtt_endpoint, 8883)

# GPIOピン番号と設定
green_led_pin = 23
red_led_pin = 24
flame_sensor_pin = 17
buzzer_pin = 18
dht_pin = board.D22
servo_pin = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.setup(flame_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(servo_pin, GPIO.OUT)

# DHT11センサーの初期化
dht_sensor = adafruit_dht.DHT11(dht_pin)

# ブザーとサーボモーターの初期化
buzzer_pwm = GPIO.PWM(buzzer_pin, 1000)
buzzer_pwm.start(0)
servo_pwm = GPIO.PWM(servo_pin, 50)
servo_pwm.start(0)

def move_servo(angle):
    # サーボモーターを動かす関数
    duty_cycle = (angle / 18) + 2
    servo_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)
    servo_pwm.ChangeDutyCycle(0)

def publish_sensor_data(temperature, humidity, flame_status):
    # センサーデータをAWS IoTに発行する関数
    payload = {
        "temperature": temperature,
        "humidity": humidity,
        "flame": flame_status,
        "timestamp": get_japan_time()
    }
    mqtt_client.publish(topic, json.dumps(payload))

try:
    while True:
        try:
            temperature_celsius = dht_sensor.temperature
            humidity_percent = dht_sensor.humidity
        except RuntimeError as error:
            print("DHT11 エラー: ", error)
            continue

        flame_status = GPIO.input(flame_sensor_pin)
        current_time = get_japan_time()
        print(f"温度: {temperature_celsius}°C, 湿度: {humidity_percent}%, 炎: {flame_status}, 時間: {current_time}")

        publish_sensor_data(temperature_celsius, humidity_percent, flame_status)

        if flame_status == GPIO.HIGH:
            GPIO.output(green_led_pin, GPIO.LOW)
            GPIO.output(red_led_pin, GPIO.HIGH)
            move_servo(90)
            for _ in range(5):
                buzzer_pwm.ChangeFrequency(600)
                buzzer_pwm.ChangeDutyCycle(50)
                time.sleep(0.2)
                buzzer_pwm.ChangeFrequency(1000)
                buzzer_pwm.ChangeDutyCycle(50)
                time.sleep(0.2)

            #SMS転送    
            message = f"火災が検知されました🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥"
            sns_client.publish(
                TopicArn=sns_topic_arn, #セキュリティ上の理由により任意設定
                Message=message,
                Subject="火災検知"
            )
        else:
            GPIO.output(green_led_pin, GPIO.HIGH)
            GPIO.output(red_led_pin, GPIO.LOW)
            buzzer_pwm.ChangeDutyCycle(0)
            move_servo(0)

        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    mqtt_client.disconnect()
