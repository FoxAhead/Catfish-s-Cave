import os
import gzip
import shutil

dir_in = 'jpwbeest2'
dir_out = 'jpwbeest2_out'

def IsGzip(_filePath):
    _return = False
    try:
        with gzip.GzipFile(_filePath) as gzipobj:
            data = gzipobj.read()
        _return = True
    except Exception as inst:
        _return = False
    return _return
    
for subdir, dirs, files in os.walk(dir_in):
    for filename in files:
        file_in = os.path.join(subdir, filename)
        file_out = os.path.join(dir_out, file_in)
        directory = os.path.dirname(file_out)
        if not os.path.exists(directory):
            os.makedirs(directory)
        if IsGzip(file_in):
            print('UNGZIP', end = ': ')
            with gzip.open(file_in, 'rb') as f_in:
                with open(file_out, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
        else:
            print('COPY', end = ': ')
            with open(file_in, 'rb') as f_in:
                with open(file_out, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
        print(file_in, end = '-> ')
        print(file_out)


