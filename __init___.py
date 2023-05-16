from download import Downloader
from parse import Parse
from data import Jobber

def process(url,path,path2):
    downloader = Downloader(url, path)
    downloader.get_html()
    downloader.save()
    parse = Parse(path, path2)
    parse.read()
    parse.titles()
    parse.save()

    Jobber.initialize(Jobber, path2)
    Jobber.pricheshi(Jobber)
    Jobber.do_smth(Jobber)

process("https://myanimelist.net/topanime.php","parser\download","parser\parse")
