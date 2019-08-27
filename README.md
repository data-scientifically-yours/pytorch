![PyTorch Logo](https://i.ibb.co/7nMS8yz/nvidia-pytorch.png)

_______________________________________________________________________________________________

PyTorch is a Python package that provides two high-level features:
- Tensor computation (like NumPy) with strong GPU acceleration
- Deep neural networks built on a tape-based autograd system

- [Creating a GPU enabled VM Instance From GCP](#Creating-a-GPU-enabled-VM-Instance-From-GCP)
- [Install Nvidia Driver](#Install-Nvidia-Driver)
- [Install Conda](#Install-Conda)
- [Build From Source](#Build-From-Source)
  - [With CUDA](#)
  - [Without CUDA (CPU-only)](#)
  - [Verify your installation](#)

## Creating a GPU enabled VM Instance From GCP

```bash
export PROJECT='YOUR_PROJECT'
export ZONE='us-central1-a'
gcloud config set project "$PROJECT"
gcloud beta compute --project="$PROJECT" instances create pytorch-rebuild --zone="$ZONE" --machine-type=n1-standard-4 --subnet=default --network-tier=PREMIUM --maintenance-policy=TERMINATE --scopes=https://www.googleapis.com/auth/cloud-platform --accelerator=type=nvidia-tesla-k80,count=1 --tags=http-server,https-server --image=ubuntu-minimal-1804-bionic-v20190814 --image-project=ubuntu-os-cloud --boot-disk-size=30GB --boot-disk-type=pd-standard --boot-disk-device-name=pytorch-rebuild --reservation-affinity=any
```

## Install Nvidia Driver

```bash
wget http://us.download.nvidia.com/tesla/418.87/nvidia-driver-local-repo-ubuntu1804-418.87.00_1.0-1_amd64.deb
sudo apt-key add /var/nvidia-driver-local-repo-418.87.00/7fa2af80.pub
sudo dpkg -i nvidia-driver-local-repo-ubuntu1804-418.87.00_1.0-1_amd64.deb
sudo apt-get update
sudo apt-get install cuda-drivers
sudo reboot
nvidia-smi
```

## Install Conda

```bash
cd /tmp
curl -O https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh
sha256sum Anaconda3-2019.07-Linux-x86_64.sh
bash Anaconda3-2019.07-Linux-x86_64.sh
source ~/.bashrc
conda list
```

## Build From Source

Note: at the time of writing, the latest Python is 3.7.3 and NumPy 1.16.3. Feel free to change these versions for your build.


### With CUDA

As of writing, PyTorch officially supports CUDA up to 10.0 unless PyTorch 
adds MAGMA support for CUDA 10.1 (i.e. when this package becomes available).

When building anything, it’s safer to do it in a conda environment lest you mess 
up and pollute your system environment. Let’s first install the prerequisite packages.
Make sure you are using this environment for the rest of the article.

```bash
conda create --name pytorch-build python=3.7.3 numpy=1.16.3
conda activate pytorch-build # or `source activate pytorch-build`
conda install numpy pyyaml mkl mkl-include setuptools cmake cffi \ typing
conda install -c pytorch magma-cuda100
```

Then, we want to tell CMake (building tool) where to put the resulting files.

```bash
export CMAKE_PREFIX_PATH="$HOME/anaconda3/envs/pytorch-build"
```

As a precaution against older Anaconda symbolic linking mistakes, we 
temporarily rename its compatibility linker, before renaming it back later:

```bash
cd ~/anaconda3/envs/pytorch-build/compiler_compat
mv ld ld-old
```

Now, for some reason, PyTorch cannot find OpenMP out of the box, so we 
have to explicitly install OpenMP, a library for better CPU multi-threading:

```bash
sudo apt-get install libomp-dev
```

You may be able to ignore this paragraph, but for the sake of completion, 
there used to be an issue with the Intel ideep/mkldnn module version 0.17.3 
on which PyTorch depended. However, Intel has since updated the submodule to 0.18.1 
so you shouldn’t have to deal with it. However, your build gives you any problem, 
you may be able to follow this PyTorch Github thread.

Anyway, you can now build and install the library with the following steps:

```bash
export USE_CUDA=1 USE_CUDNN=1 USE_MKLDNN=1
cd ~/pytorch
python setup.py install
```

Now remember to rename back the Anaconda compiler linker:

```bash
cd ~/anaconda3/envs/pytorch-build/compiler_compat
mv ld-old ld
```

You are done!

### Without CUDA (CPU-only)

This is easier than the CUDA version. Let’s set up the environment, but 
without the need for MAGMA-CUDA support. Make sure you are using this 
environment for the rest of the article..

```bash
conda create --name pytorch-build python=3.7.3 numpy=1.16.3
conda activate pytorch-build
conda install numpy pyyaml mkl mkl-include setuptools cmake cffi typing
```

Then, we want to tell CMake (building tool) where to put the resulting files.

```bash
export CMAKE_PREFIX_PATH="$HOME/anaconda3/envs/pytorch-build"
```

As a precaution against older Anaconda symbolic linking mistakes, we 
temporarily rename its compatibility linker, before renaming it back later:

```bash
cd ~/anaconda3/envs/pytorch-build/compiler_compat
mv ld ld-old
```

Now, for some reason, PyTorch cannot find OpenMP out of the box, so we 
have to explicitly install OpenMP, a library for better CPU multi-threading:

```bash
sudo apt-get install libomp-dev
```

Now that we’ve done all the prep work, download PyTorch code into your home folder for convenience.

```bash
cd ~
git clone --recursive https://github.com/data-scientifically-yours/pytorch.git
```

You may be able to ignore this paragraph, but for the sake of completion, 
there used to be an issue with the Intel ideep/mkldnn module version 
0.17.3 on which PyTorch depended. However, Intel has since updated the 
submodule to 0.18.1 so you shouldn’t have to deal with it. However, your 
build gives you any problem, you may be able to follow this PyTorch Github 
thread.

Anyway, you can now build and install the library with the following steps:

```bash
export USE_CUDA=0 USE_CUDNN=0 USE_MKLDNN=1
cd ~/pytorch
python setup.py install
```

Now remember to rename back the Anaconda compiler linker:

```bash
cd ~/anaconda3/envs/pytorch-build/compiler_compat
mv ld-old ld
```

You are done!

### Verify your installation

Still under the pytorch-build environment, let’s run some examples to make 
sure your installation is correct. First, let’s build the torchvision library from 
source.

```bash
cd ~
git clone https://github.com/pytorch/vision.git
cd vision
python setup.py install
```

Next, we must install tqdm (a dependency for downloading torchvision datasets) 
with pip in order to run the MNIST example. Otherwise download will error out.

```bash
pip install tqdm
```

Now download the examples and run MNIST:

```bash
cd ~
git clone https://github.com/pytorch/examples.git
cd examples/mnist
python main.py
```

Voilà!!!


## License

PyTorch is BSD-style licensed, as found in the LICENSE file.
