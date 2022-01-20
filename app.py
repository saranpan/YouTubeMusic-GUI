#import lib
import sqlite3,datetime,locale,urllib.request,re
from tkinter import *
from PIL import Image,ImageTk
from tkinter import Label, messagebox
from tkinter.ttk import Style
from tkinter.font import Font, nametofont

import sys, os 
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Setup

#Launch database file (utube3.db)
conn = sqlite3.connect(resource_path('utube3.db'))
c = conn.cursor()

'''

c.execute("""create table Artists(
        Artist_id INTEGER primary key,
        artist char(255),
        Most_listened_song char(255));""")


c.execute("""create table Genres(
        Genre_id INTEGER primary key,
        Genre char(255));""")


c.execute("""create table Songs(
        Song_ID INTEGER Primary key,
        Song char(255),
        Artist_ID INTEGER,
        FtArtist_ID INTEGER null,
        Genre_ID INTEGER,
        dates Date,
        views INTEGER,
        Foreign key(Artist_ID) references Artists(Artist_ID),
        Foreign key(FtArtist_ID) references Artists(Artist_ID),Foreign Key(Genre_ID) references Genres(Genre_ID));""")



c.execute("""create table Results(
        Result_ID INTEGER Primary key,
        Result char(255),
        Frequency INTEGER);""")


c.execute("insert into Artists values(1,'Blackpink','DDU-DU DDU-DU')");
c.execute("insert into Artists values(2,'Lady gaga','Bad Romance')");
c.execute("insert into Artists values(3,'Harry Style','Sign of the times')");
c.execute("insert into Artists values(4,'Bradley Cooper','Black Eyes')");
c.execute("insert into Artists values(5, 'Metallica', 'Nothing Else Matters')");
c.execute("insert into Artists values(6, 'Frank Sinatra', 'I Love You Baby')");
c.execute("insert into Artists values(7, 'Frank Ocean', 'Chanel')");
c.execute("insert into Artists values(8, 'Bruno Mars', 'The Lazy Song')");
c.execute("insert into Artists values(9, 'Katy Perry', 'Roar')");
c.execute("insert into Artists values(10, 'Sam Smith', 'Too Good at Goodbyes')");

c.execute("insert into genres values(1,'Pop')");
c.execute("insert into genres values(2,'Rap')");
c.execute("insert into genres values(3,'R&B')");
c.execute("insert into genres values(4,'Rock')");
c.execute("insert into genres values(5,'EDM')");
c.execute("insert into genres values(6,'Metal')");
c.execute("insert into genres values(7,'K-Pop')");
c.execute("insert into genres values(8,'Oldies')");
c.execute("insert into genres values(9,'Country')");
c.execute("insert into genres values(10,'Jazz')");
          
c.execute("insert into Songs values(1,'DDUDUDDUDU',1,NULL,7,'2018-15-07',1396933546)");
c.execute("insert into Songs values(2,'Kill This Love',1,NULL,7,'2018-04-04',1112760946)");
c.execute("insert into Songs values(3,'Sour Candy',2,1,1,'2020-05-28',87905442)");
c.execute("insert into Songs values(4,'Bad Romance',2,NULL,1,'2009-11-24',1295293121)");
c.execute("insert into Songs values(5,'Shallow',2,4,9,'2019-08-16',974436173)");
c.execute("insert into Songs values(6,'Sign of the times',3,NULL,1,'2017-05-08',689414402)");
c.execute("insert into Songs values(7,'Watermelon Sugar',3,NULL,1,'2020-05-18',150251404)");
c.execute("insert into songs values(8, 'Nothing Else Matters', 5, NULL, 6, '2009-10-27', 855670896)");
c.execute("insert into songs values(9, 'I Love You Baby', 6, NULL, 10, '2017-01-07', 107854458)");
c.execute("insert into songs values(10, 'Chanel', 7, NULL, 3, '2017-06-28', 39741580)");

c.execute("insert into results values(1,'music video',4)");
c.execute("insert into results values(2,'karaoke',1)");
c.execute("insert into results values(3,'Acoustic',2)");
c.execute("insert into results values(4,'Remix',0)");
c.execute("insert into results values(5,'live',0)");
c.execute("insert into results values(6,'reaction',0)");
c.execute("insert into results values(7,'cover',0)");
c.execute("insert into results values(8,'concert',0)");
c.execute("insert into results values(9,'dance',0)");
c.execute("insert into results values(10,'lyrics',0)");

'''

