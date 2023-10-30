from scenedetect import detect, ContentDetector

class pysc: 
    filepath="E:\original"
    def ope(raw):
        scene_list = detect(raw.filepath, ContentDetector(),None,False,None)
        # cap = cv2.VideoCapture(fn)
# length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))-1
# width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps    = cap.get(cv2.CAP_PROP_FPS)
# dur=length/fps
# print( length,width,fps)
        bb=[]
        for scene in scene_list:
            # print('    Scene %2d: Start: %s / Frame %d, End %s / Frame %d' % (
            #     i+1,
            #     scene[0].get_timecode(), scene[0].get_frames(),
            #     scene[1].get_timecode(), scene[1].get_frames())
            # )
            bb.append([int(scene[0].get_frames()),int(scene[1].get_frames())-1])
        bb[len(bb)-1][1]=bb[len(bb)-1][1]+1
        return bb
