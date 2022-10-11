from setuptools import setup, find_packages

setup(
    name="vht",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "ConfigArgParse",
#        "torch@https://download.pytorch.org/whl/cu113/torch-1.10.2%2Bcu113-cp39-cp39-linux_x86_64.whl",
#        "torchvision@https://download.pytorch.org/whl/cu113/torchvision-0.11.3%2Bcu113-cp39-cp39-linux_x86_64.whl",
#        "pytorch3d@https://dl.fbaipublicfiles.com/pytorch3d/packaging/wheels/py39_cu113_pyt1100/pytorch3d-0.6.1-cp39-cp39-linux_x86_64.whl",
#        "matplotlib",
#        "tensorboard",
#        "scipy",
#        "opencv-python",
#        "chumpy",
#        "face-alignment",
#        "face-detection-tflite",
    ],
)