conn.commit()
conn.close()


#FOR CHECK THE SPECIFIC TABLE
conn = sqlite3.connect('utube3.db')
c = conn.cursor()
c.execute("""Select Songs.Song,Artists.artist , Songs.views, Songs.dates FROM Songs 
            INNER JOIN Artists
            ON Artists.Artist_Id = Songs.Artist_Id
            where Songs.song='Sour Candy'
            UNION
            Select Songs.Song,Artists.artist , Songs.views , Songs.dates FROM Songs           
            LEFT JOIN Artists
            ON Artists.Artist_Id = Songs.FtArtist_Id 
            where Artists.artist <> 'None' and Songs.song='Sour Candy'
            """)
  
allsong = c.fetchall()
print(allsong)           
conn.commit()
conn.close()


#GUI
root = Tk()


root.title('Youtube Music')
root.iconbitmap('static/ytmusic.ico')

background_label = Label(root, bg='#c4302b')
background_label.place(relwidth=1, relheight=1)



img = ImageTk.PhotoImage(Image.open('static/searchtool.png'))
img2 = ImageTk.PhotoImage(Image.open('static/songplus.png'))

img_video = ImageTk.PhotoImage(Image.open('static/vid_template.png'))



################################################################### ''''


def userinput():
    
    conn = sqlite3.connect('utube3.db')
    c= conn.cursor()
    
    window = Tk()
    window.title("Artist & Song Data")
    window.iconbitmap('static/ytmusic.ico')
    window.geometry('900x850+0+0')


    #Songs

    L2= Label(window, text= "Song Name", font=("arial",16)).place(x=100,y=340)
    L3= Label(window, text="Artist_ID", font=("arial",16)).place(x=100,y=390)
    L4= Label(window, text="FtArtist_ID", font=("arial",16)).place(x=100,y=440)
    L5= Label(window, text="Genre_ID", font=("arial",16)).place(x=100,y=490)
    L6= Label(window, text="Date", font=("arial",16)).place(x=100,y=540)
    l7= Label(window, text="Views", font=("arial",16)).place(x=100,y=590)
    l11=Label(window, text="Insert New Song", font=("arial",18, "bold")).place(x=250,y=300)

    #Artists
    l8= Label(window,text="Please proceed to the next section if your artist already exists.", font=("arial",14, "italic")).place(x=105,y=45)

    l10= Label(window,text="Artist Name", font=("arial",16)).place(x=100,y=95)
    l12=Label(window,text="Most Listened to Song", font=("arial",16)).place(x=2,y=145)
    l13= Label(window,text="Insert New Artist", font=("arial",18,"bold")).place(x=250,y=13)


    #Create variables for each list
        #Song

    Song = StringVar(window)
    Artist_ID = StringVar(window)
    FtArtist_ID = StringVar(window)
    Genre_ID= StringVar(window)
    dates = StringVar(window)
    views= StringVar(window)
    #Artist
    artist_id= StringVar(window)
    artist= StringVar(window)
    Most_listened_song= StringVar(window)

    #Entry for 'input' in GUI
    #Song


    son = Entry(window, textvariable=Song)
    son.place(x=220,y=345)

    artid = Entry(window, textvariable=Artist_ID)
    artid.place(x=220,y=395)

    ftartid = Entry(window, textvariable= FtArtist_ID)
    ftartid.place(x=220,y=445)

    genid = Entry(window, textvariable=Genre_ID)
    genid.place(x=220,y=495)

    da= Entry(window, textvariable= dates)
    da.place(x=220, y=545)

    vie= Entry(window, textvariable= views)
    vie.place(x=220, y=595)
    
    #Artist


    art= Entry(window, textvariable= artist)
    art.place(x=220,y=100)

    mos= Entry(window, textvariable= Most_listened_song)
    mos.place(x=220,y=150)



    #get func to isolate the text entered in the entry boxes and submit to database
    def get_s():
        print("You have submitted a record to Song table.")
        
        c.execute('INSERT INTO Songs(Song, Artist_ID,FtArtist_ID,Genre_ID,dates,views) VALUES (:Song, :Artist_ID, :FtArtist_ID, :Genre_ID, :dates, :views )',
                  {
                   'Song': Song.get() if Song.get() !="" else None,
                   'Artist_ID': Artist_ID.get() if Artist_ID.get() !="" else None,
                   'FtArtist_ID': FtArtist_ID.get() if FtArtist_ID.get() !="" else None,
                   'Genre_ID': Genre_ID.get() if Genre_ID.get() !="" else None,
                   'dates': dates.get() if dates.get() !="" else None,
                   'views': views.get() if views.get() !="" else None            
                   })
       
        conn.commit()
        
