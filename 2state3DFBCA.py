#This code takes a 3D FBCA data structure (glorified 3D array) and outputs an obj file which renders boxes for every filled state
#Made in hopes that the resulting structures will be interesting to analyze 
#Matthew Kreitzer, August 2020
import random
import math
import os 
import numpy
#For testing a method to initalize the FBCAs was generated
CALength=8
CAWidth=8
CAHeight=4
numOfStates=2
numOfGens=100
sizeOfCubes=1.0 #Will be changed later
random.seed(1)  #1 for held  
sMs=[[0.1,1.2,2.0,0],[0.1,1.2,2.0,0]]
genObjs=1 #Does this generate OBJs?
QUANTIFER="This Gets Changed To the Score Matrix Name"

class CACell:
    state=0
    score=0
class Fbca:
    width=0
    length=0
    height=0
    n=0
    levelMap=[]
    scoreMatrix=[]

#COMMENT CORRECTLY
def init3DFBCA(fBCA):
    #fills empty list with random states (x then y: downward strips)
    for x in range(fBCA.length):
        holder2=[]
        for y in range(fBCA.width):
            holder1=[]
            for z in range(fBCA.height):
                holder1.append(CACell())
                holder1[z].state=random.randint(0,fBCA.n-1)
            holder2.append(holder1)
        fBCA.levelMap.append(holder2)
    return(fBCA.levelMap)

#COMMENT CORRECTLY
def genCube(x,y,z,size,fileName,num=0):
    #Starting gibberish
    fileName.write("o Cube."+str(num)+"\n")
    #GENERATE POINTS
    xpoints=[];ypoints=[];zpoints=[]
    xpoints.append(x-size/2);xpoints.append(x+size/2)   
    ypoints.append(y-size/2);ypoints.append(y+size/2)   
    zpoints.append(z-size/2);zpoints.append(z+size/2)   
    for x2 in xpoints:
        for y2 in ypoints: 
            for z2 in zpoints:
                fileName.write("v  "+str(z2)+"  "+str(y2)+"  "+str(x2)+"\n")
    #generate surface normals (Only done if not done before)
    #fileName.write("usemtl Material.001 \ns off \n")
    fileName.write("vn 1.0 0.0 0.0 \n")
    fileName.write("vn -1.0 0.0 0.0 \n")
    fileName.write("vn 0.0 1.0 0.0 \n")
    fileName.write("vn 0.0 -1.0 0.0 \n")
    fileName.write("vn 0.0 0.0 1.0 \n")
    fileName.write("vn 0.0 0.0 -1.0 \n")
    #generates faces
    one=1+num*8;two=2+num*8;three=3+num*8;four=4+num*8;five=5+num*8;six=6+num*8;seven=7+num*8;eight=8+num*8
    fileName.write("f "+str(one)+"//"+str(six)+" "+str(two)+"//"+str(six)+" "+str(three)+"//"+str(six)+"\n") 
    fileName.write("f "+str(two)+"//"+str(six)+" "+str(three)+"//"+str(six)+" "+str(four)+"//"+str(six)+"\n") 
    fileName.write("f "+str(five)+"//"+str(five)+" "+str(six)+"//"+str(five)+" "+str(seven)+"//"+str(five)+"\n") 
    fileName.write("f "+str(six)+"//"+str(five)+" "+str(seven)+"//"+str(five)+" "+str(eight)+"//"+str(five)+"\n") 
    fileName.write("f "+str(one)+"//"+str(four)+" "+str(two)+"//"+str(four)+" "+str(five)+"//"+str(four)+"\n") 
    fileName.write("f "+str(two)+"//"+str(four)+" "+str(five)+"//"+str(four)+" "+str(six)+"//"+str(four)+"\n") 
    fileName.write("f "+str(three)+"//"+str(three)+" "+str(four)+"//"+str(three)+" "+str(seven)+"//"+str(three)+"\n")  
    fileName.write("f "+str(four)+"//"+str(three)+" "+str(seven)+"//"+str(three)+" "+str(eight)+"//"+str(three)+"\n") 
    fileName.write("f "+str(two)+"//"+str(one)+" "+str(four)+"//"+str(one)+" "+str(six)+"//"+str(one)+"\n") 
    fileName.write("f "+str(four)+"//"+str(one)+" "+str(six)+"//"+str(one)+" "+str(eight)+"//"+str(one)+"\n") 
    fileName.write("f "+str(one)+"//"+str(two)+" "+str(three)+"//"+str(two)+" "+str(five)+"//"+str(two)+"\n") 
    fileName.write("f "+str(three)+"//"+str(two)+" "+str(five)+"//"+str(two)+" "+str(seven)+"//"+str(two)+"\n")      
    fileName.write("\n\n")
    return(num+1)

