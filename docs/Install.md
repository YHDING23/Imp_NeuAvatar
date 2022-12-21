# Installation

In this section we demonstrate how to prepare an environment with PyTorch.

This implementation requests `pytorch3d` to be installed and based on our experience, the best way to install `pytorch3d` is from Anaconda Cloud. The implementation requires Python3.9, CUDA 11.3+ and PyTorch 1.10+

## Opt 1. Installation with Docker

We provide a Dockerfile to build an image. Ensure that your docker version >= 19.03.

```angular2html
# build an image with PyTorch 1.10.0, CUDA 11.3
# if you prefer other versions, just modified the Dockerfile
sudo docker build -t centaurusinfra/dlt-avatar docker/
```
Run it with
```angular2html
sudo docker run --gpus all --shm-size=8g -it -v {DATA_DIR}:/avatar/assets centaurusinfra/dlt-avatar
```

The `DATA_DIR` in our case is `/nfs_2/Avatar/` which includes 1) pretrained model and data, 2) flame model setup and 3) head tracker setup. 

In the container, you are able to train the avatar against your own video by following the instruction on [README](https://github.com/YHDING23/Imp_NeuAvatar/blob/main/README.md). Please note this docker installation does not include how to setup your jupyter notebook and demonstrate the avatar reenactment.   

## Opt 2. Installation with our best practices

- This implementation requests `pytorch3d` to be installed and based on my experience, the best way to install `pytorch3d` is from Anaconda Cloud:
  - Install Anaconda/mimiconda following the instruction on https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html#install-linux-silent.
  - conda create virtual environment: 
    ```angular2html
      conda create -n avatar python=3.9
      conda activate avatar
      ```
  - install torch and cuda, accordingly
    ```angular2html
      conda install -c pytorch pytorch=1.10.0 torchvision cudatoolkit=11.3
      conda install -c fvcore -c iopath -c conda-forge fvcore iopath 
      ```
    
  - install pytorch3d dependencies:
    ```angular2html
    pip install scikit-image \
    matplotlib \
    imageio \
    black \
    isort \
    flake8 \
    flake8-bugbear \
    flake8-comprehensions
    ```
  - install with CUDA support form Anaconda Cloud
    ```angular2html
      conda install pytorch3d -c pytorch3d
      conda install -c anaconda ffmpeg ## ffmpeg is for generating video clips 
      conda install jupyter
      ```
- Git clone this repo and setup. 
```
git clone https://github.com/YHDING23/Imp_NeuAvatar.git 
pip install -e . 
```

Now your environment has been setup and the jupyter notebooks provide 3 demonstrations: 
  - Notebook 1. Manually adjust expression and pose parameters 
  - Notebook 2. Video-to-Video reenactment
  - Notebook 3. real-time reenactment (ongoing)

Download pretrained models from [external website](https://edmond.mpdl.mpg.de/api/access/datafile/182303) or [our NFS]() `/nfs_2/Avatar/ckpts_and_data.tar.gz`. The folder layout:
```angular2html
    ckpts_and_data/
    ├── data   # frame-by-frame tracking results (face normal, parsing, landmark detection, etc.) from two subjects 
        ├── person_0000
        ├── person_0004
    ├── nha    # the pretrained models from two subjects
    ├── tracking    # the head tracking files (.npz)
```

Download the flame head model ```generic_model.pkl``` from [external website](https://flame.is.tue.mpg.de/) or [our NFS]() ```/nfs_2/Avatar/generic_model.pkl```, and put `.pkl` file under `./assets/flame`. Then run 
```
jupyter notebook jupyter_notebooks
```













