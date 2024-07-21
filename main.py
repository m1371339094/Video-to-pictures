import cv2
from collections import deque
import os
import shutil
from pysce import pysc
from tkinter import filedialog
import codecs
# def txlis(txt="frm.txt"):
#  with open(txt,"r") as mlt:
#     x=mlt.read()
#  return json.loads(x)       
def create_dir(video_path):
        filename = os.path.basename(video_path)
        folder_name = os.path.splitext(filename)[0]
        thumbs=os.path.dirname(video_path)+"\\thumbs"
        if not os.path.exists(thumbs):
            os.makedirs(thumbs)
            return video_path
        else:
            # Move the video file into the new folder
            new_folder_path = os.path.join(os.path.dirname(video_path), folder_name)
            thumbs = os.path.join(new_folder_path, "thumbs")
            os.makedirs(new_folder_path, exist_ok=True)
            shutil.move(video_path, new_folder_path)
            return new_folder_path
def vidtx(fn="pro1\video.mp4",vid=cv2.VideoCapture("pro1\video.mp4")):
    pat=os.path.dirname(fn)
    tx=codecs.open(pat+"\\videosInfo.txt","w","utf-8")
    # with open(pat+"\\videosInfo.txt","w","utf-8") as tx:
    ll=["1\n",os.path.basename(fn)+"\n",str(int(vid.get(cv2.CAP_PROP_FRAME_COUNT))-1)+"\n",str(vid.get(cv2.CAP_PROP_FPS))]
    # print(ll)
    tx.writelines(ll)
    tx.close


def pystodmd(fn="E:\\src\\out.mp4",fms=10,q=deque()):
    video_capture = cv2.VideoCapture(fn)
    vidtx(fn,video_capture)
    fn=create_dir(fn)
    pat=os.path.dirname(fn)
    main=deque()
    while q:
       start,end=q.popleft()
       inc=start
       while inc<end-2:
          main.append(inc)
          if inc==start:
            if end-start>5:
                main.append(start+1)
                main.append(start+2)
          inc=inc+fms
       if end-start>3:
           main.append(end-2)
           main.append(end-1) 
       main.append(end) 
    qq=deque()
    deq=str("00000000")
    # print(main)
    for num in main:
        qq.append("0"*(8-len(str(num)))+str(num))
    print(qq)
    while True:
        frame_is_read, frame = video_capture.read()
        if frame_is_read==True:       
            cv2.imwrite(f"{pat}\\thumbs\\{os.path.basename(fn)}^{str(deq)}.jpg", frame)
            if qq:
                deq=qq.popleft()
                video_capture.set(cv2.CAP_PROP_POS_FRAMES, int(deq))
            else:
                break
                      
def pcked(fp):
    clas=pysc()
    clas.filepath=fp
    print("start printing")
    lis=clas.ope()
    print("py finish")
    pystodmd(fp,10,lis)
    print("all finish")
if __name__ == '__main__':
    print("start")
    fn = filedialog.askopenfilename(initialdir=".",
                                             title="edited",
                                             filetypes= (("text files","*.mp4"),
                                             ("all files","*.*")))
    print("inpc")
    pcked(fn)
# fn="E:\\src\\out.mp4"   
# pat=os.path.dirname((fn))
# print(pat+"\\videosInfo.txt")
# if pat=="":
#     pat=os.getcwd()+"\\"+fn
# print(pat)    
# print(os.path.dirname(__file__))      
# print(os.path.basename(__file__))   
# dir = os.listdir(os.getcwd()+"\\thumbs")        
# if len(dir) == 0:
#     print("Empty directory")
# else:
#     print("Not empty directory")  
