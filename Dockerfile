# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
FROM jupyter/scipy-notebook

MAINTAINER Yury Kashnitsky

USER root

RUN pip install --upgrade pip

RUN apt-get update && apt-get -y install vowpal-wabbit

# Vowpal Wabbit
#RUN add-apt-repository ppa:boost-latest/ppa && \
#apt-get update
#RUN apt-get -y install libboost-program-options-dev zlib1g-dev && \
#apt-get -y install libboost-python-dev && \


#git clone https://github.com/JohnLangford/vowpal_wabbit.git && \
#cd vowpal_wabbit && \
#make && \
#make install

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

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_USER