#Reset fields after submit
        Song.set('')
        Artist_ID.set('')
        FtArtist_ID.set('')
        Genre_ID.set('')
        dates.set('')
        views.set('')
        
        
    def get_a():
        print("You have submitted a record to Artist table.")
        
        c.execute('INSERT INTO Artists(artist,Most_listened_song) VALUES (:artist, :Most_listened_song)', 
                  {                
                    'artist': artist.get() if artist.get() != "" else None,
                    'Most_listened_song': Most_listened_song.get() if Most_listened_song.get() != "" else None                    
                      })
                      
                      
#Reset fields after submit        
        artist.set('')
        Most_listened_song.set('')
        

#Clear boxes when submit button is hit
    def clear_s():
        Song.set('')
        Artist_ID.set('')
        FtArtist_ID.set('')
        Genre_ID.set('')
        dates.set('')
        views.set('')
        
    def clear_a():
        
        artist.set('')
        Most_listened_song.set('')
                
        

    #Show records in db
    def record_s():
        c.execute('SELECT * FROM Songs')

        frame = Frame(window)
        frame.place(x= 470, y = 580)
    
        Lb = Listbox(frame, height = 7, width = 45,font=("arial", 12)) 
        Lb.pack(side = LEFT, fill = Y)
    
        scroll = Scrollbar(frame, orient = VERTICAL) # set scrollbar to list box for when entries exceed size of list box
        scroll.config(command = Lb.yview)
        scroll.pack(side = RIGHT, fill = Y)
        Lb.config(yscrollcommand = scroll.set) 
    

        Lb.insert(0, 'Song_ID, Song, Artist_ID, FtArtist_ID, Genre_ID, dates, views') #first row in listbox
    
        data = c.fetchall() # Gets the data from the table
    
        for row in data:
            Lb.insert(1,row) # Inserts record row by row in list box

        conn.commit()
    
    def record_a():
        c.execute('SELECT * FROM Artists')

        frame = Frame(window)
        frame.place(x= 470, y = 113)
    
        Lb = Listbox(frame, height = 4, width = 45,font=("arial", 12)) 
        Lb.pack(side = LEFT, fill = Y)
    
        scroll = Scrollbar(frame, orient = VERTICAL) # set scrollbar to list box for when entries exceed size of list box
        scroll.config(command = Lb.yview)
        scroll.pack(side = RIGHT, fill = Y)
        Lb.config(yscrollcommand = scroll.set) 
    

        Lb.insert(0, 'artist_id, artist, Most_listened_song') #first row in listbox
    
        data = c.fetchall() # Gets the data from the table
    
        for row in data:
            Lb.insert(1,row) # Inserts record row by row in list box
    
        conn.commit()


    #all buttons
    #songs
    button_1 = Button(window, text="Submit",command=get_s)
    button_1.place(x=320,y=650)

    button_2 = Button(window,text= "Clear",command=clear_s)
    button_2.place(x=220,y=650)
    
    button_3 = Button(window, text="Refresh",command=record_s)
    button_3.place(x=560,y=750)

    #artists
    button_4 = Button(window, text="Submit",command=get_a)
    button_4.place(x=320,y=198)

    button_5 = Button(window,text= "Clear",command=clear_a)
    button_5.place(x=220,y=198)

    button_6 = Button(window, text="Refresh",command=record_a)
    button_6.place(x=560,y=198)


    #List Boxes
    #Song Records
    l16= Label(window,text="Existing Song Records", font=("arial",14,"bold")).place(x=470,y=520)
    c.execute('SELECT * FROM Songs')

    frame = Frame(window)
    frame.place(x= 470, y = 580)
    
    Lb = Listbox(frame, height = 7, width = 45,font=("arial", 12)) 
    Lb.pack(side = LEFT, fill = Y)
    
    scroll = Scrollbar(frame, orient = VERTICAL) # set scrollbar to list box for when entries exceed size of list box
    scroll.config(command = Lb.yview)
    scroll.pack(side = RIGHT, fill = Y)
    Lb.config(yscrollcommand = scroll.set) 
    

    Lb.insert(0, 'Song_ID, Artist_ID, FtArtist_ID, Genre_ID, dates, views') #first row in listbox    
    data = c.fetchall() # Gets the data from the table
    
    for row in data:
        Lb.insert(1,row) # Inserts record row by row in list box

    conn.commit()

    #Genre Records
    l15= Label(window,text="Existing Genre Records", font=("arial",14,"bold")).place(x=470,y=330)
    l17= Label(window,text="No changes can be made to this table",font=("arial",12,"italic")).place(x=470,y=353)
    c.execute('SELECT * FROM Genres')

    frame = Frame(window)
    frame.place(x= 470, y = 374)
    
    Lb = Listbox(frame, height = 7, width = 45,font=("arial", 12)) 
    Lb.pack(side = LEFT, fill = Y)
    
    scroll = Scrollbar(frame, orient = VERTICAL) # set scrollbar to list box for when entries exceed size of list box
    scroll.config(command = Lb.yview)
    scroll.pack(side = RIGHT, fill = Y)
    Lb.config(yscrollcommand = scroll.set) 
    

    Lb.insert(0, 'Genre_id, Genre') #first row in listbox    
    data = c.fetchall() # Gets the data from the table
    
    for row in data:
        Lb.insert(1,row) # Inserts record row by row in list box
    
    conn.commit()

    #Artist Records
    l14= Label(window,text="Existing Artist Records", font=("arial",14,"bold")).place(x=470,y=85)
    c.execute('SELECT * FROM Artists')

    frame = Frame(window)
    frame.place(x= 470, y = 113)
    
    Lb = Listbox(frame, height = 4, width = 45,font=("arial", 12)) 
    Lb.pack(side = LEFT, fill = Y)
    
    scroll = Scrollbar(frame, orient = VERTICAL) # set scrollbar to list box for when entries exceed size of list box
    scroll.config(command = Lb.yview)
    scroll.pack(side = RIGHT, fill = Y)
    Lb.config(yscrollcommand = scroll.set) 
    

    Lb.insert(0, 'artist_id,artist, Most_listened_song') #first row in listbox
    
    data = c.fetchall() # Gets the data from the table
    
    for row in data:
        Lb.insert(1,row) # Inserts record row by row in list box

    conn.commit()

    window.mainloop()

