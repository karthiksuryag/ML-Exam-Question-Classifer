from gensim import corpora, models, similarities
from CONNECTION.DB_Handling import DBHandler

class SementicSimilarityCheckerAll:


    def getSementicSimilarityValues(self,documents,questionno,query):

        # documents = ["When did it happen","hello world"]

        stoplist = set('for a of the and to in'.split())

        texts = [[word for word in document.lower().split() if word not in stoplist]
                 for document in documents]

        # remove words that appear only once
        all_tokens = sum(texts, [])
        tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)

        texts = [[word for word in text if word not in tokens_once]
                 for text in texts]

        dictionary = corpora.Dictionary(texts)
        dictionary.save('Taxonomy.dict')

        corpus = [dictionary.doc2bow(text) for text in texts]
        # print(corpus)
        corpora.MmCorpus.serialize('Taxonomy.mm', corpus)

        # TODO: work with streamed corpus from filesystem, rather than full in-memory corpus

        tfidf = models.TfidfModel(corpus)

        corpus_tfidf = tfidf[corpus]

        lsi_tfidf = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=100)
        lsi_tfidf.save('Taxonomy.lsi_tfidf')

        # Add a second lazy executing wrapper to our corpus
        corpus_lsi_tfidf = lsi_tfidf[corpus_tfidf]

        lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=100)
        corpus_lsi = lsi[corpus]

        index = similarities.MatrixSimilarity(corpus_lsi)
        index.save('Taxonomy.index')

        # query = "Explain what is happening inside singleton design pattern"

        query_bow = dictionary.doc2bow(query.lower().split())
        query_lsi = lsi[query_bow]

        query_similarities = enumerate(index[query_lsi])
        sort_key = lambda item: -item[1] #sort by similarity descending
        sorted_similarities = sorted(query_similarities, key=sort_key)


        # valueWithOutTFIDF = sorted_similarities[0][1]
        # sumvalueWithOutTFIDF = sum(sorted_similarities[0])
        #
        print( "Without TDIDF:")
        # print ("\n".join(["%.10f - %s" % (score, documents[index]) for index, score in sorted_similarities]))
        iteration = 0
        NumberofKnowledge=0
        NumberofComprehension =0
        NumberofApplication=0
        NumberofAnalysis =0
        NumberofSynthesis=0
        NumberofEvaluation=0
        NumberofKnowledge10=0
        NumberofComprehension10 =0
        NumberofApplication10=0
        NumberofAnalysis10 =0
        NumberofSynthesis10=0
        NumberofEvaluation10=0
        NumberofKnowledge15=0
        NumberofComprehension15 =0
        NumberofApplication15=0
        NumberofAnalysis15 =0
        NumberofSynthesis15=0
        NumberofEvaluation15=0
        for items in sorted_similarities:
            getquestion=[]
            if(iteration==0):
                iteration = iteration+1
                questionnoexist = "select * from  question_gem_simliar_no where question_id=" +str(questionno)+ ""
                getquestion=DBHandler().getData(questionnoexist)
                if not(getquestion):
                    insertquestionno ="insert into question_gem_simliar_no(question_id) values(" + str(questionno)+") "
                    print(insertquestionno)
                    DBHandler().setData(insertquestionno)
            elif(iteration<=5):

                getsqldatabase = "select Question_category from question_list where Quetion_OrderNo=" +str(items[0]) + ""
                getsql=DBHandler().getData(getsqldatabase)
                print(getsql[0][0])

                if(getsql[0][0]==1):
                    NumberofKnowledge = NumberofKnowledge +1
                    NumberofKnowledge10 = NumberofKnowledge10 +1
                    NumberofKnowledge15 = NumberofKnowledge15 +1
                if(getsql[0][0]==2):
                    NumberofComprehension = NumberofComprehension +1
                    NumberofComprehension10 = NumberofComprehension10 +1
                    NumberofComprehension15 = NumberofComprehension15 +1
                if(getsql[0][0]==3):
                    NumberofApplication = NumberofApplication +1
                    NumberofApplication10 = NumberofApplication10 +1
                    NumberofApplication15 = NumberofApplication15 +1
                if(getsql[0][0]==4):
                    NumberofAnalysis = NumberofAnalysis +1
                    NumberofAnalysis10 = NumberofAnalysis10 +1
                    NumberofAnalysis15 = NumberofAnalysis15 +1
                if(getsql[0][0]==5):
                    NumberofSynthesis = NumberofSynthesis +1
                    NumberofSynthesis10 = NumberofSynthesis10 +1
                    NumberofSynthesis15 = NumberofSynthesis15 +1

                if(getsql[0][0]==6):
                    NumberofEvaluation = NumberofEvaluation +1
                    NumberofEvaluation10 = NumberofEvaluation10 +1
                    NumberofEvaluation15 = NumberofEvaluation15 +1

                iteration = iteration + 1
            elif(iteration<=10):

                getsqldatabase = "select Question_category from question_list where Quetion_OrderNo=" +str(items[0]) + ""
                getsql=DBHandler().getData(getsqldatabase)
                print(getsql[0][0])
                if(getsql[0][0]==1):
                    NumberofKnowledge10 = NumberofKnowledge10 +1
                    NumberofKnowledge15 = NumberofKnowledge15 +1
                if(getsql[0][0]==2):
                    NumberofComprehension10 = NumberofComprehension10 +1
                    NumberofComprehension15 = NumberofComprehension15 +1
                if(getsql[0][0]==3):
                    NumberofApplication10 = NumberofApplication10 +1
                    NumberofApplication15 = NumberofApplication15 +1
                if(getsql[0][0]==4):
                    NumberofAnalysis10 = NumberofAnalysis10 +1
                    NumberofAnalysis15 = NumberofAnalysis15 +1
                if(getsql[0][0]==5):
                    NumberofSynthesis10 = NumberofSynthesis10 +1
                    NumberofSynthesis15 = NumberofSynthesis15 +1
                if(getsql[0][0]==6):
                    NumberofEvaluation10 = NumberofEvaluation10 +1
                    NumberofEvaluation15 = NumberofEvaluation15 +1
                iteration = iteration + 1
            elif(iteration<=15):

                getsqldatabase = "select Question_category from question_list where Quetion_OrderNo=" +str(items[0]) + ""
                getsql=DBHandler().getData(getsqldatabase)
                print(getsql[0][0])
                if(getsql[0][0]==1):

                    NumberofKnowledge15 = NumberofKnowledge15 +1
                if(getsql[0][0]==2):

                    NumberofComprehension15 = NumberofComprehension15 +1
                if(getsql[0][0]==3):

                    NumberofApplication15 = NumberofApplication15 +1
                if(getsql[0][0]==4):

                    NumberofAnalysis15 = NumberofAnalysis15 +1
                if(getsql[0][0]==5):

                    NumberofSynthesis15 = NumberofSynthesis15 +1
                if(getsql[0][0]==6):

                    NumberofEvaluation15 = NumberofEvaluation15 +1
                iteration = iteration + 1

            else:
                print("NumberofKnowledge",NumberofKnowledge)
                print("NumberofComprehension",NumberofComprehension)
                print("NumberofApplication",NumberofApplication)
                print("NumberofAnalysis",NumberofAnalysis)
                print("NumberofSynthesis",NumberofSynthesis)
                print("NumberofEvaluation",NumberofEvaluation)

                print("within 10")
                print("NumberofKnowledge10",NumberofKnowledge10)
                print("NumberofComprehension10",NumberofComprehension10)
                print("NumberofApplication10",NumberofApplication10)
                print("NumberofAnalysis10",NumberofAnalysis10)
                print("NumberofSynthesis10",NumberofSynthesis10)
                print("NumberofEvaluation10",NumberofEvaluation10)

                print("within 15")
                print("NumberofKnowledge15",NumberofKnowledge15)
                print("NumberofComprehension15",NumberofComprehension15)
                print("NumberofApplication15",NumberofApplication15)
                print("NumberofAnalysis15",NumberofAnalysis15)
                print("NumberofSynthesis15",NumberofSynthesis15)
                print("NumberofEvaluation15",NumberofEvaluation15)
                insertsql=" update nlp_compare.question_gem_simliar_no set numberofKnowledge= "+str(NumberofKnowledge)+"," \
                           "numberofComprehension= " +str(NumberofComprehension)  +",numberofApplication =" +str(NumberofApplication) +\
                     ",numberofAnalysis = " +str(NumberofAnalysis)  +",numberofSynthesis =" +str(NumberofSynthesis) +\
                     ",numberofEvaluation= " +str(NumberofEvaluation)  +",numberofKnowledge10 =" +str(NumberofKnowledge10) +\
                     ",numberofComprehension10= " +str(NumberofComprehension10)  +",numberofApplication10 =" +str(NumberofApplication10) +\
                     ",numberofAnalysis10= " +str(NumberofAnalysis10)  +",numberofSynthesis10 =" +str(NumberofSynthesis10) +\
                     ",numberofEvaluation10= " +str(NumberofEvaluation10)  +",NumberofKnowledge15 =" +str(NumberofKnowledge15) +\
                    ",numberofComprehension15= " + str(NumberofComprehension15)  +",numberofApplication15 =" +str(NumberofApplication15) +\
                    ",numberofAnalysis15= " + str(NumberofAnalysis15)  +",numberofSynthesis15 =" +str(NumberofSynthesis15) +\
                    ",numberofEvaluation15= " + str(NumberofEvaluation15)  +" where question_id =" + str(questionno) + ""
                print(insertsql)
                DBHandler().setData(insertsql)
                updaterank=[]
                updaterank=DBHandler().getData("select * from question_gem_simliar_no where question_id=" + str(questionno)+ "")
                maxupto5 =  max(updaterank[0][1],updaterank[0][2],updaterank[0][3],updaterank[0][4],updaterank[0][5],updaterank[0][6])
                maxupto10 = max(updaterank[0][7],updaterank[0][8],updaterank[0][9],updaterank[0][10],updaterank[0][11],updaterank[0][12])
                maxupto15 =  max(updaterank[0][13],updaterank[0][14],updaterank[0][15],updaterank[0][16],updaterank[0][17],updaterank[0][18])
                newupdaterank=""
                newupdaterank=" update nlp_compare.question_gem_simliar_no set numberofKnowledge_Nor= "+str(updaterank[0][1]/maxupto5)+"," \
                           "numberofComprehension_Nor= " +str(updaterank[0][2]/maxupto5)  +",numberofApplication_Nor =" +str(updaterank[0][3]/maxupto5) +\
                     ",numberofAnalysis_Nor = " +str(updaterank[0][4]/maxupto5)  +",numberofSynthesis_Nor =" +str(updaterank[0][5]/maxupto5) +\
                     ",numberofEvaluation_Nor= " +str(updaterank[0][6]/maxupto5)  +",numberofKnowledge10_Nor =" +str(updaterank[0][7]/maxupto10) +\
                     ",numberofComprehension10_Nor= " +str(updaterank[0][8]/maxupto10)  +",numberofApplication10_Nor =" +str(updaterank[0][9]/maxupto10) +\
                     ",numberofAnalysis10_Nor= " +str(updaterank[0][10]/maxupto10)  +",numberofSynthesis10_Nor =" +str(updaterank[0][11]/maxupto10) +\
                     ",numberofEvaluation10_Nor= " +str(updaterank[0][12]/maxupto10) +",NumberofKnowledge15_Nor =" +str(updaterank[0][13]/maxupto15) +\
                    ",numberofComprehension15_Nor= " + str(updaterank[0][14]/maxupto15) +",numberofApplication15_Nor =" +str(updaterank[0][15]/maxupto15) +\
                    ",numberofAnalysis15_Nor= " + str(updaterank[0][16]/maxupto15)  +",numberofSynthesis15_Nor =" +str(updaterank[0][17]/maxupto15) +\
                    ",numberofEvaluation15_Nor= " + str(updaterank[0][18]/maxupto15)  +" where question_id =" + str(questionno) + ""
                print(newupdaterank)
                DBHandler().setData(newupdaterank)

                break;

        # index = similarities.MatrixSimilarity(corpus_lsi_tfidf)
        # index.save('Taxonomy_tfidf.index')
        #
        # query_lsi = lsi_tfidf[query_bow]

        query_similarities = enumerate(index[query_lsi])
        sort_key = lambda item: -item[1]
        sorted_similarities1 = sorted(query_similarities, key=sort_key)
        print(sorted_similarities1)

        # print ("With TDIDF:")
        # print ("\n".join(["%.10f - %s" % (score, documents[index]) for index, score in sorted_similarities]))

    #     SementicSimilarityChecker().insertSementicSimilarityData(taxonomyno,questionno,subjectcode,totalHighvalue,sumTotalvalue,valueWithOutTFIDF,valueWithTFIDF,sumvalueWithOutTFIDF,sumvvalueWithTFIDF)
    #
    #
    # def insertSementicSimilarityData(self,taxonomyID,questionno,subjectcode,totalHighvalue,sumTotalvalue,valueWithOutTFIDF,valueWithTFIDF,sumvalueWithOutTFIDF,sumvvalueWithTFIDF):
    #     text = ""
    #     if taxonomyID == 1:
    #         text = "UPDATE question_analysis_stem SET max_sen_value_A = '"+str(totalHighvalue)+"',sum_sen_value_A = '"+str(sumTotalvalue)+"',max_sen_TFIDF_A= '"+str(valueWithTFIDF)+ "',max_sen_NO_TFIDF_A = '"+str(valueWithOutTFIDF)+"',sum_sen_TFIDF_A = '"+str(sumvvalueWithTFIDF)+"',sum_sen_NO_TFIDF_A = '"+str(sumvalueWithOutTFIDF)+"' WHERE question_id='"+str(questionno)+"' and subject_code='"+str(subjectcode)+"'"
    #         print(text)
    #     elif taxonomyID == 2:
    #         text = "UPDATE question_analysis_stem SET max_sen_value_B = '"+str(totalHighvalue)+"',sum_sen_value_B = '"+str(sumTotalvalue)+"',max_sen_TFIDF_B= '"+str(valueWithTFIDF)+ "',max_sen_NO_TFIDF_B = '"+str(valueWithOutTFIDF)+"',sum_sen_TFIDF_B = '"+str(sumvvalueWithTFIDF)+"',sum_sen_NO_TFIDF_B = '"+str(sumvalueWithOutTFIDF)+"' WHERE question_id='"+str(questionno)+"' and subject_code='"+str(subjectcode)+"'"
    #     elif taxonomyID == 3:
    #         text = "UPDATE question_analysis_stem SET max_sen_value_C = '"+str(totalHighvalue)+"',sum_sen_value_C = '"+str(sumTotalvalue)+"',max_sen_TFIDF_C= '"+str(valueWithTFIDF)+ "',max_sen_NO_TFIDF_C = '"+str(valueWithOutTFIDF)+"',sum_sen_TFIDF_C = '"+str(sumvvalueWithTFIDF)+"',sum_sen_NO_TFIDF_C = '"+str(sumvalueWithOutTFIDF)+"' WHERE question_id='"+str(questionno)+"' and subject_code='"+str(subjectcode)+"'"
    #         print(text)
    #     elif taxonomyID == 4:
    #         text = "UPDATE question_analysis_stem SET max_sen_value_D = '"+str(totalHighvalue)+"',sum_sen_value_D = '"+str(sumTotalvalue)+"',max_sen_TFIDF_D= '"+str(valueWithTFIDF)+ "',max_sen_NO_TFIDF_D = '"+str(valueWithOutTFIDF)+"',sum_sen_TFIDF_D = '"+str(sumvvalueWithTFIDF)+"',sum_sen_NO_TFIDF_D = '"+str(sumvalueWithOutTFIDF)+"' WHERE question_id='"+str(questionno)+"' and subject_code='"+str(subjectcode)+"'"
    #     elif taxonomyID == 5:
    #         text = "UPDATE question_analysis_stem SET max_sen_value_E = '"+str(totalHighvalue)+"',sum_sen_value_E = '"+str(sumTotalvalue)+"',max_sen_TFIDF_E= '"+str(valueWithTFIDF)+ "',max_sen_NO_TFIDF_E = '"+str(valueWithOutTFIDF)+"',sum_sen_TFIDF_E = '"+str(sumvvalueWithTFIDF)+"',sum_sen_NO_TFIDF_E = '"+str(sumvalueWithOutTFIDF)+"' WHERE question_id='"+str(questionno)+"' and subject_code='"+str(subjectcode)+"'"
    #     elif taxonomyID == 6:
    #         text = "UPDATE question_analysis_stem SET max_sen_value_F = '"+str(totalHighvalue)+"',sum_sen_value_F = '"+str(sumTotalvalue)+"',max_sen_TFIDF_F= '"+str(valueWithTFIDF)+ "',max_sen_NO_TFIDF_F = '"+str(valueWithOutTFIDF)+"',sum_sen_TFIDF_F = '"+str(sumvvalueWithTFIDF)+"',sum_sen_NO_TFIDF_F = '"+str(sumvalueWithOutTFIDF)+"' WHERE question_id='"+str(questionno)+"' and subject_code='"+str(subjectcode)+"'"
    #     DBHandler().setData(text)


    def allquestionGensim(self,questionid,question):
        documents = DBHandler().getData("SELECT question FROM nlp_compare.question_list where Question_category !=0 and Quetion_OrderNo!=0")
        sentences = []
        for line in documents:
                sentences.append(line[0])



        self.getSementicSimilarityValues(sentences,questionid,question)

