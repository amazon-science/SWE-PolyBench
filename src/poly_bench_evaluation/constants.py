# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: CC-BY-NC-4.0
JAVA_TIMEOUT = 1200
DEFAULT_TIMEOUT = 1200

REPO_TO_PARSER_CLASS = {
    "google/guava": "JavaGenericParser",
    "google/gson": "JavaGenericParser",
    "apache/dubbo": "JavaGenericParser",
    "apolloconfig/apollo": "JavaGenericParser",
    "apache/rocketmq": "JavaGenericParser",
    "trinodb/trino": "JavaGenericParser",
    "mrdoob/three.js": "JavascriptGenericParser",
    "sveltejs/svelte": "JavascriptGenericParser",
    "prettier/prettier": "JavascriptJestPR",
    "serverless/serverless": "JavascriptMocha",
    "microsoft/vscode": "TypescriptMocha",
    "angular/angular": "TypescriptBazelAngular",
    "mui/material-ui": "TypescriptMochaFileName",
    "tailwindlabs/tailwindcss": "TypescriptJestTW",
    "coder/code-server": "TypescriptJest",
    "Significant-Gravitas/AutoGPT": "PythonPyUnit",
    "huggingface/transformers": "PythonPyUnit",
    "langchain-ai/langchain": "PythonPyUnit",
    "yt-dlp/yt-dlp": "PythonPyUnit",
    "tensorflow/models": "PythonPyUnit",
    "keras-team/keras": "PythonPyUnit",
}

_DOCKERFILE_JS_BASE = r"""
FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

RUN apt update && apt install -y \
bzip2 \
libgtk-3-0 \
libasound2 \
libx11-xcb1 \
wget \
git \
build-essential \
libffi-dev \
libtiff-dev \
python3 \
python3-pip \
jq \
curl \
locales \
locales-all \
tzdata \
&& rm -rf /var/lib/apt/lists/*

ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 16.20.2
RUN mkdir -p $NVM_DIR
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
RUN . $NVM_DIR/nvm.sh \
    && nvm install 20.16.0 \
    && nvm install 18.8.0 \
    && nvm install $NODE_VERSION \
    && nvm install 12.22.12 \
    && nvm install 8.9.1 \
    && nvm install 6.9.1 \
    && nvm install 4.9.1 \
    && nvm alias default $NODE_VERSION \
    && nvm use default

# smoke test installed node versions
RUN . $NVM_DIR/nvm.sh \
    && nvm use 20 && node --version && node -e 'console.log("hello world");' \
    && nvm use 18 && node --version && node -e 'console.log("hello world");' \
    && nvm use 16 && node --version && node -e 'console.log("hello world");' \
    && nvm use 12 && node --version && node -e 'console.log("hello world");' \
    && nvm use 8 && node --version && node -e 'console.log("hello world");' \
    && nvm use 6 && node --version && node -e 'console.log("hello world");' \
    && nvm use 4 && node --version && node -e 'console.log("hello world");' 

# install yarn on all node versions
RUN . $NVM_DIR/nvm.sh \
    && nvm use 20 && npm install -g yarn \
    && nvm use 18 && npm install -g yarn \
    && nvm use 16 && npm install -g yarn \
    && nvm use 12 && npm install -g yarn \
    && nvm use 8 && npm install -g yarn \
    && nvm use 6 && npm install -g yarn \
    && nvm use 4 && npm install -g yarn 

RUN wget -O firefox.tar.xz "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US" && \
    tar xJf firefox.tar.xz -C /opt/ && \
    ln -s /opt/firefox/firefox /usr/bin/firefox && \
    rm firefox.tar.xz

RUN apt update && apt install -y chromium-browser
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb \
    || apt -y --fix-broken install

RUN adduser --disabled-password --gecos 'dog' nonroot
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH
"""

_DOCKERFILE_JAVA_BASE = r"""
FROM amazonlinux

RUN yum groupinstall -y "Development Tools"
RUN yum install -y \
wget \
git \
jq \
tar

# Set up dependencies for Java test cases
RUN yum install -y java-1.8.0-amazon-corretto-devel \
java-11-amazon-corretto-devel \
java-11-amazon-corretto-jmods \
java-17-amazon-corretto-devel \
java-17-amazon-corretto-jmods

RUN cd /usr/local \
   && wget https://dlcdn.apache.org/maven/maven-3/3.9.11/binaries/apache-maven-3.9.11-bin.tar.gz \
   && tar zxvf apache-maven-3.9.11-bin.tar.gz \
   && rm apache-maven-3.9.11-bin.tar.gz

ENV MAVEN_HOME="/usr/local/apache-maven-3.9.11"
ENV M2_HOME="/usr/local/apache-maven-3.9.11"
ENV PATH="$M2_HOME/bin:$PATH"
"""

