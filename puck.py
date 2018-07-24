# -*- coding: utf-8 -*-

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit

#client = LINE()
#client = LINE("EvoBbWqUN1lxhN6Bs4t3.m7QAK9mmg/fv3Yt11op1GW.5fLIhx9QFPz1MihDNI/+x7KGz0HqDcswb73TWXrxUmA=")
#client = LINE("EvoPkXQ90eu3UK1vx0a3.Ri4/RX6YPvDWVXddSJv8mW.EShzr3s9pszLIBJo4FTV/LAMyBaCd19LThhjoCXw+qk=")
client = LINE("Ev0FrM6DTZyCZCQSTNG3.m7QAK9mmg/fv3Yt11op1GW.gogCmbiU5FT05GnAbxI8NDONSUHtO3k/1MWirpUObaA=") #DESKTOPWIN
#client = LINE('daffykhadaffy18@gmail.com','Dapuymuhammad123')
clientMid = client.profile.mid
clientProfile = client.getProfile()
clientSettings = client.getSettings()
clientPoll = OEPoll(client)
botStart = time.time()

msg_dict = {}
simisimi = []

admin ="uac8e3eaf1eb2a55770bf10c3b2357c33"

settings = {
    "autoAdd": True,
    "autoJoin": True,
    "autoLeave": False,
    "autoRead": False,
    "lurk": True,
    "autoRespon": False,
    "autoJoinTicket": False,
    "checkContact": True,
    "selfbot":True,
    "checkPost": True,
    "Sambutan": False,
    "checkSticker": False,
    "changeDisplayPicture": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    },
    "setKey": False,
    "unsendMessage": True
}

