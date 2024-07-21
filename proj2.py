from tkinter import *
from tkinter import font
from tkinter import filedialog
from PIL import Image, ImageTk
from math import ceil
import os,re,glob
from pathlib import Path
import playfromste
import threading
from collections import deque
from auto import writemla,listwrite

class AutoUpdateList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update()

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.update()

    def update(self):
        if self[2] is not None:
            self[2][3] = self[0]
        if self[3] is not None:
            self[3][3] = self[0]   
class proj(Frame):
    width=1100
    height=800
    w=0
    h=0
    classes=[]
    files=0
    curpic=0
    gor:list=[]
    store={}
    aa=0
    # right=None

    gorap=[None,None,None]
    
    #which_page, frame[0], list->aj[0], list->aj[1], self.pa, frame[1]
    num_file="my_list.txt"
    vid_button_ind=0
    # button_postion=0
    def addtor(self,lis):
        list = self.frame.grid_slaves()
        list0 = self.frame0.grid_slaves()
        for l in list:
            l.destroy()
        for l in list0:
            l.destroy()
        # aa=len(list)
        for aa in range(len(lis)):
            self.rbut=Button(self.frame,text=str(aa), command=lambda aa=aa: self.show_frame(lis[aa][0])).grid(row=aa,column=0,pady=5,padx=10)
            self.rrbut=Button(self.frame0,text=str(aa), command=lambda aa=aa: self.thr(self.mainfo+self.video,lis[aa][1],lis[aa][5])).grid(row=aa,column=0,pady=5,padx=10)
        self.rcanv.yview_moveto(1.0)
        self.rrcanv.yview_moveto(1.0)
    
    def readf(self):
        l=deque()
        fn=(self.mainfo)+self.num_file
        if(os.path.isfile(fn)):
            with open(fn, "r") as file:
                for line in file:
                    a, b = line.strip().split(",")
                    l.append([int(a), int(b)])
        return l 
    def thr(s,a,b,c):
        t = threading.Thread(target=playfromste.play, args=(a,b,c))
        t.start()
    def writef(s,l):
        filename = s.mainfo+s.num_file
        with open(filename, "w") as file:
            for sublist in l:
                file.write(str(sublist[1]) + "," + str(sublist[5]) + "\n")      
    def remove_and_update(self,a,i):
        foclist=a[i]
        foclist[2][4].delete(foclist[2][1][1])
        foclist[2][4].delete(foclist[2][1][0])
        foclist[2][1][0]=None
        foclist[2][1][1]=None
        foclist[2][2]=0
        foclist[2][3]=None
        if(foclist[3]!=None):
            foclist[3][4].delete(foclist[3][1][1])
            foclist[3][4].delete(foclist[3][1][0])
            foclist[3][1][0]=None
            foclist[3][1][1]=None
            foclist[3][2]=0
            foclist[3][3]=None
        a.pop(i)
        for j in range(i, len(a)):
            # print(a[j][0],a[j][2][3],a[j][3][3])
            # print("\n")
            a[j][0] = j
            a[j][2][4].itemconfigure(a[j][2][1][1],text =str(j)+"a")
            a[j][3][4].itemconfigure(a[j][3][1][1],text =str(j)+"b")
        self.addtor(self.gor)     
        del foclist
    # def findpg(frame):

    def insert_and_sort(s,a, x):
        i = 0
        while i < len(a) and a[i][1] < x:
            i += 1
        b=AutoUpdateList([i, x,None,None,None,None])
        # print(i)
        a.insert(i,b)
        for j in range(i+1, len(a)):
            a[j][0] = j
            a[j][2][4].itemconfigure(a[j][2][1][1],text =str(j)+"a")
            a[j][3][4].itemconfigure(a[j][3][1][1],text =str(j)+"b")
        return b
    # def scrrcanv(self,e):
    #     self.rcanv.bind_all('')

    def left_click(self,event,Img,se,pa):
        #self, canvas/pcan that hold w*h, frame/p, list->aj, canvas of current grid
        h=100#event.widget.reqwidth
        w=119      
        if self.gorap[0]==None and se[2]==0:#self.zor==0 and se[2]==0
            img=Image.new('RGBA', (w,h), self.blue)
            se[1][0]=ImageTk.PhotoImage(img)
            event.create_image(0, 0, image=se[1][0], anchor='nw')
            se[2]=1
            self.gorap=self.insert_and_sort(self.gor,(Img))
            self.gorap[4]=pa
            self.gorap[2]=se
            self.bold_font = font.Font(font='Helvetica 18 bold', height=12)
            self.bb=event.create_text(0,0, text=str(se[3])+"a", font=self.bold_font,fill="wheat", anchor='nw')
            se[1][1]=self.bb
            
        elif se[2]==1 :#
            if(se==self.gorap[2]):
                self.gorap=[None,None,None]
            self.remove_and_update(self.gor,se[3])
            # if(self.gorap[1]==None):
            #     self.gorap=[None,None]
        elif se[2]==2:#
            self.remove_and_update(self.gor,se[3])

            # event.widget.delete(se[1][1])
            
        # elif zor==1:
        #     self.gorap=[None,None]
        #     se[3]=0
        #     se[1][0]=None

       
    def right_click(self,event,Img,se):
        #self, canvas/pcan that hold w*h, frame/p, list->aj
        h=100#event.widget.reqwidth
        w=119
        
        if self.gorap[2]!=None and se[2]!=1:
            self.gorap[3]=se
            img=Image.new('RGBA', (w,h), self.red)   
            se[1][0]=ImageTk.PhotoImage(img)
            event.create_image(0, 0, image=se[1][0], anchor='nw')
            self.bold_font = font.Font(font='Helvetica 18 bold', height=12)
            self.bb=event.create_text(0,0, text=str(se[3])+"b", font=self.bold_font,fill="wheat", anchor='nw')
            se[1][1]=self.bb
            self.gorap[5]=int(Img)
            se[2]=2 
            self.gorap=[None,None,None]
            # print(self.gor)
            
            self.addtor(self.gor)

        elif se[2]==2:
            self.remove_and_update(self.gor,se[3])
        self.writef(self.gor)    
  

    def thrreq(self):
        self.canv.bind("<Enter>", self._bound_to_mousewheel)
        self.canv.bind('<Leave>', self._unbound_to_mousewheel)
        t = threading.Thread(target=self.reqfile)
        t.start()

    def reqfile(self):
        if(self.var.get()==""):          
            self.video_files = filedialog.askopenfilename(initialdir=".",
                                                title="edited",
                                                filetypes= (("Video Files", "*.mp4;*.avi;*.mov;*.mkv"),
                                                ("all files","*.*")))
            if self.video_files=="":
                return 
            self.video_files=self.var.get().replace("\\","/")
            #.replace("\\","/")
            if not self.video_files.endswith("/") :
                self.video_files+="/"
            self.filenames=[]
            #all the pic path
            thumbs=os.path.dirname(self.filenames)+"\\thumbs/"
            # print(thumbs)
            #find thumbs 
            for filename in os.listdir(thumbs):
                    self.filenames.append(os.path.join(directory, filename))
            
        else:  
            self.video_files=self.var.get().replace("\\","/")
            #.replace("\\","/")
            if not self.video_files.endswith("/") :
                self.video_files+="/"
            directory=os.path.dirname(self.video_files)+"/thumbs/"
            #videopath/thumbs/jpgs
            self.filenames=[]
            for filename in os.listdir(directory):
                    self.filenames.append(os.path.join(directory, filename))
                    #[video.jpg,...]
        self.video= [f for f in os.listdir(self.video_files) if f.endswith(('.mp4', '.avi', '.mkv'))][0]
        #.../...mp4
        self.filelength=ceil(len(self.filenames)/56)
        self.canv.grid_propagate(0)
        self.canv.columnconfigure(0, weight=1)
        self.canv.rowconfigure(0, weight=1)
        self.mainfo= str(Path(self.filenames[0]).parents[1])+"/"
        #videopath/
        self.q=self.readf()
        # [(a,b),(a,b)]
        self.req=Canvas(self.can1, width=100, height=25,bg="skyblue", highlightthickness=0)#self, width=self.width, height=100, highlightthickness=0
        self.can1.create_window(1100,25,window=self.req,anchor='ne')
        self.req.grid_propagate(0)
        self.req.rowconfigure(0, weight=1)
        self.req.columnconfigure(0, weight=1)
        self.prev=Button(self.req,text="prev page",command=self.prpg)
        self.prev.grid(row=0,column=0, sticky = W+E+N+S)
        self.req=Canvas(self.can1, width=100, height=25,bg="skyblue", highlightthickness=0)#self, width=self.width, height=100, highlightthickness=0
        self.can1.create_window(1100,50,window=self.req,anchor='ne')
        self.req.rowconfigure(0, weight=1)
        self.req.columnconfigure(0, weight=1)
        self.curnext=0
        self.next=Button(self.req,text="next page",command=self.nxpg)
        self.next.grid(row=0,column=0, sticky = W+E+N+S)
        self.req=Canvas(self.can1, width=100, height=25,bg="skyblue", highlightthickness=0)#self, width=self.width, height=100, highlightthickness=0
        self.can1.create_window(1100,75,window=self.req,anchor='ne')
        self.req.rowconfigure(0, weight=1)
        self.req.columnconfigure(0, weight=1)
        self.clear=Button(self.req,text="clear",command=self.clear)
        self.clear.grid(row=0,column=0, sticky = W+E+N+S)
        self.req.grid_propagate(0)

        self.req=Canvas(self.can1, width=100, height=25,bg="skyblue", highlightthickness=0)#self, width=self.width, height=100, highlightthickness=0
        self.can1.create_window(0,100,window=self.req,anchor='sw')
        
        self.req.rowconfigure(0, weight=1)
        self.req.columnconfigure(0, weight=1)
        
        self.curpg=Label(self.req,text=str(self.curnext)+" of "+str(self.filelength-1))
        self.curpg.grid(row=0,column=0, sticky = W+E+N+S)
        
    
        self.req.grid_propagate(0)
        # self.canv.bind('<Configure>', lambda e:self.canv.configure(scrollregion=self.canv.bbox("all")))
        # self.rrcanv.bind_all("<MouseWheel>", self.screvl)
        # self.canv.bind("<Enter>", self.screv)
        # self.canv.bind("<Leave>", self.screv)
        def createpg():
            None
        for kk in range(self.filelength):#self.filelength
            # threading.Thread(target=writemla, args=(self.video_files, pp)).start()
            page:pgs=pgs(self.canv,kk,self)
            # print(page.start)
            # print(page.end)
            self.classes.append(page) 
        self.rcanv.yview_moveto(1.0)
        self.rrcanv.yview_moveto(1.0)    
        self.reqbut.destroy()
        self.sellabc.destroy()
        self.sellabd.destroy()
        self.tx.destroy()
        def thmla():
            pp=[]
            for sublist in self.gor:
                pp.append([(sublist[1]) ,(sublist[5])])
            threading.Thread(target=writemla, args=(self.video_files, pp)).start()
        self.reqbut=Button(self.reqa, text="create file",command=thmla)
        # self.req.rowconfigure(0, weight=1)
        # self.req.columnconfigure(0, weight=1)
        
        self.reqbut.pack(fill=BOTH,expand=True)


    def _bound_to_mousewheel(self, event):
        
        self.canv.bind_all("<MouseWheel>", self.screv)
        self.canv.bind_all('<Up>', lambda e:self.prpg())
        self.canv.bind_all('<Down>', lambda e:self.nxpg())


    def _unbound_to_mousewheel(self, event):
        self.canv.unbind_all("<MouseWheel>")
        self.canv.unbind_all('<Up>')
        self.canv.unbind_all('<Down>')
        
        
    def screv(self,event):
        if(int(-1*(event.delta/120))==-1): 
            self.prpg()
        if(int(-1*(event.delta/120))==1): 
            self.nxpg()  
        

    def show_frame(self, cont,option=None):
        if option:
            print(cont)
            for x in option:
                print(x)
        frame = self.classes[cont]
        self.curnext=cont
        frame.tkraise()  

    def nxpg(self):
        try:
            self.show_frame(self.curnext+1)
            self.curpg["text"]=str(self.curnext)+" of "+str(self.filelength-1)
        except:
            None   
    blue=(0, 255, 255, 76)
    red=(255, 0, 0, 76)
    def clear(self):
        self.aa=0
        self.gorap=[None,None,None]
        if self.num_file=="my_list1.txt":
            self.num_file="my_list.txt"
        else:
            self.num_file="my_list1.txt"
        # self.num_file="my_list1.txt"
        for foclist in self.gor:
            foclist[2][4].delete(foclist[2][1][1])
            foclist[2][4].delete(foclist[2][1][0])
            foclist[2][1][0]=None
            foclist[2][1][1]=None
            foclist[2][2]=0
            foclist[2][3]=None
            if(foclist[3]!=None):
                foclist[3][4].delete(foclist[3][1][1])
                foclist[3][4].delete(foclist[3][1][0])
                foclist[3][1][0]=None
                foclist[3][1][1]=None
                foclist[3][2]=0
                foclist[3][3]=None
        # self.store["mytext"]=self.gor
        self.gor=[]
        self.blue=(75, 0, 130, 76)
        self.red=(0, 139, 139, 76)
        print(self.gor)
        list = self.frame.grid_slaves()
        list0 = self.frame0.grid_slaves()
        for l in list:
            l.destroy()
        for l in list0:
            l.destroy() 
        q=self.readf()
        loop=True
        try:
            first_q,second_q=q.popleft()
        except:
            loop=False
        # print(first_q)

        h=100#event.widget.reqwidth
        w=119
        
        for page in self.classes:
            start:int=page.start
            end:int=page.end
            while (loop):
                if(self.inrange(start,end,first_q) or self.inrange(start,end,second_q)):
                    if(self.inrange(start,end,first_q)):
                        aj=page.frame_to_pic.get(first_q)
                        pcan=aj[4]
                        img=ImageTk.PhotoImage(Image.new('RGBA', (w,h), self.blue))
                        aj[1][0]=img
                        aj[2]=1
                        pcan.create_image(0, 0, image=aj[1][0], anchor='nw')
                        self.gorap=AutoUpdateList([len(self.gor), first_q,aj,None,self.canv,None])
                        #which_page, frame[0], list->aj[0], list->aj[1], self.pa, frame[1]
                        self.gor.append(self.gorap)
                        bold_font = font.Font(font='Helvetica 18 bold', height=12)
                        bb=pcan.create_text(0,0, text=str(aj[3])+"a", font=bold_font,fill="wheat", anchor='nw')
                        aj[1][1]=bb
                        if(not self.inrange(start,end,second_q)):
                            break
                    if(self.inrange(start,end,second_q)):
                        aj=page.frame_to_pic.get(second_q) 
                        pcan=aj[4]
                        self.gorap[3]=aj
                        img=ImageTk.PhotoImage(Image.new('RGBA', (w,h), self.red))
                        aj[1][0]=img
                        pcan.create_image(0, 0, image=aj[1][0], anchor='nw')
                        bold_font = font.Font(font='Helvetica 18 bold', height=12)
                        bb=pcan.create_text(0,0, text=str(aj[3])+"b", font=bold_font,fill="wheat", anchor='nw')
                        aj[1][1]=bb
                        self.gorap[5]=int(second_q)
                        aj[2]=2
                        # print(self.pini.gorap)
                        self.rbut=Button(self.frame,text=str(self.aa), command=lambda aa=self.gorap[0]: self.show_frame(aa)).grid(row=self.aa,column=0,pady=5,padx=10)
                        self.rrbut=Button(self.frame0,text=str(self.aa), command=lambda aa=self.gorap[1],bb=self.gorap[5]: self.thr(self.mainfo+self.video,aa,bb)).grid(row=self.aa,column=0,pady=5,padx=10)
                        self.aa+=1
                        self.gorap=[None,None,None]
                        try:
                            first_q,second_q=q.popleft()
                        except:
                            loop=False
                        continue  
                break
            if (not loop):
                break

    # rec=pgs
    def inrange(s,start,end,num):
        if start<=num<=end:
            return True
        return False
    def prpg(self):
        if(self.curnext!=0):
            self.show_frame(self.curnext-1)  
            self.curpg["text"]=str(self.curnext)+" of "+str(self.filelength-1) 
    def update_scrollregion(s,event,scr):
        canvas_width = event.width
        canvas_h = event.height
        event.widget.config(scrollregion=(0, 0, canvas_width, canvas_h))
        scr.config(command=event.widget.yview)         

    def __init__(self, master):
        Frame.__init__(self,master,background="yellow")
        self.pack(fill=BOTH, expand=True)
        self.can1=Canvas(self, width=self.width, height=100,bg="lightgreen", highlightthickness=0)#self, width=self.width, height=100, highlightthickness=0
        self.can1.pack(side="bottom")
        self.canv=Canvas(self, width=952, height=self.height-100, highlightthickness=0)
        self.rrcanv=Canvas(self, width=((1100-952)/2)-40, height=self.height-100, bg="white",highlightthickness=0)
        self.canv.pack(side="left")
        self.rcanv=Canvas(self, width=((1100-952)/2)-40, height=self.height-100, bg="black",highlightthickness=0)
        scra=Scrollbar(self,width=20)
        self.rcanv.config(yscrollcommand=scra.set)
        scra.config(command=self.rcanv.yview)
        self.frame=Frame(self.rcanv)
        self.rcanv.create_window((0, 0), window=self.frame, anchor=NW)
        self.rcanv.pack(side=LEFT, fill=BOTH, expand=True)
        self.frame.bind("<Configure>", lambda event, canvas=self.rcanv: canvas.configure(scrollregion=canvas.bbox("all")))
        self.rcanv.bind("<Configure>", lambda e,can=scra:self.update_scrollregion(e,can))
        self.rcanv.pack(side="left")
        scra.pack(side=LEFT, fill=Y)
        scr=Scrollbar(self,width=20)
        self.rrcanv.config(yscrollcommand=scr.set)
        scr.config(command=self.rrcanv.yview)
        self.frame0=Frame(self.rrcanv)
        self.rrcanv.create_window((0, 0), window=self.frame0, anchor=NW)
        self.rrcanv.pack(side=LEFT, fill=BOTH, expand=True)
        self.frame0.bind("<Configure>", lambda event, canvas=self.rrcanv: canvas.configure(scrollregion=canvas.bbox("all")))
        self.rrcanv.bind("<Configure>", lambda e,can=scr:self.update_scrollregion(e,can))
        self.rrcanv.pack(side="left")
        scr.pack(side=LEFT, fill=Y)
        self.reqa=Frame(self.can1, width=100, height=50,bg="skyblue", highlightthickness=0)#self, width=self.width, height=100, highlightthickness=0
        self.reqa.pack_propagate(0)
        self.can1.create_window(0,0,window=self.reqa,anchor='nw')
        self.reqbut=Button(self.reqa, text="load file",command=self.thrreq)
        self.reqbut.pack(fill=BOTH,expand=True)#grid(row=0,column=0, sticky = W+E+N+S)
        self.sellabc=Frame(self.can1, width=100, height=25, highlightthickness=0)
        self.sellabc.pack_propagate(0)
        self.tx=Label(self.sellabc,text="selecting")
        self.tx.pack(fill=BOTH,expand=True)
        self.sellabc.grid_propagate(False)
        self.can1.create_window(300,0,window=self.sellabc,anchor='nw')
        self.sellabd=Frame(self.can1, width=500, height=25, highlightthickness=0)
        self.sellabd.pack_propagate(0)
        self.can1.create_window(100,25,window=self.sellabd,anchor='nw')
        self.var=StringVar(self.sellabd)
        self.var.set('')
        
        with open("rec.txt", 'r') as file:
            lines = file.readlines()
        #find record history
        mywordlist = [line.strip() for line in lines]
        opmen=OptionMenu(self.sellabd, self.var,"",*mywordlist)
        opmen.pack(fill=BOTH,expand=True)

         
