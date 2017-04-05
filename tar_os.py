import sys
import tarfile
import os
import shutil
import time

def extracttar(tarball_name):
    #print tarball_name
    currentwd = os.getcwd()
    print currentwd
    tarball = tarfile.open('Code_reading_for_reference.tar.gz','r')
    #print tarball
    ##print tarball.getnames()
    #for items in tarball.getmembers():
        #print items.name
        #print items.size
    path_for_extract = os.path.join(currentwd,'output')
    if os.path.isdir(path_for_extract):
        shutil.rmtree(path_for_extract)
    os.mkdir(path_for_extract)
    print os.listdir(path_for_extract)
    tarfile.TarFile.extractall(tarball,path_for_extract)
    print os.listdir(path_for_extract)
    #tarball.extractall('outDir')
    #print extracted_tar
    #print os.listdir('outDir')
    #extracted_path = os.path.join(os.getcwd(),'outDir')
    return path_for_extract

def process_file(filepath):
    print filepath
    new_folder = os.path.join(filepath,'codefiles')
    #print new_folder
    if os.path.isdir(new_folder):
        shutil.rmtree(new_folder)
    os.mkdir(new_folder)
    for dirs,subdirs,files in os.walk(filepath):
        #print files
        for file in files:
            if file.endswith('.py') or file.endswith('.PY'):
                cwd = os.getcwd()
                #print cwd
                current_loc = os.path.join(dirs,file)
                #print current_loc
                new_loc = os.path.join(new_folder,file)
                #print new_loc
                shutil.move(current_loc,new_loc)
    return new_folder

def create_tar(folderpath):
    print folderpath
    tarfilename = 'codefiles_'+time.strftime('%Y-%m-%d-%H-%M-%S')+'_tarball.tar.gz'
    tarball = tarfile.open(tarfilename,'w:gz')
    cwd1 = os.getcwd()
    os.chdir(folderpath)
    folder_list= os.listdir(folderpath)
    print folder_list
    for files in folder_list:
        tarball.add(files)
    tarball.close()
    os.chdir(cwd1)
    if os.path.exists(folderpath):
        shutil.rmtree(folderpath)


if __name__ == '__main__':
    par1 = sys.argv[1]
    #print par1
    extracted_filepath = extracttar(par1)
    #print extracted_filepath
    newfiles_location = process_file(extracted_filepath)
    #print newfiles_location
    create_tar(newfiles_location)



