from os import path

import json

from datetime import datetime


def upload(drive, uploadListPath, remoteDirId, filesDir):
    def file_exists(filePath):
        return path.exists(filePath) and path.isfile(filePath)

    def file_upload(drive, filePath, fileId):
        if file_exists(filePath):
            params = {'parents': [{'id': remoteDirId}], 'title': path.basename(filePath)}
            if fileId:
                params['id'] = fileId

            gfile = drive.CreateFile(params)
            gfile.SetContentFile(filePath)
            gfile.Upload()

            now = datetime.now() \
                .strftime("%d/%m/%Y %H:%M:%S")
            print(now + " - Uploaded " + path.basename(filePath))
            return params.get('id') or gfile['id']
        else:
            print("File " + filePath + " doesn\'t exist")

    if file_exists(uploadListPath):
        with open(uploadListPath, 'r+') as json_file:
            data = json.load(json_file)
            if 'files' in data:
                for item in data['files']:
                    if 'fileName' in item:
                        print("Loading " + item['fileName'])

                        def getpath(dir, file):
                            if dir:
                                return "{}/{}".format(dir, file)
                            else:
                                return file

                        item['fileId'] = file_upload(
                            drive,
                            getpath(filesDir, item['fileName']),
                            item.get('fileId')
                        ) or item.get('fileId')

                    else:
                        print("\"fileName\" must be provided in " + uploadListPath)

                json_file.seek(0)
                json_file.truncate(0)

                json.dump(data, json_file)
                json_file.close()

            else:
                print("\"files\" doesn't exist in " + uploadListPath)
