def Like(name):
         likesongfolder = "C:\\Users\Muwaffuq\Desktop\\New Text Document.txt"
         with open(likesongfolder) as likefile:
              likefile = open(likesongfolder , "r")
              likelist = likefile.readlines()
         if len(likelist) == 0:  
            likefile = open(likesongfolder , "a")
            likefile.write("{}".format(name))
         else:
              for line in likelist:
                  print(line)
##                  if line == "{}\n".format(name):
##                     pass
##              else:
##                   likefile = open(likesongfolder , "a")
##                   likefile.write("\n{}".format(name))
##                 
         
               




def Likelist():
         likesongfolder = "C:\\Users\Muwaffuq\Desktop\\New Text Document.txt"
         songlist = []
         with open(likesongfolder, "r") as likefile:
              likefile = open(likesongfolder , "r")
         likelist = likefile.readlines()         
         index = 0
         while True:
               try: 
                   songlist.append(likelist[index].strip("\n"))
                   index += 1
               except IndexError:
                      break

         return songlist
               

Like("c")
#print(Likelist())
