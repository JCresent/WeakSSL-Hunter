import os
import sys 

outputText = None;

def inputValidation(argc, argv):
    #Output text variable
    global outputText; 

    #Make sure that the correct command was put in by user
    if argc != 5:
        return False
    if argv[1] != "-i" or argv[3] != "-o":
        return False
    
    #Get apk to analyze
    outputText = open(argv[4], "w")
    outputText.close()
    outputText = open(argv[4], "a")
    return argv[2]

def findPermissions():
    pass

def analyzeSmali():
    pass

def main():
    #Check command input is valid and then get APK path str
    inputAPK = inputValidation(len(sys.argv), sys.argv)
    if not inputAPK:
        print("Invalid input, try: python Cresent-analyze.py -i target-app.apk -o output.txt")
        sys.exit(1)

    #Use apktool to decompile APK
    os.system("apktool d " + inputAPK)

if __name__ == "__main__":
    main()