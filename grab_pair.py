import csv
import random

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

pairs = open('grab_pairs.csv','a')
result = grab_pair()
pairs.write(result + ',\n')
# print(result)
pairs.close()