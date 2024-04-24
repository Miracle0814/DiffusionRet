

from seal import SEALSearcher
import json
#searcher = SEALSearcher.load('res/sample/sample_corpus.fm_index', 'checkpoints/SEAL.NQ.pt')
searcher = SEALSearcher.load('res/NQ_sample/sample_corpus.fm_index', 'NQ_checkpoints/checkpoint.pt',device='cuda')
searcher.include_keys = True
print(searcher.device)
path = f' /fm_eval_data_NQ.jsonl'
path2 = f' /valid_NQ_src.jsonl'

with open(path, 'r') as f_reader, open(path2,'r') as f2:
    # query = "walt disney world resort. for just a few days,
    # the daily value of walt disney world resort runs $ 79. 99 per market,
    # but you can buy a business for at the time.... the prices of walt disney
    # world resort is no over. at a this one allows you to pay"
    for row,r2 in zip(f_reader,f2):
        docid = str(json.loads(row)['docid']).strip()
        query = json.loads(row)['query'].strip()

        for i, doc in enumerate(searcher.search(query, k=10)):
            # print(i, doc.score, doc.docid, *doc.text(), sep='\t')
            print("Matched:")
            matched = sorted(doc.keys, reverse=True, key=lambda x:x[2])
            matched = matched[:5]
            for ngram, freq, score in matched:
                print("{:.1f}".format(score).zfill(5), freq, repr(ngram), sep='\t')







