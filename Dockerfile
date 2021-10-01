FROM python:3.9-slim-buster

COPY . /scr
WORKDIR /scr

RUN apt-get update
RUN pip install -r ./careerskills.egg-info/requires.txt

ENTRYPOINT ["python"]
CMD ["./careerskills/docker_main.py"] #docker run -it [docker_image]

