FROM nvidia/cuda:10.1-base-ubuntu18.04
RUN apt-get update && apt-get install -y --no-install-recommends \
         build-essential \
         cmake \
         git \
         curl \
         vim \
         ca-certificates \
         zip \
         unzip \
         wget

RUN apt install -y python3-pip python3-dev chromium-chromedriver

RUN pip3 install linkedin_scraper requests beautifulsoup4 jupyter pandas

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN apt install -y ./google-chrome-stable_current_amd64.deb