#COMMENT CORRECTLY
def genObj(fBCA,updateNum=0,directory=""):
    QUANTIFER=str(fBCA.scoreMatrix)+" Gen"+str(updateNum)
    objRend= open(directory+str(QUANTIFER)+ " objRender"+".obj",'x')
    objRend.write("# "+str(QUANTIFER)+" OBJ RENDER \n")
    cubeNum=0
    for x in range(fBCA.length):
        for y in range(fBCA.width):
            for z in range(fBCA.height):
                #Considering 1 as the full state
                if (fBCA.levelMap[x][y][z].state==1):
                    #implement sizeOfCubes better
                    cubeNum=genCube(x,y,z,sizeOfCubes,objRend,cubeNum)    

#COMMENT CORRECTLY
def copyOver(fBCAOld):
    levelMapNew=[]
    #fills empty list with random states (x then y: downward strips)
    for x in range(fBCAOld.length):
        holder2=[]
        for y in range(fBCAOld.width):
            holder1=[]
            for z in range(fBCAOld.height):
                holder1.append(CACell())
                holder1[z].state=fBCA.levelMap[x][y][z].state
            holder2.append(holder1)
        levelMapNew.append(holder2)
    return(levelMapNew)

#COMMENT CORRECTLY
#took folder creation function from https://gist.github.com/keithweaver/562d3caa8650eefe7f84fa074e9ca949
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def updateMap(fBCA):

    #To start, hardcode the neighbourhood. It is a list of tuples representing the x and y offset from the center square
    neighbours=[]
    neighbours.append((0,1,0))#top (1 up)
    neighbours.append((0,-1,0))#bot (1 down)
    neighbours.append((-1,0,0))#left (1 left)
    neighbours.append((1,0,0))#right (1 right)
    neighbours.append((0,0,-1))#below (1 bot)
    neighbours.append((0,0,1))#above (1 top)
    for x in range(fBCA.length):
        for y in range(fBCA.width):
            for z in range(fBCA.height):
                #Need to get score from center square and its neighbours.
                row=0; row = fBCA.levelMap[x][y][z].state*fBCA.n #the center colour determines the row of the score matrix used 
                col=0; #the col of the score matrix used will depend on the  neighbours state
                fBCA.levelMap[x][y][z].score=0 #resets center square's score
                #sums scores
                for w in neighbours:
                    col=fBCA.levelMap[(x+w[0])%fBCA.length][(y+w[1])%fBCA.width][(z+w[2])%fBCA.height].state #mod used to connect edges
                    fBCA.levelMap[x][y][z].score+=fBCA.scoreMatrix[row+col] #since the score matrix is a list, row+col gives the correct entry
    #start by copying the map
    CAMapCopy=copyOver(fBCA)
    #for every cell, find the highest score among neighbours
    for x in range(fBCA.length):
        for y in range(fBCA.width):
            for z in range(fBCA.height):
                #NOTE: We give priority to the center square on ties. Priority continues up with the last defined neighbour to have the worst priority
                bigScore=0;bigScore=fBCA.levelMap[x][y][z].score
                #compares neighbours scores, reassigning bigScore and state if someone is bigger
                for w in neighbours:
                    if(bigScore<fBCA.levelMap[(x+w[0])%fBCA.length][(y+w[1])%fBCA.width][(z+w[2])%fBCA.height].score):
                        bigScore=fBCA.levelMap[(x+w[0])%fBCA.length][(y+w[1])%fBCA.width][(z+w[2])%fBCA.height].score
                        CAMapCopy[x][y][z].state=fBCA.levelMap[(x+w[0])%fBCA.length][(y+w[1])%fBCA.width][(z+w[2])%fBCA.height].state
    return(CAMapCopy)
#MAIN FUNCTION
#COMMENT WHAT THIS IS DOING
fBCAInit=Fbca()
fBCAInit.length=CALength
fBCAInit.width=CAWidth
fBCAInit.height=CAHeight
fBCAInit.n=numOfStates
fBCAInit.levelMap=init3DFBCA(fBCAInit)

#COMMENT WHAT THE FOR IS FOR
for idx,sM in enumerate(sMs):
    fBCA=Fbca()
    fBCA.length=CALength
    fBCA.width=CAWidth
    fBCA.height=CAHeight
    fBCA.n=numOfStates
    fBCA.scoreMatrix=sM
    fBCA.levelMap=copyOver(fBCAInit)
    #COMMENT THIS 
    if(genObjs==1): 
        fileName=str(sM)+" "+str(idx)
        createFolder(fileName)
        #since the x and y value 
        d = os.getcwd()+"/"+str(fileName)+"/"
    #runs FBCA to desired number of gens
    for genNum in range(numOfGens):
        if(genObjs==1):
            genObj(fBCA,genNum,d)
        fBCA.levelMap=updateMap(fBCA)

    print("Finished "+str(sM))
