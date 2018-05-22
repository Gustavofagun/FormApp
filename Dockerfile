FROM python
RUN pip install flask pymongo
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]
RUN ["apt-get", "install", "-y", "telnet"]

WORKDIR /app
COPY . /app
CMD ["python","app.py"]
EXPOSE 5000
