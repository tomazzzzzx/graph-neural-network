import torch, torch.nn as nn

class GCN(nn.Module):
    def __init__(self, in_f, out_f): super().__init__(); self.lin = nn.Linear(in_f, out_f)
    def forward(self, x, adj): return torch.spmm(adj, self.lin(x))

class GraphSAGE(nn.Module):
    def __init__(self, in_f, h, out_f): super().__init__(); self.c1, self.c2 = GCN(in_f,h), GCN(h,out_f)
    def forward(self, x, adj): return self.c2(torch.relu(self.c1(x,adj)), adj)
