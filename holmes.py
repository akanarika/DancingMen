#holmes.py

import graphics
from PIL import Image, ImageDraw

'''def draw(line,im,ims,i,data):
        im.paste(ims[ord(data[p])-96],(53*i,55*(line-1),50+53*i,33+55*(line-1)))

def flag(line,im,ims,i,data):
        im.paste(ims[ord(data[p])-96+26],(53*i,55*(line-1),50+53*i,33+55*(line-1)))'''


def main():
   
        '''
        win = graphics.GraphWin("DUDANDAN",800,800)    
        image = graphics.Image(graphics.Point(353,140),"dancingmen.gif")       
        image.draw(win)'''

        im = Image.open("dancingmen.gif")
        im.getbbox()
        im3 = Image.new('RGBA',(2000,4000),'white')
        im4 = Image.new('RGB',(1000,1000))
        im5 = Image.new('RGB',(5000,300))
        im6 = Image.new('RGB',(500,300))
        im3.save("new.gif")
        #print im.getbbox()

        
        ims = []
        for i in range(13):
                ims.append(im.crop((3+4*i+50*i,33,53+4*i+50*i,83)))
                im4.paste(ims[i],(50*i+3*i,0,50+3*i+50*i,50))
        for m in range(13):       
                ims.append(im.crop((3+4*m+50*m,166,53+4*m+50*m,216)))
                im4.paste(ims[m+13],(50*m+3*m,110,50+3*m+50*m,160))
        for no in range(6):
                ims.append(ims[0])
        for i in range(26):
                ims.append(ims[i])
        # i==58-1
        for j in range(13):        
                ims.append(im.crop((3+4*j+50*j,88,53+4*j+50*j,138)))
                im4.paste(ims[j+26],(50*j+3*j,55,50+3*j+50*j,105))
        for n in range(13):        
                ims.append(im.crop((3+4*n+50*n,218,53+4*n+50*n,268)))
                im4.paste(ims[n+39],(50*n+3*n,165,50+3*n+50*n,215))
        for no in range(6):
                ims.append(ims[0])
        for i in range(26):
                ims.append(ims[i+58])

        for i in range(116):
                im5.paste(ims[i],(50*i,0,50+50*i,50))
        #im5.save("5.gif")

        #im4.save("list.gif")
        #x[] = raw_input("Please enter what you want to say: \n")
        #print ord(x)
        #im3.paste(ims[x],(50*n+3*n,165,50+3*n+50*n,215))
        infile = open("txt.txt",'r')

        data = infile.read()

        line = 1
        seq = 0

        for p in range(len(data)-2):
                x = ord(data[p])
                #print x
                y = ord(data[p+1])
                #print y
                if ((x<=90)and(x>=65)or(x<=122)and(x>=97))and((y<=90)and(y>=64)or(y<=122)and(y>=97)):
                        im3.paste(ims[x-65],(53*seq,55*line,50+53*seq,50+55*line))
                        seq = seq+1
                if ((x<=90)and(x>=65)or(x<=122)and(x>=97))and(not((y<=90)and(y>=64)or(y<=122)and(y>=97))):
                                im3.paste(ims[x-65+58],(53*seq,55*line,50+53*seq,50+55*line))
                                seq = seq+1
                                im6.paste(ims[x-65+58],(53*seq,55*line,50+53*seq,50+55*line))
                if y==10:
                                seq = 0
                                line = line+1

        p = p+1
        x = ord(data[p])                        
        im3.paste(ims[x-65+58],(53*seq,55*line,50+53*seq,50+55*line))
                                
        im3.save("new.gif")
        #im6.save("6.gif")
        print "Done! Your code is in new.gif. :)"

        '''
        a = win.getMouse()
        b = win.getMouse()
        c = win.getMouse()
        d = win.getMouse()
        
        h = c.getY() - a.getY()
        w = b.getX() - a.getX()

        print "h:",h, "w:",w

        topl = win.getMouse()
        toph = win.getMouse()
        print "top:", topl.getX(),toph.getY()
        '''
        
        

        '''if win.getMouse():
                win.close()'''


main()

