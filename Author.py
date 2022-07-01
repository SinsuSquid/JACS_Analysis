class Author:
    def __init__(self,authorID,forename,initials,surname):
        self._authorID = authorID
        self._forename = forename
        self._initials = initials
        self._surname = surname
        self._fullname = Author.getFullName(forename,initials,surname)
        self._papers = []
        
    @staticmethod
    def getFullName(forename,initials,surname):
        return ' '.join([forename,initials,surname])
    
    def printInfo(self):
        fmt = 'authorID : {}\nforename: {}\ninitials: {}\nsurname: {}\nfullname: {}'
        print(fmt.format(self._authorID,self._forename,self._initials,self._surname,self._fullname))

    def printPapers(self):
        for i in self._papers:
            print(i.title)
        
    def __str__(self):
        return self._fullname
    
    @property
    def authorID(self):
        return self._authorID
    
    @property
    def forename(self):
        return self._forename
    
    @property
    def initials(self):
        return self._initals
    
    @property
    def surname(self):
        return self._surname
    
    @property
    def fullname(self):
        return self._fullname
    
    @property
    def papers(self):
        return self._papers
    
    @authorID.setter
    def authorID(self,para):
        self._authorID = para
        
    @forename.setter
    def forename(self,para):
        self._forename = para
        
    @initials.setter
    def initials(self,para):
        self._initals = para
        
    @surname.setter
    def surname(self,para):
        self._surname = para
        
    @fullname.setter
    def fullname(self,para):
        self._fullname = para
        
    @papers.setter
    def papers(self,para):
        self._papers = para