class pgs(Frame):
    def __init__(self, master,pa,pini:proj):
         Frame.__init__(self, master)
         self.pa=pini.canv
         self.grid(row=0,column=0, sticky = W+E+N+S)
         self.lower()
         self.start=None
         self.grid_propagate(0)
         self.can=Canvas(self,bg="skyblue")
         self.can.pack(fill=BOTH,expand=True)
         self.frame_to_pic={}
         self.pini=pini
         self.onpage()
    def onpage(self):
        x=8
        y=7
        xx=0
        yy=0
        self.size = (119,100)
        
        while(1):
            try:
                f=self.pini.filenames[self.pini.files]
                #prevent end
            except:
                self.pini.files=0
                xx=0
                yy=0
                #end
                return;    
            a=100*yy
            # print(a)
            b=119*xx  
            self.original = Image.open(f).resize(self.size)
            self.image = ImageTk.PhotoImage(image=self.original)
            self.pcan=Canvas(self.can,background="gray",width=self.image.width(),height=self.image.height())
            
            
            # lambda img:self.image
            #self.pini.linked_list.add_node
            #image,[color,text],012,ind
            # print(self.can.itemcget("0"))
            aj=([self.image,[None,None],0,0,self.pcan])#image,[green,red],012,ind,event,pg#

            
            # print(os.path.basename(Img))
            # print(os.path.dirname(Img))
            # print(re.findall(r"\d{8}",os.path.basename(f) )[0])
            self.can.create_window(b,a,window=self.pcan,anchor='nw')
            self.pcan.create_image(0, 0, image=aj[0], anchor="nw")
            p=int(re.findall(r"\d{8}",os.path.basename(f))[0])
            if (not self.start):
                self.start=p
            self.end=p
            # tag = f"frame_{p}"
            self.frame_to_pic[p]=aj
            # print(self.can.cget(tag))
            # print(p)
            h=100#event.widget.reqwidth
            w=119
            
            
            if self.pini.q:
                if p == self.pini.q[0][0]:
                    img=ImageTk.PhotoImage(Image.new('RGBA', (w,h), self.pini.blue))
                    aj[1][0]=img
                    aj[2]=1
                    self.pcan.create_image(0, 0, image=aj[1][0], anchor='nw')
                    self.pini.gorap=AutoUpdateList([len(self.pini.gor), p,aj,None,self.pa,None])
                    #which_page, frame[0], list->aj[0], list->aj[1], self.pa, frame[1]
                    self.pini.gor.append(self.pini.gorap)
                    bold_font = font.Font(font='Helvetica 18 bold', height=12)
                    bb=self.pcan.create_text(0,0, text=str(aj[3])+"a", font=bold_font,fill="wheat", anchor='nw')
                    aj[1][1]=bb
                    # self.pini.left_click(self.pcan,p,aj,self.pa)
                elif p == self.pini.q[0][1]:
                    # self.pini.right_click(self.pcan,p,aj)
                    # print(self.pini.gorap)
                    self.pini.gorap[3]=aj
                    img=ImageTk.PhotoImage(Image.new('RGBA', (w,h), self.pini.red))
                    aj[1][0]=img
                    self.pcan.create_image(0, 0, image=aj[1][0], anchor='nw')
                    bold_font = font.Font(font='Helvetica 18 bold', height=12)
                    bb=self.pcan.create_text(0,0, text=str(aj[3])+"b", font=bold_font,fill="wheat", anchor='nw')
                    aj[1][1]=bb
                    self.pini.gorap[5]=int(p)
                    aj[2]=2
                    # print(self.pini.gorap)
                    self.pini.rbut=Button(self.pini.frame,text=str(self.pini.aa), command=lambda aa=self.pini.gorap[0]: self.pini.show_frame(aa)).grid(row=self.pini.aa,column=0,pady=5,padx=10)
                    self.pini.rrbut=Button(self.pini.frame0,text=str(self.pini.aa), command=lambda aa=self.pini.gorap[1],bb=self.pini.gorap[5]: self.pini.thr(self.pini.mainfo+self.pini.video,aa,bb)).grid(row=self.pini.aa,column=0,pady=5,padx=10)
                    self.pini.aa+=1
                    self.pini.gorap=[None,None,None]
                    # self.pini.button_postion+=1
                    # self.rcanv.yview_moveto(1.0)
                    # self.rrcanv.yview_moveto(1.0)   
                    self.pini.q.popleft()
            self.pcan.bind("<Button-1>", lambda e, p=p,se=aj,pa=self.pa:self.pini.left_click(e.widget,p,se,pa))#ze=self.pini.curpic
            self.pcan.bind("<Button-3>", lambda e, p=p,se=aj:self.pini.right_click(e.widget,p,se))
            self.pini.curpic+=1
            self.pini.files+=1  
            if(yy==y):
                break
            if(xx+1==x):
               yy+=1
               xx=0
            else:
                xx+=1 


        


root=Tk()
app=proj(root)

root.geometry("{}x{}+{}+{}".format(app.width,app.height,200,10))



root.resizable(False,False)
root.mainloop()