

from os import listdir
from os.path import isdir, isfile, basename, getsize

start_path = r'E:'

def Walkpas(path):
    if isfile(path) and ( 200 * 1024 * 1024 < getsize(path) < 1024 * 1024 * 3000) :   
        file_source = open(path, 'r')
        file_content = file_source.read(4)
        if file_content in ('.RMF', 'RIFF'):
            print 'Found target file:' + path
        file_source.close()
    if isdir(path):
        try:
            for item in listdir(path):
                Walkpas(path+'\\'+item)
        except:
            pass
		   
def main():
    Walkpas(start_path)
    raw_input('Finished!!! Press any key to continue!\n')
if __name__ == '__main__':
    main()
    
