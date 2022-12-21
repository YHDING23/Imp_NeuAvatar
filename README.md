# An Implementation of Neural Head Avatars from Monocular RGB Videos

This is an implementation of neural head avatars. The code is heavily based on [this repo NerFace](https://github.com/gafniguy/4D-Facial-Avatars) [CVPR 2021] and [this repo Neural Head Avatar](https://github.com/philgras/neural-head-avatars) [CVPR 2022]. The target is to extrapolate unseen poses and view points of an animatable human avatar from a monocular RGB portrait video including a range of different expressions and views.

![Reenactment GIF](./misc/gif_combined.gif)

## Installation

- Install Python3.9 following the instruction on https://www.python.org/

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
  - install with CUDA support form Anaconda Cloud
    ```angular2html
      conda install pytorch3d -c pytorch3d
      conda install -c anaconda ffmpeg ## ffmpeg is for generating video clips
      ```
- Git clone this repo and setup.
```
git clone https://github.com/YHDING23/Imp_NeuAvatar.git
pip install -e .
```

## Quickstart with pretrained models

- Download pretrained models from [external website](https://edmond.mpdl.mpg.de/api/access/datafile/182303) or [our NFS]() `/nfs_2/Avatar/ckpts_and_data.tar.gz`. The folder layout:
```angular2html
    ckpts_and_data/
    ├── data   # frame-by-frame tracking results (face normal, parsing, landmark detection, etc.) from two subjects
        ├── person_0000
        ├── person_0004
    ├── nha    # the pretrained models from two subjects
"README.md" 136L, 8852C                                                                     6,0-1         Top
# An Implementation of Neural Head Avatars from Monocular RGB Videos

This is an implementation of neural head avatars. The code is heavily based on [this repo NerFace](https://github.com/gafniguy/4D-Facial-Avatars) [CVPR 2021] and [this repo Neural Head Avatar](https://github.com/philgras/neural-head-avatars) [CVPR 2022]. The target is to extrapolate unseen poses and view points of an animatable human avatar from a monocular RGB portrait video including a range of different expressions and views.

![Reenactment GIF](./misc/gif_combined.gif)

## Installation

- Install Python3.9 following the instruction on https://www.python.org/

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
  - install with CUDA support form Anaconda Cloud
    ```angular2html
      conda install pytorch3d -c pytorch3d
      conda install -c anaconda ffmpeg ## ffmpeg is for generating video clips
      ```
- Git clone this repo and setup.
```
git clone https://github.com/YHDING23/Imp_NeuAvatar.git
pip install -e .
```

## Quickstart with pretrained models

- Download pretrained models from [external website](https://edmond.mpdl.mpg.de/api/access/datafile/182303) or [our NFS]() `/nfs_2/Avatar/ckpts_and_data.tar.gz`. The folder layout:
```angular2html
    ckpts_and_data/
    ├── data   # frame-by-frame tracking results (face normal, parsing, landmark detection, etc.) from two subjects
        ├── person_0000
        ├── person_0004
    ├── nha    # the pretrained models from two subjects
-- INSERT --                                                                                6,1           Top
