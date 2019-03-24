# updating the cosine value of a question paper if it is more than .35
import nltk

from CONNECTION.DB_Handling import DBHandler


class CosinePreprocess:

    def cosinePreprocess_papers(self,getpaperno,questionno):
        DataList=[]
        maxValue=""
        getsqltonormalize = "SELECT * from question_max_cosine INNER JOIN question_list" \
                            " ON `nlp_compare`.`question_list`.question_id =`nlp_compare`.`question_max_cosine`.question_id" \
                            " where  `nlp_compare`.`question_list`.paperno="+getpaperno+ " and `nlp_compare`.`question_list`.question_id='" +str(questionno)+ "' "

        DataList = DBHandler().getData(getsqltonormalize)
        for newLine in DataList:
            maxValue = max([str(newLine[1]),str(newLine[2]),str(newLine[3]),str(newLine[4]),str(newLine[5]),str(newLine[6])])
            if(float(maxValue) <.35):
                updatesql="update question_max_cosine set preprocess_cosine_A=0, preprocess_cosine_B=0, preprocess_cosine_C=0, preprocess_cosine_D=0, preprocess_cosine_E=0, preprocess_cosine_F=0 where question_id=" +str(newLine[0])+ ""

            else:

                updatesql="update question_max_cosine set preprocess_cosine_A=" +str(float(newLine[1])/float(maxValue))+ ", preprocess_cosine_B=" + str(float(newLine[2])/float(maxValue)) +", preprocess_cosine_C=" + str(float(newLine[3])/float(maxValue)) + ", preprocess_cosine_D=" + str(float(newLine[4])/float(maxValue)) + ", preprocess_cosine_E=" + str(float(newLine[5])/float(maxValue)) +", preprocess_cosine_F=" + str(float(newLine[6])/float(maxValue))+ "where question_id=" +str(newLine[0])+ ""
            print(updatesql)
            DBHandler().setData(updatesql)

