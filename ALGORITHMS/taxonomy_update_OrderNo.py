from CONNECTION.DB_Handling import DBHandler


DataList = DBHandler().getData("SELECT Question_category,question_id from question_list ")
for newLine in DataList:
    updatesql="update question_dataset set question_category='" +str(newLine[0])+ "' where question_id='"+ str(newLine[1]) +"'"
    DBHandler().setData(updatesql)
    print(updatesql)