try:
    from Tkinter import Label
    from ttk import Style
    from tkFont import Font, nametofont
except ImportError:
    from tkinter import Label
    from tkinter.ttk import Style
    from tkinter.font import Font, nametofont
   
    
def get_background_of_widget(widget):
    try:
        # We assume first tk widget
        background = widget.cget("background")
    except:
        # Otherwise this is a ttk widget
        style = widget.cget("style")

        if style == "":
            # if there is not style configuration option, default style is the same than widget class
            style = widget.winfo_class()

        background = Style().lookup(style, 'background')
    
    return background

# Thanks to the below code snippet to allow access the hyperlink via tk button @killian95
class Link_Button(Label, object):
    def __init__(self, master, image, background=None, font=None, familiy=None, size=None, underline=True, visited_fg = "#551A8B", normal_fg = "#0000EE", visited=False, action=None):
        self._visited_fg = visited_fg
        self._normal_fg = normal_fg
        
        if visited:
            fg = self._visited_fg
        else:
            fg = self._normal_fg

        if font is None:
            default_font = nametofont("TkDefaultFont")
            family = default_font.cget("family")

            if size is None:
                size = default_font.cget("size")

            font = Font(family=family, size=size, underline=underline)

        Label.__init__(self, master, image=image, fg=fg, cursor="hand2", font=font)

        if background is None:
            background = get_background_of_widget(master)

        self.configure(background=background)

        self._visited = visited
        self._action = action

        self.bind("<Button-1>", self._on_click)

    @property
    def visited(self):
        return self._visited
        
    @visited.setter
    def visited(self, is_visited):
        if is_visited:
            self.configure(fg=self._visited_fg)
            self._visited = True
        else:
            self.configure(fg=self._normal_fg)
            self._visited = False

    def _on_click(self, event):
        if not self._visited:
            self.configure(fg=self._visited_fg)

        self._visited = True

        if self._action:
            self._action()


