ns-train nerfacto --vis viewer+wandb --experiment-name redsea-seathru --data .\data\redsea\ colmap

ns-train nerfacto --vis viewer+wandb --experiment-name redsea-seahthru --data .\data\redsea\ colmap

ns-train sa3d --experiment-name sa3d-redsea-seathru --data .\data\redsea\ --load-dir .\outputs\redsea-seathru\{STIME_RUN}\nerfstudio_models\ colmap


