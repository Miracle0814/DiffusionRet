
import json
path = f'/SeqDiffuSeq/data/NQ/nq_dev_unique.jsonl'
# path2 = f'/DiffuSeq/datasets/valid_pre.jsonl'
id = []
q = []
d = []
gen_doc = []
with open(path, 'r') as f_reader:

    print("open")
    for row in f_reader:
        docid = str(json.loads(row)['docid']).strip()
        query = json.loads(row)['query'].strip()
        doc = json.loads(row)['doc'].strip()
        id.append(docid)
        q.append(query)
        d.append(doc)
for line in open('data/NQ/NQ_sample.txt',encoding='utf-8'):
    line = line[8:]
    # print(line)
    ans = line.find(", \"\\\" : \\")
    p1 = line[:ans]
    # print(p1)
    # p22 = line[ans+9:]
    # p2 = p22[:-2]
    p1 = p1.replace("\\\\","\\")
    p1 = p1[2:-1]

    gen_doc.append(p1)
    # ref.append(p2)

for ids, gens, lables in zip(id, gen_doc, d):
    fout = open('/SEAL/fm_eval_data.jsonl', 'a')
    print(json.dumps({"docid": ids, "query": gens, "doc": lables}), file=fout)