read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
settings["myProfile"]["displayName"] = clientProfile.displayName
settings["myProfile"]["statusMessage"] = clientProfile.statusMessage
settings["myProfile"]["pictureStatus"] = clientProfile.pictureStatus
coverId = client.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    client.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                client.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def logError(text):
    client.log("[ RINDA ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
            error.write("\n[ {} ] {}".format(str(time), text))
            
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
def helpmessage():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpMessage =   "   「 Helper 」     " + "\n" + \
                    " " "1) " + key + " More help" + "\n" + \
                    " " "2) " + key + " About Rinda" + "\n" + \
                    " " "3) " + key + " Rinda bye" + "\n" + \
                    " " "4) " + key + " Rinda get token" + "\n\n" + \
                    " " "「 Get Reader 」" + "\n" + \
                    " " "1) " + key + " Rinda get reader On/Off - [For SetRead]" + "\n" + \
                    " " "2) " + key + " Rinda get reader reset - [For Reset point]" + "\n" + \
                    " " "3) " + key + " Rinda get readers - [For CheckRead]" + "\n\n" + \
                    "  「Use < " + key + " > For the Prefix」" + "\n" + \
                    "  「*Creator : @!*」"
    return helpMessage

def helpmenu2():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpMenu2 =     " " "「 All Can Used 」" + "\n" + \
                    " " "1) " + key + "  Asking [query]" + "\n" + \
                    " " "2) " + key + "  Hasil Dari [query]/[contoh : Hasil dari 22x22]" + "\n" + \
                    " " "3) " + key + "  Timezone [query]" + "\n" + \
                    " " "4) " + key + "  Smule [query]" + "\n" + \
                    " " "5) " + key + "  Twitter [query]" + "\n" + \
                    " " "6) " + key + "  Memelist" + "\n" + \
                    " " "7) " + key + "  Randomlose" + "\n" + \
                    " " "8) " + key + "  Playstore [query]" + "\n" + \
                    " " "9) " + key + "  Rinda Get Motivation" + "\n" + \
                    " " "10) " + key + " Rinda get Suggestion to [query]" + "\n" + \
                    " " "11) " + key + " Rinda Groupinfo [number of groups]" + "\n" + \
                    " " "12) " + key + " Rinda Grouplist" + "\n" + \
                    " " "13) " + key + " Rinda get Memberlist to [number of groups]" + "\n" + \
                    " " "14) " + key + " Rinda Mention to [number of groups]" + "\n" + \
                    " " "15) " + key + " Rinda get devianart [query]" + "\n" + \
                    " " "16) " + key + " Rinda get Image [query]" + "\n" + \
                    " " "17) " + key + " Rinda get Quotes" + "\n" + \
                    " " "18) " + key + " Rinda get 1Cak" + "\n" + \
                    " " "19) " + key + " Rinda get video [query]" + "\n" + \
                    " " "20) " + key + " Rinda get Wikipedia [query]" + "\n" + \
                    " " "21) " + key + " Rinda getmeme dwight*Hei*Rin" + "\n" + \
                    " " "22) " + key + " Rinda get lockscreen [query]" + "\n" + \
                    " " "23) " + key + " Rinda get creepypasta" + "\n" + \
                    " " "24) " + key + " Rinda get gif [query]" + "\n\n" + \
                    "  「Use < " + key + " > For the Prefix」" + "\n" + \
                    "  「*Creator : @!*」"
    return helpMenu2

def helpmedia():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpMedia = "╔══[ Media Helper ]" + "\n" + \
                    "╠ " + key + "CheckDate [Date]" + "\n" + \
                    "╠ " + key + "CheckWebsite [url]" + "\n" + \
                    "╠ " + key + "CheckPraytime [Location]" + "\n" + \
                    "╠ " + key + "CheckWeather [Location]" + "\n" + \
                    "╠ " + key + "CheckLocation [Location]" + "\n" + \
                    "╠ " + key + "InstaStory [UserName]*[Number]" + "\n" + \
                    "╠ " + key + "InstaInfo [UserName]" + "\n" + \
                    "╠ " + key + "InstaPost [UserName]*[Number]" + "\n" + \
                    "╠ " + key + "SearchYoutube[query]" + "\n" + \
                    "╠ " + key + "SearchMusic [query]" + "\n" + \
                    "╠ " + key + "SearchLyric [query]" + "\n" + \
                    "╠ " + key + "SearchImage [query]" + "\n" + \
                    "╠ 「*Creator : @!*」" + "\n" + \
                    "╚══[*] 「Use < " + key + " > For the Prefix」"
    return helpMedia

def helpsett():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpSett = "╔══[ Settings Helper ]" + "\n" + \
                    "╠ " + key + "AutoAdd「On/Off」" + "\n" + \
                    "╠ " + key + "AutoJoin「On/Off」" + "\n" + \
                    "╠ " + key + "AutoJoinTicket「On/Off」" + "\n" + \
                    "╠ " + key + "AutoLeave「On/Off」" + "\n" + \
                    "╠ " + key + "AutoRead「On/Off」" + "\n" + \
                    "╠ " + key + "AutoRespon「On/Off」" + "\n" + \
                    "╠ " + key + "CheckContact「On/Off」" + "\n" + \
                    "╠ " + key + "CheckPost「On/Off」" + "\n" + \
                    "╠ " + key + "CheckSticker「On/Off」" + "\n" + \
                    "╠ " + key + "UnsendChat「On/Off」" + "\n" + \
                    "╠ 「*Creator : @!*」" + "\n" + \
                    "╚══[*] 「Use < " + key + " > For the Prefix」"
    return helpSett
    
def helpgroup():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpGroup = "╔══[ Group Helper ]" + "\n" + \
                    "╠ " + key + "GroupCreator" + "\n" + \
                    "╠ " + key + "GroupId" + "\n" + \
                    "╠ " + key + "GroupName" + "\n" + \
                    "╠ " + key + "GroupPicture" + "\n" + \
                    "╠ " + key + "GroupTicket" + "\n" + \
                    "╠ " + key + "GroupMemberList" + "\n" + \
                    "╠ " + key + "GroupList" + "\n" + \
                    "╠ " + key + "GroupInfo" + "\n" + \
                    "╠ " + key + "ChangeGroupPicture" + "\n" + \
                    "╠ 「*Creator : @!*」" + "\n" + \
                    "╚══[*] 「Use < " + key + " > For the Prefix」"
    return helpGroup
    
def helpself():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpSelf = "╔══[ Self Helper ]" + "\n" + \
                    "╠ " + key + "Me" + "\n" + \
                    "╠ " + key + "MyMid" + "\n" + \
                    "╠ " + key + "MyName" + "\n" + \
                    "╠ " + key + "MyBio" + "\n" + \
                    "╠ " + key + "ChangeBio:「Query」" + "\n" + \
                    "╠ " + key + "ChangeName:「Query」" + "\n" + \
                    "╠ " + key + "MyPicture" + "\n" + \
                    "╠ " + key + "MyVideoProfile" + "\n" + \
                    "╠ " + key + "MyCover" + "\n" + \
                    "╠ " + key + "StealContact「Mention」" + "\n" + \
                    "╠ " + key + "StealMid「Mention」" + "\n" + \
                    "╠ " + key + "StealName「Mention」" + "\n" + \
                    "╠ " + key + "StealBio「Mention」" + "\n" + \
                    "╠ " + key + "StealPicture「Mention」" + "\n" + \
                    "╠ " + key + "StealVideoProfile「Mention」" + "\n" + \
                    "╠ " + key + "StealCover「Mention」" + "\n" + \
                    "╠ " + key + "CloneProfile「Mention」" + "\n" + \
                    "╠ " + key + "RestoreProfile" + "\n" + \
                    "╠ " + key + "BackupProfile" + "\n" + \
                    "╠ " + key + "ChangePictureProfile" + "\n" + \
                    "╠ 「*Creator : @!*」" + "\n" + \
                    "╚══[*] 「Use < " + key + " > For the Prefix」"    
    return helpSelf

def clientBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return

        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                client.findAndAddContactsByMid(op.param1)
            sendMention(op.param1, "@! Thx for add")

        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            if clientMid in op.param3:
                if settings["autoJoin"] == True:
                    client.acceptGroupInvitation(op.param1)
                sendMention(op.param1, "@! Thx for invite")

        if op.type in [22, 24]:
            print ("[ 22 And 24 ] NOTIFIED INVITE INTO ROOM & NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                sendMention(op.param1, "@! hmm?")
                client.leaveRoom(op.param1)

        if op.type == 26:
           if settings["selfbot"] == True:
               msg = op.message
               if msg.to in simisimi:
                   try:
                       if msg.text is not None:
                           simi = msg.text
                           r = requests.get("http://leert.corrykalam.gq/chatbot.php?text="+simi)
                           data = r.text
                           data = json.loads(data)
                           if data["status"] == 200:
                               aditmadzs.sendMessage(msg.to, str(data["answer"]))
                   except Exception as error:
                       pass

        if op.type == 26:
            try:
                print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
                            if cmd == "help":
                              if settings["selfbot"] == True:
                                helpMessage = helpmessage()
                                client.sendMessage(to, str(helpMessage))
                            if cmd == "help sett":
                              if settings["selfbot"] == True:
                                helpSett = helpsett()
                                poey = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                creator = client.getContact(poey)
                                #client.sendMessage(to, str(helpSett))
                                sendMention(to, str(helpSett), [poey])
                            if cmd == "more help":
                              if settings["selfbot"] == True:
                                helpMenu2 = helpmenu2()
                                poey = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                creator = client.getContact(poey)
                                #client.sendMessage(to, str(helpSett))
                                sendMention(to, str(helpMenu2), [poey])
                            if cmd == "help group":
                              if settings["selfbot"] == True:
                                helpGroup = helpgroup()
                                poey = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                creator = client.getContact(poey)
                                #client.sendMessage(to, str(helpGroup))
                                sendMention(to, str(helpGroup), [poey])
                            if cmd == "help self":
                              if settings["selfbot"] == True:
                                helpSelf = helpself()
                                poey = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                creator = client.getContact(poey)
                                #client.sendMessage(to, str(helpSelf))
                                sendMention(to, str(helpSelf), [poey])
                            if cmd == "rinda pause":
                              if settings["selfbot"] == True:
                                if msg._from in admin:
                                  settings["selfbot"] = False
                                  poey = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                  creator = client.getContact(poey)
                                  #puy.sendMessage(msg.to, "Rinda diberhentikan sementara oleh")
                                  sendMention(to, "Rinda diberhentikan sementara oleh @!", [poey])
                            if cmd == "rinda comeon":
                              if settings["selfbot"] == True:
                                if msg._from in admin:
                                  poey = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                  creator = client.getContact(poey)                                    
                                  #puy.sendMessage(msg.to, "Rinda aktif kembali")
                                  sendMention(to, "Rinda diaktifkan kembali oleh @!", [poey])
                            elif cmd.startswith("changekey:"):
                              if msg._from in admin:
                                sep = text.split(" ")
                                key = text.replace(sep[0] + " ","")
                                if " " in key:
                                    client.sendMessage(to, "Key tidak bisa menggunakan spasi")
                                else:
                                    settings["keyCommand"] = str(key).lower()
                                    client.sendMessage(to, "Berhasil mengubah key command menjadi [ {} ]".format(str(key).lower()))
                            elif cmd == "sp1":
                              if settings["selfbot"] == True:
                                start = time.time()
                                client.sendMessage(to, "Counting...")
                                speed = time.time() - start
                                ping = speed * 1000
                                client.sendMessage(to, "The result is {} ms".format(str(speed(ping))))
                            elif cmd == "sp2":
                                if msg._from in admin:
                                  if settings["selfbot"] == True:
                                    start = time.time()
                                    client.sendMessage(to, "...")
                                    elapsed_time = time.time() - start
                                    client.sendMessage(to, "{}".format(str(elapsed_time)))
                            elif cmd.startswith("sp3"):
                                if settings["selfbot"] == True:
                                  Ownerz = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                  get_profile_time_start = time.time()
                                  get_profile = client.getProfile()
                                  get_profile_time = time.time() - get_profile_time_start
                                  get_group_time_start = time.time()
                                  get_group = client.getGroupIdsJoined()
                                  get_group_time = time.time() - get_group_time_start
                                  get_contact_time_start = time.time()
                                  get_contact = client.getContact(Ownerz)
                                  get_contact_time = time.time() - get_contact_time_start
                                  client.sendMessage(msg.to, "About Group speed is <%.10f>\nAbout Info Profile speed is <%.10f>\nAbout Contact speed is <%.10f>" % (get_profile_time/3,get_contact_time/3,get_group_time/3))
                            elif cmd == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                client.sendMessage(to, "Rinda already actived of {}".format(str(runtime)))
                            elif cmd == "restart":
                                client.sendMessage(to, "Berhasil merestart Bot bos")
                                restartBot()
# Pembatas Script #

                            elif cmd == "rinda statuss":
                              if wait["selfbot"] == True:
                                if msg._from in admin:
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    md = " < S T A T U S >\n\n"
                                    if wait["unsend"] == True: md+=" [*Unsend Actived*]\n"
                                    else: md+=" [*Unsend Unactived*]\n"
                                    if wait["sticker"] == True: md+=" [*StickerInfo Actived*]\n"
                                    else: md+=" [*StickerInfo Unactived*]\n"
                                    if wait["contact"] == True: md+=" [*GetInfo Actived*]\n"
                                    else: md+=" [*GetInfo Unactived*]\n"
                                    if wait["Mentionkick"] == True: md+=" [*Mentionkick Actived*]\n"
                                    else: md+=" [*Mentionkick Unactived*]\n"
                                    if wait["detectMention"] == True: md+=" [*Autoreplytag Actived*]\n"
                                    else: md+=" [*Autoreplytag Unactived*]\n"
                                    if wait["Mentiongift"] == True: md+=" [*Mentiongift Actived*]\n"
                                    else: md+=" [*Mentiongift Unactived*]\n"
                                    if wait["autoJoin"] == True: md+=" [*AutoJoin Actived*]\n"
                                    else: md+=" [*AutoJoin Unactived*]\n"
                                    if settings["autoJoinTicket"] == True: md+=" [*JoinQR Actived*]\n"
                                    else: md+=" [*JoinQR Unactived*]\n"
                                    if msg.to in simisimi: md+=" [*Simisimi Actived*]\n"
                                    else: md+=" [*Simisimi Unactived*]\n"
                                    if wait["autoAdd"] == True: md+=" [*AutoaddMsg Actived*]\n"
                                    else: md+=" [*AutoaddMsg Unactived*]\n"
                                    if msg.to in welcome: md+=" [*WelcomeMsg Actived*]\n"
                                    else: md+=" [*WelcomeMsg Unactived*]\n"
                                    if wait["autoLeave"] == True: md+=" [*LeaveMsg Actived*]\n"
                                    else: md+=" [*LeaveMsg Unactived*]\n"
                                    client.sendMessage(msg.to, md+"\nPada : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n<"+ datetime.strftime(timeNow,'%H:%M:%S')+">\n")
                                
                            elif cmd == "autoadd on":
                                settings["autoAdd"] = True
                                client.sendMessage(to, "Auto add is Actived!")
                            elif cmd == "welcome on":
                                settings["Sambutan"] == True
                                client.sendMessage(to,"Sudah On")
                            elif cmd == "welcome off":
                                settings["Sambutan"] == False
                                client.sendMessage(to,"Sudah Off")
                            elif cmd == "autoadd off":
                                settings["autoAdd"] = False
                                client.sendMessage(to, "Auto add is Nonactived!")
                            elif cmd == "autojoin on":
                                settings["autoJoin"] = True
                                client.sendMessage(to, "Auto join is Actived!")
                            elif cmd == "autojoin off":
                                settings["autoJoin"] = False
                                client.sendMessage(to, "Auto join is Nonactived!")   
                            elif cmd == "changedp on":
                                settings["changeDisplayPicture"] = True
                                client.sendMessage(to, "Change Display Picture is Actived!") 
                            elif cmd == "changedp off":
                                settings["changeDisplayPicture"] = False
                                client.sendMessage(to, "Change Display Picture is Nonactived!")                                
                            elif cmd == "lurkingset on":
                                settings["lurk"] = True
                                client.sendMessage(to, "Lurking is Actived!")     
                            elif cmd == "lurkingset off":
                                settings["lurk"] = False
                                client.sendMessage(to, "Lurking is Nonactived!")                                
                            elif cmd == "autoleave on":
                                settings["autoLeave"] = True
                                client.sendMessage(to, "Auto leave is Actived!")
                            elif cmd == "autoleave off":
                                settings["autoLeave"] = False
                                client.sendMessage(to, "Auto leave is Nonactived!")
                            elif cmd == "autorespon on":
                                settings["autoRespon"] = True
                                client.sendMessage(to, "Auto respon is Actived")
                            elif cmd == "autorespon off":
                                settings["autoRespon"] = False
                                client.sendMessage(to, "Auto respon is Nonactived")
                            elif cmd == "autoread on":
                                settings["autoRead"] = True
                                client.sendMessage(to, "Auto read is Actived")
                            elif cmd == "autoread off":
                                settings["autoRead"] = False
                                client.sendMessage(to, "Auto read is Nonactived")
                            elif cmd == "autojointicket on":
                                settings["autoJoinTicket"] = True
                                client.sendMessage(to, "Auto join by Ticket is Actived")
                            elif cmd == "autoJoinTicket off":
                                settings["autoJoin"] = False
                                client.sendMessage(to, "Auto join by Ticket is Nonactived")
                            elif cmd == "checkcontact on":
                                settings["checkContact"] = True
                                client.sendMessage(to, "Check details contact is Actived")
                            elif cmd == "checkcontact off":
                                settings["checkContact"] = False
                                client.sendMessage(to, "Check details contact is Nonactived")
                            elif cmd == "checkpost on":
                                settings["checkPost"] = True
                                client.sendMessage(to, "Check details post is Actived")
                            elif cmd == "checkpost off":
                                settings["checkPost"] = False
                                client.sendMessage(to, "Check details post is Nonactived")
                            elif cmd == "checksticker on":
                                settings["checkSticker"] = True
                                client.sendMessage(to, "Check details sticker is Actived")
                            elif cmd == "checksticker off":
                                settings["checkSticker"] = False
                                client.sendMessage(to, "Check details sticker is Nonactived")
                            elif cmd == "unsendchat on":
                                settings["unsendMessage"] = True
                                client.sendMessage(to, "Unsend Message Detect is Actived")
                            elif cmd == "unsendchat off":
                                settings["unsendMessage"] = False
                                client.sendMessage(to, "Unsend Message Detect is Nonactived")
                            elif cmd == "status":
                                try:
                                    ret_ = "*Status*"
                                    if settings["autoAdd"] == True: ret_ += "\n*[ ON ] Auto Add"
                                    else: ret_ += "\n*[ OFF ] Auto Add"
                                    if settings["autoJoin"] == True: ret_ += "\n*[ ON ] Auto Join"
                                    else: ret_ += "\n*[ OFF ] Auto Join"
                                    if settings["autoLeave"] == True: ret_ += "\n*[ ON ] Auto Leave Room"
                                    else: ret_ += "\n*[ OFF ] Auto Leave Room"
                                    if settings["autoJoinTicket"] == True: ret_ += "\n*[ ON ] Auto Join Ticket"
                                    else: ret_ += "\n*[ OFF ] Auto Join Ticket"
                                    if settings["autoRead"] == True: ret_ += "\n*[ ON ] Auto Read"
                                    else: ret_ += "\n*[ OFF ] Auto Read"
                                    if settings["autoRespon"] == True: ret_ += "\n*[ ON ] Detect Mention"
                                    else: ret_ += "\n*[ OFF ] Detect Mention"
                                    if settings["checkContact"] == True: ret_ += "\n*[ ON ] Check Contact"
                                    else: ret_ += "\n*[ OFF ] Check Contact"
                                    if settings["checkPost"] == True: ret_ += "\n*[ ON ] Check Post"
                                    else: ret_ += "\n*[ OFF ] Check Post"
                                    if settings["checkSticker"] == True: ret_ += "\n*[ ON ] Check Sticker"
                                    else: ret_ += "\n*[ OFF ] Check Sticker"
                                    if settings["lurk"] == True: ret_ += "\n*[ ON ] Lurkset"
                                    else: ret_ += "\n*[ OFF ] Lurkset"                                    
                                    if settings["setKey"] == True: ret_ += "\n*[ ON ] Set Key"
                                    else: ret_ += "\n*[ OFF ] Set Key"
                                    if settings["unsendMessage"] == True: ret_ += "\n*[ ON ] Unsend Message"
                                    else: ret_ += "\n*[ OFF ] Unsend Message"
                                    ret_ += ""
                                    client.sendMessage(to, str(ret_))
                                except Exception as e:
                                    client.sendMessage(msg.to, str(e))
# Pembatas Script #
                            elif cmd == "crashing":
                                client.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                            elif cmd.startswith("changename:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = client.getProfile()
                                    profile.displayName = string
                                    client.updateProfile(profile)
                                    client.sendMessage(to,"Successfully changed display name to{}".format(str(string)))
                            elif cmd.startswith("changebio:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = client.getProfile()
                                    profile.statusMessage = string
                                    client.updateProfile(profile)
                                    client.sendMessage(to,"Successfully changed status message to{}".format(str(string)))
                            #elif cmd == "me":
                                #sendMention(to, "@!", [sender])
                                #client.sendContact(to, sender)
                            elif cmd == "sticker":
                                try:
                                    query = msg.text.replace("sticker", "")
                                    query = int(query)
                                    if type(query) == int:
                                        client.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        client.sendText(receiver, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        client.sendText(receiver, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    client.sendText(receiver, str(e))     
                            elif cmd == "unsendme":
                                client.unsendMessage(msg_id)                                    
                            elif cmd == "mymid":
                                client.sendMessage(to, "[ MID ]\n{}".format(sender))
                            elif cmd == "myname":
                                contact = client.getContact(sender)
                                client.sendMessage(to, "[ Display Name ]\n{}".format(contact.displayName))
                            elif cmd == "mybio":
                                contact = client.getContact(sender)
                                client.sendMessage(to, "[ Status Message ]\n{}".format(contact.statusMessage))
                            elif cmd == "mypicture":
                                contact = client.getContact(sender)
                                client.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "myvideoprofile":
                                contact = client.getContact(sender)
                                client.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                            elif cmd == "mycover":
                                channel = client.getProfileCoverURL(sender)          
                                path = str(channel)
                                client.sendImageWithURL(to, path)
                            elif cmd.startswith("cloneprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.cloneContactProfile(ls)
                                        client.sendMessage(to, "Successfully clone profile {}".format(contact.displayName))
                            elif cmd == "restoreprofile":
                                try:
                                    clientProfile = client.getProfile()
                                    clientProfile.displayName = str(settings["myProfile"]["displayName"])
                                    clientProfile.statusMessage = str(settings["myProfile"]["statusMessage"])
                                    clientProfile.pictureStatus = str(settings["myProfile"]["pictureStatus"])
                                    client.updateProfileAttribute(8, clientProfile.pictureStatus)
                                    client.updateProfile(clientProfile)
                                    coverId = str(settings["myProfile"]["coverId"])
                                    client.updateProfileCoverById(coverId)
                                    client.sendMessage(to, "Successfully restore profile wait a while until profile change")
                                except Exception as e:
                                    client.sendMessage(to, "Failed restore profile")
                                    logError(error)
                            elif cmd == "backupprofile":
                                try:
                                    profile = client.getProfile()
                                    settings["myProfile"]["displayName"] = str(profile.displayName)
                                    settings["myProfile"]["statusMessage"] = str(profile.statusMessage)
                                    settings["myProfile"]["pictureStatus"] = str(profile.pictureStatus)
                                    coverId = client.getProfileDetail()["result"]["objectId"]
                                    settings["myProfile"]["coverId"] = str(coverId)
                                    client.sendMessage(to, "Successfully backup profile")
                                except Exception as e:
                                    client.sendMessage(to, "Failed backup profile")
                                    logError(error)
                            elif cmd.startswith("stealmid "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    ret_ = "[ Mid User ]"
                                    for ls in lists:
                                        ret_ += "\n{}".format(str(ls))
                                    client.sendMessage(to, str(ret_))
                            elif cmd.startswith("stealname "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendMessage(to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                            elif cmd.startswith("stealbio "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendMessage(to, "[ Status Message ]\n{}".format(str(contact.statusMessage)))
                            elif cmd.startswith("stealpicture"):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                        client.sendImageWithURL(to, str(path))
                            elif cmd.startswith("stealvideoprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                        client.sendVideoWithURL(to, str(path))
                            elif cmd.startswith("stealcover "):
                                if client != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            channel = client.getProfileCoverURL(ls)
                                            path = str(channel)
                                            client.sendImageWithURL(to, str(path))
# Pembatas Script #
                            elif cmd == 'groupcreator':
                                group = client.getGroup(to)
                                GS = group.creator.mid
                                client.sendContact(to, GS)
                            elif cmd == 'groupid':
                                gid = client.getGroup(to)
                                client.sendMessage(to, "[ID Group : ]\n" + gid.id)
                            elif cmd == 'grouppicture':
                                group = client.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                client.sendImageWithURL(to, path)
                            elif cmd == 'groupname':
                                gid = client.getGroup(to)
                                client.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                            elif cmd == 'groupticket':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        ticket = client.reissueGroupTicket(to)
                                        client.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                                    else:
                                        client.sendMessage(to, "The qr group is not open please open it first with the command {}openqr".format(str(settings["keyCommand"])))
                            elif cmd == 'groupticket on':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        client.sendMessage(to, "The qr group is already open")
                                    else:
                                        group.preventedJoinByTicket = False
                                        client.updateGroup(group)
                                        client.sendMessage(to, "Berhasil membuka grup qr")
                            elif cmd == 'groupticket off':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == True:
                                        client.sendMessage(to, "The qr group is already closed")
                                    else:
                                        group.preventedJoinByTicket = True
                                        client.updateGroup(group)
                                        client.sendMessage(to, "Berhasil menutup grup qr")
                            elif cmd == 'groupinfo':
                                group = client.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Not Found"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Closed"
                                    gTicket = "There is no"
                                else:
                                    gQr = "Opened"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "* Group Info Started *"
                                ret_ += "\n*Group name : {}".format(str(group.name))
                                ret_ += "\n*ID Group : {}".format(group.id)
                                ret_ += "\n*Group maker : {}".format(str(gCreator))
                                ret_ += "\n*Number of Members : {}".format(str(len(group.members)))
                                ret_ += "\n*Number of Pending Members : {}".format(gPending)
                                ret_ += "\n*Group Qr : {}".format(gQr)
                                ret_ += "\n*Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                client.sendMessage(to, str(ret_))
                                client.sendImageWithURL(to, path)
                            elif cmd == 'groupmemberlist':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    ret_ = "╔══[ Member List ]"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                                    client.sendMessage(to, str(ret_))
                            elif cmd == 'grouplist':
                                    groups = client.groups
                                    ret_ = "╔══[ Group List ]"
                                    no = 0 + 1
                                    for gid in groups:
                                        group = client.getGroup(gid)
                                        ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                        no += 1
                                    ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                                    client.sendMessage(to, str(ret_))
# Pembatas Script #
                            elif cmd == "changedp":
                                settings["changeDisplayPicture"] = True
                                client.sendMessage(to, "*Change Display Picture*\n\nHow to change dp?\n: Just type *changedp* And you will be prompted to Send 1 Picture")
                            elif cmd == "changegp":
                                if msg.toType == 2:
                                    if to not in settings["changeGroupPicture"]:
                                        settings["changeGroupPicture"].append(to)
                                    client.sendMessage(to, "*Change Group Picture*\n\nHow to changegp?\n: Just type *changegp* And you will be prompted to Send 1 Picture")
                            elif cmd == 'mention':
                                group = client.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//100
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*100 : (a+1)*100]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Zero \n'
                                    client.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    client.sendMessage(to, "Total {} Mention".format(str(len(nama))))  
        
                            elif cmd == "lurking reset":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read["readPoint"]:
                                    try:
                                        del read["readPoint"][msg.to]
                                        del read["readMember"][msg.to]
                                        del read["readTime"][msg.to]
                                        del read["ROM"][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    client.sendMessage(msg.to, "Reset reading point : \n" + readTime)
                                else:
                                    client.sendMessage(msg.to, "Lurking is nonactive\n\nType *lurking on* for actived a lurkmode!")
                                    
                            elif text.lower() == 'spamcall':
                                if msg.toType == 2:
                                    sep = text.split(" ")
                                    strnum = text.replace(sep[0] + " ","")
                                    num = int(strnum)
                                    client.sendMessage(to, "Berhasil mengundang kedalam telponan group")
                                    for var in range(0,num):
                                        group = client.getGroup(to)
                                        members = [mem.mid for mem in group.members]
                                        client.acquireGroupCallRoute(to)
                                        client.inviteIntoGroupCall(to, contactIds=members)                                    
                                    
                            elif msg.text.lower().startswith("Gbc "):   
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                groups = client.groups
                                for group in groups:
                                    client.sendMessage(group, "[ Broadcast ]\n{}".format(str(txt)))
                                    client.sendMessage(to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                                    
                            elif cmd == "lurking":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        client.sendMessage(receiver,"Tidak Ada Sider")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = client.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '[R E A D E R ]\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\n" + readTime
                                    try:
                                        client.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                        #logError(error)
                                    pass
                                else:
                                    client.sendMessage(receiver,"Lurking is nonactive\n\nType *lurking on* for actived a lurkmode!")
# Pembatas Script #   
                            elif cmd.startswith("checkwebsite"):
                                try:
                                    sep = text.split(" ")
                                    query = text.replace(sep[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                    data = r.text
                                    data = json.loads(data)
                                    client.sendImageWithURL(to, data["result"])
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkdate"):
                                try:
                                    sep = msg.text.split(" ")
                                    tanggal = msg.text.replace(sep[0] + " ","")
                                    r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                    data=r.text
                                    data=json.loads(data)
                                    ret_ = "[ D A T E ]"
                                    ret_ += "\nDate Of Birth : {}".format(str(data["data"]["lahir"]))
                                    ret_ += "\nAge : {}".format(str(data["data"]["usia"]))
                                    ret_ += "\nBirthday : {}".format(str(data["data"]["ultah"]))
                                    ret_ += "\nZodiak : {}".format(str(data["data"]["zodiak"]))
                                    client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkpraytime "):
                                separate = msg.text.split(" ")
                                location = msg.text.replace(separate[0] + " ","")
                                r = requests.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(location))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isya : ":
                                    ret_ = "* Jadwal Sholat Sekitar *" + data[0] + " ]"
                                    ret_ += "\n* Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n* Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\n* " + data[1]
                                    ret_ += "\n* " + data[2]
                                    ret_ += "\n* " + data[3]
                                    ret_ += "\n* " + data[4]
                                    ret_ += "\n* " + data[5]
                                    ret_ += ""
                                    client.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("checkweather "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    tz = pytz.timezone("Asia/Makassar")
                                    timeNow = datetime.now(tz=tz)
                                    if "result" not in data:
                                        ret_ = "* Weather Status *"
                                        ret_ += "\n* Location : " + data[0].replace("Temperatur di kota ","")
                                        ret_ += "\n* Suhu : " + data[1].replace("Suhu : ","") + "°C"
                                        ret_ += "\n* Kelembaban : " + data[2].replace("Kelembaban : ","") + "%"
                                        ret_ += "\n* Tekanan udara : " + data[3].replace("Tekanan udara : ","") + "HPa"
                                        ret_ += "\n* Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + "m/s"
                                        ret_ += "\n* Time Status *"
                                        ret_ += "\n* Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                        ret_ += "\n* Jam : " + datetime.strftime(timeNow,'%H:%M:%S') + " WIB"
                                        ret_ += ""
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checklocation "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "* Location Status *"
                                        ret_ += "\n* Location : " + data[0]
                                        ret_ += "\n* Google Maps : " + link
                                        ret_ += ""
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instainfo"):
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://www.instagram.com/{}/?__a=1".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "* Profile Instagram *"
                                        ret_ += "\n* Nama : {}".format(str(data["graphql"]["user"]["full_name"]))
                                        ret_ += "\n* Username : {}".format(str(data["graphql"]["user"]["username"]))
                                        ret_ += "\n* Bio : {}".format(str(data["graphql"]["user"]["biography"]))
                                        ret_ += "\n* Followers : {}".format(str(data["graphql"]["user"]["edge_followed_by"]["count"]))
                                        ret_ += "\n* Following : {}".format(str(data["graphql"]["user"]["edge_follow"]["count"]))
                                        if data["graphql"]["user"]["is_verified"] == True:
                                            ret_ += "\n* Verified : Sudah"
                                        else:
                                            ret_ += "\n* Verified : Belum"
                                        if data["graphql"]["user"]["is_private"] == True:
                                            ret_ += "\n* Private Account : Iya"
                                        else:
                                            ret_ += "\n* Private Account : Tidak"
                                        ret_ += "\n* Total Post : {}".format(str(data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]))
                                        ret_ += "\n* [ https://www.instagram.com/{} ]".format(search)
                                        path = data["graphql"]["user"]["profile_pic_url_hd"]
                                        client.sendImageWithURL(to, str(path))
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instapost"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")   
                                    cond = text.split("|")
                                    username = cond[0]
                                    no = cond[1] 
                                    r = requests.get("http://rahandiapi.herokuapp.com/instapost/{}/{}?key=betakey".format(str(username), str(no)))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["find"] == True:
                                        if data["media"]["mediatype"] == 1:
                                            client.sendImageWithURL(msg.to, str(data["media"]["url"]))
                                        if data["media"]["mediatype"] == 2:
                                            client.sendVideoWithURL(msg.to, str(data["media"]["url"]))
                                        ret_ = "* Info Post *"
                                        ret_ += "\n* Number of Like : {}".format(str(data["media"]["like_count"]))
                                        ret_ += "\n* Number of Comment : {}".format(str(data["media"]["comment_count"]))
                                        ret_ += "\n* [ Caption ]\n{}".format(str(data["media"]["caption"]))
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instastory"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")
                                    cond = text.split("|")
                                    search = str(cond[0])
                                    if len(cond) == 2:
                                        r = requests.get("http://rahandiapi.herokuapp.com/instastory/{}?key=betakey".format(search))
                                        data = r.text
                                        data = json.loads(data)
                                        if data["url"] != []:
                                            num = int(cond[1])
                                            if num <= len(data["url"]):
                                                search = data["url"][num - 1]
                                                if search["tipe"] == 1:
                                                    client.sendImageWithURL(to, str(search["link"]))
                                                if search["tipe"] == 2:
                                                    client.sendVideoWithURL(to, str(search["link"]))
                                except Exception as error:
                                    logError(error)
                                    
                            elif cmd.startswith("say-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("say-" + lang + " ","")
                                if lang not in list_language["list_textToSpeech"]:
                                    return client.sendMessage(to, "Language not found")
                                tts = gTTS(text=say, lang=lang)
                                tts.save("hasil.mp3")
                                client.sendAudio(to,"hasil.mp3")
                                
                            elif cmd.startswith("searchimage"):
                                try:
                                    separate = msg.text.split(" ")
                                    search = msg.text.replace(separate[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["result"] != []:
                                        items = data["result"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        client.sendImageWithURL(to, str(path))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("searchmusic "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "* Result Music *"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n* {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n* [ Total {} Music ]".format(str(len(data["result"])))
                                    ret_ += "\n\nUntuk Melihat Details Music, silahkan gunakan command {}SearchMusic {}|「number」".format(str(setKey), str(search))
                                    client.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "* Music *"
                                            ret_ += "\n* Title : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n* Album : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n* Size : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n* Link : {}".format(str(data["result"]["mp3"][0]))
                                            ret_ += "\n* Finish *"
                                            client.sendImageWithURL(to, str(data["result"]["img"]))
                                            client.sendMessage(to, str(ret_))
                                            client.sendAudioWithURL(to, str(data["result"]["mp3"][0]))
                            elif cmd.startswith("searchlyric"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ Result Lyric ]"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n╠ {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n╚══[ Total {} Music ]".format(str(len(data["results"])))
                                    ret_ += "\n\nUntuk Melihat Details Lyric, silahkan gunakan command {}SearchLyric {}|「number」".format(str(setKey), str(search))
                                    client.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                        client.sendMessage(msg.to, str(lyric))
                            elif cmd.startswith("searchyoutube"):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                params = {"search_query": search}
                                r = requests.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "* Youtube Result *"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n* [ {} ]".format(str(data["title"]))
                                    ret_ += "\n* https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n* [ Total {} ]".format(len(datas))
                                client.sendMessage(to, str(ret_))
                            elif cmd.startswith("tr-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("tr-" + lang + " ","")
                                if lang not in list_language["list_translate"]:
                                    return client.sendMessage(to, "Language not found")
                                translator = Translator()
                                hasil = translator.translate(say, dest=lang)
                                A = hasil.text
                                client.sendMessage(to, str(A))
# SC #
                            elif cmd.startswith("about rinda"):
                                try:
                                    arr = []
                                    Ownerz = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                    creator = client.getContact(Ownerz)
                                    contact = client.getContact(puyMid)
                                    grouplist = client.getGroupIdsJoined()
                                    contactlist = client.getAllContactIds()
                                    blockedlist = client.getBlockedContactIds()
                                    ret_ = " "
                                    ret_ += " Bot Name : {}".format(contact.displayName)
                                    ret_ += "\n  In Groups : {}".format(str(len(grouplist)))
                                    ret_ += "\n  Friends : {}".format(str(len(contactlist)))
                                    ret_ += "\n  Blocked Account : {}".format(str(len(blockedlist)))                                    
                                    #ret_ += "\n  [ About Selfbot ]"
                                    #ret_ += "\n  Version : Premium"
                                    #ret_ += "\n  Creator : {}".format(creator.displayName)
                                    #ret_ += "\n  Creator : @!".format(Owner)
                                    client.sendMessage(to, str(ret_))
                                    #client.sendMessage(to, "「 Read Text Below 」")
                                    sendMention(to, "「 About Rinda 」\n\nThe Beginning of this Bot Comes from Helloworld, I'm just Reworked This!\n\nOf Course Special Thanks To HelloWorld, And the Friends Around Me!\n\n*Creator : @!", [Ownerz])
                                except Exception as e:
                                    client.sendMessage(msg.to, str(e))
                                    
                            elif cmd.startswith("rinda bye"):
                                heij = client.getGroupIdsJoined()
                                #G = client.getGroup(heij)
                                #client.sendMessage(to, "Gbye {}".format(str(G.name)))
                                client.sendMessage(to, "Gbye")
                                #client.getGroupIdsJoined()
                                client.leaveGroup(to)                                    

                            elif cmd == "rinda get reader on":
                              if settings["selfbot"] == True:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                read['readPoint'][msg.to] = msg_id
                                read['readMember'][msg.to] = {}
                                client.sendMessage(msg.to, "Lurking berhasil dinyalakan\n\nPada : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n[ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                            elif cmd == "rinda get reader off":
                              if settings["selfbot"] == True:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                client.sendMessage(msg.to, "Getreader berhasil dimatikan\n\nPada : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n[ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                            elif cmd == "rinda get readers":
                                if msg.to in read['readPoint']:
                                    if read['readMember'][msg.to] != {}:
                                        aa = []
                                        for x in read['readMember'][msg.to]:
                                            aa.append(x)
                                        try:
                                            arrData = ""
                                            textx = "  「 {} Reader 」\n\n1. ".format(str(len(aa)))
                                            arr = []
                                            no = 1
                                            b = 1
                                            for i in aa:
                                                b = b + 1
                                                end = "\n"
                                                mention = "@!\n"
                                                slen = str(len(textx))
                                                elen = str(len(textx) + len(mention) - 1)
                                                arrData = {'S':slen, 'E':elen, 'M':i}
                                                arr.append(arrData)
                                                tz = pytz.timezone("Asia/Jakarta")
                                                timeNow = datetime.now(tz=tz)
                                                textx += mention
                                                if no < len(aa):
                                                    no += 1
                                                    textx += str(b) + ". "
                                                else:
                                                    try:
                                                        no = "[ {} ]".format(str(client.getGroup(msg.to).name))
                                                    except:
                                                        no = "  "
                                            msg.to = msg.to
                                            msg.text = textx+"\nPada : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n* "+ datetime.strftime(timeNow,'%H:%M:%S')+"* "
                                            msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                            msg.contentType = 0
                                            client.sendMessage1(msg)
                                        except:
                                            pass
                                        try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                        except:
                                            pass
                                        read['readPoint'][msg.to] = msg.id
                                        read['readMember'][msg.to] = {}
                                    else:
                                        client.sendMessage(msg.to, "Tidak ada satupun")
                                else:
                                    client.sendMessage(msg.to, "Getreader status is Unactived")

                            elif cmd.startswith("rinda tutupqr to"):
                              if msg._from in admin:
                                number = cmd.replace("rinda tutupqr to","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    group = groups[int(number)-1]
                                    G = client.getGroup(group)
                                    try:
                                        G.preventedJoinByTicket = True
                                        client.updateGroup(G)
                                    except:
                                        G.preventedJoinByTicket = True
                                        client.updateGroup(G)
                                    client.sendMessage(to, " 「 Close Qr 」 InGroup : " + G.name)
                                except Exception as error:
                                    client.sendMessage(to, str(error))
                  
                            elif cmd.startswith("rinda bukaqr to"):
                              if msg._from in admin:
                                number = cmd.replace("rinda bukaqr to","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    group = groups[int(number)-1]
                                    G = client.getGroup(group)
                                    try:
                                        G.preventedJoinByTicket = False
                                        client.updateGroup(G)
                                        gurl = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(G.id)))
                                    except:
                                        G.preventedJoinByTicket = False
                                        client.updateGroup(G)
                                        gurl = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(G.id)))
                                    client.sendMessage(to, " 「 Close Qr 」 InGroup : " + G.name + "\n  Url : " + gurl)
                                except Exception as error:
                                    client.sendMessage(to, str(error))
                  
                            elif cmd.startswith("rinda mention to"):
                              #if msg._from in Owner:
                                number = cmd.replace("rinda mention to","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    group = groups[int(number)-1]
                                    G = client.getGroup(group)
                                    try:
                                        contact = [mem.mid for mem in G.members]
                                        text = "Mentioning To %i Members\n" %len(contact)
                                        no = 1
                                        for mid in contact:
                                            text += "\n{}. @!           ".format(str(no))
                                            no = (no+1)
                                        text += "\n\nInGroup : {}".format(str(G.name))
                                        sendMention(group, text, contact)
                                    except:
                                        contact = [mem.mid for mem in G.members]
                                        text = "Mentioning To %i Members\n" %len(contact)
                                        no = 1
                                        for mid in contact:
                                            text += "\n{}. @!           ".format(str(no))
                                            no = (no+1)
                                        text += "\n\nInGroup : {}".format(str(G.name))
                                        sendMention(group, text, contact)
                                    client.sendMessage(to, "Sended Mention To Group : " + G.name)
                                except Exception as error:
                                    client.sendMessage(to, str(error))

                            elif cmd.startswith("rinda crash to"):
                              if msg._from in admin:
                                number = cmd.replace("rinda crash to","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    group = groups[int(number)-1]
                                    G = client.getGroup(group)
                                    try:
                                        client.sendContact(group, "uc7d319b7d2d38c35ef2b808e3a2aeed9',")
                                    except:
                                        client.sendContact(group, "uc7d319b7d2d38c35ef2b808e3a2aeed9',")
                                    client.sendMessage(to, "Sended Crash To Group : " + G.name)
                                except Exception as error:
                                    client.sendMessage(to, str(error))

                            elif cmd.startswith("rinda get creepypasta"):
                                r=requests.get("http://hipsterjesus.com/api")
                                data=r.text
                                data=json.loads(data)
                                hasil = " 「 Creepypasta 」\n\n" 
                                hasil += str(data["text"])
                                client.sendMessage(msg.to, str(hasil))

                            elif cmd.startswith("timezone "):
                                try:
                                    query = cmd.replace("timezone ","")
                                    #search = cmd.replace("timezone ","")
                                    r = requests.get("https://time.siswadi.com/geozone/{}".format(urllib.parse.quote(query)))
                                    data=r.text
                                    data=json.loads(data)
                                    ret_ = "\n"
                                    ret_ += "\n Latitude : " +str(data["data"]["latitude"])
                                    ret_ += "\n Longitude : " +str(data["data"]["longitude"])
                                    ret_ += "\n Address : " +str(data["data"]["address"])
                                    ret_ += "\n Country : " +str(data["data"]["country"])
                                    #client.sendMessage(to, str(ret_))
                                    client.sendMessage(to, " 「 Timezone " + query + " 」  " + str(ret_))
                                except Exception as error:
                                    client.sendMessage(to, str(error))

                            elif cmd.startswith("rinda get image "):
                                try:
                                    query = cmd.replace("rinda get image ","")
                                    #search = cmd.replace("client image ","")
                                    r = requests.get("https://xeonwz.herokuapp.com/images/google.api?q={}".format(query))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["content"] != []:
                                        items = data["content"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        client.sendMessage(to, " Search Image 「 " + query + " 」  ")
                                        client.sendImageWithURL(to, str(path))
                                except Exception as error:
                                     logError(error)
                                     var= traceback.print_tb(error.__traceback__)
                                     client.sendMessage(to,str(var))

                            elif cmd.startswith("rinda get 1cak"):
                                r=requests.get("http://api-1cak.herokuapp.com/random")
                                data=r.text
                                data=json.loads(data)
                                hasil = "「 1CAK Result 」"
                                hasil += "\n\n  Judul : \n " + str(data["title"])
                                hasil += " \n\n  ID : " +str(data["id"])                                
                                hasil += "\n  URL : " + str(data["url"])
                                hasil += "\n  Rates : " + str(data["votes"])
                                hasil += "\n  Nsfw : " + str(data["nsfw"])
                                image = str(data["img"])
                                client.sendImageWithURL(msg.to, str(image))
                                client.sendMessage(msg.to, str(hasil))

                            elif cmd.startswith("rinda get devianart "):
                                query = cmd.replace("rinda get devianart ","")
                                try:
                                    search = cmd.replace("rinda get devianart ","")
                                    r = requests.get("https://xeonwz.herokuapp.com/images/deviantart.api?q={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["content"] != []:
                                        items = data["content"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        client.sendMessage(msg.to, "Search Image 「 " + query + " 」")
                                        client.sendImageWithURL(to, str(path))                                        
                                except Exception as error:
                                     logError(error)
                                     var= traceback.print_tb(error.__traceback__)
                                     client.sendMessage(to,str(var))

                            elif cmd.startswith("hasil dari "):
                                query = cmd.replace("hasil dari ","")
                                puy1 = requests.get("https://www.calcatraz.com/calculator/api?c={}".format(urllib.parse.quote(query)))
                                data=puy1.text
                                data=json.loads(data)
                                client.sendMessage(msg.to, "Hasil dari 「" + query + "」 = " + str(data))

                            elif cmd.startswith("github "):
                                query = cmd.replace("github ","")
                                b = urllib.parse.quote(query)
                                #client.sendMessage(to,"「 Searching 」\n" "Type: GitHub Search\nStatus: Processing...")
                                client.sendMessage(to, " " + b + "\nhttps://github.com/search?q="+query)
                                
                            elif cmd.startswith("playstore "):
                                query = cmd.replace("playstore ","")
                                client.sendMessage(to, "「 Searched : "+query+"」\nhttps://play.google.com/store/search?q="+query)
                  
                            elif cmd.startswith("twitter "):
                                query = cmd.replace("twitter ","")
                                b = urllib.parse.quote(query)
                                #client.sendMessage(to,"「 Searching 」\n" "Type:Search Info\nStatus: Processing")
                                client.sendMessage(to, "https://www.twitter.com/"+query)
                                #client.sendMessage(to,"「 Searching 」\n" "Type:Search Info\nStatus: Success")

                            elif 'Simi ' in msg.text:
                              #if msg._from in admin:
                                spl = msg.text.replace('Simi ','')
                                if spl == 'on':
                                    if msg.to in simisimi:
                                         msgs = "Simi Mode tidak aktif"
                                    else:
                                         simisimi.append(msg.to)
                                         ginfo = client.getGroup(msg.to)
                                         msgs = "Simi Mode diaktifkan Di Group : \n「" +str(ginfo.name + "」")
                                    client.sendMessage(msg.to, "Diaktifkan\n" + msgs)
                                elif spl == 'off':
                                      if msg.to in simisimi:
                                           simisimi.remove(msg.to)
                                           ginfo = client.getGroup(msg.to)
                                           msgs = "Simi Mode dimatikan Di Group : \n「" +str(ginfo.name + "」")
                                      else:
                                           msgs = "Simi Mode tidak aktif"
                                      client.sendMessage(msg.to, "Dinonaktifkan\n" + msgs)

                            elif cmd.startswith("rinda get motivation"):
                                puy1 = requests.get("https://talaikis.com/api/quotes/random")
                                data=puy1.text
                                data=json.loads(data)
                                client.sendMessage(to, " 「 Motivation 」 \n" + str(data["quote"]))

                            elif cmd.startswith("rinda get suggestion to "):
                                query = cmd.replace("rinda get suggestion to ","")
                                puy1 = requests.get("http://api.ntcorp.us/se/v1/?q={}".format(urllib.parse.quote(query)))
                                data=puy1.text
                                data=json.loads(data)
                                no = 0
                                ret_ = "\n"                                                                                                                       
                                anu = data["result"]["suggestions"]
                                for s in anu:
                                    hmm = s
                                    no += 1
                                    ret_ += "\n" + str(no) + ") " + "{}\n".format(str(hmm))
                                client.sendMessage(msg.to, " This is Suggestion to 「 " + query + " 」  " + str(ret_))

                            elif cmd.startswith("rinda get gif "):
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                count = urutan.split("*")
                                search = str(count[0])
                                r = requests.get("https://api.tenor.com/v1/search?key=PVS5D2UHR0EV&limit=10&q="+str(search))
                                data = json.loads(r.text)
                                if len(count) == 1:
                                    no = 0
                                    hasil = "       「 Gifs Menu 」\n"
                                    for aa in data["results"]:
                                        no += 1
                                        hasil += "\n" + str(no) + ") " + str(aa["title"])
                                        ret_ = "\n\nRinda get gif {}*number".format(str(search))
                                    client.sendMessage(to,hasil+ret_)
                                elif len(count) == 2:
                                    try:
                                        num = int(count[1])
                                        b = data["results"][num - 1]
                                        c = str(b["id"])
                                        hasil = " Gif ID : "+str(c)
                                        hasil += ""
                                        client.sendMessage(msg.to,hasil)
                                        dl = str(b["media"][0]["loopedmp4"]["url"])
                                        client.sendVideoWithURL(msg.to,dl)
                                    except Exception as e:
                                        client.sendMessage(to," "+str(e))

                            elif cmd.startswith("rinda get topnews"):
                                mpui = requests.get("https://newsapi.org/v2/top-headlines?country=id&apiKey=1214d6480f6848e18e01ba6985e2008d")
                                data = mpui.text
                                data = json.loads(data)
                                hasil = "      「 Top News 」\n\n"
                                hasil += "1) \n<" + str(data["articles"][0]["title"] + ">")
                                hasil += "\n     Sumber : " + str(data["articles"][0]["source"]["name"])
                                hasil += "\n     Penulis : " + str(data["articles"][0]["author"])
                                hasil += "\n     Link : " + str(data["articles"][0]["url"])
                                hasil += "\n\n2) \n<" + str(data["articles"][0]["title"] + ">")
                                hasil += "\n     Sumber : " + str(data["articles"][1]["source"]["name"])
                                hasil += "\n     Penulis : " + str(data["articles"][1]["author"])   
                                hasil += "\n     Link : " + str(data["articles"][1]["url"])
                                hasil += "\n\n3) \n<" + str(data["articles"][0]["title"] + ">")
                                hasil += "\n     Sumber : " + str(data["articles"][2]["source"]["name"])
                                hasil += "\n     Penulis : " + str(data["articles"][2]["author"])
                                hasil += "\n     Link : " + str(data["articles"][2]["url"])
                                path = data["articles"][3]["urlToImage"]
                                client.sendMessage(msg.to, str(hasil))
                                client.sendImageWithURL(msg.to, str(path))

                            elif cmd.startswith("rinda get lockscreen "):
                              #if msg._from in Owner:
                                query = cmd.replace("rinda get lockscreen ","")
                                cond = query.split("*")
                                search = str(cond[0])
                                result = requests.get("https://api.eater.tech/wallp/{}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "[ Lockscreen Search ]\n"
                                    for sam in data["result"]:
                                        num += 1
                                        ret_ += "\n{}. {}".format(str(num),str(sam["judul"]))
                                    ret_ += "\n\nMore : Rinda get lockscreen {}*(number) to Details.".format(str(search))
                                    client.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        sam = data["result"][num - 1]
                                        result = requests.get("https://api.eater.tech/wallp/{}".format(str(search)))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            client.sendImageWithURL(to, str(sam["link"]))

                            elif cmd.startswith("rindabc: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                pesan = text.replace(sep[0] + " ","")
                                saya = puy.getGroupIdsJoined()
                                for group in saya:
                                   puy.sendMessage(group,"" + str(pesan))

                            elif cmd.startswith("smule "):
                                query = cmd.replace("smule ","")
                                b = urllib.parse.quote(query)
                                #client.sendMessage(to,"Searching to id smule..")
                                client.sendMessage(to, "Name : "+b+"\nId smule : http://smule.com/"+query)

                            elif cmd.startswith("asking "):
                                query = cmd.replace("asking ","")
                                #kata = cmd.replace("asking ", "")
                                sch = query.replace(" ","+")
                                with requests.session() as web:
                                   urlz = "http://lmgtfy.com/?q={}".format(str(sch))
                                   r = web.get("http://tiny-url.info/api/v1/create?apikey=A942F93B8B88C698786A&provider=cut_by&format=json&url={}".format(str(urlz)))
                                   data = r.text
                                   data = json.loads(data)
                                   url = data["shorturl"]
                                   ret_ = "\n"
                                   ret_ += " 「 Link : {}".format(str(url) + " 」")
                                   #client.sendMessage(to, str(ret_))
                                   client.sendMessage(msg.to, "「 Question is *" + query + "* 」  " + str(ret_))

                            elif cmd.startswith("rinda get wikipedia "):
                                query = cmd.replace("rinda get wikipedia ","")
                                try:
                                    sep = msg.text.split(" ")
                                    wiki = msg.text.replace(sep[0] + " ","")
                                    wikipedia.set_lang("id")
                                    pesan=" 「 Judul 」 "
                                    pesan+=wikipedia.page(wiki).title
                                    pesan+="\n 「 Teks 」 "
                                    pesan+=wikipedia.summary(wiki, sentences=1)
                                    pesan+="\n 「 Alamat url 」 "+wikipedia.page(wiki).url
                                    pesan+="\n"
                                    client.sendMessage(to, pesan)
                                except:
                                        try:
                                            pesan="Teks terlalu panjang, Klik url untuk lebih lengkap\n"
                                            pesan+=wikipedia.page(wiki).url
                                            #client.sendMessage(to, pesan)
                                            client.sendMessage(to, " Wikipedia Search 「 " + query + " 」  " + pesan)
                                        except Exception as e:
                                            #client.sendMessage(to, "Wikipedia [ " + query + " ] " + str(e))
                                            client.sendMessage(msg.to, " Wikipedia Search 「 " + query + " 」 " + str(e))

                            elif cmd.startswith("rinda getmeme "):
                                query = cmd.replace("rinda getmeme ","")
                                #data = r.text
                                #data = json.loads(data)
                                meme = query.split('*')
                                meme = meme[0].replace(' ','_')
                                atas = query.split('*')
                                atas = atas[1].replace(' ','_')
                                bawah = query.split('*')
                                bawah = bawah[2].replace(' ','_')
                                memes = 'https://memegen.link/'+meme+'/'+atas+'/'+bawah+'.jpg'
                                client.sendMessage(msg.to, "Creating Meme " + query + "...")
                                client.sendImageWithURL(msg.to, memes)

                            elif cmd == "me":
                                contact = client.getContact(sender)
                                userid = "https://line.me/ti/p/~" + client.profile.userid
                                sendMention(to, "@!", [sender])
                                #client.sendContact(to, sender)
                                client.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))

                            elif cmd == 'rinda memelist':
                                client.sendMessage(to,"10 Guy = tenguy\nAfraid to Ask Andy = afraid\nAn Older Code Sir, But It Checks Out = older\nAncient Aliens Guy = aag\nAt Least You Tried = tried\nBaby Insanity Wolf = biw\nBad Luck Brian = blb\nBut That's None of My Business = kermit\nButthurt Dweller = bd\nCaptain Hindsight = ch\nComic Book Guy = cbg\nCondescending Wonka = wonka\nConfession Bear = cb\nConspiracy Keanu = keanu\nDating Site Murderer = dsm\nDo It Live! = live\nDo You Want Ants? = ants\nDoge = doge\nDrake Always On Beat = alwaysonbeat\nErmahgerd = ermg\nFirst World Problems = fwp\nForever Alone = fa\nFoul Bachelor Frog = fbf\nFuck Me, Right? = fmr\nFuturama Fry = fry\nGood Guy Greg = ggg\nHipster Barista = hipster\nI Can Has Cheezburger? = icanhas\nI Feel Like I'm Taking Crazy Pills = crazypills\nI Immediately Regret This Decision! = regret\nI Should Buy a Boat Cat = boat\nI Would Be So Happy = sohappy\nI am the Captain Now = captain\nInigo Montoya = inigo\nInsanity Wolf = iw\nIt's A Trap! = ackbar\nIt's Happening = happening\nIt's Simple, Kill the Batman = joker\nJony Ive Redesigns Things = ive\nLaughing Lizard = ll\nMatrix Morpheus = morpheus\nMilk Was a Bad Choice = badchoice\nMinor Mistake Marvin = mmm\nNothing To Do Here = jetpack\nOh, Is That What We're Going to Do Today? = red\nOne Does Not Simply Walk into Mordor = mordor\nOprah You Get a Car = oprah\nOverlay Attached Girlfriend = oag\nPepperidge Farm Remembers = remembers\nPhilosoraptor = philosoraptor\nProbably Not a Good Idea = jw\nSad Barack Obama = sad-obama\nSad Bill Clinton = sad-clinton\nSad Frog / Feels Bad Man = sadfrog\nSad George Bush = sad-bush\nSad Joe Biden = sad-biden\nSad John Boehner = sad-boehner\nSarcastic Bear = sarcasticbear\nSchrute Facts = dwight\nScumbag Brain =  sb\nScumbag Steve = ss\nSealed Fate = sf\nSee? Nobody Cares = dodgson\nShut Up and Take My Money! = money\nSo Hot Right Now = sohot\nSocially Awesome Awkward Penguin = awesome-awkward\nSocially Awesome Penguin = awesome\nSocially Awkward Awesome Penguin = awkward-awesome\nSocially Awkward Penguin = wkward\nStop Trying to Make Fetch Happen = fetch\nSuccess Kid = success\nSuper Cool Ski Instructor = ki\nThat Would Be Great = officespace\nThe Most Interesting Man in the World = interesting\nThe Rent Is Too Damn High = toohigh\nThis is Bull, Shark = bs\nWhy Not Both? = Both\nWinter is coming = winter\nX all the Y = xy\nX, X Everywhere = buzz\nXzibit Yo Dawg = yodawg\nY U NO Guy = yuno\nY'all Got Any More of Them = yallgot\nYou Should Feel Bad = bad\nYou Sit on a Throne of Lies = elf\nYou Were the Chosen One! = chosen\n\nUsage : Rinda getmeme sohot*Hello*Rin")

                            elif cmd.startswith("rinda get quotes"):
                                r=requests.get("https://talaikis.com/api/quotes/random")
                                data=r.text
                                data=json.loads(data)
                                hasil = "  [ Search Random Quote ]\n\n"
                                hasil += "Genre : " +str(data["cat"])
                                hasil += "\n\n" +str(data["quote"])
                                hasil += "\n\n From : " +str(data["author"])+ " "
                                client.sendMessage(msg.to, str(hasil))

                            elif cmd.startswith("rinda leave to"):
                                number = cmd.replace("rinda leave to","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    group = groups[int(number)-1]
                                    G = client.getGroup(group)
                                    try:
                                        client.leaveGroup(G.id)
                                    except:
                                        client.leaveGroup(G.id)
                                    client.sendMessage(to, "Leave To Group : " + G.name)
                                except Exception as error:
                                    client.sendMessage(to, str(error))
                  
                            elif cmd == "rinda look errorlogs":
                                with open('logError.txt', 'r') as er:
                                        error = er.read()
                                client.sendMessage(to, str(error))

                            elif cmd.startswith("rinda get imageart "):
                                try:                                   
                                    search = cmd.replace("rinda get imageart ","")
                                    puy1 = requests.get("https://xeonwz.herokuapp.com/images/deviantart.api?q={}".format(search))
                                    data = puy1.text
                                    data = json.loads(data)
                                    if data["content"] != []:
                                        items = data["content"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        client.sendMessage(to,"Image in #%s From #%s." %(str(a),str(b)))
                                        client.sendImageWithURL(to, str(path))
                                        log.info("Art #%s from #%s." %(str(a),str(b)))
                                except Exception as error:
                                    logError(error)
                                    traceback.print_tb(error.__traceback__)

# Pembatas Script #
                        if text.lower() == "mykey":
                            client.sendMessage(to, "KeyCommand Saat ini adalah [ {} ]".format(str(settings["keyCommand"])))
                        if text.lower() == "token win10":
                            req = requests.get(url = 'https://api.eater.host/WIN10')
                            a = req.text
                            b= json.loads(a)
                            tknop= codecs.open("tkn.json","r","utf-8")
                            tkn = json.load(tknop)
                            tkn['{}'.format(msg._from)] = []
                            tkn['{}'.format(msg._from)].append({
                                'qr': b['result'][0]['linkqr'],
                                'tkn': b['result'][0]['linktkn']
                                })
                            qrz = b['result'][0]['linkqr']
                            client.sendMessage(msg.to, '{}'.format(qrz))
                            with open('tkn.json', 'w') as outfile:
                                json.dump(tkn, outfile)    
                        elif text.lower() == 'announce':
                            gett = client.getChatRoomAnnouncements(receiver)
                            for a in gett:
                                aa = client.getContact(a.creatorMid).displayName
                                bb = a.contents
                                cc = bb.link
                                textt = bb.text
                                client.sendMessage(receiver, 'Link: ' + str(cc) + '\nText: ' + str(textt) + '\nMaker: ' + str(aa))
                        elif text.lower() == "setkey on":
                            settings["setKey"] = True
                            client.sendMessage(to, "Berhasil mengaktifkan setkey")
                        elif text.lower() == "setkey off":
                            settings["setKey"] = False
                            client.sendMessage(to, "Berhasil menonaktifkan setkey")
# Pembatas Script #
                    elif msg.contentType == 1:
                        if settings["changeDisplayPicture"] == True:
                            path = client.downloadObjectMsg(msg_id)
                            settings["changeDisplayProfile"] = False
                            client.updateProfilePicture(path)
                            client.sendMessage(to, "Successfully changed profile photo")
                        if msg.toType == 2:
                            if to in settings["changeGroupPicture"]:
                                path = client.downloadObjectMsg(msg_id)
                                settings["changeGroupPicture"].remove(to)
                                client.updateGroupPicture(to, path)
                                client.sendMessage(to, "Successfully changed group photo")
                    elif msg.contentType == 7:
                        if settings["checkSticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "* Sticker Info *"
                            ret_ += "\n* STICKER ID : {}".format(stk_id)
                            ret_ += "\n* STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\n* STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\n* STICKER URL : line://shop/detail/{}".format(pkg_id)
                            ret_ += ""
                            client.sendMessage(to, str(ret_))
                    elif msg.contentType == 13:
                        if settings["checkContact"] == True:
                            try:
                                contact = client.getContact(msg.contentMetadata["mid"])
                                if client != None:
                                    cover = client.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Tidak dapat masuk di line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                    client.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "*--[* Details Contact *]--*"
                                ret_ += "\n* Name : {}".format(str(contact.displayName))
                                ret_ += "\n* MID : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\n* Bio : {}".format(str(contact.statusMessage))
                                ret_ += "\n* Profile Picture : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\n* Cover Picture : {}".format(str(cover))
                                ret_ += ""
                                client.sendMessage(to, str(ret_))
                            except:
                                client.sendMessage(to, "Invalid contact")
                    elif msg.contentType == 16:
                        if settings["checkPost"] == True:
                            try:
                                ret_ = "* Details Post *"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = client.getContact(sender)
                                    auth = "\n* Author : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n* Author : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n* URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n* Object URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n* Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n* Object URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n* Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n* Object URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n* Object URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n* Sticker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n* the contents of writing : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n"
                                client.sendMessage(to, str(ret_))
                            except:
                                client.sendMessage(to, "Invalid post")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 26:
            try:
                print ("[ 26 ] RECIEVE MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    #if settings["autoRead"] == True:
                    #    client.sendChatChecked(to, msg_id)
                    #if to in read["readPoint"]:
                    #    if sender not in read["ROM"][to]:
                    #        read["ROM"][to][sender] = True
                    if settings["unsendMessage"] == True:
                        try:
                            msg = op.message
                            if msg.toType == 0:
                                client.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                            else:
                                client.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                                msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                        except Exception as error:
                            logError(error)
                    if msg.contentType == 0:
                        if text is None:
                            return
                        if "/ti/g/" in msg.text.lower():
                            if settings["autoJoinTicket"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = client.findGroupByTicket(ticket_id)
                                    client.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    client.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if clientMid in mention["M"]:
                                    if settings["autoRespon"] == True:
                                        sendMention(sender, "Oi Asw @!,jangan main tag tag", [sender])
                                    break
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya':  
                            ginfo = client.getGroup(at)                           
                            contact = client.getContact(msg_dict[msg_id]["from"])
                            zx = ""
                            zxc = ""
                            zx2 = []       
                            xpesan =  "「 Gambar Dihapus 」\n◤ Pengirim : "             
                            ret_ = "◤ Nama Grup : {}".format(str(ginfo.name))   
                            ret_ += "\n◤ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))  
                            ry = str(contact.displayName)
                            pesan = ''
                            pesan2 = pesan+"@x \n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':contact.mid}
                            zx2.append(zx)
                            zxc += pesan2
                            text = xpesan + zxc + ret_ + ""
                            client.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            cl.sendImage(at, msg_dict[msg_id]["data"])     
                        else:              
                            ginfo = client.getGroup(at)
                            contact = client.getContact(msg_dict[msg_id]["from"])    
                            ret_ =  "「 Pesan Dihapus 」\n"
                            ret_ += "◤ Pengirim : {}".format(str(contact.displayName))
                            ret_ += "\n◤ Nama Grup : {}".format(str(ginfo.name))
                            ret_ += "\n◤ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                            ret_ += "\n◤ Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                            client.sendMessage(at, str(ret_))          
                        del msg_dict[msg_id]      
                except Exception as e:                    
                    print(e)                 
        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                                ginfo = client.getGroup(at)
                                contact = client.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "◤ Pengirim : {}".format(str(contact.displayName))
                                ret_ += "\n◤ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n◤ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict[msg_id]["text"]))
                                client.sendMessage(at, str(ret_))
                                client.sendImage(at, msg_dict[msg_id]["data"])
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)
                
        if op.type == 17:
           print ("MEMBER JOIN TO GROUP")
           if settings["Sambutan"] == True:
             if op.param2 in lineMID:
                 return
             ginfo = client.getGroup(op.param1)
             contact = client.getContact(op.param2)
             image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
             client.sendMessage(op.param1,"Hi " + client.getContact(op.param2).displayName + "\nWlc")
             client.sendImageWithURL(op.param1,image)

        if op.type == 15:
           print ("MEMBER LEAVE TO GROUP")
           if settings["Sambutan"] == True:
             if op.param2 in lineMID:
                 return
             ginfo = client.getGroup(op.param1)
             contact = client.getContact(op.param2)
             image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
             client.sendImageWithURL(op.param1,image)
             client.sendMessage(op.param1,"Selamat jalan " + client.getContact(op.param2).displayName + "")                
                
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                else:
                   pass
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

while True:
    try:
        delete_log()
        ops = clientPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                clientBot(op)
                clientPoll.setRevision(op.revision)
    except Exception as error:
        logError(error)
        
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
