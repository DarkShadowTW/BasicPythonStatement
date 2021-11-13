import torch

#1 - Generate pytorch tensor 1 dimension
#-----------------------------------------------
#[MEMO] torch.zeros(5) => tensor([0., 0., 0., 0., 0.])
#[MEMO] torch.ones(5) => tensor([1., 1., 1., 1., 1.])
#[MEMO] torch.tensor([4.0, 1.0, 5.0, 3.0, 2.0]) => tensor([4., 1., 5., 3., 2.])
a = torch.ones(5)
print(a)
#[OUTPUT] : tensor([1., 1., 1., 1., 1.])


#2 - Get element from pytorch tensor
#-----------------------------------------------
print(a[1])
#[OUTPUT] : tensor(1.)


#3 - How to convert pytorch tensor to float
#-----------------------------------------------
print(float(a[1]))
#[OUTPUT] : 1.0


#4 - How to change pytorch tensor value by index
#-----------------------------------------------
a[3] = 3
print(a)
#[OUTPUT] : tensor([1., 1., 1., 3., 1.])


#5 - Generate pytorch tensor 2 dimension
#-----------------------------------------------
#[MEMO] torch.zeros(2,2) => tensor([[0., 0.],
#                                   [0., 0.]])
#[MEMO] torch.ones(2,2) => tensor([[1., 1.],
#                                  [1., 1.]])
#[MEMO] torch.tensor([[4.0, 1.0], [5.0, 3.0]]) => tensor([[4., 1.],
#                                                         [5., 3.]])
b = torch.tensor([[4.0, 1.0], [5.0, 3.0]])
print(b)
#[OUTPUT] : tensor([[4., 1.],
#                   [5., 3.]])

#6 - How to get pytorch tensor SIZE
#-----------------------------------------------
#[MEMO] two index in the output value, first axis has 2 elements, second axis has 2 elements
print(b.shape)
print(b.shape[0])
print(b.shape[1])
#[OUTPUT] torch.Size([2, 2])
#[OUTPUT] 2
#[OUTPUT] 2

#2-3
