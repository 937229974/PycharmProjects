import subprocess, os, sys, time

globalStartupInfo = subprocess.STARTUPINFO()
globalStartupInfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW



def runCmd(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.getcwd(), shell=False,
                         startupinfo=globalStartupInfo)
    p.wait()
    re = p.stdout.read().decode()
    return re

def more_demo():
    for i in range(1,11):
        cmd = "python E:/workSpace/paipaidai_2000/paipaiDai_%s000.py" %str(i)
        print(cmd)
        runCmd(cmd)
more_demo()