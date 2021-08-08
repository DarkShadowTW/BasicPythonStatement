import numpy as np

#Manual create numpy
np_3D = np.array([[[1, 2], [3, 4]],
                  [[5, 6], [7, 8]]])
print(np_3D.shape)                       #(2, 2, 2)

#Convert Numpy to torch
import torch

torch_3D = torch.from_numpy(np_3D)
print(torch_3D.shape)                    #torch.Size([2, 2, 2])


torch_4D = torch.unsqueeze(torch_3D, 0)  #torch.Size([1, 2, 2, 2])
print(torch_4D.shape)