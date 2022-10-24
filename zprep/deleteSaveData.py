import directory
import shutil
import tkinter
from appdirs import *

def delete_save_data():
    dir = directory.data_path.replace(directory.file_name, '').replace(directory.appname, '')
    shutil.rmtree(dir)

tki = tkinter.Tk()
tki.geometry("250x150")
tki.title(directory.appname)

text = tkinter.Label(text="本当にセーブデータを削除しますか？")
text.place(x=40, y=30)

yes_btn = tkinter.Button(tki, text= "はい", height=1, width=5,
                        command=lambda: [delete_save_data(), tki.destroy()])
yes_btn.place(x=50, y=80)

no_btn = tkinter.Button(tki, text= "いいえ", height=1, width=5,
                        command=lambda: tki.destroy())
no_btn.place(x=150, y=80)

tki.iconbitmap(directory.resource_path('../icon.ico'))

tki.mainloop()
