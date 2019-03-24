from CONNECTION.DB_Handling import DBHandler
import nltk

class pattern_generation:

    def generation(self):

        QuestionStemList = DBHandler().getData("SELECT * from question_stems where pattern_set ='no' ")
        for Question in QuestionStemList:
            TagPatterngrammer=""
            Tagpattern = []
            print(Question[2])
            text = nltk.word_tokenize(Question[2])
            results= nltk.pos_tag(text)
            for(word,tag)in results:
                Tagpattern.append(tag)
                TagPatterngrammer+="<"+tag+">"
            covertstring = ','.join(Tagpattern)
            print(covertstring)
            patternset="yes"
            updatestring = "update question_stems set Tag_pattern= '" +\
                           str(covertstring) + "',grammer_tag_pattern='"  \
                           + TagPatterngrammer + "',pattern_set='"  + patternset \
                           + "',No_tags=" +str(len(Tagpattern))+ " where id="+str(Question[0])+ " and taxonomy_id=" +str(Question[1])+  ""
            DBHandler().setData(updatestring)
