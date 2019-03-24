import re
import string
from CONNECTION.DB_Handling import DBHandler

class Extract:


# this function is used to extract the questions from the papers before inserting it to the
# database

    def BreakText(self,file,academicYear,subjectCode,semester,paperNo):
        print("start")
        list=[]
        for line in file:
           list.append(line.strip())
        AllQuestion = ''.join(list)
        questionmarks = 0
        noOfMainQuestions = len(re.findall(r'\[Q\d\]',AllQuestion))
        for num in range(1,noOfMainQuestions+1):
            mainbody = []
            if(num != noOfMainQuestions):
                mainbody = re.findall(r"\[Q"+str(num)+"\](.*)\[Q"+str(num+1)+"\]",AllQuestion)
            else:
                mainbody = re.findall(r"\[Q"+str(num)+"\](.*)",AllQuestion)
            noOfSubQuestions = len(re.findall(r'\(\d\)',''.join(mainbody)))
            mainQuestion = (re.findall(r"\[Q"+str(num)+"\](.*?)\(1\)",AllQuestion))

            # DBHandler().setData("Insert Into question_list (main_question_id,sub_id,sub_sub_id,"
            #                    "academic_year,subject_code,question) VALUES ('"+str(num)+"',"
            #                    "'"+str(0)+"','"+str(0)+"','"+str(Extract.AcademicYear)+"','"+
            #                    str(Extract.SubjectCode)+"','"+mainQuestion[0]+"')")

            print(mainQuestion)
            # insertquestion ="insert into question_list(subject_code,question,Years,Semester,questionmarks,paperno)" \
            #             "values('"+subjectCode+ "','"+ mainQuestion[0] +"',"+academicYear \
            #             +"," +semester+","+questionmarks +","+paperNo+")"
            # print(insertquestion)
            # DBHandler().setData(insertquestion)

            for index in range(1,noOfSubQuestions+1):
                subBody = []
                if(index != noOfSubQuestions):
                    subBody = re.findall(r"\("+str(index)+"\)(.*)\("+str(index+1)+"\)",''.join(mainbody))
                else:
                    subBody = re.findall(r"\("+str(index)+"\)(.*)",''.join(mainbody))

                noOfSub_SubQuestions = len(re.findall(r'\([a-z]\)',''.join(subBody)))

                if(noOfSub_SubQuestions != 0):
                    subQuestion = (re.findall(r"\("+str(index)+"\)(.*?)\(a\)",''.join(mainbody)))
                    # DBHandler().setData("Insert Into question_list (main_question_id,sub_id,sub_sub_id,academic_year,subject_code,question) VALUES ('"+str(num)+"','"+str(index)+"','"+str(0)+"','"+str(Extract.AcademicYear)+"','"+str(Extract.SubjectCode)+"','"+subQuestion[0]+"')")

                elif(noOfSub_SubQuestions == 0):
                    print(subBody)
                    # DBHandler().setData("Insert Into question_list (main_question_id,sub_id,sub_sub_id,academic_year,subject_code,question) VALUES ('"+str(num)+"','"+str(index)+"','"+str(0)+"','"+str(Extract.AcademicYear)+"','"+str(Extract.SubjectCode)+"','"+subBody[0]+"')")

                for part in range(1,noOfSub_SubQuestions+1):
                    sub_SubBody = []
                    if(part != noOfSub_SubQuestions):
                        sub_SubBody = re.findall(r"\("+chr(97+part-1)+"\)(.*)\("+chr(97+part)+"\)",''.join(subBody))
                        print(sub_SubBody)

                    else:
                        sub_SubBody = re.findall(r"\("+chr(97+part-1)+"\)(.*)",''.join(subBody))
                        print(sub_SubBody)
                    # DBHandler().setData("Insert Into question_list (main_question_id,sub_id,sub_sub_id,academic_year,subject_code,question) VALUES ('"+str(num)+"','"+str(index)+"','"+str(part)+"','"+str(Extract.AcademicYear)+"','"+str(Extract.SubjectCode)+"','"+sub_SubBody[0]+"')")


