import nltk
from CONNECTION.DB_Handling import DBHandler
import itertools
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import RegexpTokenizer
import re
import re, math
from collections import Counter
WORD = re.compile(r'\w+')
class cosine_similarity_checker:



    def get_cosine_Question(self,vec1AssignmentStem, vec2ComAssignmentStem):
         intersection = set(vec1AssignmentStem.keys()) & set(vec2ComAssignmentStem.keys())
         numerator = sum([vec1AssignmentStem[x] * vec2ComAssignmentStem[x] for x in intersection])

         sum1 = sum([vec1AssignmentStem[x]**2 for x in vec1AssignmentStem.keys()])
         sum2 = sum([vec2ComAssignmentStem[x]**2 for x in vec2ComAssignmentStem.keys()])
         denominator = math.sqrt(sum1) * math.sqrt(sum2)

         if not denominator:
            return 0.0
         else:
            return float(numerator) / denominator

    def text_to_vector(self,text):
         words = WORD.findall(text)
         return Counter(words)

# generate cosine patter for each question stems based on the tag pattern, tag length as well as the question

    def run_for_each_category(self,taxonomy_id,tagpattern,taglongestlength,getquestion_id):
            print(taglongestlength)
            listpattern=[]
            sqlstring="select question_stem from question_stems where taxonomy_id=" + taxonomy_id + " and Tag_pattern='" + tagpattern + "'"
            listpattern=DBHandler().getData(sqlstring)
            print(listpattern)
            if(len(listpattern)):
                maxvaluelist=[]
                maxvalue=''
                for singlestem in listpattern:
                    mappattern=singlestem[0]
                    print("check pattern",mappattern)
                    print("tag logestlengh",taglongestlength)

                    vector1 = cosine_similarity_checker().text_to_vector(taglongestlength.lower())
                    vector2 = cosine_similarity_checker().text_to_vector(mappattern.lower())
                    cosine = cosine_similarity_checker().get_cosine_Question(vector1, vector2)
                    maxvaluelist.append(cosine)
                    print('taxonomy id',taxonomy_id)
                    print ('Cosine:', cosine)
                maxvalue=max(maxvaluelist)
                print("maxvalue for taxonomy",taxonomy_id,"- ",max(maxvaluelist),getquestion_id)
                cosine_similarity_checker().insert_cosine_database(taxonomy_id,maxvalue,getquestion_id)

#inserting the cosine value to the database.
    def insert_cosine_database(self,taxonomy_id,maxvalue,getquestion_id):
        checkquestionid=[]
        print("taxonomyno")
        sqlstatement="select * from question_max_cosine where question_id=" + str(getquestion_id)+ ""
        print(sqlstatement)
        checkquestionid=DBHandler().getData("select * from question_max_cosine where question_id=" + str(getquestion_id)+ "")
        if not(checkquestionid):
            insertstatement ="insert into question_max_cosine(question_id) values(" + str(getquestion_id)+ ")"
            print(insertstatement)
            DBHandler().setData(insertstatement)
        column_name=''
        if(taxonomy_id=='1'):
            column_name="max_cosine_A"
        if(taxonomy_id=='2'):
             column_name="max_cosine_B"
        if(taxonomy_id=='3'):
             column_name="max_cosine_C"
        if(taxonomy_id=='4'):
             column_name="max_cosine_D"
        if(taxonomy_id=='5'):
             column_name="max_cosine_E"
        if(taxonomy_id=='6'):
             column_name="max_cosine_F"

        updatesql="update question_max_cosine set " + column_name+ "=" + str(maxvalue) + " where question_id= " + str(getquestion_id)+ ""
        print(updatesql)
        DBHandler().setData(updatesql)

    def generateCosinepatterns(self,paperno,questionno):
        fullquestion=[]
        questioncosine = "select * from question_list where paperno =" +paperno+"  and question_id='" +str(questionno)+ "'  "
        fullquestion=DBHandler().getData(questioncosine)
        for onequetion in fullquestion:
            sentences = onequetion[2]
            DBHandler().setData("delete from temp_cosine_pattern_check")
        #questionset = DBHandler().getData("SELECT grammer_tag_pattern FROM question_stems where taxonomy_id ='" + str(i+1) + "'")
            TestQuestion = str(sentences)
            sentencesFile = TestQuestion.split(".")
            sentences = []

            for i in range(6):
                          print("taxonomy:" +str(i))
                          Allcorrectsentense = []
                          Allcorrecttagset = []
                          questionset = DBHandler().getData("SELECT grammer_tag_pattern FROM question_stems where taxonomy_id ='" + str(i+1) + "' order by No_tags asc")
                          grammer=""
                          for questionpattern in questionset:
                                questionpatterns= ''.join(questionpattern[0])
                                grammer = "Comprehension:{" + questionpatterns +  "}\n" + grammer
                          grammer = "r" + grammer + ""
                          #print(grammer)


                          #print(sentencesFile)
                          for line in sentencesFile:
                                #print(line)
                                tagPattern = ""
                                text = nltk.word_tokenize(line)
                                results = nltk.pos_tag(text)
                                print(results)
                                cp = nltk.RegexpParser(grammer)
                                tree = cp.parse(results)
                                for subtree in tree.subtrees():
                                            correctsentense = []
                                            correcttagset = []
                                            if subtree._label == 'Comprehension':
                                               for word in subtree.leaves():

                                                   correctsentense.append(word[0])
                                                   correcttagset.append(word[1])
                                            if correctsentense:
                                                 Allcorrectsentense.append(correctsentense)
                                                 Allcorrecttagset.append(correcttagset)
                          if(Allcorrectsentense):
                           #print(Allcorrectsentense)
                           #print(Allcorrecttagset)
                           print(Allcorrectsentense)

                           for correctsentense in Allcorrectsentense:
                               print(len(correctsentense))

                               for correctsentence,categoryii in zip(Allcorrectsentense,Allcorrecttagset):
                                     tense=[]
                                     questionid=2
                                     print(len(correctsentense))
                                     tagpattern = ' '.join(correctsentence)
                                     tagset = ','.join(categoryii)
                                     querystring = "INSERT INTO temp_cosine_pattern_check (question_id,blooms_taxonomy,tag_pattern,tag_text,tag_length)values(" + str(questionid) + "," + str(i+1) + ",'" + tagpattern + "','" + tagset  + "'," + str(len(correctsentense)) + ")"
                                     print(querystring)
                                     DBHandler().setData(querystring)

            selectlist =[]
            selectlist=DBHandler().getData("select  * from temp_cosine_pattern_check  order by tag_length desc  LIMIT 1 ")
            if(selectlist):
                print(''.join(selectlist[0][3]))
                taglongestlength=''.join(selectlist[0][3])
                fullvalue=[]
                for i in range(6):
                    getList=[]
                    getList=DBHandler().getData("select * from temp_cosine_pattern_check where blooms_taxonomy=" + str(i+1) +  "")
                    if(len(getList)):
                        print(str(i+1))
                        tagpattern=getList[0][4]
                        print(tagpattern)
                        cosine_similarity_checker().run_for_each_category(str(i+1),tagpattern,taglongestlength,onequetion[0])