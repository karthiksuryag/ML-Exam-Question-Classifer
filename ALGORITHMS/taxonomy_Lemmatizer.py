from nltk.stem import WordNetLemmatizer

class Lemmatizer:

    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def getLematizedWord(self, list):
        """

        :rtype : object
        """
        newList = []
        for word in list:
            newList.append(self.lemmatizer.lemmatize(word, pos='v'))
        return newList
