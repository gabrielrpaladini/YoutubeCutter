import pandas as pd
from downloadvid import DownloadVideo
from video import Video
import os

# Ask if file exists

file_y_n = str(input('File exists: (n/y): ')).upper()

if file_y_n == 'Y':

    files_list = os.listdir('downloads/')

    for i in range(len(files_list)):

        print('Press {} to {}: '.format(i, files_list[i]))

    file_number = int(input('Number: '))

    video_title = files_list[i]

    video_title = str(video_title).replace('.mp4', '')

    print('*** video title: {}'.format(video_title))

else:

    # Ask url

    url_target = str(input('Url youtube: '))

    # Instance download class

    download_utils = DownloadVideo(url_target)

    print('*** starting download')

    download_utils.download()

    print('*** video downloaded')

    video_title = download_utils.returntitle()

    print('*** video title: {}'.format(video_title))

video_utils = Video(video_title+'.mp4')

start_time_hours = float(input('When the cut starts (Hours): '))
start_time_minutes = float(input('When the cut starts (Minutes): '))
start_time_secs = float(input('When the cut starts (Seconds): '))

start_time_hours = start_time_hours * 3600
start_time_minutes = start_time_minutes * 60

start_time = start_time_hours + start_time_minutes + start_time_secs

end_time_hours = float(input('When the cut ends (Hours): '))
end_time_minutes = float(input('When the cut ends (Minutes): '))
end_time_secs = float(input('When the cut ends (Seconds): '))

end_time_hours = end_time_hours * 3600
end_time_minutes = end_time_minutes * 60

end_time = end_time_hours + end_time_minutes + end_time_secs

targetname = str(input('Name the exit file: ')) + '.mp4'

video_utils.CutVideo(start_time, end_time, targetname)

print('*** cut video')

frame_cut = int(input('*** Insert frame to cut image: '))
image_name = str(input('*** Insert image name: '))

image_name = 'thumbnail_'+image_name

video_utils.CutImage(frame_cut, image_name)

print('*** {} created'.format(image_name))
