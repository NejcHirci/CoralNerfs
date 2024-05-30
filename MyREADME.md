# CoralNerfs

Source code for Coral NeRFs project for Differentiable Programming Course @ FRI 2023/24

This repository is largely based on existing work, but with a number of modifications and fixes in order 
to be able to use the SA3D model with a SeaThruNeRF model and to support currently unsupported point input
for the SA3D model.

## Authors

- [Nejc Hirci](https://github.com/NejcHirci)

## Credits

This project is based on the following projects:

- Initial [SA3D model implementation for Nerfstudio](https://github.com/Jumpat/SegmentAnythingin3D/tree/nerfstudio-version) by [Jumpat](https://github.com/Jumpat)
- [UIESS model implementation](https://github.com/fordevoted/UIESS) by [fordevoted](https://github.com/fordevoted)
- [SeaThruNeRF model implementation for Nerfstudio](https://github.com/AkerBP/seathru_nerf) by [AkerBP](https://github.com/AkerBP)

## Project Idea

Goal to test out the SA3D model for extracting objects from a scene with a pretrained NeRF model in particular on coral reef scenes. 
The idea is also to test out different possible pipelines for extracting individual objects and possibly see how well the models can be converted to an actual mesh.

## Installation Guide

### SAM3D Steps

```bash
git clone https://github.com/NejcHirci/CoralNerfs
cd CoralNerfs

conda create -n coralnerfs python=3.10
conda activate coralnerfs
```

### NeRFStudio

Following steps are also covered in the [NeRFStudio documentation](https://docs.nerf.studio/quickstart/installation.html).

```bash
python -m pip install --upgrade pip
pip install torch==2.1.2+cu118 torchvision==0.16.2+cu118 --extra-index-url https://download.pytorch.org/whl/cu118
conda install -c "nvidia/label/cuda-11.8.0" cuda-toolkit
pip install ninja git+https://github.com/NVlabs/tiny-cuda-nn/#subdirectory=bindings/torch
pip install nerfstudio
```

### SAM and Grounding-DINO:

```bash
cd sa3d/self_prompting; # now the folder 'dependencies' is under 'sa3d/self_prompting';

# Download SAM_ckpt
cd sam_ckpt
wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
cd segment-anything; pip install -e .

# Installing Grounding-DINO
cd GroundingDINO/; pip install -e .
mkdir weights; cd weights
wget https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth
```

### SA3D
In the root directory of this repo, conduct
```bash
pip install -e .
```

### UIESS steps

### SeaThruNeRF steps

## TODO

- [x] Prepare a custom dataset that has distinct corals.
- [x] Train a SeaThruNeRFmodel on the dataset.
- [x] Train a baseline Nerfacto model on data processed with UIE and a baseline Nerfacto.
- [ ] Extract individual corals using the SA3D model from each of the models.
- [ ] Convert the extracted corals to a mesh.
- [ ] Evaluate the quality of the extracted mesh.
