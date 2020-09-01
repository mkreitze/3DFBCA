#This code takes a 3D FBCA data structure (glorified 3D array) and outputs an obj file which renders boxes for every filled state
#Made in hopes that the resulting structures will be interesting to analyze 
#Matthew Kreitzer, August 2020

#For testing a method to initalize the FBCAs was generated
CALength=20
CAWidth=20
CAHeight=20
numOfStates=2
sizeOfCubes=1.0 #Will be changed later
QUANTIFER="TestOBJ"

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
                #holder[z].state=random.randint(0,fBCA.n)
                holder1[z].state=1
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
    fileName.write("usemtl Material.001 \ns off \n")
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

def genObj(fBCA):
    objRend= open(str(QUANTIFER)+ " objRender"+".obj",'x')
    objRend.write("# "+str(QUANTIFER)+" OBJ RENDER \n")
    cubeNum=0
    for x in range(fBCA.length):
        for y in range(fBCA.width):
            for z in range(fBCA.height):
                #Considering 1 as the full state
                if (fBCA.levelMap[x][y][z].state==1):
                    #implement sizeOfCubes better
                    cubeNum=genCube(x,y,z,sizeOfCubes,objRend,cubeNum)    


#MAIN FUNCTION
fBCA=Fbca()
fBCA.length=CALength
fBCA.width=CAWidth
fBCA.height=CAHeight
fBCA.n=numOfStates
fBCA.levelMap=init3DFBCA(fBCA)
genObj(fBCA)