if __name__ == "__main__":
    import webbrowser

    try:
        from Tkinter import Tk, Frame
    except ImportError:
        from tkinter import Tk, Frame    

        
#MAIN PART : open the link : utube        
    def callback():
        webbrowser.open_new(utube)

#######################################################################################



def on_click(event):
    B.config(foreground='black')
    if B.get() == "Search your song here":
        event.widget.delete(0, END)
    else:
        B.config(foreground='black')

        
def stringIn(search_words, forbidden_like_list):
    
    output1 = []
    
    for song in forbidden_like_list:
        if any(word in song for word in search_words):
            output1.append(song)
       
    return output1        



def setTextInput(text):
    B.delete(0,"end")
    B.insert(0, text)
    
    for k in range(len(Autput1)):
        Autput1[k].destroy()
    



def getsong():    
    conn = sqlite3.connect('utube3.db')
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    
    input1 = [str(B.get())] 
    
    c.execute("Select song from songs")
    input2 = c.fetchall()


    j=0 
    for i in range(len(input2)):
        if input1[0] == input2[i]:
            j=1
            global result1
            result1 = input2[i]                 
                      
            pre_create_window()
            
            break

        
#Suggest the similar song(s)
    if j==0:
        output1 = stringIn(input1,input2)
        
        global Autput1
        
        Autput1 = []
        
        k=0
        
        for e in output1:
                                               
            Autput1.append(Button(root,text=e,bg='#ffffff',command=lambda e=e:setTextInput(str(e))))
            Autput1[k].grid()           
            k+=1
    
    #No Result case   

    if Autput1 == []:
        messagebox.showerror("Youtube Music","No Results found")  
        
    conn.commit()
    conn.close()


def pre_create_window():

    
    conn = sqlite3.connect('utube3.db')
    
    c = conn.cursor()

    
    c.execute("""Select Songs.Song,Artists.artist FROM Songs 
            INNER JOIN Artists
            ON Artists.Artist_Id = Songs.Artist_Id
            where Songs.song=?""",(result1,))
    input5 = c.fetchall()
    #print(input5)
    
    global result2
    result2 = input5[0][1]
    #print(result2)
    
    global pizza
    pizza = StringVar()
    pizza.set("any")
    
    if len(input5) > 1:
        
        messagebox.showwarning("Youtube Music","Oops! Duplicated song title, please pick one of the Artist you are looking for for this song ") 
        
        root3 = Toplevel(root)
        root3.iconbitmap('static/ytmusic.ico')
        root3.title('Youtube Music')
        
        Artist1 = []
        
        for i in input5:
            Artist1.append((i[1],i[1]))
            
        for text, art in Artist1:
            Radiobutton(root3, text=text, variable=pizza, value=art).grid()
        
        def clicked(value):
            
            global result2
            result2 = str(value)
            #print(result2)
            
            create_window()
            #root3.destroy()
            
            
        myButton = Button(root3, text="Enter!", command=lambda: clicked(pizza.get()))
        myButton.grid()
        
        root3.mainloop()
        
    
    else:
        result2 = str(pizza.get())
        #print(result2)
    
    #print(result2)
    conn.commit()
    conn.close()
    

    create_window()
    
    #######################################################################
    
