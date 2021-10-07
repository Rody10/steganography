import sys

def openImage(name):
    with open(name, 'r') as ppm:
        image = ppm.read()
    return image


def removeComments(rawImage):
    cleanedImage = rawImage.splitlines() 
    for n in cleanedImage:
        if n[0]=='#':
            cleanedImage.remove(n)
    return cleanedImage


def getColumns(cleanedImage):
    info = cleanedImage[1].split()
    numColumns = info[0]
    return numColumns
    
def getRows(cleanedImage):
    info = cleanedImage[1].split()
    numRows = info[1]
    return numRows

def getMaxColour(image):
    maxColour = max(image)
    return maxColour

def createPpmFile(imageListData,numColumns,numRows,maxColour,imgFormat):
    ppmList = []
    ppmList.append(imgFormat)
    ppmList.append(str(numColumns) + ' ' + str(numRows))
    ppmList.append(maxColour)

    for n in imageListData:   #copy values of newly calculated image
        ppmList.append(n)


    f = open("newImage.ppm","w+")
    for n in ppmList:
        f.write(str(n))
        f.write("\n")

    f.close()
#-----------------------------------------------------------------------------



def hideMessage(cleanedImage, message, numColumns, numRows):
    newImage = []
   
        
    
    messageLength = len(message)
    if (messageLength<10):
        newImage.append(0)
        newImage.append(0)
        newImage.append(messageLength)
    if (messageLength>10 and messageLength<100):
        newImage.append(0)
        for char in str(messageLength):
            newImage.append(int(char))

    for char in message:
        aValue = ord(char)
        if (aValue<100):
            newImage.append(0)
            for c in str(aValue):
                newImage.append(int(c))
        else:
            for c in str(aValue):
                newImage.append(int(c))

    maxColour = getMaxColour(newImage)
    createPpmFile(newImage,numColumns,numRows,maxColour, "P2")
    print("Message has been hidden in newImage.ppm")



def revealMessage(cleanedImage):
    message = ""
    x = range(6,len(cleanedImage),3)
    for n in x:
        message = message + chr(int((cleanedImage[n])+(cleanedImage[n+1])+(cleanedImage[n+2])))
        
    print("Hidden message is: " + message)


def main():
    operation = input("Do you want to hide or reveal information? Type hide or reveal.")
    imageName = input ("Enter the image name: ")


    rawImage = openImage(imageName)
    cleanedImage = removeComments(rawImage)
    numColumns = getColumns(cleanedImage)
    numRows = getRows(cleanedImage)

    if (operation == 'hide'):
        message = input("Enter the message you want to hide: ")
        hideMessage(cleanedImage, message, numColumns, numRows)
    if (operation == 'reveal'):
        revealMessage(cleanedImage)
                      






if __name__ == "__main__":
    main()
