import os

class Directory():

    def __init__(self):

        self.paths = ['images/', 'downloads/', 'cuts']

    def create_directory(self):

        for path in self.paths:

            exists = os.path.exists(path)

            if exists == False:

                os.mkdir(path)