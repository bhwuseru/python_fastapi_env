FROM nvidia/cuda:11.8.0-base-ubuntu22.04

# コンテナ内の環境変数を定義するための引数
ARG PROJECT_NAME
ARG PASSWORD
ARG USER

# 環境変数を設定する
ENV PROJECT_NAME=${PROJECT_NAME}
ENV USER=${USER}
ENV PASSWORD=${PASSWORD}


# システム依存パッケージをインストール
RUN apt-get update && apt-get install -y \
    python3 python3-venv python3-pip ffmpeg git 

# 必要なライブラリのインストール
RUN 
RUN pip install fastapi uvicorn jinja2 python-multipart

# Real-ESRGANをクローン
RUN git clone https://github.com/xinntao/Real-ESRGAN.git /var/www/html/Real-ESRGAN
WORKDIR /var/www/html/Real-ESRGAN

# RIFEをクローン
RUN git clone https://github.com/megvii-research/ECCV2022-RIFE.git /var/www/html/RIFE
WORKDIR /var/www/html/RIFE

# FastAPI Web UI
WORKDIR /var/www/html
