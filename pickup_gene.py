gene_file = '/cl/work/shusuke-t/mori_lab_clust0604/data/orig/epsilon2_GIgenes6_DTU190308_LB_genome_dip_normed3_1_clust1000_geneinfo.txt'
with open(gene_file, 'r') as r:
    gene = [g.split('	')[3] for g in r]
gene = [g.lower() for g in gene if len(g) > 1]

read_file = '../vectors.txt'
with open(read_file, 'r') as r:
    vocab = [v.strip() for v in r]

gene_list = []
for v in vocab:
    splited = v.split(' ')
    token = splited[0]
    if token in gene:
        vec = splited[1:]
        gene_list.append((token, vec))

print(gene_list)
print(len(gene_list))

import pickle
with open('gene_list.pkl', 'wb') as wb:
    pickle.dump(gene_list, wb)
'''
gene_listのうち、インデックス上位の遺伝子の方が、出現数が多い為、
正確なベクトルを取得している可能性が高い
'''
