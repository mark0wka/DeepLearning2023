FROM python:3.10.11

RUN apt-get update

RUN pip install --upgrade pip

RUN apt-get update && \
    apt-get install git

RUN git clone https://github.com/IDEA-Research/GroundingDINO && \
    cd GroundingDINO && \
    pip install -r requirements.txt && \
    pip install -q -e . && \
    mkdir weights && \
    cd weights && \
    wget -q https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth && \
    cd ..

RUN apt-get install ffmpeg libsm6 libxext6 -y

COPY local_results.txt GroundingDINO/
COPY test.py .
COPY chairs.jpg GroundingDINO/

ENTRYPOINT python test.py

