from pygame import mixer
import random

class Infofolder:
     def __init__(self, infofolderdirectory, playdirectory):
         self.infofolderdirectory = infofolderdirectory # Music File Direcctory
         self.playdirectory = playdirectory # play File Directory
         
##  song file contain all songs information
     def Infofile(self):
          with open(self.infofolderdirectory, "r") as infofile:
               infofile = open(self.infofolderdirectory, "r")
          infolist = infofile.read()
          return infolist
     
# Play Directory that will play certain song
     def Linklist(self, index = 0):
          linklist = []
          with open(self.infofolderdirectory, "r") as infofile:
               infofile = open(self.infofolderdirectory, "r")
          link = infofile.read().splitlines()
          while True:
                try:
                   linklist.append("{}{}.mp3".format(self.playdirectory, link[index]))
                   index += 1
                except IndexError:
                       break
          return linklist

class Song:
     def __init__(self, infolist):
        self.infolist = infolist
        
# Song List                         
     def Songlist(self, index = 0):
         songlist = []
         infolist = self.infolist.splitlines()
         while True:
               try:
                   detail = infolist[index]
                   songname = detail[detail.index("-")+2:len(detail)]
                   if "-" in detail.split()[0]:
                      songlist.append(detail[len(detail.split()[0])+3:len(detail)])
                   else:
                        songlist.append(songname)
                   index += 1                       
               except IndexError:
                      break
         return songlist
     
     def Play(self, songlink):
         mixer.init()
         mixer.music.load(songlink)
         mixer.music.play()
     
     def Shuffle(self):
         linklist = self.linklist
         songname = random.choice(linklist)
         shufflesongindex = linklist.index(songname)
         return songindex

     def Nextsong(self, songlist, songindex):
         if songindex == len(songlist)-1:
            nextsongindex = 0
         else:
              nextsongindex = songindex+1 
         return nextsongindex
     
     def Previoussong(self, songlist, songindex):
         if songindex == 0:
            previoussongindex = len(songlist)-1
         else:
              previoussongindex = songindex-1
         return previoussongindex

class Artist:
     def __init__(self, infolist, linklist):
         self.infolist = infolist
         self.linklist = linklist
         
# Artist List
     def Artistlist(self, index = 0):
         artistlist = []
         infolist = self.infolist.splitlines()
         while True:
               try:
                   detail = infolist[index]
                   artistname = detail[0:detail.index("-")-1]
                   if len(artistlist) == 0:
                      if "-" in detail.split()[0]:
                         artistlist.append(detail.split()[0])
                      else:
                           artistlist.append(artistname)         
                   else:
                        if "-" in detail.split()[0]:
                             if detail.split()[0] in artistlist: pass
                             else:
                                  artistlist.append(detail.split()[0])
                        elif artistname in artistlist: pass
                        else:
                             artistlist.append(artistname)
                   index += 1
               except IndexError:
                      break
         return artistlist   

## artist song
     def Artistsonglist(self, songlist, artistlist, index = 0):
         artistsonglist = []
         infolist = self.infolist.splitlines()
         while True:
               try:
                   artistsong = []
                   artistname = artistlist[index]          
                   for info in infolist:
                       if artistname in info:
                          artistsong.append(songlist[infolist.index(info)])                        
                   artistsonglist.append(artistsong)
                   index += 1
               except IndexError:
                      break
         return artistsonglist

# artist song link list
     def Artistsonglinklist(self, artistsonglist, index = 0):
         artistssonglinklist = []
         linklist = self.linklist
         while True:
               try:
                   artistsonglinklist = []
                   artistsong = artistsonglist[index]
                   for songname in artistsong:
                       for link in linklist:
                           if songname in link:
                              artistsonglinklist.append(link)
                   artistssonglinklist.append(artistsonglinklist)
                   index += 1
               except IndexError:
                      break
         return artistssonglinklist

class Favouritesong:
     def __init__(self, favouritesongdiroctory, songlist):
        self.favouritesongdiroctory = favouritesongdiroctory
        
     def Like(self, songname):
         likesongfolder = self.favouritesongdiroctory
        

     def Like(self):
         likesongfolder = self.favouritesongdiroctory
         with open(likesongfolder, "r") as likefile:
              likefile = open(likesongfolder , "r")
         likelist = likefile.readlines()
         if likedsong in likelist:
            pass
         else:
               with open(likesongfolder, "a") as likefile:
                    likefile = open(likesongfolder , "a")
               likefile.write("{}\n".format(likedsong))

