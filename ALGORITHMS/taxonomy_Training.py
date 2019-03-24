import random
from PyQt4 import QtCore, QtGui
import nltk
from CONNECTION.DB_Handling import DBHandler
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from PyQt4.QtGui import *

class MachineLearning:

    def taxonomy_features(self,tuple):
        features = {}
        features["max_value_A"] = tuple[1]
        features["max_value_B"] = tuple[2]
        features["max_value_C"] = tuple[3]
        features["max_value_D"] = tuple[4]
        features["max_value_E"] = tuple[5]
        features["max_value_F"] = tuple[6]
        features["max_Count_A"] = tuple[7]
        features["max_Count_B"] = tuple[8]
        features["max_Count_C"] = tuple[9]
        features["max_Count_D"] = tuple[10]
        features["max_Count_E"] = tuple[11]
        features["max_Count_F"] = tuple[12]
        features["max_Sum_A"] = tuple[13]
        features["max_Sum_B"] = tuple[14]
        features["max_Sum_C"] = tuple[15]
        features["max_Sum_D"] = tuple[16]
        features["max_Sum_E"] = tuple[17]
        features["max_Sum_F"] = tuple[18]
        features["max_sen_value_A"] = tuple[19]
        features["max_sen_value_B"] = tuple[20]
        features["max_sen_value_C"] = tuple[22]
        features["max_sen_value_D"] = tuple[22]
        features["max_sen_value_E"] = tuple[23]
        features["max_sen_value_F"] = tuple[24]
        features["sum_sen_value_A"] = tuple[25]
        features["sum_sen_value_B"] = tuple[26]
        features["sum_sen_value_C"] = tuple[27]
        features["sum_sen_value_D"] = tuple[28]
        features["sum_sen_value_E"] = tuple[29]
        features["sum_sen_value_F"] = tuple[30]
        features["max_value_rank_A"] = tuple[31]
        features["max_value_rank_B"] = tuple[32]
        features["max_value_rank_C"] = tuple[33]
        features["max_value_rank_D"] = tuple[34]
        features["max_value_rank_E"] = tuple[35]
        features["max_value_rank_F"] = tuple[36]
        features["max_Count_rank_A"] = tuple[37]
        features["max_Count_rank_B"] = tuple[38]
        features["max_Count_rank_C"] = tuple[39]
        features["max_Count_rank_D"] = tuple[40]
        features["max_Count_rank_E"] = tuple[41]
        features["max_Count_rank_F"] = tuple[42]
        features["max_Sum_rank_A"] = tuple[43]
        features["max_Sum_rank_B"] = tuple[44]
        features["max_Sum_rank_C"] = tuple[45]
        features["max_Sum_rank_D"] = tuple[46]
        features["max_Sum_rank_E"] = tuple[47]
        features["max_Sum_rank_F"] = tuple[48]
        features["max_sen_value_rank_A"] = tuple[49]
        features["max_sen_value_rank_B"] = tuple[50]
        features["max_sen_value_rank_C"] = tuple[51]
        features["max_sen_value_rank_D"] = tuple[52]
        features["max_sen_value_rank_E"] = tuple[53]
        features["max_sen_value_rank_F"] = tuple[54]
        features["sum_sen_value_rank_A"] = tuple[55]
        features["sum_sen_value_rank_B"] = tuple[56]
        features["sum_sen_value_rank_C"] = tuple[57]
        features["sum_sen_value_rank_D"] = tuple[58]
        features["sum_sen_value_rank_E"] = tuple[59]
        features["sum_sen_value_rank_F"] = tuple[60]
        features["max_cosine_A"] = tuple[61]
        features["max_cosine_B"] = tuple[62]
        features["max_cosine_C"] = tuple[63]
        features["max_cosine_D"] = tuple[64]
        features["max_cosine_E"] = tuple[65]
        features["max_cosine_F"] = tuple[66]
        features["preprocess_cosine_A"] = tuple[67]
        features["preprocess_cosine_B"] = tuple[68]
        features["preprocess_cosine_C"] = tuple[69]
        features["preprocess_cosine_D"] = tuple[70]
        features["preprocess_cosine_E"] = tuple[71]
        features["preprocess_cosine_F"] = tuple[72]
        features["numberofgem_5_A"] = tuple[73]
        features["numberofgem_5_B"] = tuple[74]
        features["numberofgem_5_C"] = tuple[75]
        features["numberofgem_5_D"] = tuple[76]
        features["numberofgem_5_E"] = tuple[77]
        features["numberofgem_5_F"] = tuple[78]
        features["numberofgem_10_A"] = tuple[79]
        features["numberofgem_10_B"] = tuple[80]
        features["numberofgem_10_C"] = tuple[81]
        features["numberofgem_10_D"] = tuple[82]
        features["numberofgem_10_E"] = tuple[83]
        features["numberofgem_10_F"] = tuple[84]
        features["numberofgem_15_A"] = tuple[85]
        features["numberofgem_15_B"] = tuple[86]
        features["numberofgem_15_C"] = tuple[87]
        features["numberofgem_15_D"] = tuple[88]
        features["numberofgem_15_E"] = tuple[89]
        features["numberofgem_15_F"] = tuple[90]
        features["numberofgem_5_Nor_A"] = tuple[91]
        features["numberofgem_5_Nor_B"] = tuple[92]
        features["numberofgem_5_Nor_C"] = tuple[93]
        features["numberofgem_5_Nor_D"] = tuple[94]
        features["numberofgem_5_Nor_E"] = tuple[95]
        features["numberofgem_5_Nor_F"] = tuple[96]
        features["numberofgem_10_Nor_A"] = tuple[97]
        features["numberofgem_10_Nor_B"] = tuple[98]
        features["numberofgem_10_Nor_C"] = tuple[99]
        features["numberofgem_10_Nor_D"] = tuple[100]
        features["numberofgem_10_Nor_E"] = tuple[101]
        features["numberofgem_10_Nor_F"] = tuple[102]
        features["numberofgem_15_Nor_A"] = tuple[103]
        features["numberofgem_15_Nor_B"] = tuple[104]
        features["numberofgem_15_Nor_C"] = tuple[105]
        features["numberofgem_15_Nor_D"] = tuple[106]
        features["numberofgem_15_Nor_E"] = tuple[107]
        features["numberofgem_15_Nor_F"] = tuple[108]

        return features

    def classify(self,data):
        records = DBHandler().getData("Select * from question_dataset where question_category!=0 order by 1 asc")
        labeled_names = ([(dataRecord, dataRecord[109]) for dataRecord in records])
        random.shuffle(labeled_names)
        featuresets = [(self.taxonomy_features(tuple), taxonomy) for (tuple, taxonomy) in labeled_names]
        training_set = featuresets[:300]
        testing_set = featuresets[300:]
        classifier = nltk.NaiveBayesClassifier.train(featuresets)
        MNB_classifier = SklearnClassifier(MultinomialNB())
        MNB_classifier.train(training_set)
        print("MultinomialNB accuracy percent:",nltk.classify.accuracy(MNB_classifier, testing_set))

        BNB_classifier = SklearnClassifier(BernoulliNB())
        BNB_classifier.train(training_set)
        print("BernoulliNB accuracy percent:",nltk.classify.accuracy(BNB_classifier, testing_set))

        LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
        LogisticRegression_classifier.train(training_set)
        print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

        SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
        SGDClassifier_classifier.train(training_set)
        print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

        SVC_classifier = SklearnClassifier(SVC())
        SVC_classifier.train(training_set)
        print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

        LinearSVC_classifier = SklearnClassifier(LinearSVC())
        LinearSVC_classifier.train(training_set)
        print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

        # NuSVC_classifier = SklearnClassifier(NuSVC())
        # NuSVC_classifier.train(training_set)
        # print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

        taxonomyId = SVC_classifier.classify(self.taxonomy_features(data))
        question = DBHandler().getData("SELECT question from question_list where question_id = '"+str(data[0])+"'")

        updatequestionlist="update question_list set Question_category='" +str(taxonomyId)+ "'  where question_id = '"+str(data[0])+"'"
        DBHandler().setData(updatequestionlist)



        taxonomyName = DBHandler().getData("Select taxonomy_namel from blooms_taxonomy where taxonomy_id = '"+str(taxonomyId)+"'")
        print(taxonomyName[0][0])
        print(question[0][0])
        # print(str(question[0][0]) +" : "+ str(taxonomyName[0][0]))

    def questionClassification(self,paperID):
        getrecords = "Select * from question_dataset INNER JOIN question_list" \
                     " on question_dataset.question_id=question_list.question_id" \
                     " where question_list.Question_category=0 and question_list.paperno='" +str(paperID)+"'"
        print(getrecords)
        lastrecord = DBHandler().getData(getrecords)
        if(lastrecord):
            for classifyquestion in lastrecord:
                MachineLearning().classify(classifyquestion)
        else:
            print("no value")