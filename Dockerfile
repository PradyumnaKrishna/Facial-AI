FROM tensorflow/tensorflow:2.4.1
LABEL org.opencontainers.image.source=https://github.com/PradyumnaKrishna/Facial-AI
LABEL MAINTAINER="Pradyumna Krishna"


COPY . /app
WORKDIR /app

RUN apt update && apt install -y libgl1-mesa-dev
RUN pip install --upgrade -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["main.py"]
