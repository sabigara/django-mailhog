FROM ubuntu:18.04

ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING utf-8

ENV PROJECT_NAME project
ENV HOME /root
ENV DEPLOY_DIR /opt/${PROJECT_NAME}
ENV PY_VERSION 3.7.3

RUN apt update

RUN apt install -y locales
RUN sed -i -e "s/# ja_JP.UTF-8 UTF-8/ja_JP.UTF-8 UTF-8/" /etc/locale.gen \
    && locale-gen
ENV LANG ja_JP.UTF-8
#ENV LANGUAGE en_US:en
ENV LC_ALL ja_JP.UTF-8

RUN apt install -y wget \
    build-essential \
    zlib1g-dev \
    libssl-dev \
    libffi-dev

WORKDIR ${HOME}
RUN wget https://www.python.org/ftp/python/${PY_VERSION}/Python-${PY_VERSION}.tgz \
    && tar zxf Python-${PY_VERSION}.tgz \
    && cd Python-${PY_VERSION} \
    && ./configure --enable-optimizations \
    && make altinstall

RUN update-alternatives --install /usr/local/bin/python3 python3 /usr/local/bin/python3.7 1
RUN update-alternatives --install /usr/local/bin/pip3 pip3 /usr/local/bin/pip3.7 1
RUN pip3 install -U pip

RUN apt install -y vim
RUN apt install -y libmysqlclient-dev
RUN apt install -y sqlite3
RUN apt install mysql-client -y

RUN mkdir -p ${DEPLOY_DIR}
WORKDIR ${DEPLOY_DIR}
COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . ${DEPLOY_DIR}

CMD ["scripts/run.sh"]