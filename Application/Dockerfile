FROM ubuntu:22.04
WORKDIR /projet
RUN apt-get -y update && \
    apt-get install -y python3-pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY modelo.pth ./
COPY Models ./
COPY appli.py Home.py CaptureDegats.py model_functions.py PredictAuto.py ./
CMD ["streamlit", "run", "appli.py"]