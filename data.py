import json
import webbrowser
import random
import PySimpleGUI as sg


class Jobber:
    r = 0
    good_text = ""
    all_list = []
    # anime_list = []
    all_url = []
    sg.theme('DarkAmber')
    layout = [  [sg.Text('Наше ПО может:', font=('Montserrat', 18))], 
            [sg.Button('Вывести топ аниме', font=('Montserrat', 18), size = (25,1), key = '-top_anime-')],
            [sg.Button('Вывести случайное аниме', font=('Montserrat', 18), size = (25,1), key = '-random_anime-')],
            [sg.Button('Выйти из программы', font=('Montserrat', 18), size = (25,1), key = '-exit-')]]

    top_active, random_active = False, False

    def initialize(cls, file):
        with open(file) as t:
            cls.text = json.loads(t.read()) #Список словарей
    
    def pricheshi(cls):
        for slovar in cls.text:
            #cls.anime_list.append("№{} - ".format(slovar['pos']) + "Название: {} ───※ ·❆· ※─── ".format(slovar['title']) + "{} ───※ ·❆· ※─── ".format(slovar['type']) + "Количество эпизодов: {} ───※ ·❆· ※─── ".format(slovar['eps'].replace('eps', "")) + "URL: {}".format(slovar['URL']))
            cls.good_text += "№{} - ".format(slovar['pos']) + "Название: {}   ".format(slovar['title']) + "{}   ".format(slovar['type']) + "Количество эпизодов: {} ".format(slovar['eps'].replace('eps', "") + "\n")
            cls.all_list.append("№{} - ".format(slovar['pos']) + "Название: {}   ".format(slovar['title']) + "{}   ".format(slovar['type']) + "Количество эпизодов: {} ".format(slovar['eps'].replace('eps', "")))
            cls.all_url.append(slovar['URL'])

    def random_list(cls):
        cls.r = random.randint(0, len(cls.all_list))
        return [cls.all_list[cls.r], cls.all_url[cls.r]]

    def do_smth(cls): #Функционал: рандомное аниме, возможность сортировать список, огласите список, функция мне мало
        window = sg.Window('Аниме', cls.layout, element_justification='center')

        while True:  # Event Loop
            event, values = window.read()
            print(event, values)

            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            
            if not cls.top_active and event == '-top_anime-':
                cls.top_active = True
                top_layout = [[sg.Text(cls.good_text, font=('Montserrat', 10))],
                              [sg.Button('Закрыть окно', font=('Montserrat', 15), size = (15 ,1), key='-2_exit-'), ]]
                top_layout = [[sg.Text(cls.all_list[i], font=('Montserrat', 15)), sg.Button('URL', font=('Montserrat', 15), key = '')] for i in range(0, len(cls.all_list))]
                top_window = sg.Window('Топ аниме', top_layout)

            if cls.top_active:
                events2, values2 = top_window.Read()
                if events2 is None or events2 == '-2_exit-':
                    cls.top_active  = False
                    top_window.close()

            if not cls.random_active and event == '-random_anime-':
                cls.random_active = True
                random_layout = [[sg.Text(Jobber.random_list(Jobber)[0], font=('Montserrat', 18)), sg.Button('URL', font=('Montserrat', 18), key='-url_button-')],
                         [sg.Button('Закрыть окно', font=('Montserrat', 15), size = (15 ,1), key='-3_exit-')]]
                random_window = sg.Window('Случайное аниме', random_layout)

            if cls.random_active:
                events3, values3 = random_window.Read()
                if events3 is None or events3 == '-3_exit-':
                    cls.random_active  = False
                    random_window.close()
                    
            if event == '-exit-':
                window.close()

            try: 
                if events3 == '-url_button-':
                    webbrowser.open (cls.all_url[cls.r])
            except: pass

        window.close()

            # if line == "":
            #     print("Спасибо что воспользовались нашей программой")
            #     break
            # try:
            #     line = int(line)
            # except ValueError:
            #     print("Почему вы ввели не число?")
            # match line:
            


