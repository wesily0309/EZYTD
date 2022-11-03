#視窗
from cProfile import label
from pydoc import text
from tkinter import*
#
#
#
def Ytd():
    #抓取輸入框訊息
    gui輸入目錄=inp.get()
    gui輸入連結=inp2.get()
    #變數設定
    from pytube import YouTube
    輸入連結=gui輸入連結
    #print(type(輸入連結))
    輸入下載檔案目錄=gui輸入目錄
    yt = YouTube(輸入連結)#C:\\Video
    #下載
    stream = yt.streams.first()
    print(yt.title + '')# 輸出影片標題
    yt.streams.filter().get_highest_resolution().download(輸入下載檔案目錄)#下載處理
    print(yt.title + " 檔案已在下載資料夾")
    input()
#視窗設定
win=Tk()
win.title("yt影片下載器")

#lb
lb=Label(text="分別輸入目錄和影片連結")
lb.pack()
#輸入框(下載目錄)
inp=Entry()
inp.pack()
#輸入框(下載連節)
inp2=Entry()
inp2.pack()
#按鈕
button =Button(win, text= '下載') 
button.config(command=Ytd)
button.pack()

win.mainloop()#設為常駐視窗

                   