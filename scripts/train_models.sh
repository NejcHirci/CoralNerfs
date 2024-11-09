# Baseline Nerfacto model
#ns-train nerfacto --vis viewer+wandb --experiment-name redsea-nerfacto --data .\data\redsea\ colmap

# Nerfacto + Processed model
#ns-train nerfacto --vis viewer+wandb --experiment-name redsea-processed --data .\data\redsea-processed\ colmap

# Seathru model
ns-train seahtru-nerf --vis viewer+wandb --experiment-name redsea-seathrunerf --enable-seathru True --data .\data\redsea\ colmap