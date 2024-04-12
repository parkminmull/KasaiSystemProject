# 🔥火災検知システム
就職作品プレゼンテーション<br>
<img width="1036" alt="スクリーンショット 2024-04-12 21 25 25" src="https://github.com/parkminmull/KasaiSystemProject/assets/114851426/ceb693f8-741a-424a-a62d-db5e147e7853"><br>


Raspberry pi,AWSを活用した火災検知システム


## 概要動画

[![Video Label](http://img.youtube.com/vi/odktV89QTxg/0.jpg)](https://youtu.be/odktV89QTxg)<br>
↑クリックしてください！

## 🙋🏼自己紹介

• 作品番号: 東京PI007<br>
• 学校: HAL東京 情報処理学科 2年生<br>
• 氏名: PARK SEWON(パク セウォン)<br>
• 希望業界: IT業界<br>

## 1. プロジェクトの概要

• このプロジェクトは、炎センサーを用いた火災検知システムであり、リアルタイムでの火災通知 とデータ管理をAWSサービスを通じて実現します。<br>
• システムは自動的に火災を検知すると同時に、赤いランプが点灯し、ブザーが鳴ります。 • さらに、非常口の役割を果たすサーボモーターが動作し、迅速な避難を支援します。<br>
• 関連するデータはAWS IoT CoreとLambda関数を介してDynamoDBに保存され、火災の詳細な 記録と分析が可能になります。<br>


## 2. システムの機能

• 炎センサーによる火災検知<br>
• ブザーと非常灯による現場での警報<br>
• サーボモーターによる非常口の操作<br>
• AWS SNSを通じたユーザーへの緊急通知<br>
• 温度、湿度、火災検知データのリアルタイム収集とAWS DynamoDBへの保存<br>


## 3. 技術スタック

• Raspberry Pi<br>
• Python<br>
• AWS IoT Core, DynamoDB, SNS<br>


## 4. ラズベリーパイの回路図と使用モジュールの紹介
<img width="1596" alt="raspberrypi" src="https://github.com/parkminmull/kasaisystemproject/assets/114851426/86bbdc4d-9725-4fdb-a635-c0ce880ac498"><br>
1.炎センサー (ky-026):火災を検知するセンサーです。炎や高温を検知すると、 Raspberry Piに信号を送信します。<br>
2.Adafruit DHT11センサー:温度と湿度を測定するセンサーです。このデータは環境モニ タリングや火災状況の分析に使用されます。<br>
3.サーボモーター (sgー90):精密な位置制御が可能なモーターです。非常口の操作や他の 機械的な動作に使用されます。<br>
4.ブザー (Buzzer):警報を発する装置です。火災が検知されると、音で周囲に警告を発します。<br>


## 5. AWSクラウドサービスのアーキテクチャの説明
![Cloud-Architecture](https://github.com/parkminmull/kasaisystemproject/assets/114851426/a52b6a69-fef5-432a-8d3b-4bc71a9f3d3c)
このプロジェクトでは、AWSのクラウドアーキテクチャを活用して、リアルタイムでの 火災検知とデータ管理を実現しています。主な構成要素は以下の通りです。<br>
1. AWS IoT Core: ラズベリーパイからのセンサーデータを受け取り、処理するための 中核的なサービスです。炎センサーからのデータがこのプラットフォームを通じてリア ルタイムで処理されます。<br>
2. AWS Lambda: センサーデータを受け取った後のロジックを実行するためのサービスで す。Lambda関数は、データを加工し、DynamoDBに保存するプロセスを自動的に行い ます。<br>
3. Amazon DynamoDB: 収集されたセンサーデータ(温度、湿度、炎の検知データなど) を保存するためのNoSQLデータベースサービスです。高速でスケーラブルなデータベー スにより、大量のデータを効率的に管理できます。<br>
4. Amazon SNS (Simple Notification Service): 火災発生時にユーザーの携帯電話に 緊急通知を送るためのサービスです。リアルタイムでの警報配信が可能です。<br>


## 6. AWSクラウドサービスのアーキテクチャの説明
AWS でのリアルタイムデータのモニタリングと携帯SMS通知<br>
![실행화면](https://github.com/parkminmull/kasaisystemproject/assets/114851426/9df8ba34-7c02-423a-a740-81c2f237fa86)


## 7. 将来の展望

• API Gatewayを利用したリアルタイムAPIの開発<br>
• AWS EC2を用いたウェブアプリケーションでのデータモニタリングと警報<br>

## 結論

このプロジェクトは、<br>
クラウド技術とIoTデバイスを組み合わせることで、より迅速で効果的な火災対策を提供します。<br>
今後は、このシステムのデータを活用してさらなるアプリケーション開発を目指します。<br>


### 🎯 成果
- 本就職作品プレゼンテーションを通じて、複数の企業から声かけをいただきました。


