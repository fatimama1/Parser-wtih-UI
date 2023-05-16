import bs4
import json

class Parse:
    def __init__(self,input_file_path,output_file_path):
        self.input_file_path=input_file_path
        self.soup=None
        self.output_file_path=output_file_path
        self.title=[]
    
    def read(self):
        with open(self.input_file_path) as fp:
            self.soup=bs4.BeautifulSoup(fp,features='html.parser')

    def titles(self):
        k=1
        for i in self.soup.find_all("tr", class_="ranking-list"):
            name=i.find("h3", class_="hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3")
            inf=i.find('div',class_='information di-ib mt4')
            inf=inf.text.split('\n')
            for j in range(1,4):
                inf[j]=(inf[j].replace(' ','').split('('))
            self.title.append({'pos': k,
                           'title': name.text,
                           'URL': i.find('a')['href'],
                           'type': inf[1][0],
                           'eps': inf[1][1][:-1],
                           'date': inf[2],
                           'members': inf[3]})
            k+=1

    def save(self):
        self.title=json.dumps(self.title)
        with open(self.output_file_path, 'w') as output_file:
            output_file.write(self.title)
