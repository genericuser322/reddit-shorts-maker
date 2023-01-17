import praw
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, CompositeAudioClip
import pyttsx3
import os
from random import randint
from time import sleep



class _TTS:

    engine = None
    
    rate = None
    def __init__(self):
        self.engine = pyttsx3.init()


    def start(self,text_):
        self.engine.say(text_)
        self.engine.runAndWait()


# Read-only instance
reddit_read_only = praw.Reddit(
    client_id=" ",         # your client id
    client_secret=" ",      # your client secret
    user_agent=" ")        # your user agent

subreddit = reddit_read_only.subreddit("AskReddit")

def fixText(textt):
    text = textt
    counter = 0
    counter2 = 1
    oldcounter = 0
    first = True
    mylist = []
    oldi= 0
    numofchars = 30
    newText = ''
    for i in range(len(text)):
        if i > numofchars+oldi:
            counter+=1
            if text[i] == ' ':       
                oldi = i
                
                
                newText = newText+text[i-(numofchars+counter):i]+'\n'
                oldcounter = counter
                counter = 0
                counter2+=1
                first = False
        if len(text)//numofchars!=0:
            if len(text)==i+1:
                newText += text[oldi:len(text)]+'\n'
                return str(newText)
        else:
            return str(text)

def textFix(text):
    counter = 0
    counter2 = 1
    oldcounter = 0
    first = True
    mylist = []
    oldi= 0
    numofchars = 30
    newText = ''
    charlimit = 100
    for i in range(len(text)):
        if i > numofchars+oldi:
            counter+=1
            if text[i] == ' ':       
                oldi = i
                
                
                newText = newText+text[i-(numofchars+counter):i]+'\n'
                oldcounter = counter
                counter = 0
                counter2+=1
                first = False
        if len(text)//numofchars!=0:
            if len(text)==i+1:
                newText += text[oldi:len(text)]+'\n'
                return str(newText)
        else:
            return str(text)

def textFixComments(text):
    global clipList
    global audioList
    counter = 0
    counter2 = 1
    oldcounter = 0
    first = True
    mylist = []
    oldi= 0
    numofchars = 30
    newText = ''
    charlimit = 300
    oldcharlimit = 0
    for i in range(len(text)):
        if i > numofchars+oldi:
            counter+=1
            if text[i] == ' ':       
                oldi = i
                
                
                newText = newText+text[i-(numofchars+counter):i]+'\n'

                oldcounter = counter
                counter = 0
                counter2+=1
                first = False
        elif len(text)//numofchars!=0:
            if len(text)==i+1:
                newText += text[oldi:len(text)]+'\n'
                return str(newText)

        elif i>charlimit+oldcharlimit:
            counter+=1
            if text[i] == ' ':       
                oldi = i
                
                
                newText = newText+text[i-(numofchars+counter):i]+'\n'

                oldcounter = counter
                counter = 0
                counter2+=1
                first = False

def do(text):
    global clipList
    global audioList
    global audio_length
    global current_comment
    counter = 0
    counter2 = 1
    oldcounter = 0
    first = True
    mylist = []
    oldi= 0
    numofchars = 30
    newText = ''
    charlimit = 30
    oldcharlimit = 0
    totalAudioLenght = 0
    AudioLength = 0
    newAudioList = []
    newTextList = []
    saveCounter = 0
    global randomList
    newText2 = ''
    randomList2 = []

    for i in range(len(text)):
        if i > numofchars+oldi:
            counter+=1
            if text[i] == ' ':       
                oldi = i
                
                
                newText = newText+text[i-(numofchars+counter):i]+'\n'
                newText2 = newText2+text[i-(numofchars+counter):i]
                oldcounter = counter
                counter = 0
                counter2+=1
                first = False
                #print('1')
        elif len(text)//numofchars!=0:
            if len(text)==i+1:
                newText += text[oldi:len(text)]+'\n'
                newText2 = newText2+text[oldi:len(text)]
                

                newTextList.append(newText)
                randomList.append(newText)
                randomList2.append(newText2)
                newText = ''
                newText2 = ''
                #saveCounter += 1
                #print('2')
        nlines = newText.count('\n')
        if nlines > 10:
            newTextList.append(newText)
            randomList.append(newText)
            randomList2.append(newText2)
            newText = ''
            newText2 = ''
    errorCheck = False
    check2 = 0
    success1 = 0
    check3 = 0
    sss = 0
    for i in range(len(randomList2)):
        newstr = randomList2[i].replace('\n', ' ')
        randomList2[i] = newstr
    print(randomList2)

    for i in range(len(randomList2)):
        #print(len(randomList2))
        if not errorCheck:
            print('test001')
            while check3<=10 and success1<i+1 and audio_length<60:
                print('test002')
                #try:
                filename = '/home/user/Desktop/test2/comment'+str(current_comment)+'_'+str(i)+'.mp3'
                filename2 = 'comment'+str(current_comment)+'_'+str(i)+'.mp3'
                tts = _TTS()
                tts.engine.save_to_file(randomList2[i], filename2)
                tts.engine.runAndWait()
                tts.engine.stop()
                del(tts)
                sleep(1)
                print('test5')
                totalAudioLenght2 = audio_length+totalAudioLenght
                commentAudio = AudioFileClip(filename2)
                txt_clip = TextClip(newTextList[i], fontsize = 20, color = 'black', stroke_color='white', stroke_width=1)
                if len(newAudioList) > 0:
                    commentAudio = commentAudio.set_start(totalAudioLenght+audio_length)
                    txt_clip = txt_clip.set_start(totalAudioLenght+audio_length)
                else:
                    commentAudio = commentAudio.set_start(audio_length)
                    txt_clip = txt_clip.set_start(audio_length)

                print('success1!')
                check3+=11

                success1+=1


                #try:

                AudioLength = commentAudio.duration
                previousAudioLength = AudioLength
                totalAudioLenght += AudioLength
                
                txt_clip = txt_clip.set_position('center')
                txt_clip = txt_clip.set_duration(AudioLength)

                print('success2')
                if audio_length <= 60:
                    newAudioList.append(commentAudio)
                    clipList.append(txt_clip)
                    print('XZXZXZXZXZXZXZXZXZXZXZX'+newTextList[i]+'\n'+'XZXZXZXZXZXZXZXZXZXZXZX')




    if not errorCheck and totalAudioLenght+audio_length<=60 :
        audio_length += totalAudioLenght
        for i in newAudioList:
            audioList.append(i)
        for i in mylist:
            clipList.append(i)
