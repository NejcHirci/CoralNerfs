ns-train nerfacto --vis viewer+wandb --experiment-name redsea-processed --data .\data\redsea-processed\ colmap

ns-train nerfacto --vis viewer+wandb --experiment-name redsea --data .\data\redsea\ colmap

ns-train sa3d --experiment-name sa3d-redsea-nerfacto --data .\data\redsea\ --load-dir .\outputs\redsea-nerfacto\nerfacto\{STIME_RUN}\nerfstudio_models\ colmap


