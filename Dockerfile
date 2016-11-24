# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
FROM jupyter/scipy-notebook

MAINTAINER Yury Kashnitsky

USER root

RUN pip install --upgrade pip


# Vowpal Wabbit
RUN apt-get install git && \
apt-get -y install build-essential && \
apt-get -y install automake && \
apt-get -y install autoconf && \
apt-get -y install libxmu-dev && \
apt-get -y install gcc && \
apt-get -y install libpthread-stubs0-dev && \
apt-get -y install libtool && \
apt-get -y install libboost-program-options-dev && \
apt-get -y install zlib1g-dev && \
apt-get -y install libc6 && \
apt-get -y install libgcc1 && \
apt-get -y install libstdc++6 && \
git clone https://github.com/JohnLangford/vowpal_wabbit.git && \
cd vowpal_wabbit && \
./autogen.sh && \
./configure && \
make && \
make install

# Install XGBoost
RUN git clone --recursive https://github.com/dmlc/xgboost && \
    cd xgboost && \
    make -j4 && \
    cd python-package; python setup.py install && cd ../..

# TensorFlow 
RUN wget https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0rc0-cp35-cp35m-linux_x86_64.whl && \
    pip install tensorflow-0.10.0rc0-cp35-cp35m-linux_x86_64.whl

# update main conda packages
RUN conda update --quiet --yes numpy scipy pandas matplotlib seaborn scikit-learn

USER $NB_USER