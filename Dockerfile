FROM python:3
WORKDIR /usr/src/MyPhotos
COPY . .
RUN pip3 install -Ur requirements.txt
EXPOSE 4459
ENTRYPOINT ["python", "./server-client/server.py"]

