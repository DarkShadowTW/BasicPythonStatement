import numpy as np

#Manual create numpy
np_3D = np.array([[[1, 2], [3, 4]],
                  [[5, 6], [7, 8]]])
print(np_3D.shape)

#Convert Numpy to torch
import torch

torch_3D = torch.from_numpy(np_3D)
print(torch_3D.shape)

#OUTPUT
#(2, 2, 2)
#torch.Size([2, 2, 2])