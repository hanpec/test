import torch

x = torch.tensor([1., -1.])
w = torch.tensor([1.0, 0.5], requires_grad=True)

loss = -torch.dot(x, w).sigmoid().log()
loss.backward()
print(loss.item())
print(w.grad)