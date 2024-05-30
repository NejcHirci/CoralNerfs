# Copyright 2022 The Nerfstudio Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Segment Anything in 3D configuration file.
"""

from nerfstudio.cameras.camera_optimizers import CameraOptimizerConfig
from nerfstudio.configs.base_config import ViewerConfig
from nerfstudio.data.dataparsers.nerfstudio_dataparser import NerfstudioDataParserConfig
from nerfstudio.plugins.types import MethodSpecification

from sa3d.sa3d_datamanager import SA3DDataManagerConfig
from sa3d.sa3d import SA3DModelConfig, SA3DSeathruModelConfig
from sa3d.sa3d_pipeline import SA3DPipelineConfig, SA3DSeathruPipelineConfig
from sa3d.sa3d_trainer import SA3DTrainerConfig
from sa3d.sa3d_optimizer import SGDOptimizerConfig
from nerfstudio.engine.optimizers import AdamOptimizerConfig, RAdamOptimizerConfig
from sa3d.self_prompting.sam3d import SAM3DConfig
from sa3d.sa3d_field import TCNNMaskFieldConfig


# Change the pipeline for SeaThru or Original

original_pipeline = SA3DPipelineConfig(
            text_prompt='the center object',
            toggle_text_point=False,  # False is point, True is text
            point_prompt=[[887, 540], [890, 545]], # [529, 502] is for FERN # HORNS [450, 300], [480, 500]
            datamanager=SA3DDataManagerConfig(
                dataparser=NerfstudioDataParserConfig(),
                train_num_rays_per_batch=4096,
                eval_num_rays_per_batch=4096,
            ),
            model=SA3DModelConfig(
                mask_fields=TCNNMaskFieldConfig(
                    base_res=128,
                    num_levels=10,
                    max_res=1024,
                    log2_hashmap_size=19,
                    mask_threshold=1e-1
                ),
                background_color='black',
                eval_num_rays_per_chunk=1 << 11,
                remove_mask_floaters=True,
                # use_lpips=True,
            ),
            network=SAM3DConfig(
                num_prompts=10,
                neg_lamda=0.15
            )
        )

seathru_lite_pipeline = SA3DSeathruPipelineConfig(
            text_prompt='the center object',
            toggle_text_point=False,  # False is point, True is text
            # [[887, 540], [890, 545]] is for yellow coral
            point_prompt=[[887, 540], [890, 545]], # [529, 502] is for FERN # HORNS [450, 300], [480, 500]
            datamanager=SA3DDataManagerConfig(
                dataparser=NerfstudioDataParserConfig(),
                train_num_rays_per_batch=4096,
                eval_num_rays_per_batch=4096,
            ),
            model=SA3DSeathruModelConfig(
                mask_fields=TCNNMaskFieldConfig(
                    base_res=128,
                    num_levels=10,
                    max_res=2048,
                    log2_hashmap_size=19,
                    mask_threshold=1e-1
                ),
                remove_mask_floaters=True,
                eval_num_rays_per_chunk=1 << 15,
                num_nerf_samples_per_ray=64,
                num_proposal_samples_per_ray=(256, 128),
                max_res=2048,
                log2_hashmap_size=19,
                hidden_dim=64,
                bottleneck_dim=31,
                hidden_dim_colour=64,
                hidden_dim_medium=64,
                proposal_net_args_list=[
                    {
                        "hidden_dim": 16,
                        "log2_hashmap_size": 17,
                        "num_levels": 5,
                        "max_res": 128,
                        "use_linear": False,
                    },
                    {
                        "hidden_dim": 16,
                        "log2_hashmap_size": 17,
                        "num_levels": 5,
                        "max_res": 256,
                        "use_linear": False,
                    },
                ],
            ),
            network=SAM3DConfig(
                num_prompts=10,
                neg_lamda=0.15
            )
        )

# Define the SA3D method
sa3d_method = MethodSpecification(
    config=SA3DTrainerConfig(
        method_name="sa3d",
        max_num_iterations=17,
        save_only_latest_checkpoint=True,
        mixed_precision=False,
        pipeline=seathru_lite_pipeline,
        seathru_pipeline=seathru_lite_pipeline,
        enable_seathru=False,
        optimizers={
            "mask_fields": {
                "optimizer": SGDOptimizerConfig(lr=1e-1),
                #"optimizer": AdamOptimizerConfig(lr=1, eps=1e-15),
                "scheduler": None,
            },
            "camera_opt": {
                "mode": "off"
            }
        },
        viewer=ViewerConfig(num_rays_per_chunk=1 << 15),
        vis="viewer",

    ),
    description="Segment Anything in 3D method",
)
