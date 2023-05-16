import requests
import bs4


class Downloader:

    def __init__(self,URL,file_path,params=None):
        self.URL=URL
        self.file_path=file_path
        self.html=None
        self.params=params
        self.k=50
        
    def get_html(self):
        self.html=bs4.BeautifulSoup(requests.get(self.URL).text,features='html.parser')
        self.html=self.html.find_all("tr", class_="ranking-list")

    def save(self):
        with open(self.file_path, 'w') as output_file:
            output_file.write(str(self.html))
            
    def poshla_gorachay(self):
        for i in range(len(self.URL)-1,-1,-1):
            if i== '=':
                self.URL=self.URL[:i]
        self.html=bs4.BeautifulSoup(requests.get(self.URL+str(self.k)).text,features='html.parser')
        self.k+=50
        self.html=self.html.find_all("tr", class_="ranking-list")
        with open(self.file_path, 'w') as output_file:
            output_file.write(str(self.html))
        

