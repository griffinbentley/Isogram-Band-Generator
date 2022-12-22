import csv

def generate_pairs_csv():
    words1 = open('Isograms.csv','r')
    pairs = open('generate_pairs_csv.csv','w')
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

generate_pairs_csv()