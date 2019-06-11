from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import pickle

with open('gene_list.pkl', 'rb') as rb:
    gene_list = pickle.load(rb)

#X = [[i] for i in [2, 8, 0, 4, 1, 9, 9, 0]]
X = [gene[1] for gene in gene_list[:100]]

Y = [gene[0] for gene in gene_list[:100]]

# 階層型クラスタリングの実施
# ウォード法 x ユークリッド距離
Z = linkage(X, method='ward', metric='euclidean')

# 階層型クラスタリングの可視化
fig = plt.figure(figsize=(12, 6), dpi=200)
dn = dendrogram(Z, labels=Y)
plt.show()
