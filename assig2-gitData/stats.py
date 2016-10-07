import fileinput
import csv
from Array_queue import ArrayQueue
import pandas as pd

wordAq = ArrayQueue()
charAq = ArrayQueue()

class Stats:
    
    def getWordCharCount(self,inF):

        # num_words = 0
        # num_chars = 0
        # word_len_list = []

        with open(inF, 'r') as input_file:
            for line in input_file:
                line_words = line.split()
                wordAq.enqueue(len(line.split(' '))) 
                charAq.enqueue(len(line.strip(' ')))
                # num_words += len(line_words)
                # for word in line_words:
                #     num_chars += len(word)

    def writeToCsv(self,inFile,outFile):

        wordlst = []
        charlst = []
        for i in range(wordAq.len()):
            wordlst.append(wordAq.dequeue())
            # print val

        for i in range(charAq.len()):
            charlst.append(charAq.dequeue())

        with open(inFile, 'r') as f:
            for line in f:
                d = {'WordCount' : pd.Series(wordlst), 'Character Count' : pd.Series(charlst)}
        df = pd.DataFrame(d)
        df.to_csv(outFile)


if __name__ == '__main__':

    st = Stats()
    st.getWordCharCount("/home/manick/devopsAssasination/assig2-gitData/data/clean.txt")
    st.writeToCsv("/home/manick/devopsAssasination/assig2-gitData/data/clean.txt","/home/manick/devopsAssasination/assig2-gitData/data/test.csv")
