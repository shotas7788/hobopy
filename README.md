# hobopy
hobopy

# 概要
ほぼPythonだけでサーバーレスアプリをつくろう (技術の泉シリーズ（NextPublishing）)に沿って作成したToDoアプリです。
Python3.7.4, バックエンド：chalice, フロントエンド：transcryptにより作成しております。
本番環境はバックエンド：APIgateway, Lambda, DynamoDB、フロントエンド：S3により稼働しており、
バックエンド、フロントエンドそれぞれ、CodepipelineによるCICDを構築しており、
CodecommitへコミットされたコードがCodebuildによりビルドされステージング環境へデプロイされる仕組みとなっております。
現在、pytestによるテストを実装中です。

# 本番環境
http://hobopy-frontend-ss-20200420.s3-website-ap-northeast-1.amazonaws.com/