#def trySuccesfullyCreateAudiofile(comment, name):
#    check = False
#    while not check:
#        engine.save_to_file(comment, name)
#        
#        try:
#            commentAudio = AudioFileClip(name)
#            check = True
#        except:
#            print('Fail')

def soundTimings():
    global audioList
    newaudioList = []
    for i in range(len(audioList)):
        if i == 0:
            newaudioList.append(audioList[i])
        else:
            elnum = i-1
            coolnum = str(audioList[elnum].duration)
            print(coolnum)
            print(audioList[i].start(coolnum))
            newaudioList.append(audioList[i].start(coolnum))
    return newaudioList


audio_length = 0
current_comment = 0
randomList = []
videoCount = 0
#for post in subreddit.top(time_filter="all"):
for post in subreddit.hot(limit=100):
    
    if post.over_18 or len(post.comments)<5:
        print('NSFW post or too few replies, cant get data.')
    else:
        #try:
            audio_length = 0
            videostr = 'Video'+str(randint(1, 4))+'.mp4'
            clip = VideoFileClip(videostr)
            clipList = []
            audioList = []
            illegalChar = False

            print(post.title)
            title = post.title
            for i in range(len(title)):
                            if title[i] == '/':
                                illegalChar = True
            if not illegalChar:

                tts = _TTS()
                tts.engine.save_to_file(title, 'title.mp3')
                tts.engine.runAndWait()
                tts.engine.stop()
                del(tts)
                sleep(1)
                titleAudio = AudioFileClip('title.mp3')

                audioList.append(titleAudio)
                titleDuration = titleAudio.duration
                fixedTitle = fixText(title)
                txt_clip = TextClip(fixedTitle, fontsize = 20, color = 'black', stroke_color='white', stroke_width=1)
                txt_clip = txt_clip.set_duration(titleDuration)
                txt_clip = txt_clip.set_position('center')

                clipList.append(txt_clip)
                audio_length += titleDuration

                print('/////////////////////////')
                post.comments.replace_more(limit=0)
                while audio_length < 58 and len(post.comments)>current_comment:
                #for top_level_comment in post.comments:

                    top_level_comment = post.comments[current_comment]
                    check = 0
                    for i in top_level_comment.body:
                        if i == '/':
                            check = 1
                    if top_level_comment.author != '' and post.comments.__len__()>=current_comment and check == 0:
                        do(top_level_comment.body)
                        #for i in randomList:
                        #    print(i+'\n'+'0000000000000000000000000000'+'\n')
                    else:
                        print(post.comments.__len__)
                    current_comment += 1
                current_comment = 0
                #audio_length =0
                illegalChar = False

                #putting together all audio files into a single file to put on the video
                if audio_length > 20:
                    if not audio_length>= 58:
                        audio_length += 2
                    if audio_length >= 58:
                        audio_length-=0.1
                    finalAudio = CompositeAudioClip(audioList)
                    #finalAudio.write_audiofile('finalaudio.mp3')
                    #finalAudio = AudioFileClip('finalaudio.mp3')
                    clip = clip.set_audio(finalAudio)
                    clipList.insert(0, clip)
                    print(clipList)
                    video = CompositeVideoClip(clipList)
                    video = video.subclip(0, audio_length)
                    video.write_videofile('vids/finalvid'+str(videoCount)+'.mp4')

                    clipList = []
                    audioList = []
                    clipList.append(txt_clip)
                    videoCount += 1


            print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
        #except:
        #    print('an error occured.')
