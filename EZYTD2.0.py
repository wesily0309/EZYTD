from pytube import YouTube
輸入連結=input('輸入影片連結')
輸入下載檔案目錄=input('輸入下載檔案目錄:')#EX:
yt = YouTube(輸入連結)##C:\\Video
#以上變數設定#EX:
#以下為下載處理
stream = yt.streams.first()
print(yt.title + '')# 輸出影片標題
yt.streams.filter().get_highest_resolution().download(輸入下載檔案目錄)#下載處理
print(yt.title + " 檔案已在下載資料夾")
input()

