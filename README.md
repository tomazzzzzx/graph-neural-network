# Graph Neural Network

Scalable GNN framework for molecular property prediction.

## Models
- GIN, GAT, GraphSAGE
- SchNet for 3D molecular graphs
- DimeNet++ for quantum chemistry

## Datasets
- MoleculeNet (BBBP, Tox21, ESOL, FreeSolv)
- QM9 (12 properties)
- OGB (molpcba, molhiv)

## Results (QM9 MAE)
| Property | SchNet | DimeNet++ | Ours |
|----------|--------|-----------|------|
| mu | 0.033 | 0.029 | 0.026 |

## License
MIT
