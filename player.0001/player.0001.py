import pygame
import random

class Infofolder:
     def __init__(self, infofolderdirectory, playdirectory):
         self.infofolderdirectory = infofolderdirectory # Info folder
         self.playdirectory = playdirectory # Song file
         
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
     
class Artist:
     def __init__(self, infolist, linklist):
         self.infolist = infolist
         self.linklist = linklist

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
     def __init__(self, songlinklist):
        self.linklist = songlinklist
        
     def Likelist(self, index = 0):
         with open(self.favouritesongdiroctory) as likefile:
              likefile = open(self.favouritesongdiroctory, "r")
         filelist = likefile.readlines()
         likelist = []
         while True:
               try:
                   likelist.append(filelist[index].strip("\n"))
                   index += 1      
               except IndexError:
                      break
         return likelist

# like song link list
     def Linklist(self, likelist, index = 0):
         linklist = []
         while True:
               try:
                   songname = likelist[index]
                   for link in self.linklist:
                       if songname in link:
                          linklist.append(link)
                   index += 1
               except IndexError:
                      break
         return linklist

##  lyrics file contains the lyrics
class Lyrics:
     def __init__(self, lyricsfolderdirectory):
        self.lyricsfolderdirectory = lyricsfolderdirectory #Lyrics File Directory

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

class Function:
     def __init__(self, linklist, favouritesongdiroctory):
         self.linklist = linklist
         self.favouritesongdiroctory = favouritesongdiroctory
         
     def Play(self, songlink):
         pygame.mixer.init()
         pygame.mixer.music.load(songlink)
         pygame.mixer.music.play()
         
     def Select(self, select):
         if type(select) is str:
            for link in self.linklist:
                if select in link:
                   songlink = link
                   return songlink
                if select == "shuffle":
                     songlink = random.choice(self.linklist)
                     return songlink                    
                elif select == "previous":
                     songlink = self.linklist
                     return songlink    
                elif select == "next":
                     songlink = self.linklist
                     return songlink
                else:
                     return select
                    
     def Push(self, push):
         if push == "pause":
              pygame.mixer.music.pause()
         elif push == "resume":
              pygame.mixer.music.unpause()
         elif push == "stop":
              pygame.mixer.music.stop()
         else:
              return push

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

     def Playingnow(self, songlink, songlist, artistlist):
         pass

def main():     
      ##objects
      infofolder = Infofolder("D:\\little python projects\Player\infofolder\songfile.txt", "C:\\Users\Muwaffuq\Music\\")
      song = Song(infofolder.Infofile())
      artist = Artist(infofolder.Infofile(), infofolder.Linklist())
      favourite = Favouritesong(infofolder.Linklist())
      lyrics = Lyrics("D:\\little python projects\Player\Lyricsfolder")
      page = Page(song.Songlist(), artist.Artistlist(), artist.Artistsonglist(song.Songlist(), artist.Artistlist()))
      function = Function(infofolder.Linklist(), "D:\\little python projects\Player\\Favouritesong\\likefile.txt")
      ui = UserInterface(song.Songlist(), artist.Artistlist(), artist.Artistsonglist(song.Songlist(), artist.Artistlist()))

      ##app body
      while True:
      selection = input("songs artists likelist\n")

      if selection == "songs":
         songlist = song.Songlist() # song list
         print(ui.Show(songlist, "songs"))
         songname = input("songname:\n") # song name
                 
         songindex = songlist.index(songname) # song index
         function.Play(songlink) # select button

      elif selection == "artists":
           artistlist = artist.Artistlist() # artist list
           print(ui.Show(artistlist, "artists"))
           artistname = input("artistname:\n") # artist name
           artistindex = artistlist.index(artistname) # artist index
           songlist = page.Artistsongpage(artistindex) # song list
           print(ui.Show(songlist, "songs"))
           songindex = songlist.index(input("songname:\n")) # song index
           artistsonglist = artist.Artistsonglinklist(artist.Artistsonglist(song.Songlist(), artist.Artistlist()))
           linklist = artistsonglist[artistindex] # link list
           songlink = linklist[songindex] # song link
           function.Play(songlink) # select button

      elif selection == "likelist":
           songlist = favourite.Likelist() # song list
           print(ui.Show(songlist, "song"))
           songname = input("songname:\n")
           songindex = songlist.index(songname) # song index
           linklist = favourite.Linklist(favourite.Likelist()) # link list
           songlink = linklist[songindex] # song link
           function.Play(songlink) # select button
           
      ## control function
      def control_finction(action):
          return function.Select(function.Push(action))
     
      while True:
           action = input("shuffle\nprevious pause next\nlike resume stop\n")
           control = control_finction(action)
           function.Play(songlink)

if __name__ == "__main__": 
   main()