from pytube import YouTube
from pytube import exceptions


def welcome():
  print("""
            :7L7.                                                                 :                                                                                                                                                                                                   
     .BBBu:.rdBBBQ                                                             BBd    rBBBBBBBBBBBBBBBBBB               .
   vBBr    7    BBBi                                                           BB   1BBB7   BBBBPEBBBBBD             BBBB.
  BBB   BBBB    rBBB                                                          .BB  QBB.    rBBBB                    vBBBB
 BBB   BBBBB     BBBB                                                         BB.  BBB     BBBB7                    BBBB:
 BBB   BBBB      BBBB     iBBBBB.     BBBB   :BBBB  BBBE   BBBB uBBBU         BB  .BBi     BBBB     BBBB   .BBBB    BBBBbBBB5       iBBBBB:
 IBB  .BBBB      BBBB   7BBBB  BBr   BBBBB   BBBBR  7BBB  BBBBBBBBBBBB       7BQ   BBE    MBBBB    MBBBB   BBBBB   PBBBBsiQBBB    7BBBP  BB
      BBBBg     5BBBB  BBBBS   BBB   BBBB    BBBB     BB  BBBBQ   BBBB       BB           BBBB.    BBBB:   BBBB    BBBB.   BBB.  BBBBv   BB
      BBBB      BBBBr PBBBB   iBBBBPBBBBB   XBBBB     BZ :BBBB    BBBB       BB          .BBBB     BBBB   vBBBB    BBBB    2BBi 2BBBB   BBi
     vBBBB      BBBB  BBBB     BBR  BBBBg   BBBBi    BB  BBBBq   BBBB.      PB5          BBBBQ    BBBBB   BBBBJ   BBBBB    BBB  BBBBv BBB
     BBBBs     BBBBi UBBBB     BB   BBBB    BBBB    .BB  BBBB    BBBB       BB           BBBB     BBBB    BBBB    BBBB     BBB :BBBBPP:
     BBBB     BBBBQ  BBBBB    BBB  7BBBB   BBBBQ    BB  jBBBB   uBBBs   BY  BB          7BBBB    :BBBB   BBBBB   UBBBB    BBB  MBBBB       B:
    DBBBB    BBBBD   5BBBB   BBB   QBBBB  BBBBBB  BBB   BBBBv   BBBBB  BB  BBr          BBBBS    PBBBB  BBBBBB  QBBBBB   BBB.  7BBBB     BB:
    BBBBBBBBBBBB.     BBBBBBBBi     BBBBBBi.BBBBBBBv   .BBBB     BBBBBBB   BB           BBBB      BBBBBBv BBBBBBg BBBBBBBBM     BBBBBBBBB2
    :...  idgJ           :r.         .7i     .r7:       :...      .rr     .BB           :...       .7r     .7i      :77:          .rvr
                                                                          BB.                                                                                                                                
                                                                          BB                                                                                                                                                                                                        
                                                                         jBB                                                                                                                                                                                                        
                                                                         BB                                                                                                                                                                                                         
  """)


i = 0
is_url_ok = True
welcome()
global video
global itag
while is_url_ok:
    try:
        url_str = input("\r\n"+"Add the URL address to the video you wish to download:")
        video = YouTube(url_str)
        is_url_ok = False
    except exceptions.RegexMatchError:
        print("\r\n" + "Please enter a valid argument. We support downloading only Youtube videos.")
        continue
        pass
video_title = video.title
video_thumbnail = video.thumbnail_url
video_views = video.views
video_published = video.publish_date
video_published = video_published.date()
video_streams = video.streams
vid_info = "The video\'s title is \"{}\" it was published on {} and it has {} views as of current."
is_downloading = True
print("\r\n"+vid_info.format(video_title, video_published, f"{video_views:,}"))
print("\r\n"+"Available download types for the video:"+"\r\n")
while i < len(video_streams):
    print(video_streams[i])
    i += 1

itag = int()

while is_downloading:
    try:
        itag = input("\r\n"+"Choose which version of the video you want to download by entering the according \"itag\" number:")
        stream = video.streams.get_by_itag(itag)
        stream.download()
        print("\r\n" + "Downloading video..." + "\r\n")
        is_downloading = False
    except AttributeError:
        print("\r\n" + "No such version of the video exists.")
        continue
        pass
    except ValueError:
        print("\r\n" + "Please enter a valid itag number.")
        continue
        pass

print("\r\n"+"Download Successful! Thank you for using Down/Tube!"+"\r\n")





































