import torch

#from : Pytorch 深度學習攻略 3-11 ~ 3-13

#[MEMO] declare torch tensor
l_torch_tensor = torch.tensor([[4.0, 1.0, 2.0], [5.0, 3.0, 2.0], [2.0, 1.0, 5.0]])
print(l_torch_tensor)
#[OUTPUT] :
#tensor([[4., 1., 2.],      <-- row0
#        [5., 3., 2.],      <-- row1
#        [2., 1., 5.]])     <-- row2
#         ^   ^   ^
#         |   |   column2
#         |   column1
#         column0

#####COLUMN#####

#[MEMO] get all elements of column0
print("get all elements of column0 :")
print(l_torch_tensor[0:, 0])
#[OUTPUT] :
#tensor([4., 5., 2.])

#[MEMO] get all elements of column1
print("get all elements of column1 :")
print(l_torch_tensor[0:, 1])
#[OUTPUT] :
#tensor([1., 3., 1.])

#[MEMO] get all elements after column0
print("get all elements after column0 :")
print(l_torch_tensor[:, 1])
#[OUTPUT] :
#tensor([1., 3., 1.])


#####ROW#####

#[MEMO] get all elements from rows0
print("get all elements from rows0 :")
print(l_torch_tensor[0, :])
#[OUTPUT] :
#tensor([4., 1.])

#[MEMO] get all elements from rows1
print("get all elements from rows1 :")
print(l_torch_tensor[1, :])
#[OUTPUT] :
#tensor([5., 3.])

#[MEMO] get all elements before row2 (exclude row2)
print("get all elements before row2 (exclude row2) :")
print(l_torch_tensor[0:2, :])
#[OUTPUT] :
#tensor([[4., 1.],
#        [5., 3.]])

#[MEMO] get all elements after first rows (exclude row0)
print("get all elements after first rows (exclude row0) :")
print(l_torch_tensor[1:, :])
#[OUTPUT] :
#tensor([[5., 3.],
#        [2., 1.]])




