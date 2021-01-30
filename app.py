from downloadvid import DownloadVideo
from video import Video, Image
import os
import sys
from directory import Directory

if __name__ == "__main__":

    if len(sys.argv) < 2:

        raise ValueError('System Parameters are required')

    paths = Directory()

    paths.create_directory()

    exists_video = sys.argv[1]

    if exists_video == '-u':

        url_target = sys.argv[2]

        download_utils = DownloadVideo(url_target)
        
        print('Start a download...')

        download_utils.download()

        print('video downloaded...')

        video_title = download_utils.returntitle()

    elif exists_video == '-n':

        video_title = sys.argv[2]
        video_title = str(video_title).replace('.mp4', '')

    time_ini = sys.argv[3]
    time_end = sys.argv[4]

    targetname = sys.argv[5]+'.mp4'

    video_utils = Video(video_title+'.mp4')

    video_utils.cut_video(time_ini, time_end, targetname)

    print(f'Video {video_title} cutted.')
