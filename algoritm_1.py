import parmap
from gensim.models import Word2Vec
import os
import re
import numpy as np
from nltk.corpus import stopwords
from multiprocessing import Pool
from sklearn.metrics.pairwise import cosine_similarity
print 'start import'
model = Word2Vec.load_word2vec_format('/home/sda/data/src/bio.nlplab.org/wikipedia-pubmed-and-PMC-w2v.bin', binary=True)
print 'model imported'
stop = stopwords.words('english')
sents = []
key1 = []
name_sents = '/home/sda/data/src/atlas/QA/sents'
name_keys = '/home/sda/data/src/atlas/QA/keys'
sent_files = os.listdir(name_sents)
key_files = os.listdir(name_keys)
#verb_files = os.listdir('/home/andrew/work/milk_books/full_verbs')
for row in sent_files:
    name = name_sents + '/' + row
    f = open(name,'r')
    a = f.read()
    sents.append(a)
    f.close()
    name1 = name_keys + '/' + row
    g = open(name1,'r')
    b = g.read()
    g.close()
    key1.append(b)
keys = []
for row in key1:
    ss = re.sub("'",'',row)
    ss = re.sub(',','',ss)
    ssd = ss.split()
    ssd = list(set(ssd))
    keys.append(ssd)
answervectors = []
for k,row in enumerate(keys):
    tmp = []
    for line in row:
        try:
            vector = model[line]
            tmp.append(vector)
        except KeyError:
            f = 0
    answervectors.append((k,np.array(tmp)))
print 'answers generated'
def calculate_sim(line, qvectors):
#    print 'hello'
    global an1
    try:
        tmp1 = []
        for row in qvectors:
            tmp = []
            for f in line[1]:
                p = cosine_similarity(f.reshape(1,-1),row.reshape(1,-1))
                tmp.append(p)
            t = max(tmp)
            if t > 0.6:
                tmp1.append(t)
            else:
                tmp1.append(0)
        q = sum(tmp1)/len(qvectors)
#        an1.append((line[0],q))
#        print an1
        an1 = (line[0],q)
    except ValueError:
#        print 'hello'
        q = 0
    return an1

def calculate_qvectors(text):
    sentence = text.lower()
    sentence = re.sub(',','',sentence)
    sentence = re.sub('\?','',sentence)
    filt = ['i', 'there', 'if']
    quest = []
    for row in sentence.split():
        if row not in stop and row not in filt:
            quest.append(row)
    global qvectors
    qvectors = []
    if 'why' in quest:
        quest.append('because')
    for word in quest:
        try:
            vect = model[word]
            qvectors.append(vect)
    #            wd = model.most_similar(ma)
    #            for ln in wd[0:2]:
    #                vect1 = model[ln[0]]
    #                qvectors.append(vect1) 
        except KeyError:
            fl = 0
    return qvectors
from sklearn.metrics.pairwise import cosine_similarity
question = 'is milk associated with breast cancer?'
qvectors = 0
#an1 = []
#an2 = []
def return_answer(text):
    print 'searching...'
    global an1
#arr = np.array(qvectors)
#qvector = arr.sum(axis = 0)/len(arr)
    qvectors = calculate_qvectors(text)
#    print qvectors
#    from sklearn.metrics.pairwise import cosine_similarity
#    an2 = []
    an2 = parmap.map(calculate_sim, answervectors[:35000], qvectors, pool = Pool(12))
#    print an2
#    pool.close()
#    pool.join()
    try:
        qq = sorted(an2, key=lambda x: x[1], reverse = True)
        ans=[]
        for t in qq[0:5]:
            ans.append(sents[t[0]])
    except IndexError:
            ans = 'error'
    return ans