def create_window():
    
    root2 = Toplevel()
    root2.iconbitmap('static/ytmusic.ico')
    root2.title('Youtube Music')

    
     #HYPERLINK

    
    conn = sqlite3.connect('utube3.db')    
    c = conn.cursor()
    c.execute("""Select Artists.artist FROM Artists
                    INNER JOIN Songs 
                    ON Songs.Artist_Id = Artists.Artist_Id
                    where Songs.song=?""",(result1, ))
    
    
    input4 = c.fetchall()
    
    if result2 == 'any':
        search_keyword = result1 + 'song' + str(input4[0])
    else:
        search_keyword = result1 + 'song' + str(result2)
    
    
    search_keyword = search_keyword.replace(' ', '+')
    
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword )
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    
    global utube
    
    utube = "https://www.youtube.com/watch?v="+video_ids[0]

    #######################################################################   
    
    wordd = (result1, result2, result1, )
    
    #Increase views by 1 everytime we clicked the button
    if result2 == 'any':
        
        c.execute("""UPDATE Songs Set views = views+1 where Song = ? """,(result1,))
    
        c.execute("""Select Songs.Song,Artists.artist , Songs.views, Songs.dates FROM Songs 
                INNER JOIN Artists
                ON Artists.Artist_Id = Songs.Artist_Id
                where Songs.song=?
                UNION
                Select Songs.Song,Artists.artist , Songs.views, Songs.dates FROM Songs           
                LEFT JOIN Artists
                ON Artists.Artist_Id = Songs.FtArtist_Id 
                where Artists.artist <> 'None' and Songs.song=?
                """,(result1, result1, ))  
        
        input3 = c.fetchall()    
        #print(input3)
        conn.commit()
        conn.close()
    
    else:
        c.execute("""UPDATE Songs SET views = views + 1 FROM Artists 
                    WHERE Artists.Artist_ID = Songs.Artist_ID 
                    AND Songs.Song = ? AND Artists.Artist = ?""",(result1,result2,))
        
        #update t1 set value1 = (select value2 from t2 where t2.id = t1.id) where t1.value1 = 0;
    
        c.execute("""Select Songs.Song,Artists.artist , Songs.views, Songs.dates FROM Songs 
                INNER JOIN Artists
                ON Artists.Artist_Id = Songs.Artist_Id
                where Songs.song=? and Artists.artist=?
                UNION
                Select Songs.Song,Artists.artist , Songs.views, Songs.dates FROM Songs           
                LEFT JOIN Artists
                ON Artists.Artist_Id = Songs.FtArtist_Id 
                where Artists.artist <> 'None' and Songs.song=?
                """,(result1, result2, result1, ))    
        input3 = c.fetchall()    
        #print(input3)
        conn.commit()
        conn.close()
    
        
        
    if len(input3) == 1 :
        for i in input3:
            if i[0] == result1:
                r = Link_Button(root2, image=img_video, action=callback)
                r.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
            
                z= Label(root2,text=i[1]+'- '+i[0],font=('Roboto',15))
                z.grid(row=5,column=0,sticky=W,padx=10,pady=3)
            
                #a= Label(root2,text=i[0],font=('Roboto',20))
                #a.grid(row=5,column=1)
            
                b= Label(root2,text=str("{:,}".format(i[2]))+'views • '+str(i[3]),font=('Roboto',10),fg='gray')
                b.grid(row=6,column=0,sticky=W,padx=10,pady=3)
            
    if len(input3) == 2 :
                
                r = Link_Button(root2, image=img_video, action=callback)              
                r.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
            
                z= Label(root2,text=input3[1][1]+'- '+input3[0][0]+' ft.'+ input3[0][1],font=('Roboto',15))
                z.grid(row=5,column=0,sticky=W,padx=10,pady=3)
            
                #a= Label(root2,text=i[0],font=('Roboto',20))
                #a.grid(row=5,column=1)
            
                b= Label(root2,text=str("{:,}".format(input3[0][2]))+'views • '+ str(input3[0][3]),font=('Roboto',10),fg='gray')
                b.grid(row=6,column=0,sticky=W,padx=10,pady=3)         
            
    
    #conn.commit()
    #conn.close()
    
    root2.mainloop()
    
    
    
    
    
    
#A = Label(root,text="Search your song here",font=('Roboto',10),bg='#c4302b')
#A.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

myvar = StringVar()
myvar.set("Search your song here")


B = Entry(root,font=('Roboto',20),textvariable=myvar,fg='gray')
B.config(foreground='gray')
B.bind("<Button-1>", on_click)
B.bind("<FocusIn>", on_click)
B.grid(row=1,column=0,columnspan=2,padx=20,pady=10)


C= Button(root,image=img,command=getsong)
C.grid(row=1,column=2,padx=10,pady=10)

d= Button(root,image=img2,command=userinput)
d.grid(row=0,column=3,padx=10,pady=10)

mainloop()

