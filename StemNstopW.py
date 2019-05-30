import re
import os
# from numba import jit
# from numba import cuda
dir_path = os.path.dirname(os.path.realpath(__file__))
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
#import GetData as gt
factory = StemmerFactory()
factoryStop = StopWordRemoverFactory()
stemmer = factory.create_stemmer()
stopword = factoryStop.create_stop_word_remover()


def getData(alamat):
    lineList = list()
    with open(dir_path + '/' + alamat, encoding = "ISO-8859-1") as f:
        for line in f:
            lineList.append(line.rstrip('\n'))
    return lineList

# @cuda.jit(device=True)
def save_kta():    
    with open(dir_path + '/' +"data_stemmer/last_use_k.txt", "w") as f:
        for s in last_use_k:
            f.write(str(s) +"\n")
    with open(dir_path + '/' +"data_stemmer/last_use_r.txt", "w") as f:
        for s in last_use_r:
            f.write(str(s) +"\n")
    with open(dir_path + '/' +"data_stemmer/last_use_aneh.txt", "w") as f:
        for s in last_use_aneh:
            f.write(str(s) +"\n")

last_use_k = getData('data_stemmer/last_use_k.txt')
last_use_r = getData('data_stemmer/last_use_r.txt')
last_use_aneh = getData('data_stemmer/last_use_aneh.txt')
kata_dasar = getData('data_stemmer/kata-dasar.txt')
# last_use_k = list()
# last_use_r = list()
# last_use_aneh = list()
# @cuda.jit(device=True)
def stemmer_kata(teks):
    teks_s = str(teks).split()
    for i, kt in enumerate(teks_s):
        if kt in last_use_k:
            teks_s[i] = last_use_r[last_use_k.index(kt)]
        elif kt in last_use_r or kt in last_use_aneh or kt in kata_dasar:
            continue
        else:
            teks_s[i] = stemmer.stem(kt)
            if teks_s[i] != kt:
                last_use_k.append(kt)
                last_use_r.append(teks_s[i])
            else:
                if kt not in last_use_aneh:
                    last_use_aneh.append(kt)
    # save_kta()
    return " ".join(teks_s)

def stop_word(kata):
    return stopword.remove(kata)