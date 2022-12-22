import csv
import random

def generate_pairs_csv():
    words1 = open('Isograms.csv','r')
    pairs = open('Isogram_Combos.csv','w')
    reader1 = csv.reader(words1)
    for word1 in reader1:
        #print(word1[0])
        words2 = open('Isograms.csv','r')
        reader2 = csv.reader(words2)
        for word2 in reader2:
            viable = True
            for letter1 in word1[0]:
                for letter2 in word2[0]:
                    if letter1 == letter2:
                        viable = False
            if viable:
                #print([word1[0] + ' ' + word2[0]])
                pairs.write(word1[0] + ' ' + word2[0] + ',\n')
        words2.close()

    words1.close()
    pairs.close()

def grab_pair():
    pair = ['', '']
    while pair[1] == '':
        words = open('Isograms.csv','r')
        reader = csv.reader(words)
        i = 0
        rn = random.random() * 4375
        for word in reader:
            if i < rn:
                pass
            else:
                if pair[0] == '':
                    pair[0] = word[0]
                else:
                    viable = True
                    for letter1 in pair[0]:
                        for letter2 in word[0]:
                            if letter1 == letter2:
                                viable = False
                    if viable:
                        pair[1] = word[0]
                break
            i += 1
    return pair[0] + ' ' + pair[1]


#generate_pairs_csv()
#print(grab_pair())