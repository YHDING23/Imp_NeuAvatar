FROM pytorch/pytorch:1.10.0-cuda11.3-cudnn8-devel

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC 
# to fix recv-key issue in your server

# Install conda, because the most stable installation of pytorch3d is using conda
RUN apt-get update && apt-get install -y wget git vim-tiny libsm6 libxext6 git ninja-build libglib2.0-0 libsm6 libxrender-dev libxext6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
RUN bash ~/miniconda.sh -b -p $HOME/miniconda
RUN $HOME/miniconda/bin/conda init
# RUN source ~/.bashrc
ENV PATH /root/miniconda/bin:$PATH


# Install pytorch3d
RUN conda update --all
RUN conda create -y -n avatar python=3.9
RUN echo "conda activate avatar" >> ~/.bashrc

# RUN conda install --name avatar --yes -c pytorch pytorch=1.10.0 torchvision cudatoolkit=11.3
RUN conda install --name avatar --yes -c fvcore -c iopath -c conda-forge fvcore iopath
RUN conda install --name avatar --yes -c anaconda ffmpeg
RUN conda install --name avatar --yes jupyter

RUN /bin/bash -c ". activate avatar && \
    pip install --upgrade pip && \
    pip install \
    scikit-image \
    matplotlib \
    imageio \
    black \
    isort \
    flake8 \
    flake8-bugbear \
    flake8-comprehensions"

RUN conda install --name avatar pytorch3d -c pytorch3d-nightly


RUN git clone https://github.com/YHDING23/Imp_NeuAvatar.git
ENV FORCE_CUDA="1"
WORKDIR ./Imp_NeuAvatar
RUN pip install --no-cache-dir -e .
#WORKDIR ./deps/video-head-tracker
#RUN pip install --no-cache-dir -e .
#WORKDIR /workspace/Imp_NeuAvatar
