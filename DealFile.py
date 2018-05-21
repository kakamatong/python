#coding:utf-8
import os
import shutil
import zipfile
# shutil.copyfile("oldfile","newfile") oldfile和newfile都只能是文件
# 创建多级目录：os.makedirs（"/Users/ximi/version"）
# 创建单个目录：os.mkdir（"project"）
# #复制文件
# shutil.copyfile('listfile.py', 'd:/test.py')
# shutil.rmtree("dir") 空目录、有内容的目录都可以删
# 检验给出的路径是否真地存:os.path.exists()

files = [

]

channelIDs = [

]

hotupPath = [

]

dirs = [

]

def deleteFilesAndDirs():
    for f in files:
        path = os.path.join(f)
        if os.path.isfile(path):
            os.remove(path)
    for f in dirs:
        path = os.path.join(f)
        if os.path.isdir(path):
            shutil.rmtree(path)
    copyResToChannel()
    pass

def copyResToChannel():
    for strdir in channelIDs:
        #mkdir(strdir)
        tmpPath2 = os.path.join(os.getcwd(), strdir, "Resources")
        if os.path.exists(tmpPath2):
            shutil.rmtree(tmpPath2)
            pass
        #print tmpPath2
        shutil.copytree("Resources", tmpPath2)
        tmpPath3 = os.path.join(tmpPath2, "GameHotUpdate")
        if os.path.exists(tmpPath3):
            shutil.rmtree(tmpPath3)
            pass
        for hppath in hotupPath:
            nowPath = os.path.join("5.0GD",strdir,hppath)
            toPath = os.path.join(tmpPath3, hppath)
            if os.path.exists(nowPath):
                shutil.copytree(nowPath, toPath)
                print "copy " + toPath + " success"
                pass
            else:
                print nowPath + " not exist!"
                pass
            pass
        tmpzipPath = os.path.join(os.getcwd(), strdir)
        startZip(tmpzipPath)
        pass
    pass

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print path + " create success"
        pass
    else:
        print "dir is existed"
        pass
    pass


def startZip(filePaths):
    zipName = "Resources.zip"
    z = zipfile.ZipFile(zipName, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(filePaths):
        fpath = dirpath.replace(filePaths,'') #这一句很重要，不replace的话，就从根目录开始复制
        fpath = fpath and fpath + os.sep or ''#这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
        for filename in filenames:
            print ("files:"+os.path.join(dirpath, filename))
            z.write(os.path.join(dirpath, filename),fpath+filename)
        for dirName in dirnames:
            print ("dir:"+os.path.join(dirpath, dirName))
            pass
        #print ('zip success')
        pass
    z.close()
    pass

deleteFilesAndDirs()