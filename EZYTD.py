from pytube import YouTube
輸入連結=input('輸入影片連結')
輸入下載檔案目錄=input('輸入下載檔案目錄=')
path=輸入下載檔案目錄#EX:
link=輸入連結       #C:\\Video
yt = YouTube(link)
#以上變數處理
#以下為下載處理
stream = yt.streams.first()
print(yt.title + ' 下載完成')
stream.download(path)
print(yt.title + " 檔案已在下載資料夾")

