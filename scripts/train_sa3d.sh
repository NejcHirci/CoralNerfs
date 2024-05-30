# Note must give appropriate path to data and load-dir (probably replace TIME with appropriate time)
ns-train sa3d --experiment-name sa3d-seathru --load-dir ./outputs/redsea-seathrunerf/seathru-nerf-lite/2024-05-29_153452/nerfstudio_models/ --data ./data/redsea/ --enable-seathru True colmap

# Note must give appropriate path to data and load-dir (probably replace TIME with appropriate time)
ns-train sa3d --experiment-name sa3d-nerfacto --load-dir outputs/redsea-nerfacto/nerfacto/2024-05-30_144132/nerfstudio_models/ --data ./data/redsea/ --enable-seathru False colmap

# Note must give appropriate path to data and load-dir (probably replace TIME with appropriate time)
ns-train sa3d --experiment-name sa3d-nerfacto-processed --load-dir outputs/redsea-processed/nerfacto/2024-05-30_141135/nerfstudio_models/ --data data/redsea-processed/ --enable-seathru False colmap