_DOCKERFILE_TS_BASE = r"""
FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

RUN apt update && apt install -y \
    g++ \
    bzip2 \
    libgtk-3-0 \
    libasound2 \
    libx11-xcb1 \
    wget \
    git \
    build-essential \
    libffi-dev \
    libtiff-dev \
    python3 \
    python3-pip \
    jq \
    curl \
    locales \
    locales-all \
    tzdata \
    libx11-dev \
    libkrb5-dev \
    gnupg \
    unzip \
    software-properties-common \
    git-lfs \
    libxkbfile-dev \
    libsecret-1-dev \
    jq \
    quilt \
    rsync \
    bats \
    xvfb \
    libxtst6 \
    libxss1 \
    libgtk-3-0 \
    libnss3 \
    libasound2 \
    libxkbfile-dev \
    pkg-config \
    libgbm-dev \
    libgbm1 \
    && curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash \
    && curl -sL https://github.com/goreleaser/nfpm/releases/download/v2.15.1/nfpm_2.15.1_Linux_x86_64.tar.gz | tar xz -C /usr/local/bin nfpm \
    && rm -rf /var/lib/apt/lists/*

ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 16.20.2
RUN mkdir -p $NVM_DIR

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

RUN . $NVM_DIR/nvm.sh \
    && nvm install 20.16.0 \
    && nvm install 18.8.0 \
    && nvm install $NODE_VERSION \
    && nvm install 14.21.3 \
    && nvm install 12.22.12 \
    && nvm install 10.24.1 \
    && nvm install 8.9.1 \
    && nvm install 6.9.1 \
    && nvm install 4.9.1 \
    && nvm alias default $NODE_VERSION \
    && nvm use default

# smoke test installed node versions
RUN . $NVM_DIR/nvm.sh \
    && nvm use 20 && node --version && node -e 'console.log("hello world");' \
    && nvm use 18 && node --version && node -e 'console.log("hello world");' \
    && nvm use 16 && node --version && node -e 'console.log("hello world");' \
    && nvm use 14 && node --version && node -e 'console.log("hello world");' \
    && nvm use 12 && node --version && node -e 'console.log("hello world");' \
    && nvm use 10 && node --version && node -e 'console.log("hello world");' \
    && nvm use 8 && node --version && node -e 'console.log("hello world");' \
    && nvm use 6 && node --version && node -e 'console.log("hello world");' \
    && nvm use 4 && node --version && node -e 'console.log("hello world");' 

# install yarn on all node versions
RUN . $NVM_DIR/nvm.sh \
    && nvm use 20 && npm install -g yarn \
    && nvm use 18 && npm install -g yarn \
    && nvm use 16 && npm install -g yarn \
    && nvm use 14 && npm install -g yarn \
    && nvm use 12 && npm install -g yarn \
    && nvm use 10 && npm install -g yarn \
    && nvm use 8 && npm install -g yarn \
    && nvm use 6 && npm install -g yarn \
    && nvm use 4 && npm install -g yarn 

RUN wget -O firefox.tar.xz "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US" && \
    tar xJf firefox.tar.xz -C /opt/ && \
    ln -s /opt/firefox/firefox /usr/bin/firefox && \
    rm firefox.tar.xz

RUN apt update && apt install -y chromium-browser
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb \
    || apt -y --fix-broken install

RUN adduser --disabled-password --gecos 'dog' nonroot

ENV VSCODECRASHDIR=/app/.build/crashes
ENV DISPLAY=:99
EXPOSE 4000 4200 4433 5000 8080 9876
ENV CHROME_BIN=/usr/bin/chromium
ENV FIREFOX_BIN=/usr/bin/firefox-esr
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH
"""

LANGUAGE_TO_BASE_DOCKERFILE = {
    "JavaScript": _DOCKERFILE_JS_BASE,
    "Java": _DOCKERFILE_JAVA_BASE,
    "TypeScript": _DOCKERFILE_TS_BASE,
}
