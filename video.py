from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import cv2

class Video:

    def __init__(self, title):

        self.title = 'downloads/' + title
        self.targetname = ''

    def CutVideo(self, start_time, end_time, targetname):

        targetname = 'cuts/' + targetname

        self.targetname = targetname
        
        ffmpeg_extract_subclip(self.title, start_time, end_time, targetname=targetname)


    def CutImage(self, frame, name):

        vidcap = cv2.VideoCapture(self.targetname)

        sucess, image = vidcap.read()

        count = 0

        while sucess:

            if count != frame:

                pass

            else:

                cv2.imwrite('images/{}_{}.jpg'.format(name, count), image)
                print('*** Printing')

            sucess, image = vidcap.read()
            
            count += 1