#feat. Los.Pros

import speech_recognition as sr
import os
import subprocess
r = sr.Recognizer()

def reco(inputfile):
    with sr.AudioFile(inputfile) as source:

        audio_text = r.listen(source)
    try:
        
        text = r.recognize_google(audio_text, language = 'el-GR')
        print('Converting audio transcripts into text ...')
        tmp=open('TextLog.txt','a+',encoding="utf-8")
        tmp.write(inputfile[:inputfile.rfind('.')]+':\n|'+text+'|\n\n') #file name without extension
        tmp.close()
    except:
        print('Sorry.. run again...')

#Main
tmp = open('extensions.txt','r')
extlist = tmp.readlines() #Imported in a list
tmp.close()
try:
    tmp = open('TextLog.txt','r',encoding="utf-8")
    oldrecs=tmp.readlines()
    tmp.close()
except:
    print("No history")
    open('TextLog.txt', 'a').close()
    oldrecs=''


for i in range(len(extlist)):
	extlist[i]=extlist[i].strip('\n')


for dirs in os.listdir():
    if dirs[:dirs.rfind('.')]+':\n' in oldrecs: #checks if it already has been transcribed
        continue
    for i in extlist:
        if dirs.endswith(i):
            newwav=dirs[:-len(i)]+'.wav'
            subprocess.call(['ffmpeg', '-i', dirs,newwav])
            reco(newwav) #EPICO
            os.remove(newwav)
    if dirs.endswith('.wav'):
        reco(dirs)


#for dirs in os.listdir():
#    if dirs.endswith('.mp3') or dirs.endswith('.amr') or dirs.endswith('.aac'):
#        subprocess.call(['ffmpeg', '-i', dirs,dirs[:-4]+'.wav'])
#        reco(dirs[:-4]+'.wav') #beautiful
#    if dirs.endswith('.wav'):
#        reco(dirs)
#dirs.rfind('.')
# ffmpeg -i '.\00302111001001(00302111001001)_20200901231557.mp3' -f segment -segment_time 30 -c copy output%04d.wav