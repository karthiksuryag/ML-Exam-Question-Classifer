from CONNECTION.DB_Handling import DBHandler


class Normilize_algoWLGTag:

    def normalize_WLGT(self,getpaperno,questionno):
        insertnewquestionlist="INSERT INTO question_analysis_groupresults(SELECT `question_analysis`.`question_id`,`question_list`.`question`,`question_analysis`.`subject_code`, sum(`question_analysis`.`max_value_A`),sum(`question_analysis`.`max_value_B`)" \
                              ",sum(`question_analysis`.`max_value_C`),sum(`question_analysis`.`max_value_D`)," \
                              "sum(`question_analysis`.`max_value_E`),sum(`question_analysis`.`max_value_F`),sum(`question_analysis`.`max_Count_A`)" \
                              ",sum(`question_analysis`.`max_Count_B`),sum(`question_analysis`.`max_Count_C`),sum(`question_analysis`.`max_Count_D`)," \
                              "sum(`question_analysis`.`max_Count_E`),sum(`question_analysis`.`max_Count_F`),sum(`question_analysis`.`max_Sum_A`)," \
                              "sum(`question_analysis`.`max_Sum_B`),sum(`question_analysis`.`max_Sum_C`),sum(`question_analysis`.`max_Sum_D`)," \
                              "sum(`question_analysis`.`max_Sum_E`),sum(`question_analysis`.`max_Sum_F`),`question_analysis_stem`.`max_sen_value_A`," \
                              "`question_analysis_stem`.`max_sen_value_B`,`question_analysis_stem`.`max_sen_value_C`,`question_analysis_stem`.`max_sen_value_D`," \
                              "`question_analysis_stem`.`max_sen_value_E`,`question_analysis_stem`.`max_sen_value_F`,`question_analysis_stem`.`sum_sen_value_A`," \
                              "`question_analysis_stem`.`sum_sen_value_B`,`question_analysis_stem`.`sum_sen_value_C`,`question_analysis_stem`.`sum_sen_value_D`," \
                              "`question_analysis_stem`.`sum_sen_value_E`,`question_analysis_stem`.`sum_sen_value_F`,`question_analysis`.`question_id` FROM `nlp_compare`.`question_analysis` " \
                              "INNER JOIN `nlp_compare`.`question_analysis_stem` ON `nlp_compare`.`question_analysis`.question_id=`nlp_compare`.`question_analysis_stem`.question_id " \
                              "INNER JOIN question_list ON `nlp_compare`.`question_list`.question_id=`nlp_compare`.`question_analysis_stem`.question_id where " \
                              "`nlp_compare`.`question_list`.paperno="+getpaperno+ " and `nlp_compare`.`question_list`.question_id='"+str(questionno)+"'  group by question_id)"
        print(insertnewquestionlist)
        DBHandler().setData(insertnewquestionlist)

        getsqltonormalize = "SELECT * from question_analysis_groupresults INNER JOIN question_list" \
                            " ON `nlp_compare`.`question_list`.question_id =`nlp_compare`.`question_analysis_groupresults`.question_id" \
                            " where  `nlp_compare`.`question_list`.paperno="+getpaperno+ "  and `nlp_compare`.`question_list`.question_id='" +str(questionno)+"'"
        print(getsqltonormalize)
        DataList = DBHandler().getData(getsqltonormalize)
        for newLine in DataList:

           # maximum value of wordnet

             print("max count value")
             print([float(str(newLine[3])),float(str(newLine[4])),float(str(newLine[5])),float(str(newLine[6])),float(str(newLine[7])),float(str(newLine[8]))])
             max_Value = max([float(str(newLine[3])),float(str(newLine[4])),float(str(newLine[5])),float(str(newLine[6])),float(str(newLine[7])),float(str(newLine[8]))])
             print(max_Value)
             #print([float(str(newLine[3]))/float(max_Value),float(str(newLine[4]))/float(max_Value),float(str(newLine[5]))/float(max_Value),float(str(newLine[6]))/float(max_Value),float(str(newLine[7]))/float(max_Value),float(str(newLine[8]))/float(max_Value)])
             if(max_Value>0):
                 max_value_A= float(str(newLine[3]))/float(max_Value)
                 max_value_B= float(str(newLine[4]))/float(max_Value)
                 max_value_C= float(str(newLine[5]))/float(max_Value)
                 max_value_D= float(str(newLine[6]))/float(max_Value)
                 max_value_E= float(str(newLine[7]))/float(max_Value)
                 max_value_F= float(str(newLine[8]))/float(max_Value)
             else:
                 max_value_A= str(newLine[3])
                 max_value_B= str(newLine[4])
                 max_value_C= str(newLine[5])
                 max_value_D= str(newLine[6])
                 max_value_E= str(newLine[7])
                 max_value_F= str(newLine[8])
            #Max count value

             print("max count value")
             print([float(str(newLine[9])),float(str(newLine[10])),float(str(newLine[11])),float(str(newLine[12])),float(str(newLine[13])),float(str(newLine[14]))])
             max_Count = max([float(str(newLine[9])),float(str(newLine[10])),float(str(newLine[11])),float(str(newLine[12])),float(str(newLine[13])),float(str(newLine[14]))])
             print(max_Count)
             #print([float(str(newLine[9]))/float(max_Count),float(str(newLine[10]))/float(max_Count),float(str(newLine[11]))/float(max_Count),float(str(newLine[12]))/float(max_Count),float(str(newLine[13]))/float(max_Count),float(str(newLine[14]))/float(max_Count)])
             if(max_Count>0):
                 max_Count_A= float(str(newLine[9]))/float(max_Count)
                 max_Count_B= float(str(newLine[10]))/float(max_Count)
                 max_Count_C= float(str(newLine[11]))/float(max_Count)
                 max_Count_D= float(str(newLine[12]))/float(max_Count)
                 max_Count_E= float(str(newLine[13]))/float(max_Count)
                 max_Count_F= float(str(newLine[14]))/float(max_Count)
             else:
                 max_Count_A= str(newLine[9])
                 max_Count_B= str(newLine[10])
                 max_Count_C= str(newLine[11])
                 max_Count_D= str(newLine[12])
                 max_Count_E= str(newLine[13])
                 max_Count_F= str(newLine[14])

              #Max sum value
             print("max sum value")
             print([float(str(newLine[15])),float(str(newLine[16])),float(str(newLine[17])),float(str(newLine[18])),float(str(newLine[19])),float(str(newLine[20]))])
             max_Sum = max([float(str(newLine[15])),float(str(newLine[16])),float(str(newLine[17])),float(str(newLine[18])),float(str(newLine[19])),float(str(newLine[20]))])
             print(max_Sum)
             #print([float(str(newLine[15]))/float(max_Sum),float(str(newLine[16]))/float(max_Sum),float(str(newLine[17]))/float(max_Sum),float(str(newLine[18]))/float(max_Sum),float(str(newLine[19]))/float(max_Sum),float(str(newLine[20]))/float(max_Sum)])

             if(max_Sum>0):
                 max_Sum_A= float(str(newLine[15]))/float(max_Sum)
                 max_Sum_B= float(str(newLine[16]))/float(max_Sum)
                 max_Sum_C= float(str(newLine[17]))/float(max_Sum)
                 max_Sum_D= float(str(newLine[18]))/float(max_Sum)
                 max_Sum_E= float(str(newLine[19]))/float(max_Sum)
                 max_Sum_F= float(str(newLine[20]))/float(max_Sum)
             else:
                 max_Sum_A= str(newLine[15])
                 max_Sum_B= str(newLine[16])
                 max_Sum_C= str(newLine[17])
                 max_Sum_D= str(newLine[18])
                 max_Sum_E= str(newLine[19])
                 max_Sum_F= str(newLine[20])
               #Max sum value
             print("max sentenst value")
             print([float(str(newLine[21])),float(str(newLine[22])),float(str(newLine[23])),float(str(newLine[24])),float(str(newLine[25])),float(str(newLine[26]))])
             max_Senten = max([float(str(newLine[21])),float(str(newLine[22])),float(str(newLine[23])),float(str(newLine[24])),float(str(newLine[25])),float(str(newLine[26]))])
             print(max_Senten)
             #print([float(str(newLine[21]))/float(max_Senten),float(str(newLine[22]))/float(max_Senten),float(str(newLine[23]))/float(max_Senten),float(str(newLine[24]))/float(max_Senten),float(str(newLine[25]))/float(max_Senten),float(str(newLine[26]))/float(max_Senten)])

             if(max_Senten>0):
                 max_Senten_A= float(str(newLine[21]))/float(max_Senten)
                 max_Senten_B= float(str(newLine[22]))/float(max_Senten)
                 max_Senten_C= float(str(newLine[23]))/float(max_Senten)
                 max_Senten_D= float(str(newLine[24]))/float(max_Senten)
                 max_Senten_E= float(str(newLine[25]))/float(max_Senten)
                 max_Senten_F= float(str(newLine[26]))/float(max_Senten)
             else:
                 max_Senten_A= (str(newLine[21]))
                 max_Senten_B= (str(newLine[22]))
                 max_Senten_C= (str(newLine[23]))
                 max_Senten_D= (str(newLine[24]))
                 max_Senten_E= (str(newLine[25]))
                 max_Senten_F= (str(newLine[26]))


          #Max sum value
             print("sum sentenst value")
             print([float(str(newLine[27])),float(str(newLine[28])),float(str(newLine[29])),float(str(newLine[30])),float(str(newLine[31])),float(str(newLine[32]))])
             sum_Senten = max([float(str(newLine[27])),float(str(newLine[28])),float(str(newLine[29])),float(str(newLine[30])),float(str(newLine[31])),float(str(newLine[32]))])
             print(sum_Senten)
            # print([float(str(newLine[27]))/float(sum_Senten),float(str(newLine[28]))/float(sum_Senten),float(str(newLine[29]))/float(sum_Senten),float(str(newLine[30]))/float(sum_Senten),float(str(newLine[31]))/float(sum_Senten),float(str(newLine[32]))/float(sum_Senten)])

             if(sum_Senten>0):
                 sum_Senten_A= float(str(newLine[27]))/float(sum_Senten)
                 sum_Senten_B= float(str(newLine[28]))/float(sum_Senten)
                 sum_Senten_C= float(str(newLine[29]))/float(sum_Senten)
                 sum_Senten_D= float(str(newLine[30]))/float(sum_Senten)
                 sum_Senten_E= float(str(newLine[31]))/float(sum_Senten)
                 sum_Senten_F= float(str(newLine[32]))/float(sum_Senten)
             else:
                 sum_Senten_A= (str(newLine[27]))
                 sum_Senten_B= (str(newLine[28]))
                 sum_Senten_C= (str(newLine[29]))
                 sum_Senten_D= (str(newLine[30]))
                 sum_Senten_E= (str(newLine[31]))
                 sum_Senten_F= (str(newLine[32]))

             Query = "insert into nlp_compare.question_analysis_normalized_groupresults(question_id,question,subject_code," \
                        "max_value_A,max_value_B,max_value_C,max_value_D,max_value_E,max_value_F," \
                        "max_Count_A,max_Count_B,max_Count_C,max_Count_D,max_Count_E,max_Count_F," \
                        "max_Sum_A,max_Sum_B,max_Sum_C,max_Sum_D,max_Sum_E,max_Sum_F," \
                        "max_sen_value_A,max_sen_value_B,max_sen_value_C,max_sen_value_D,max_sen_value_E,max_sen_value_F,"\
                        "sum_sen_value_A,sum_sen_value_B,sum_sen_value_C,sum_sen_value_D,sum_sen_value_E,sum_sen_value_F,class_type)"\
                        "values('" + str(newLine[0])+"','"+ str(newLine[1])+ "','" +str(newLine[2]) + "',"\
                        + str(max_value_A)+ ", "+ str(max_value_B)+ ", "+ str(max_value_C)+ ", "+ str(max_value_D)+ ", "+ str(max_value_E)+ ", "+ str(max_value_F)+ "," \
                        + str(max_Count_A)+ ", "+ str(max_Count_B)+ ", "+ str(max_Count_C)+ ", "+ str(max_Count_D)+ ", "+ str(max_Count_E)+ ", "+ str(max_Count_F)+ "," \
                        + str(max_Sum_A)+ ", "+ str(max_Sum_B)+ ", "+ str(max_Sum_C)+ ", "+ str(max_Sum_D)+ ", "+ str(max_Sum_E)+ ", "+ str(max_Sum_F)+ "," \
                        + str(max_Senten_A)+ ", "+ str(max_Senten_B)+ ", "+ str(max_Senten_C)+ ", "+ str(max_Senten_D)+ ", "+ str(max_Senten_E)+ ", "+ str(max_Senten_F)+ "," \
                        + str(sum_Senten_A)+ ", "+ str(sum_Senten_B)+ ", "+ str(sum_Senten_C)+ ", "+ str(sum_Senten_D)+ ", "+ str(sum_Senten_E)+ ", "+ str(sum_Senten_F) \
                        +",0)"

             print(Query)
             DBHandler().setData(Query)
           #sum of sentense value


             # print(max([float(str(newLine[29])),float(str(newLine[29])),float(str(newLine[30])),float(str(newLine[31])),float(str(newLine[32]))]))
             # sum_Sen_Value = max([float(str(newLine[27])),float(str(newLine[28])),float(str(newLine[29])),float(str(newLine[30])),float(str(newLine[31])),float(str(newLine[32]))])
             # print([float(str(newLine[27])),float(str(newLine[28])),float(str(newLine[29])),float(str(newLine[30])),float(str(newLine[31])),float(str(newLine[32]))])
             # print([float(str(newLine[27]))/float(sum_Sen_Value),float(str(newLine[28]))/float(sum_Sen_Value),float(str(newLine[29]))/float(sum_Sen_Value),float(str(newLine[30]))/float(sum_Sen_Value),float(str(newLine[31]))/float(sum_Sen_Value),float(str(newLine[32]))/float(sum_Sen_Value)])


            #question_complete_query = "UPDATE question_list SET process_complete='yes' WHERE question_id = '"+str(newLine[0])+"' and subject_code='"+str(newLine[1])+"' and process_complete='no'"
           # DBHandler().setData(question_complete_query)
           # query = "UPDATE question_analysis SET max_value='"+str(maxValue)+"' WHERE verb = '"+str(newLine[2])+"' and question_id='"+str(newLine[0])+"' and subject_code='"+str(newLine[1])+"'"
            #DBHandler().setData(query)


