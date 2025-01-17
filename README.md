# FastAPIの環境構築
- [FastAPIの環境構築](#fastapiの環境構築)
	- [Fast APIのdocker-compose環境構築手順](#fast-apiのdocker-compose環境構築手順)
	- [make自動化スクリプト実行手順](#make自動化スクリプト実行手順)
	- [開発時に使用するコマンド](#開発時に使用するコマンド)
	- [コンテナ内で以下を実行する](#コンテナ内で以下を実行する)

## Fast APIのdocker-compose環境構築手順
1. ルートディレクトリ直下の`.envrc.example`を.envrcにリネームしてポート設定やプロジェクト名などの設定を編集をする。<br>
- **補足**<br>
.envrc定義情報を元にdocker-compose.ymlが参照する.envファイルを作成する。<br>
**ポートはホスト側のポートと衝突しないようにする。**<br>
## make自動化スクリプト実行手順
以下コマンドを実行するとdockerのコンテナを自動で作成と削除を実行してくれる。
1. makeが導入されていない場合は以下コマンドで導入する。
    ```
    sudo apt install make
    ```
2. .envrcファイルの定義情報を元にdocker-composeの開発環境を構築する。
	```
    make container-init
	```
3. .envrcで定義した環境変数`${PROJECT_NAME}-python`というdockerコンテナが作成されているので、ダッシュボードからアタッチする。<br> 
または下記コマンドを実行するとコンテナ内に入れる。
	```
	docker exec -it ${PROJECT_NAME}-python  /bin/bash  
	```
4. コンテナ内に入るとinstall.shスクリプトが配置されているのでプロジェクトがまだ一度も作成されていない場合は以下を実行する。
	```
	. ./install.sh
	```
5. docker-composeの環境を一旦削除して初期状態に戻したい場合は以下を実行する。
    ```
    make container-remove 
    ```

## 開発時に使用するコマンド

- プロジェクトルートディレクトで以下のスクリプトを実行後に
.envrc `export PYTHON_PORT`のポートにアクセスすると開発環境にアクセスできる。

1. `. ./start_app.sh`
2. http://localhost:PYTHON_PORT

## コンテナ内で以下を実行する

1. venvを有効化
`venv/bin/activate`
2. 開発サーバー立ち上げ
`uvicorn main:app --host 0.0.0.0 --reload`
