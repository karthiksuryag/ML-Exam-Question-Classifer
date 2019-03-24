from CONNECTION.DB_Handling import DBHandler
from itertools import groupby

class Getthepriority:




    def ranking_numbers(self,array,questionno,category):

            srt = sorted(array,key=lambda x: x[1], reverse=True)
            rankings = []
            rank = 1

            for k,v in groupby(srt,lambda x: x[1]): # group by score
                grp = [(rank,tup[0]) for tup in v] # get item tup[0] and put it in a tuple with the rank
                rankings += grp
                rank += len(grp) # increase rank for next grouping


            Getthepriority().insertranktodatabase(rankings,questionno,category)



    #[(0, 'item1'), (0, 'item4'), (2, 'item3'), (3, 'item2')]

    #print(all)
    def insertranktodatabase(self,getlist,questionno,category):
        print(getlist)
        print(getlist[0][0])
        print(getlist[0][1])
        print(getlist[1][0])
        print(getlist[1][1])
        print(getlist[2][0])
        print(getlist[2][1])
        print(getlist[3][0])
        print(getlist[3][1])
        updatesql ="update question_analysis_normalized_groupresults set " \
                   +str(getlist[0][1]) + "=" +str(getlist[0][0])+ ","\
                   +str(getlist[1][1]) + "=" +str(getlist[1][0]) + "," \
                   +str(getlist[2][1]) + "=" +str(getlist[2][0]) + ","\
                   +str(getlist[3][1]) + "=" +str(getlist[3][0]) + "," \
                   +str(getlist[4][1]) + "=" +str(getlist[4][0]) + "," \
                   +str(getlist[5][1]) + "=" +str(getlist[5][0]) + \
                   " where question_id= '" + str(questionno) + "' and subject_code='" + str(category) + "'"
        print(updatesql)
        DBHandler().setData(updatesql)


    def normalized_group_rank(self,getpaperno,questionno):
        all=[]
        sum_sen_value_A=''
        sum_sen_value_B=''
        sum_sen_value_C=''
        sum_sen_value_D=''
        sum_sen_value_E=''
        sum_sen_value_F=''

        getsqltonormalize = "SELECT * from question_analysis_groupresults INNER JOIN question_list" \
                            " ON `nlp_compare`.`question_list`.question_id =`nlp_compare`.`question_analysis_groupresults`.question_id" \
                            " where  `nlp_compare`.`question_list`.paperno="+getpaperno+ "  and `nlp_compare`.`question_list`.question_id='" +str(questionno)+ "' "
        questionsList = DBHandler().getData(getsqltonormalize)

        print(questionsList)

        taxonomyList = []

        for question in questionsList:

            max_value_A=question[3]
            print(max_value_A)
            max_value_B=question[4]
            max_value_C=question[5]
            max_value_D=question[6]
            max_value_E=question[7]
            max_value_F=question[8]

            words=['max_value_rank_A','max_value_rank_B','max_value_rank_C','max_value_rank_D','max_value_rank_E','max_value_rank_F']
            value=[max_value_A,max_value_B,max_value_C,max_value_D,max_value_E,max_value_F]
            zip(value,words)
            array1=list(zip(words,value))
            print(array1)
            Getthepriority().ranking_numbers(array1,question[0],question[2])

            #get the  max count rank value set###############################################################################

            max_Count_rank_A=question[9]
            max_Count_rank_B=question[10]
            max_Count_rank_C=question[11]
            max_Count_rank_D=question[12]
            max_Count_rank_E=question[13]
            max_Count_rank_F=question[14]

            wordscount=['max_Count_rank_A','max_Count_rank_B','max_Count_rank_C','max_Count_rank_D','max_Count_rank_E','max_Count_rank_F']
            valuecount=[max_Count_rank_A,max_Count_rank_B,max_Count_rank_C,max_Count_rank_D,max_Count_rank_E,max_Count_rank_F]
            arraycount=list(zip(wordscount,valuecount))
            print(arraycount)
            Getthepriority().ranking_numbers(arraycount,question[0],question[2])

             #get the  max sum r rank value set###############################################################################

            max_Sum_rank_A=question[15]
            max_Sum_rank_B=question[16]
            max_Sum_rank_C=question[17]
            max_Sum_rank_D=question[18]
            max_Sum_rank_E=question[19]
            max_Sum_rank_F=question[20]

            wordssum=['max_Sum_rank_A','max_Sum_rank_B','max_Sum_rank_C','max_Sum_rank_D','max_Sum_rank_E','max_Sum_rank_F']
            valuesum=[max_Sum_rank_A,max_Sum_rank_B,max_Sum_rank_C,max_Sum_rank_D,max_Sum_rank_E,max_Sum_rank_F]
            arraysum=list(zip(wordssum,valuesum))
            print(arraysum)
            Getthepriority().ranking_numbers(arraysum,question[0],question[2])

             #get the  max senten r rank value set###############################################################################

            max_sen_value_rank_A=question[21]
            max_sen_value_rank_B=question[22]
            max_sen_value_rank_C=question[23]
            max_sen_value_rank_D=question[24]
            max_sen_value_rank_E=question[25]
            max_sen_value_rank_F=question[26]

            maxwordssum=['max_sen_value_rank_A','max_sen_value_rank_B','max_sen_value_rank_C','max_sen_value_rank_D','max_sen_value_rank_E','max_sen_value_rank_F']
            maxvaluesum=[max_sen_value_rank_A,max_sen_value_rank_B,max_sen_value_rank_C,max_sen_value_rank_D,max_sen_value_rank_E,max_sen_value_rank_F]
            maxarraysum=list(zip(maxwordssum,maxvaluesum))
            print(maxarraysum)
            Getthepriority().ranking_numbers(maxarraysum,question[0],question[2])

            #get the  sum max senten r rank value set###############################################################################

            sum_sen_value_rank_A=question[27]
            sum_sen_value_rank_B=question[28]
            sum_sen_value_rank_C=question[29]
            sum_sen_value_rank_D=question[30]
            sum_sen_value_rank_E=question[31]
            sum_sen_value_rank_F=question[32]

            sumwordssum=['sum_sen_value_rank_A','sum_sen_value_rank_B','sum_sen_value_rank_C','sum_sen_value_rank_D','sum_sen_value_rank_E','sum_sen_value_rank_F']
            sumvaluesum=[sum_sen_value_rank_A,sum_sen_value_rank_B,sum_sen_value_rank_C,sum_sen_value_rank_D,sum_sen_value_rank_E,sum_sen_value_rank_F]
            sumarraysum=list(zip(sumwordssum,sumvaluesum))
            print(sumarraysum)
            Getthepriority().ranking_numbers(sumarraysum,question[0],question[2])

