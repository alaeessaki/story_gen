import  random
import sys
import os
import shutil

#P >> program
#T >> theme
#I >> Image

#Images manipulation
#initial Lists
ImagesPathList = []
ImagesList = []

#intial data
data = []


char1 = sys.argv[1]
data.append(char1)

char2 = sys.argv[2]
data.append(char2)

scriptFile = sys.argv[3]
data.append(scriptFile)

#Structure The Script.rpy (with 3 choices )
# here !!!


# manipulation functions
def moveFileFunc(src,dest):
    shutil.move(src , dest)

def changeDirFunc(dir):
    os.chdir(dir)

def joinPathFunc(pathDer):
    cwd = os.getcwd()
    path = os.path.join(cwd , pathDer)
    return path


def getListOfFilesFunc(dirName):
    for dir , subDir , files in os.walk(dirName):
        ImagesPathList.append(dir)

        for subF in files :
            ImagesList.append(subF)


def Main():

    #reading scene file
    scene = open(data[2] , "r+")
    scene1 = scene.read()
    sceneRen = open("script.rpy", "w")

    #Init Characters
    #moveFileFunc(joinPathFunc("Characters") , joinPathFunc("images") )
    changeDirFunc(joinPathFunc("images"))
    dirName = os.getcwd()
    print(getListOfFilesFunc(dirName))

    #Structure The Script.rpy (without choices)
    char1 = 'define client = Character("{}")\n'.format(data[0])
    char2 = 'define agent = Character("{}")\n'.format(data[1])
    selectedImg = random.choice(ImagesList)
    img = 'image eileen happy = "{}"\n'.format(selectedImg)
    startP = "label start :\n"
    sceneT = "scene bg room\n"
    sceneI = "show eileen happy with dissolve:\n    xzoom 0.5 yzoom 0.5\n"
    exe_c = "\nreturn"

    sceneRen.write(char1)
    sceneRen.write(char2)
    sceneRen.write(img)
    sceneRen.write(startP)
    sceneRen.write(sceneT)
    sceneRen.write(sceneI)
    sceneRen.write(str(scene1))
    sceneRen.write(exe_c)

    #close files
    scene.close()
    sceneRen.close()

if __name__ == "__main__":
    Main()
