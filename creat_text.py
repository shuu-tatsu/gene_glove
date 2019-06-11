import json
import retokenizer as tokenizer
from tqdm import tqdm


with open('ignore_list/0603.txt', 'r') as r:
    freq_list = [v.strip() for v in r]
freq_list.extend([',', '.', '(', ')', ';'])

read_file = '/cl/work/shusuke-t/mori_lab_clust0604/data/doc/bNO_doc/all_bNO.json'
write_file = '../gene_text'

text = json.load(open(read_file, 'r', encoding='utf-8'))

extracted_text_list = []
for gene, doc in tqdm(text.items()):
    if len(doc) > 0 and None not in doc:
        joined = ' '.join(doc)
        temp1 = tokenizer.raw_tokenize(joined).split()
        temp2 = [token.lower() for token in temp1 if not token.isnumeric()] #数値排除と小文字化
        temp3 = [token for token in temp2 if token not in freq_list] #一般用語の排除
        extracted_text_list.extend(temp3)

joined_text = ' '.join(extracted_text_list)

with open(write_file, 'w') as w:
    w.write(joined_text)
