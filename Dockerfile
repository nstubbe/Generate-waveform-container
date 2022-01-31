FROM ubuntu:20.04 as builder
ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update && apt-get install -y \
    sudo \
    curl \
    software-properties-common \ 
    python3-pip

# Install Azure package for Python
RUN pip install azure-storage-blob

# Install AudioWaveForm
RUN add-apt-repository ppa:chris-needham/ppa
RUN apt-get update && apt-get install -y \
    audiowaveform

COPY ./GenerateWaveform.py .
ENTRYPOINT [ "python3" ]
CMD [ "GenerateWaveform.py" ]