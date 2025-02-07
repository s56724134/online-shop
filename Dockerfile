FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式文件
COPY . .

# 開放容器的 5000 端口
EXPOSE 5000


