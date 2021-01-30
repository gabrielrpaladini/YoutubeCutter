from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import cv2

class Video:

    def __init__(self, title):

        self.title = 'downloads/' + title
        self.targetname = ''

    def calculate_time_inputs(self, time):

        time = time.split(':')

        time_hours = int(time[0])
        time_minutes = int(time[1])
        time_secs = int(time[2])

        time_hours = time_hours * 3600
        time_minutes = time_minutes * 60

        total_time = time_hours + time_minutes + time_secs

        return total_time

    def cut_video(self, time_ini, time_end, targetname):

        time_ini = self.calculate_time_inputs(time_ini)
        time_end = self.calculate_time_inputs(time_end)

        targetname = 'cuts/' + targetname

        self.targetname = targetname
        
        ffmpeg_extract_subclip(self.title, time_ini, time_end, targetname=targetname)

class Image(Video):

    def __init(self, targetname):

        super().__init__(targetname)

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