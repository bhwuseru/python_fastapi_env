FROM python:3.9-alpine

# コンテナ内の環境変数を定義するための引数
ARG PROJECT_NAME
ARG PASSWORD
ARG USER

# 環境変数を設定する
ENV PROJECT_NAME=${PROJECT_NAME}
ENV USER=${USER}
ENV PASSWORD=${PASSWORD}

# ユーザーをルートに切り替える
USER root
# Bashをインストール
RUN apk add --no-cache bash
# sudoをインストール
RUN apk add --no-cache sudo

WORKDIR /home/root

CMD ["bash"]
