import os
import subprocess
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
    
    #Get apk to analyze, create output file for results to be written
    outputText = open(argv[4], "w")
    outputText.close()
    outputText = open(argv[4], "a")
    return argv[2]


def findInternetPermission(app):
    #Change directory to the decompiled app directory
    try:
        os.chdir(app)
        #print(os.getcwd())
    except:
        print("Error: App directory not found")
        return False
    
    permission = "android.permission.INTERNET"
    manifest = "AndroidManifest.xml"
    grep_command = f"grep -r '{permission}' {manifest}"
    result = subprocess.run(grep_command, shell=True, capture_output=True, text=True)
    os.chdir('..')
    #print(os.getcwd())

    # Print the output
    #print(result.stdout)
    if len(result.stdout) == 0:
        return False
    return True


def getPackagePath(app):

    #Change directory to package directory (app code) using grep to find package
    try:
        os.chdir(app)
        #print(os.getcwd())
    except:
        print("Error: App directory not found")
        return False
    
    permission = "package="
    manifest = "AndroidManifest.xml"
    grep_command = f"grep -r '{permission}' {manifest}"
    result = subprocess.run(grep_command, shell=True, capture_output=True, text=True)
    os.chdir('..')
    resultStr = result.stdout
    start = resultStr.find('package="') + 9
    end = resultStr.find('"', start)
    pkg = app + "/" + "smali/" + resultStr[start:end]
    pkg = pkg.replace(".", "/")
    print(pkg)
    return pkg

def analyzeSmali(package):
    pass



def main():
    #Check command input is valid and then get APK path str
    inputAPK = inputValidation(len(sys.argv), sys.argv)
    if not inputAPK:
        print("Invalid input, try: python Cresent-analyze.py -i target-app.apk -o output.txt")
        sys.exit(1)
    # print("APK path: " + inputAPK)

    #Use apktool to decompile APK
    # os.system("apktool d " + inputAPK)

    #Slice apk path to get path to the decomplied app directory 
    start = inputAPK.find("/") + 1
    end = inputAPK.find(".apk")
    app = inputAPK[start:end]
    # print("App name: " + app)

    #First checking if app has INTERNET permission, if not no need to check for SSL errors
    if findInternetPermission(app) == True:
        #print("App has INTERNET permission")
        path = getPackagePath(app)
        analyzeSmali(path)
    else:
        print("App does not have INTERNET permission, no need to go any further. Exiting...")
        sys.exit(1)

if __name__ == "__main__":
    main()