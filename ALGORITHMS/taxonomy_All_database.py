

from CONNECTION.DB_Handling import DBHandler

class taxonomy_allDatabase:
    
    def inserttoDatabase(self,questionno):


            insertquestionno = "insert into question_dataset(question_id)values('"+ str(questionno) + "')"
            documents = DBHandler().setData(insertquestionno)
            print(documents)

            normalizedsql="SELECT * FROM nlp_compare.question_analysis_normalized_groupresults where question_id='" +str(questionno)+ "'"
            documents = DBHandler().getData(normalizedsql)
            print(documents)
            if(len(documents)):
                for questions in documents:

                    updatesql="update `question_dataset` set  `question_dataset`.`max_value_A`='" +str(questions[3])+ "',`question_dataset`.`max_value_B`='" +str(questions[4])+ "'," \
                           "`question_dataset`.`max_value_C`='" +str(questions[5])+ "',`question_dataset`.`max_value_D`='" +str(questions[6])+ "',`question_dataset`.`max_value_E`='" +str(questions[7])+ "'," \
                           "`question_dataset`.`max_value_F`='" +str(questions[8])+ "',`question_dataset`.`max_Count_A`='" +str(questions[9])+ "',`question_dataset`.`max_Count_B`='" +str(questions[10])+ "'," \
                           "`question_dataset`.`max_Count_C`='" +str(questions[11])+ "',`question_dataset`.`max_Count_D`='" +str(questions[12])+ "',`question_dataset`.`max_Count_E`='" +str(questions[13])+ "'," \
                           "`question_dataset`.`max_Count_F`='" +str(questions[14])+ "',`question_dataset`.`max_Sum_A`='" +str(questions[15])+ "',`question_dataset`.`max_Sum_B`='" +str(questions[16])+ "'," \
                           "`question_dataset`.`max_Sum_C`='" +str(questions[17])+ "',`question_dataset`.`max_Sum_D`='" +str(questions[18])+ "',`question_dataset`.`max_Sum_E`='" +str(questions[19])+ "'," \
                           "`question_dataset`.`max_Sum_F`='" +str(questions[20])+ "',`question_dataset`.`max_sen_value_A`='" +str(questions[21])+ "',`question_dataset`.`max_sen_value_B`='" +str(questions[22])+ "'," \
                           "`question_dataset`.`max_sen_value_C`='" +str(questions[23])+ "',`question_dataset`.`max_sen_value_D`='" +str(questions[24])+ "',`question_dataset`.`max_sen_value_E`='" +str(questions[25])+ "'," \
                           "`question_dataset`.`max_sen_value_F`='" +str(questions[26])+ "',`question_dataset`.`sum_sen_value_A`='" +str(questions[27])+ "',`question_dataset`.`sum_sen_value_B`='" +str(questions[28])+ "'," \
                           "`question_dataset`.`sum_sen_value_C`='" +str(questions[29])+ "',`question_dataset`.`sum_sen_value_D`='" +str(questions[30])+ "',`question_dataset`.`sum_sen_value_E`='" +str(questions[31])+ "'," \
                           "`question_dataset`.`sum_sen_value_F`='" +str(questions[32])+ "',`question_dataset`.`max_value_rank_A`='" +str(questions[33])+ "',`question_dataset`.`max_value_rank_B`='" +str(questions[34])+ "'," \
                           "`question_dataset`.`max_value_rank_C`='" +str(questions[35])+ "',`question_dataset`.`max_value_rank_D`='" +str(questions[36])+ "',`question_dataset`.`max_value_rank_E`='" +str(questions[37])+ "'," \
                           "`question_dataset`.`max_value_rank_F`='" +str(questions[38])+ "',`question_dataset`.`max_Count_rank_A`='" +str(questions[39])+ "',`question_dataset`.`max_Count_rank_B`='" +str(questions[40])+ "'," \
                           "`question_dataset`.`max_Count_rank_C`='" +str(questions[41])+ "',`question_dataset`.`max_Count_rank_D`='" +str(questions[42])+ "',`question_dataset`.`max_Count_rank_E`='" +str(questions[43])+ "'," \
                           "`question_dataset`.`max_Count_rank_F`='" +str(questions[44])+ "',`question_dataset`.`max_Sum_rank_A`='" +str(questions[45])+ "',`question_dataset`.`max_Sum_rank_B`='" +str(questions[46])+ "'," \
                           "`question_dataset`.`max_Sum_rank_C`='" +str(questions[47])+ "',`question_dataset`.`max_Sum_rank_D`='" +str(questions[48])+ "',`question_dataset`.`max_Sum_rank_E`='" +str(questions[49])+ "'," \
                           "`question_dataset`.`max_Sum_rank_F`='" +str(questions[50])+ "',`question_dataset`.`max_sen_value_rank_A`='" +str(questions[51])+ "',`question_dataset`.`max_sen_value_rank_B`='" +str(questions[52])+ "'," \
                           "`question_dataset`.`max_sen_value_rank_C`='" +str(questions[53])+ "',`question_dataset`.`max_sen_value_rank_D`='" +str(questions[54])+ "',`question_dataset`.`max_sen_value_rank_E`='" +str(questions[55])+ "'," \
                           "`question_dataset`.`max_sen_value_rank_F`='" +str(questions[56])+ "',`question_dataset`.`sum_sen_value_rank_A`='" +str(questions[57])+ "',`question_dataset`.`sum_sen_value_rank_B`='" +str(questions[58])+ "'," \
                           "`question_dataset`.`sum_sen_value_rank_C`='" +str(questions[59])+ "',`question_dataset`.`sum_sen_value_rank_D`='" +str(questions[60])+ "',`question_dataset`.`sum_sen_value_rank_E`='" +str(questions[61])+ "'," \
                           "`question_dataset`.`sum_sen_value_rank_F`='" +str(questions[62])+ "' where `question_dataset`.`question_id`='" + str(questionno)+"' "
                    print(updatesql)
                    DBHandler().setData(updatesql)

            getsqlcosine = "select * from question_max_cosine where question_id='"+str(questionno)+"'"
            cosinevalues = DBHandler().getData(getsqlcosine)
            print(cosinevalues)
            if(len(cosinevalues)):
                for cosquestions in cosinevalues:
                        cosinesimilaritysql="update `question_dataset` set   `question_dataset`.`max_cosine_A`='" +str(cosquestions[1])+ "',`question_dataset`.`max_cosine_B`='" +str(cosquestions[2])+ "'," \
                           "`question_dataset`.`max_cosine_C`='" +str(cosquestions[3])+ "',`question_dataset`.`max_cosine_D`='" +str(cosquestions[4])+ "',`question_dataset`.`max_cosine_E`='" +str(cosquestions[5])+ "'," \
                           "`question_dataset`.`max_cosine_F`='" +str(cosquestions[6])+ "',`question_dataset`.`preprocess_cosine_A`='" +str(cosquestions[7])+ "',`question_dataset`.`preprocess_cosine_B`='" +str(cosquestions[8])+ "'," \
                           "`question_dataset`.`preprocess_cosine_C`='" +str(cosquestions[9])+ "',`question_dataset`.`preprocess_cosine_D`='" +str(cosquestions[10])+ "',`question_dataset`.`preprocess_cosine_E`='" +str(cosquestions[11])+ "'," \
                           "`question_dataset`.`preprocess_cosine_F`='" +str(cosquestions[12])+ "' WHERE question_id='" + str(questionno)+ "'"
                        print(cosinesimilaritysql)
                        DBHandler().setData(cosinesimilaritysql)


            getsqlgensim = "select * from question_gem_simliar_no where question_id='"+str(questionno)+"'"
            sqlgensim = DBHandler().getData(getsqlgensim)
            print(sqlgensim)
            if(len(sqlgensim)):
                for gen_questions in sqlgensim:

                    updatesqlgensim="update `question_dataset` set  `question_dataset`.`numberofgem_5_A`='" +str(gen_questions[1])+ "',`question_dataset`.`numberofgem_5_B`='" +str(gen_questions[2])+ "'," \
                           "`question_dataset`.`numberofgem_5_C`='" +str(gen_questions[3])+ "',`question_dataset`.`numberofgem_5_D`='" +str(gen_questions[4])+ "',`question_dataset`.`numberofgem_5_E`='" +str(gen_questions[5])+ "'," \
                           "`question_dataset`.`numberofgem_5_F`='" +str(gen_questions[6])+ "',`question_dataset`.`numberofgem_10_A`='" +str(gen_questions[7])+ "',`question_dataset`.`numberofgem_10_B`='" +str(gen_questions[8])+ "'," \
                           "`question_dataset`.`numberofgem_10_C`='" +str(gen_questions[9])+ "',`question_dataset`.`numberofgem_10_D`='" +str(gen_questions[10])+ "',`question_dataset`.`numberofgem_10_E`='" +str(gen_questions[11])+ "'," \
                           "`question_dataset`.`numberofgem_10_F`='" +str(gen_questions[12])+ "',`question_dataset`.`numberofgem_15_A`='" +str(gen_questions[13])+ "',`question_dataset`.`numberofgem_15_B`='" +str(gen_questions[14])+ "'," \
                           "`question_dataset`.`numberofgem_15_C`='" +str(gen_questions[15])+ "',`question_dataset`.`numberofgem_15_D`='" +str(gen_questions[16])+ "',`question_dataset`.`numberofgem_15_E`='" +str(gen_questions[17])+ "'," \
                           "`question_dataset`.`numberofgem_15_F`='" +str(gen_questions[18])+ "',`question_dataset`.`numberofgem_5_Nor_A`='" +str(gen_questions[19])+ "',`question_dataset`.`numberofgem_5_Nor_B`='" +str(gen_questions[20])+ "'," \
                           "`question_dataset`.`numberofgem_5_Nor_C`='" +str(gen_questions[21])+ "',`question_dataset`.`numberofgem_5_Nor_D`='" +str(gen_questions[22])+ "',`question_dataset`.`numberofgem_5_Nor_E`='" +str(gen_questions[23])+ "'," \
                           "`question_dataset`.`numberofgem_5_Nor_F`='" +str(gen_questions[24])+ "',`question_dataset`.`numberofgem_10_Nor_A`='" +str(gen_questions[25])+ "',`question_dataset`.`numberofgem_10_Nor_B`='" +str(gen_questions[26])+ "'," \
                           "`question_dataset`.`numberofgem_10_Nor_C`='" +str(gen_questions[27])+ "',`question_dataset`.`numberofgem_10_Nor_D`='" +str(gen_questions[28])+ "',`question_dataset`.`numberofgem_10_Nor_E`='" +str(gen_questions[29])+ "'," \
                           "`question_dataset`.`numberofgem_10_Nor_F`='" +str(gen_questions[30])+ "',`question_dataset`.`numberofgem_15_Nor_A`='" +str(gen_questions[31])+ "',`question_dataset`.`numberofgem_15_Nor_B`='" +str(gen_questions[32])+ "'," \
                           "`question_dataset`.`numberofgem_15_Nor_C`='" +str(gen_questions[33])+ "',`question_dataset`.`numberofgem_15_Nor_D`='" +str(gen_questions[34])+ "',`question_dataset`.`numberofgem_15_Nor_E`='" +str(gen_questions[35])+ "'," \
                           "`question_dataset`.`numberofgem_15_Nor_F`='" +str(gen_questions[36])+ "' WHERE question_id='" + str(questionno)+ "'"
                    print(updatesqlgensim)
                    DBHandler().setData(updatesqlgensim)