##  lyrics file contains the lyrics
class Lyrics:
     def __init__(self, lyricsfolderdirectory):
        self.lyricsfolderdirectory = lyricsfolderdirectory # Lyrics File Directory

     def Show(self, songlist, songindex):
         lyricsfolderdirectory = self.lyricsfolderdirectory
         lyricsname = songlist[songindex]
         lyricsfiledirectory = "{}\{}.txt".format(lyricsfolderdirectory, lyricsname)
         with open(lyricsfiledirectory, "r") as lyricsfile:
              lyricsfile = open(lyricsfiledirectory, "r")
         lyrics = lyricsfile.read()
         return "\n{}\nThe End\n".format(lyrics)

class Page:
     def __init__(self, songlist, artistlist, artistsonglist):
         self.songlist = songlist
         self.artistlist = artistlist
         self.artistsonglist = artistsonglist
         
     def Artistsongpage(self, pageindex): 
         print("\n{}:".format(self.artistlist[pageindex]))
         artistsonglist = self.artistsonglist[pageindex]
         return artistsonglist
     
class UserInterface:
     def __init__(self, songlist, artistlist, artistsonglist):
         self.songlist = songlist
         self.artistlist = artistlist
         self.artistsonglist = artistsonglist

     def Show(self, List, gener, index = 0): 
         while True:
               try:
                   print(List[index])
                   index += 1
               except IndexError:
                      break
         return "{} {}\n".format(len(List), gener)
                    
     def Nowplaying(self, songlist, songindex): 
         artistlist = self.artistlist
         artistsonglist = self.artistsonglist
         songname = songlist[songindex]
         for List in artistsonglist:
             if songname in List:
                artistname = artistlist[artistsonglist.index(List)] 
         return "\nNow playing:\n{}\n{}\n".format(songname, artistname)

def main():     
      ##objects
      infofolder = Infofolder("D:\\little python projects\Player\infofolder\songfile.txt", "C:\\Users\Muwaffuq\Music\\")
      song = Song(infofolder.Infofile())
      artist = Artist(infofolder.Infofile(), infofolder.Linklist())
      favourite = Favouritesong("D:\\little python projects\Player\\Favouritesong\\likefile.txt", song.Songlist())
      lyrics = Lyrics("D:\\little python projects\Player\Lyricsfolder")
      page = Page(song.Songlist(), artist.Artistlist(), artist.Artistsonglist(song.Songlist(), artist.Artistlist()))
      ui = UserInterface(song.Songlist(), artist.Artistlist(), artist.Artistsonglist(song.Songlist(), artist.Artistlist()))



      print(ui.Show(song.Songlist()))
      favourite.Like(song.Songlist(), 1)
      print(ui.Show(favourite.Likelist(), "Favourite song"))


'''
      ##app body
      select = input("songs artists\n")

      if select == "songs":
         songlist = song.Songlist()  # song list
         print(ui.Show(songlist, "songs"))
         songindex = song.Songlist().index(input("songname:\n"))
         linklist = infofolder.Linklist() # link list
         songlink = linklist[songindex] # song link
         song.Play(songlink) # play
         print(ui.Nowplaying(songlist, songindex)) # now playing

      elif select == "artists":
           artistlist = artist.Artistlist() # artist list
           print(ui.Show(artistlist, "artists"))
           artistindex = artistlist.index(input("artistname:\n")) # artist index
           songlist = page.Artistsongpage(artistindex) # song list
           print(ui.Show(songlist, "songs"))
           songindex = songlist.index(input("songname:\n"))
           artistsonglist = artist.Artistsonglinklist(artist.Artistsonglist(song.Songlist(), artist.Artistlist()))
           linklist = artistsonglist[artistindex] # link list
           songlink = linklist[songindex] # song link
           song.Play(songlink) # play
           print(ui.Nowplaying(songlist, songindex)) # now playing
           
      while True:

         inpt = input("shuffle next previous like lyrics\n")
              
         if inpt in songlist:
            songindex = songlist.index(inpt)
            songlink = linklist[songindex] # song link
            song.Play(songlink) # play
            print(ui.Nowplaying(songlist, songindex)) # now playing

         elif inpt == "shuffle":
              songlink = song.Shuffle() # song link
              song.Play(songlink)
              print(ui.Nowplaying(songlist, songindex)) # now playing

         elif inpt == "previous":
              previoussongindex = song.Previoussong(songlist, songindex)
              songlink = linklist[previoussongindex] # song link
              song.Play(songlink) # play
              print(ui.Nowplaying(songlist, previoussongindex)) # now playing
              songindex = previoussongindex

         elif inpt == "next":
              nextsongindex = song.Nextsong(songlist, songindex)
              songlink = linklist[nextsongindex] # song link
              song.Play(songlink) # play
              print(ui.Nowplaying(songlist, nextsongindex)) # now playing
              songindex = nextsongindex
              
         elif inpt == "lyrics":
              print(lyrics.Show(songlist, songindex)) # lyrics   
         else:
              continue
'''
if __name__ == '__main__': 
    main()