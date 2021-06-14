FROM ubuntu:21.04

ARG USERNAME=mypython
ARG UID=1000
ARG GID=$UID
ENV HOME /home/$USERNAME

RUN addgroup \
  --gid=$GID \
  $USERNAME

RUN adduser \
  --disabled-password \
  --gecos "" \
  --ingroup "$USERNAME" \
  --uid "$UID" \
  "$USERNAME"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
  apt-get install -y\
  gnupg \
  apt-transport-https \
  debconf-utils \
  curl \
  wget \
  net-tools \
  python-dev \
  libxml2-dev \
  libxslt1-dev \
  antiword \
  unrtf \
  poppler-utils \
  pstotext \
  tesseract-ocr \
  flac \
  ffmpeg \
  lame \
  libmad0 \
  libsox-fmt-mp3 \
  sox \
  libjpeg-dev \
  swig \
  libpulse-dev && \
  rm -rf /var/lib/apt/lists/*

# apt-get and system utilities
RUN apt-get update && \
  ACCEPT_EULA=Y apt-get install -y \
  curl \
  wget \
  python3 \
  python3-pip \
  git \
  zip \
  wget \
  uuid-runtime \
  build-essential \
  zlib1g-dev \
  libffi-dev \
  tk-dev \
  libgdbm-dev \
  libc6-dev \
  libbz2-dev \
  unixodbc-dev \
  unixodbc \
  locales \
  && rm -rf /var/lib/apt/lists/*

# Install locale
RUN locale-gen en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8

RUN pip3 --no-cache-dir install flask==2.0.1 \
  && pip3 --no-cache-dir install certifi==2021.5.30 \
  && pip3 --no-cache-dir install Faker==8.7.0 \
  && pip3 --no-cache-dir install parse==1.19.0 \
  && pip3 --no-cache-dir install parse-type==0.5.2 \
  && pip3 --no-cache-dir install python-dateutil==2.8.1 \
  && pip3 --no-cache-dir install requests==2.25.1 \
  && pip3 --no-cache-dir install urllib3==1.26.4 \
  && pip3 --no-cache-dir install Pillow==8.2.0 \
  && pip3 --no-cache-dir install python-dateutil==2.8.1 \
  && pip3 --no-cache-dir install pytest==6.2.4 \
  && pip3 --no-cache-dir install jsonschema==3.2.0 \
  && pip3 --no-cache-dir install alchemize==0.14.0 \
  && pip3 --no-cache-dir install allure-pytest==2.9.43 \
  && pip3 --no-cache-dir install pytest-html==3.1.1 \
  && pip3 --no-cache-dir install pytest-order==1.0.0 

COPY . /opt/mypython
RUN chown -R $USERNAME:$USERNAME /opt/mypython

USER $USERNAME
