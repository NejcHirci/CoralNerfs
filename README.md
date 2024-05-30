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
git clone --recursive https://github.com/NejcHirci/CoralNerfs
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
cd sa3d/self_prompting/dependencies; # now the folder 'dependencies' is under 'sa3d/self_prompting';

# Download SAM_ckpt
cd sam_ckpt
# If you have problems with wget you can also download the file manually from the link below
wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
cd segment-anything; pip install -e .

# Installing Grounding-DINO
cd GroundingDINO/; pip install -e .
mkdir weights; cd weights
# If you have problems with wget you can also download the file manually from the link below
wget https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth
```

### SA3D
In the root directory of this repo, conduct
```bash
pip install -e .
```

### SeaThruNeRF steps

```bash
pip install git+https://github.com/AkerBP/seathru_nerf
```

### UIESS steps

Add the following packages
```bash
pip install seaborn scikit-learn
```

## Usage

### Training 

For training all 3 NeRF models, you can use the script `scripts/train_models.sh` which will train the 3 models
on the provided datasets.

Afterward you can train the 3 SA3D models with the script `scripts/train_sa3d.sh`, but NEED TO CORRECT
the paths to the trained models in the script.

Note: At the start of training the script will plot the initial SAM mask to make sure we are training the correct object.
The point prompts can be given in `sa3d/sa3d_config.py` in the `point_prompt` variable.

### Testing

To view the results of the model used the established Nerfstudio viewer with providing the path to the trained
model config file.
```bash
ns-viewer --load-config {config-dir}
```

## TODO

- [x] Prepare a custom dataset that has distinct corals.
- [x] Train a SeaThruNeRFmodel on the dataset.
- [x] Train a baseline Nerfacto model on data processed with UIE and a baseline Nerfacto.
- [x] Extract individual corals using the SA3D model from each of the models.
- [ ] Convert the extracted corals to a mesh.
- [ ] Evaluate the quality of the extracted mesh.
