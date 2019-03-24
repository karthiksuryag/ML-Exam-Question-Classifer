from gensim import corpora, models, similarities
from CONNECTION.DB_Handling import DBHandler

class SementicSimilarityChecker:


    def getSementicSimilarityValues(self,taxonomyno,documents,questionno,subjectcode,query):

        stoplist = set('for a of the and to in'.split())
        QuestionWords = [[word for word in document.lower().split() if word not in stoplist]
                 for document in documents]
        all_tokens = sum(QuestionWords, [])
        tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
        QuestionWords = [[word for word in text if word not in tokens_once]
                 for text in QuestionWords]
        dictionary = corpora.Dictionary(QuestionWords)
        dictionary.save('Taxonomy.dict')
        corpus = [dictionary.doc2bow(text) for text in QuestionWords]
        corpora.MmCorpus.serialize('Taxonomy.mm', corpus)
        tfidf = models.TfidfModel(corpus)
        corpus_tfidf = tfidf[corpus]
        lsi_tfidf = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=100)
        lsi_tfidf.save('Taxonomy.lsi_tfidf')
        corpus_lsi_tfidf = lsi_tfidf[corpus_tfidf]
        lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=100)
        corpus_lsi = lsi[corpus]
        index = similarities.MatrixSimilarity(corpus_lsi)
        index.save('Taxonomy.index')
        query_bow = dictionary.doc2bow(query.lower().split())
        Query_LSI = lsi[query_bow]
        query_similarities = enumerate(index[Query_LSI])
        sort_key = lambda item: -item[1]
        sorted_similarities = sorted(query_similarities, key=sort_key)


        valueWithOutTFIDF = sorted_similarities[0][1]
        sumvalueWithOutTFIDF = sum(sorted_similarities[0])

        # print( "Without TDIDF:")
        # print ("\n".join(["%.10f - %s" % (score, documents[index]) for index, score in sorted_similarities]))

        index = similarities.MatrixSimilarity(corpus_lsi_tfidf)
        index.save('Taxonomy_tfidf.index')

        query_lsi = lsi_tfidf[query_bow]

        query_similarities = enumerate(index[query_lsi])
        sort_key = lambda item: -item[1]
        sorted_similarities1 = sorted(query_similarities, key=sort_key)


        valueWithTFIDF = sorted_similarities1[0][1]
        sumvvalueWithTFIDF = sum(sorted_similarities1[0])

        totalHighvalue =(valueWithOutTFIDF+valueWithTFIDF)/2.0
        sumTotalvalue = (sumvalueWithOutTFIDF+sumvvalueWithTFIDF)

        # print(totalHighvalue)
        # print(sumTotalvalue)
        # print ("-" * 80)
        # print ("With TDIDF:")
        # print ("\n".join(["%.10f - %s" % (score, documents[index]) for index, score in sorted_similarities]))

        SementicSimilarityChecker().insertSementicSimilarityData(taxonomyno,questionno,subjectcode,totalHighvalue,sumTotalvalue,valueWithOutTFIDF,valueWithTFIDF,sumvalueWithOutTFIDF,sumvvalueWithTFIDF)


    def insertSementicSimilarityData(self,taxonomyID,questionno,subjectcode,totalHighvalue,sumTotalvalue,valueWithOutTFIDF,valueWithTFIDF,sumvalueWithOutTFIDF,sumvvalueWithTFIDF):
        text = ""

        if taxonomyID == 1:
            text = "UPDATE question_analysis_stem SET max_sen_value_A = '"+str(totalHighvalue)+"',sum_sen_value_A = '"+str(sumTotalvalue)+"',max_sen_TFIDF_A= '"+str(valueWithTFIDF)+ "',max_sen_NO_TFIDF_A = '"+str(valueWithOutTFIDF)+"',sum_sen_TFIDF_A = '"+str(sumvvalueWithTFIDF)+"',sum_sen_NO_TFIDF_A = '"+str(sumvalueWithOutTFIDF)+"' WHERE question_id='"+str(questionno)+"' and subject_code='"+str(subjectcode)+"'"
            print(text)
        elif taxonomyID == 2:
            text = "UPDATE question_analysis_stem SET max_sen_value_B = '"+str(totalHighvalue)+"',sum_sen_value_B = '"+str(sumTotalvalue)+"',max_sen_TFIDF_B= '"+str(valueWithTFIDF)+ "',max_sen_NO_TFIDF_B = '"+str(valueWithOutTFIDF)+"',sum_sen_TFIDF_B = '"+str(sumvvalueWithTFIDF)+"',sum_sen_NO_TFIDF_B = '"+str(sumvalueWithOutTFIDF)+"' WHERE question_id='"+str(questionno)+"' and subject_code='"+str(subjectcode)+"'"
        elif taxonomyID == 3:
            text = "UPDATE question_analysis_stem SET max_sen_value_C = '"+str(totalHighvalue)+"',sum_sen_value_C = '"+str(sumTotalvalue)+"',max_sen_TFIDF_C= '"+str(valueWithTFIDF)+ "',max_sen_NO_TFIDF_C = '"+str(valueWithOutTFIDF)+"',sum_sen_TFIDF_C = '"+str(sumvvalueWithTFIDF)+"',sum_sen_NO_TFIDF_C = '"+str(sumvalueWithOutTFIDF)+"' WHERE question_id='"+str(questionno)+"' and subject_code='"+str(subjectcode)+"'"
            print(text)
        elif taxonomyID == 4:
            text = "UPDATE question_analysis_stem SET max_sen_value_D = '"+str(totalHighvalue)+"',sum_sen_value_D = '"+str(sumTotalvalue)+"',max_sen_TFIDF_D= '"+str(valueWithTFIDF)+ "',max_sen_NO_TFIDF_D = '"+str(valueWithOutTFIDF)+"',sum_sen_TFIDF_D = '"+str(sumvvalueWithTFIDF)+"',sum_sen_NO_TFIDF_D = '"+str(sumvalueWithOutTFIDF)+"' WHERE question_id='"+str(questionno)+"' and subject_code='"+str(subjectcode)+"'"
        elif taxonomyID == 5:
            text = "UPDATE question_analysis_stem SET max_sen_value_E = '"+str(totalHighvalue)+"',sum_sen_value_E = '"+str(sumTotalvalue)+"',max_sen_TFIDF_E= '"+str(valueWithTFIDF)+ "',max_sen_NO_TFIDF_E = '"+str(valueWithOutTFIDF)+"',sum_sen_TFIDF_E = '"+str(sumvvalueWithTFIDF)+"',sum_sen_NO_TFIDF_E = '"+str(sumvalueWithOutTFIDF)+"' WHERE question_id='"+str(questionno)+"' and subject_code='"+str(subjectcode)+"'"
        elif taxonomyID == 6:
            text = "UPDATE question_analysis_stem SET max_sen_value_F = '"+str(totalHighvalue)+"',sum_sen_value_F = '"+str(sumTotalvalue)+"',max_sen_TFIDF_F= '"+str(valueWithTFIDF)+ "',max_sen_NO_TFIDF_F = '"+str(valueWithOutTFIDF)+"',sum_sen_TFIDF_F = '"+str(sumvvalueWithTFIDF)+"',sum_sen_NO_TFIDF_F = '"+str(sumvalueWithOutTFIDF)+"' WHERE question_id='"+str(questionno)+"' and subject_code='"+str(subjectcode)+"'"
        DBHandler().setData(text)

    def tagpattern_Gensim_Algorithm(self,questionno,getsubject,questions):

        #questionsList = DBHandler().getData("SELECT * from question_list where question_id BETWEEN 460 AND 529")
        #print(len(questionsList))
        taxonomyList = []

        myQuery = "Insert into question_analysis_stem (question_id,subject_code) values ("+ str(questionno) +",'"+ str(getsubject) +"')"
        print(myQuery)
        DBHandler().setData(myQuery);
        for i in range(6):
                  print("taxonomy:" +str(i))
                  documents = DBHandler().getData("SELECT question_stem FROM question_stems where taxonomy_id = '"+str(i + 1)+"'")
                  sentences = []
                  for line in documents:
                    sentences.append(line[0])
                  self.getSementicSimilarityValues((i+1),sentences,questionno,getsubject,questions)
