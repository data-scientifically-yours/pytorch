----------------------------------------------------------------------------------------------
PyTorch is a Python package that provides two high-level features:
- Tensor computation (like NumPy) with strong GPU acceleration
- Deep neural networks built on a tape-based autograd system

- [Prerequisite](#Prerequisite)
  - [GPU on GCE Nvidia enabled VM](#GPU on GCE Nvidia enabled VM)
  - [Install Nvidia Driver](#Install-Nvidia-Driver)
  - [Install Conda](#Install-Conda)
- [Build From Source](#Build-From-Source)
  - [With Cuda](#With-Cuda)
  - [CPU Only](#CPU-Only)
- [Verify your installation](#Verify-your-installation)

## Prerequisites

#### <img src="https://raw.githubusercontent.com/data-scientifically-yours/resources/master/icones/gce.png" width="30" height="30" align="center"/> Instantiate a GPU on GCE Nvidia enabled VM
  $ wget https://raw.githubusercontent.com/makramjandar/AwesomeScripts/master/gcs/gcp_vm_instantiation.sh && bash gcp_vm_instantiation.sh

#### <img src="https://raw.githubusercontent.com/data-scientifically-yours/resources/master/icones/nvidia.png" width="40" height="40" align="center"/> Install Nvidia driver
  $ wget -O - -q "https://raw.githubusercontent.com/makramjandar/AwesomeScripts/master/bash/install-nvidia.sh" | bash

#### <img src="https://raw.githubusercontent.com/data-scientifically-yours/resources/master/icones/anaconda.png" width="30" height="30" align="center"/> Install Anaconda
When building anything, it’s safer to do it in a conda environment lest you mess 
up and pollute your system environment. 
  $ wget -O - -q 'https://raw.githubusercontent.com/makramjandar/AwesomeScripts/master/bash/install-anaconda.sh' | bash

## Build From Source

#### <img src="https://raw.githubusercontent.com/data-scientifically-yours/resources/master/icones/cuda.png" width="30" height="30" align="center"/> With Cuda
  $ wget https://raw.githubusercontent.com/makramjandar/AwesomeScripts/master/bash/build-pytorch.sh && bash build-pytorch.sh cuda
  
#### <img src="https://raw.githubusercontent.com/data-scientifically-yours/resources/master/icones/cpu.png" width="30" height="30" align="center"/> CPU Only
  $ wget https://raw.githubusercontent.com/makramjandar/AwesomeScripts/master/bash/build-pytorch.sh && bash build-pytorch.sh
  
## Verify your installation




Voilà!!!


## License

PyTorch is BSD-style licensed, as found in the LICENSE file.
