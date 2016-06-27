import semrep
'''
def question_analysis(text):
    out=semrep.metamap_output(text)
    sents=[]
    fin=''
    for el in out[0]:
        fin+=el+'\n'
        #print fs
    return fin
#text='Milk intake was not associated with cancer'

#question_analysis(text)
'''

def question_analysis(text):
    out=semrep.metamap_output(text)
    sents=[]
    fin=''
    for el in out[0]:
        fin+=el+'\n'
        #print fs
    return fin