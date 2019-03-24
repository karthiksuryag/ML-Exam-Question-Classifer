from nltk.corpus import wordnet

class CountingClass:

     def getData(self, wordFromList1,wordFromList2):
        counter=0
        for syn in wordFromList1:
            for lemma in syn.lemmas():
                for syn1 in wordFromList2:
                     for lemma1 in syn1.lemmas():
                         #print(lemma.name()+ "  " +lemma1.name())
                         if(lemma.name()==lemma1.name()):

                            counter = counter +1
                            #print(counter)

        return counter