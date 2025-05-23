from PyQt5.QtWidgets import QWidget,QHBoxLayout,QInputDialog, QPushButton, QLabel, QApplication, QListWidget, QTextEdit, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
import json



def search_tag():
    tag = write_teg.text()
    if tag != '' and search_teg.text() == 'Найти заметку по тегу':
        notes_filtered= dict()
        for key in notes:
            if tag in notes[key]['теги']:
                notes_filtered[key] = notes[key]
        search_teg.setText('Сбросить поиск')
        zametka_list.clear()
        teg_list.clear()
        text.clear()
        zametka_list.addItems(notes_filtered)
    else:
        zametka_list.clear()
        zametka_list.addItems(notes)
        write_teg.clear()
        search_teg.setText('Найти заметку по тегу')

def del_tag():
    if teg_list.selectedItems():
        key = zametka_list.selectedItems()[0].text()
        tag = teg_list.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
        teg_list.clear()
        teg_list.addItems(notes[key]['теги'])
        with open('notes_data.json','w') as file:
                json.dump(notes, file, sort_keys=True, ensure_ascii=False)





def add_tag():
    if zametka_list.selectedItems():
        key = zametka_list.selectedItems()[0].text()
        tag =  write_teg.text()
        if tag != '' and not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            teg_list.addItem(tag)
            write_teg.clear()
            with open('notes_data.json','w') as file:
                json.dump(notes, file, sort_keys=True, ensure_ascii=False)


def save_note():
    if zametka_list.selectedItems():
        key = zametka_list.selectedItems()[0].text()
        
        notes[key]['текст']=text.toPlainText()
        with open('notes_data.json','w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)




def del_note():
    if zametka_list.selectedItems():
        key = zametka_list.selectedItems()[0].text()
        del notes[key]
        text.clear()
        zametka_list.clear()
        teg_list.clear()
        zametka_list.addItems(notes)
        with open('notes_data.json','w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)




def show_note():
    key = zametka_list.selectedItems()[0].text()
    text.setText(notes[key]['текст'])
    teg_list.clear()
    teg_list.addItems(notes[key]['теги'])



def add_note(): 
    notes_name, ok  = QInputDialog.getText(window,'добавить заметку','Название заметки:')
    if ok:
        notes[notes_name] = {
            'текст':'',
            'теги':[]
        }
    zametka_list.clear()
    zametka_list.addItems(notes)
    with open ('notes_data.json','w') as file:
        json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    

app = QApplication([])
print('bnhbhub')
window = QWidget()
window.resize(900,600)





                                            #создание линий
h1_line = QHBoxLayout()                             
h2_line = QHBoxLayout()
h3_line = QHBoxLayout()
v1_line = QVBoxLayout()
v2_line = QVBoxLayout()



                                            #создание виджетов
text = QTextEdit()                            
zametka = QLabel('Список заметок')
zametka_list = QListWidget()
create_zametka = QPushButton('Создать заметку')
delet_zametka = QPushButton('Удалить заметку')
allow_zametka = QPushButton('сохранить заметку')
teg = QLabel('Список тегов')
teg_list = QListWidget()
write_teg = QLineEdit()
write_teg.setPlaceholderText('Введите тег....')
create_teg = QPushButton('Добавить к заметке')
delet_teg = QPushButton('Открепить от заметки')
search_teg = QPushButton('Найти заметку по тегу')


                                    #Крепление виджетов к линиии
v1_line.addWidget(text)
v2_line.addWidget(zametka)
v2_line.addWidget(zametka_list)   
v2_line.addLayout(h2_line)


h2_line.addWidget(create_zametka)
h2_line.addWidget(delet_zametka)
 
v2_line.addWidget(allow_zametka)   
v2_line.addWidget(teg)
v2_line.addWidget(teg_list) 
v2_line.addWidget(write_teg)  
v2_line.addLayout(h3_line)
v2_line.addWidget(search_teg)   

h3_line.addWidget(create_teg)
h3_line.addWidget(delet_teg)


h1_line.addLayout(v1_line)
h1_line.addLayout(v2_line)





window.setLayout(h1_line)





with open ('notes_data.json','r') as file:
    notes = json.load(file)



zametka_list.addItems(notes)
zametka_list.itemClicked.connect(show_note)
create_zametka.clicked.connect(add_note)
delet_zametka.clicked.connect(del_note)
allow_zametka.clicked.connect(save_note)
create_teg.clicked.connect(add_tag)
delet_teg.clicked.connect(del_tag)
search_teg.clicked.connect(search_tag)


window.show()
app.exec_()
