import re
pat = re.compile('\d{4}(?=[-])')
class Paper:
    def __init__(self,paperID,type,title,volume,issue,views,citations,year):
        self._paperID = paperID
        self._type = type
        self._title = title
        self._volume = volume
        self._issue = issue
        self._views = views
        self._citations = citations
        self._authors = []
        self._year = int(pat.match(year).group())
        
    def printInfo(self):
        fmt = 'paperID: {}\ntitle: {}\ntype: {}\nyear: {}\nvolume: {}\nissue: {}\nviews: {}\ncitations: {}'
        print(fmt.format(self._paperID,self._title,self._type,self._year,self._volume,self._issue,self._views,self._citations))

    def printAuthors(self):
        for i in self._authors:
            print(i.fullname)
        
    def __str__(self):
        return self._title
        
    @property
    def paperID(self):
        return self._paperID
    
    @property
    def type(self):
        return self._type
    
    @property
    def title(self):
        return self._title
    
    @property
    def volume(self):
        return self._volume
    
    @property
    def issue(self):
        return self._issue
    
    @property
    def views(self):
        return self._views
    
    @property
    def citations(self):
        return self._citations
    
    @property
    def authors(self):
        return self._authors
    
    @property
    def year(self):
        return self._year
    
    @paperID.setter
    def paperID(self,para):
        self._paperID = para
        
    @type.setter
    def type(self,para):
        self._type = para
        
    @title.setter
    def title(self,para):
        self._title = para
        
    @volume.setter
    def volume(self,para):
        self._volume = para
        
    @issue.setter
    def issue(self,para):
        self._issue = para
        
    @views.setter
    def views(self,para):
        self._views = para
        
    @citations.setter
    def citations(self,para):
        self._citations = para
        
    @authors.setter
    def authors(self,para):
        self._authors = para
        
    @year.setter
    def year(self,para):
        self._year = para
