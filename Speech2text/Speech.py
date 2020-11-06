import speech_recognition as sr
import os
import subprocess
r = sr.Recognizer()

def reco(inba):
    with sr.AudioFile(inba) as source:

        audio_text = r.listen(source)
    try:
        text = r.recognize_google(audio_text, language = 'el-GR')
        print('Converting audio transcripts into text ...')
        bitch=open('tsitsifikos.txt','a+',encoding="utf-8")
        bitch.write(inba+':\n|'+text+'|\n\n')
        bitch.close()
    except:
        print('Sorry.. run again...')


tmp = open('extensions.txt','r')
f = tmp.readlines() #Imported in a list
tmp.close()
for i in range(len(f)):
	f[i]=f[i].strip('\n')


for dirs in os.listdir():
    for i in f:
        if dirs.endswith(i):
            subprocess.call(['ffmpeg', '-i', dirs,dirs[:-len(i)]+'.wav'])
            reco(dirs[:-len(i)]+'.wav') #EPICO
    if dirs.endswith('.wav'):
        reco(dirs)

        
#for dirs in os.listdir():
#    if dirs.endswith('.mp3') or dirs.endswith('.amr') or dirs.endswith('.aac'):
#        subprocess.call(['ffmpeg', '-i', dirs,dirs[:-4]+'.wav'])
#        reco(dirs[:-4]+'.wav') #beautiful
#    if dirs.endswith('.wav'):
#        reco(dirs)
#dirs.rfind('.')