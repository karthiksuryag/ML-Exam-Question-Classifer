import nltk
from nltk.tag import DefaultTagger
from nltk.tag import UnigramTagger
from nltk.corpus import treebank


from nltk.tag import BigramTagger, TrigramTagger
from ALGORITHMS.taxonomy_Taggers import QuadgramTagger
from ALGORITHMS.taxonomy_Taggers import backoff_tagger
from ALGORITHMS.taxonomy_Taggers import train_brill_tagger
from nltk.tag import tnt
from nltk.tag.sequential import ClassifierBasedPOSTagger
class ExtractVerb:

    def wordTagger(self, wordlist,number):
        train_sents = treebank.tagged_sents()[:3000]
        if number==1:
            taglist = nltk.pos_tag(wordlist)
        elif number ==2:
            tagger = DefaultTagger('NN')
            taglist = tagger.tag(wordlist)
        elif number ==3:
            tagger = UnigramTagger(train_sents)
            taglist = tagger.tag(wordlist)

        elif number ==4:
            tnt_tagger = tnt.TnT()
            tnt_tagger.train(train_sents)
            taglist = tnt_tagger.tag(wordlist)
        elif number ==5:
            tagger = ClassifierBasedPOSTagger(train=train_sents)
            taglist = tagger.tag(wordlist)
        return taglist

    def searchVerbs(self, tagList):
        # verbList = []
        # isVB = False
        # isNNP = False
        # isWH = False
        # for word in tagList:
        #     if((not isVB) & (str(word[1])==('VB'))):
        #         isVB = True
        #         verbList.append(str(word[0]).lower())
        #     if((not isNNP) & (str(word[1]).startswith('NNP'))):
        #         isNNP = True
        #         verbList.append(str(word[0]).lower())
        #     if((not isWH) & (str(word[1]).startswith('W'))):
        #         isWH = True
        #         verbList.append(str(word[0]).lower())
        # return verbList
        list= []
        if(str(tagList[0][1])=='NN'):
           list.append((tagList[0][0]))
           print(list)
        list.append(str(word[0]).lower() for word in tagList if ((str(word[1]).startswith('V')) | (str(word[1]).startswith('NNP')) | (str(word[0][1]).startswith('NN')) |  (str(word[1]).startswith('W'))))
        return list
    def searchVerbs1(self, tagList):
            verbList = []
            isVB = False
            isNNP = False
            isWH = False
            for word in tagList:
                    if((str(word[1]).startswith('NNP'))):

                       verbList.append(str(word[0]).lower())
                    if((str(word[1]).startswith('W'))):
                        isWH = True
                        verbList.append(str(word[0]).lower())
                    if((str(word[1]).startswith('V'))):
                        isWH = True
                        verbList.append(str(word[0]).lower())
            if(str(tagList[0][1])=='NN'):
               verbList.append(tagList[0][0])
            return verbList
           #return [str(word[0]).lower() for word in tagList if ((str(word[1]).startswith('V')) | (str(word[1]).startswith('NNP')) | (str(word[1]).startswith('W')))]
    def searchVerbs11(self, getSentenses):
            verbList = []
            isVB = False
            isNNP = False
            isWH = False
            for tagList in getSentenses:
                for word in tagList:
                        if((str(word[1]).startswith('NNP'))):

                           verbList.append(str(word[0]).lower())
                        if((str(word[1]).startswith('W'))):
                            isWH = True
                            verbList.append(str(word[0]).lower())
                        if((str(word[1]).startswith('V'))):
                            isWH = True
                            verbList.append(str(word[0]).lower())
                if(str(tagList[0][1])=='NN'):
                   verbList.append(tagList[0][0])
            return verbList