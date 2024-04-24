

import json
path = f'/SeqDiffuSeq/data/MS_MARCO/valid.jsonl'
id = []
q = []
d = []

with open(path, 'r') as f_reader:

    print("open")
    for row in f_reader:
        docid = str(json.loads(row)['docid']).strip()
        query = json.loads(row)['query'].strip()
        doc = json.loads(row)['doc'].strip()
        id.append(docid)
        q.append(query)
        d.append(doc)
    with open('sample_corpus_pre.tsv', mode = 'a') as sample:
        for i, t, x in zip(id, q, d):
            sample.write(i + '\t'+ t + '\t' + x + '\n')
