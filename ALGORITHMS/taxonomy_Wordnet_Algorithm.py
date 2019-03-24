from nltk.corpus import wordnet

from CONNECTION.DB_Handling import DBHandler
from ALGORITHMS.taxonomy_LemmaCount import CountingClass
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic


class SimilarityChecker:

    def calsulateSimilarity(self,list1, list2,questionID, subjectCode,taxonomyID):
        questiontags = ['what', 'when', 'where', 'which', 'why', 'who','how']
        initialList = []
        finalList = []

        brown_ic = wordnet_ic.ic("ic-brown.dat")
        semcor_ic = wordnet_ic.ic("ic-semcor.dat")
        similarVerbCount=0
        for word1 in list1:
            countValue=0
            initialList = []
            if(str(word1)=='be' or str(word1)=='bi'):
                continue
            countValue=0
            verbexist = []
            verbexist=DBHandler().getData("SELECT verb_Count FROM question_analysis WHERE verb = '"+str(word1)+"' and question_id='"+str(questionID)+"' and subject_code='"+str(subjectCode)+"' LIMIT 1")
            if  len(verbexist) and taxonomyID==1:
                    print(verbexist[0][0])
                    similarVerbCount=int(verbexist[0][0])+1
                    print("value increase" +str(similarVerbCount))
                    text = "UPDATE question_analysis SET  verb_Count='"+str(similarVerbCount)+"' WHERE verb = '"+str(word1)+"' and question_id='"+str(questionID)+"' and subject_code='"+str(subjectCode)+"'"
                    DBHandler().setData(text)
            DBHandler().setData("INSERT INTO question_analysis (question_id,subject_code,verb) SELECT * FROM (SELECT '"+str(questionID)+"','"+str(subjectCode)+"','"+str(word1)+"') AS tmp WHERE NOT EXISTS (SELECT verb FROM question_analysis WHERE verb = '"+str(word1)+"' and question_id='"+str(questionID)+"') LIMIT 1")
            for questionWord in questiontags:
                if questionWord == word1:
                    text = "UPDATE question_analysis SET max_value_A='"+str("1")+"', avg_A='"+str(1)+"' WHERE verb = '"+str(word1)+"' and question_id='"+str(questionID)+"' and subject_code='"+str(subjectCode)+"'"
                    DBHandler().setData(text)
            for word2 in list2:
                count=0
                wordFromList1 = wordnet.synsets(word1,'v')
                wordFromList2 = wordnet.synsets(word2,'v')
                count = CountingClass().getData(wordFromList1,wordFromList2)
                countValue = count +countValue

                if len(wordFromList1)>0 and len(wordFromList2)>0:
                    for listA in wordFromList1:
                        for listB in wordFromList2:
                            s = listA.wup_similarity(listB)

                            if str(s) == 'None':
                                s = 0
                            initialList.append(s)
            if len(initialList)>0:
                average = 0
                database = DBHandler()
                average = sum(initialList)/len(initialList)
                print("sum = " +str(sum(initialList))+ " len = "+str(len(initialList))+" Avg = "+str(average))
                if taxonomyID == 1:

                    text = "UPDATE question_analysis SET max_value_A='"+str(max(initialList))+"', avg_A='"+str(average)+"',max_Sum_A='"+str(sum(initialList))+"' , max_Count_A='"+str(countValue)+"', similarity_type=' wup_similarity' WHERE verb = '"+str(word1)+"' and question_id='"+str(questionID)+"' and subject_code='"+str(subjectCode)+"'"
                    DBHandler().setData(text)

                    #for values in initialList:
                       # wordnetsimilar_value="INSERT INTO map(question_id,subject_code,verb,taxonomy_id,algorithm_name,wordnetvalue) VALUES( "+str(questionID)+",'"+str(subjectCode)+"','"+str(word1)+"',1,' wup_similarity','"+str(values)+"') "
                        #print(values)
                        #DBHandler().setData(wordnetsimilar_value)




                elif taxonomyID == 2:
                    text = "UPDATE question_analysis SET max_value_B='"+str(max(initialList))+"' , avg_B='"+str(average)+"' ,max_Sum_B='"+str(sum(initialList))+"' , max_Count_B='"+str(countValue)+"' , similarity_type=' wup_similarity'  WHERE verb = '"+str(word1)+"' and question_id='"+str(questionID)+"' and subject_code='"+str(subjectCode)+"'"
                    database.setData(text)
                    # for values in initialList:
                    #     wordnetsimilar_value="INSERT INTO map(question_id,subject_code,verb,taxonomy_id,algorithm_name,wordnetvalue) VALUES( "+str(questionID)+",'"+str(subjectCode)+"','"+str(word1)+"',2,' wup_similarity','"+str(values)+"') "
                    #     print(values)
                    #     DBHandler().setData(wordnetsimilar_value)
                elif taxonomyID == 3:
                    text = "UPDATE question_analysis SET max_value_C='"+str(max(initialList))+"' , avg_C='"+str(average)+"' ,max_Sum_C='"+str(sum(initialList))+"' , max_Count_C='"+str(countValue)+"' , similarity_type=' wup_similarity'  WHERE verb = '"+str(word1)+"' and question_id='"+str(questionID)+"' and subject_code='"+str(subjectCode)+"'"
                    database.setData(text)
                    # for values in initialList:
                    #     wordnetsimilar_value="INSERT INTO map(question_id,subject_code,verb,taxonomy_id,algorithm_name,wordnetvalue) VALUES( "+str(questionID)+",'"+str(subjectCode)+"','"+str(word1)+"',3,' wup_similarity','"+str(values)+"') "
                    #     print(values)
                    #     DBHandler().setData(wordnetsimilar_value)

                elif taxonomyID == 4:
                    text = "UPDATE question_analysis SET max_value_D='"+str(max(initialList))+"' , avg_D='"+str(average)+"' ,max_Sum_D='"+str(sum(initialList))+"' , max_Count_D='"+str(countValue)+"' , similarity_type=' wup_similarity'  WHERE verb = '"+str(word1)+"' and question_id='"+str(questionID)+"' and subject_code='"+str(subjectCode)+"'"
                    database.setData(text)
                    # for values in initialList:
                    #     wordnetsimilar_value="INSERT INTO map(question_id,subject_code,verb,taxonomy_id,algorithm_name,wordnetvalue) VALUES( "+str(questionID)+",'"+str(subjectCode)+"','"+str(word1)+"',4,' wup_similarity','"+str(values)+"') "
                    #     print(values)
                    #     DBHandler().setData(wordnetsimilar_value)
                elif taxonomyID == 5:
                    text = "UPDATE question_analysis SET max_value_E='"+str(max(initialList))+"' , avg_E='"+str(average)+"' ,max_Sum_E='"+str(sum(initialList))+"' , max_Count_E='"+str(countValue)+"' , similarity_type=' wup_similarity' WHERE verb = '"+str(word1)+"' and question_id='"+str(questionID)+"' and subject_code='"+str(subjectCode)+"'"
                    database.setData(text)
                    # for values in initialList:
                    #     wordnetsimilar_value="INSERT INTO map(question_id,subject_code,verb,taxonomy_id,algorithm_name,wordnetvalue) VALUES( "+str(questionID)+",'"+str(subjectCode)+"','"+str(word1)+"',5,' wup_similarity','"+str(values)+"') "
                    #     print(values)
                    #     DBHandler().setData(wordnetsimilar_value)
                elif taxonomyID == 6:
                    text = "UPDATE question_analysis SET max_value_F='"+str(max(initialList))+"' , avg_F='"+str(average)+"' ,max_Sum_F='"+str(sum(initialList))+"' , max_Count_F='"+str(countValue)+"' , similarity_type= ' wup_similarity' WHERE verb = '"+str(word1)+"' and question_id='"+str(questionID)+"' and subject_code='"+str(subjectCode)+"'"
                    database.setData(text)
                    # for values in initialList:
                    #     wordnetsimilar_value="INSERT INTO map(question_id,subject_code,verb,taxonomy_id,algorithm_name,wordnetvalue) VALUES( "+str(questionID)+",'"+str(subjectCode)+"','"+str(word1)+"',6,' wup_similarity','"+str(values)+"') "
                    #     print(values)
                    #     DBHandler().setData(wordnetsimilar_value)
                myVerb = word1
                temp = [word1, max(initialList)]
                finalList.append(temp)

        return finalList
