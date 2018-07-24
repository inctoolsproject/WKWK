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
    helpMessage =   "* Help Message *" + "\n" + \
                    "* " + key + "Help" + "\n" + \
                    "* " + key + "Translate" + "\n" + \
                    "* " + key + "TTS" + "\n" + \
                    "* Status Command *" + "\n" + \
                    "* " + key + "Restart" + "\n" + \
                    "* " + key + "Runtime" + "\n" + \
                    "* " + key + "Speed" + "\n" + \
                    "* " + key + "Status" + "\n" + \
                    "* MyKey" + "\n" + \
                    "* SetKey「On/Off」" + "\n" + \
                    "* Special Command *" + "\n" + \
                    "* " + key + "Mimic「On/Off」" + "\n" + \
                    "* " + key + "MimicList" + "\n" + \
                    "* " + key + "MimicAdd「Mention」" + "\n" + \
                    "* " + key + "MimicDel「Mention」" + "\n" + \
                    "* " + key + "Mention" + "\n" + \
                    "* " + key + "Lurking「On/Off/Reset」" + "\n" + \
                    "* " + key + "Lurking" + "\n" + \
                    "* Media Command *" + "\n" + \
                    "* " + key + "CheckDate「Date」" + "\n" + \
                    "* " + key + "CheckWebsite「url」" + "\n" + \
                    "* " + key + "CheckPraytime「Location」" + "\n" + \
                    "* " + key + "CheckWeather「Location」" + "\n" + \
                    "* " + key + "CheckLocation「Location」" + "\n" + \
                    "* " + key + "InstaInfo 「UserName」" + "\n" + \
                    "* " + key + "InstaPost 「UserName」|「Number」" + "\n" + \
                    "* " + key + "InstaStory 「UserName」|「Number」" + "\n" + \
                    "* " + key + "SearchYoutube「Search」" + "\n" + \
                    "* " + key + "SearchMusic 「Search」" + "\n" + \
                    "* " + key + "SearchLyric 「Search」" + "\n" + \
                    "* " + key + "SearchImage 「Search」" + "\n" + \
                    ""
    return helpMessage

def helpsett():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpSett = " ╔══[ Settings Helper ]" + "\n" + \
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
    helpGroup = " ╔══[ Group Helper ]" + "\n" + \
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
    helpSelf = " ╔══[ Self Helper ]" + "\n" + \
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
                                helpMessage = helpmessage()
                                client.sendMessage(to, str(helpMessage))
                            if cmd == "help sett":
                                helpSett = helpsett()
                                poey = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                creator = client.getContact(poey)
                                #client.sendMessage(to, str(helpSett))
                                sendMention(to, str(helpSett), [poey])
                            if cmd == "help group":
                                helpGroup = helpgroup()
                                poey = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                creator = client.getContact(poey)
                                #client.sendMessage(to, str(helpGroup))
                                sendMention(to, str(helpGroup), [poey])
                            if cmd == "help self":
                                helpSelf = helpself()
                                poey = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                creator = client.getContact(poey)
                                #client.sendMessage(to, str(helpSelf))
                                sendMention(to, str(helpSelf), [poey])
                            elif cmd == "tts":
                                helpTextToSpeech = helptexttospeech()
                                client.sendMessage(to, str(helpTextToSpeech))
                            elif cmd == "translate":
                                helpTranslate = helptranslate()
                                client.sendMessage(to, str(helpTranslate))
                            elif cmd.startswith("changekey:"):
                                sep = text.split(" ")
                                key = text.replace(sep[0] + " ","")
                                if " " in key:
                                    client.sendMessage(to, "Key tidak bisa menggunakan spasi")
                                else:
                                    settings["keyCommand"] = str(key).lower()
                                    client.sendMessage(to, "Berhasil mengubah key command menjadi [ {} ]".format(str(key).lower()))
                            elif cmd == "speed":
                                start = time.time()
                                client.sendMessage(to, "Benchmarking...")
                                elapsed_time = time.time() - start
                                client.sendMessage(to, "[ Speed ]\nKecepatan mengirim pesan {} detik bos".format(str(elapsed_time)))
                            elif cmd == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                client.sendMessage(to, "Bot sudah aktif selama {} bos".format(str(runtime)))
                            elif cmd == "restart":
                                client.sendMessage(to, "Berhasil merestart Bot bos")
                                restartBot()
# Pembatas Script #
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
                            elif cmd == "me":
                                sendMention(to, "@!", [sender])
                                client.sendContact(to, sender)
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
                                        client.sendMessage(to, "Successfully membuka grup qr")
                            elif cmd == 'groupticket off':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == True:
                                        client.sendMessage(to, "The qr group is already closed")
                                    else:
                                        group.preventedJoinByTicket = True
                                        client.updateGroup(group)
                                        client.sendMessage(to, "Failed menutup grup qr")
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
                            elif cmd == "lurking on":
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
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    client.sendMessage(receiver,"Lurking telah diaktifkan\n\n*lurking* for check readers\n*lurking off* for Nonactived a lurkmode\n*lurking reset* for reset a readers point!")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    client.sendMessage(receiver,"Set reading point : \n" + readTime)
                            elif cmd == "lurking off":
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
                                if receiver not in read['readPoint']:
                                    client.sendMessage(receiver,"Lurking telah dinonaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    client.sendMessage(receiver,"Delete reading point : \n" + readTime)
        
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
                                    pass
                                else:
                                    client.sendMessage(receiver,"Lurking is nonactive\n\nType *lurking on* for actived a lurkmode!")
                            elif cmd.startswith("mimicadd"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        settings["mimic"]["target"][target] = True
                                        client.sendMessage(msg.to,"Target ditambahkan!")
                                        break
                                    except:
                                        client.sendMessage(msg.to,"Gagal menambahkan target")
                                        break
                            elif cmd.startswith("mimicdel"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        del settings["mimic"]["target"][target]
                                        client.sendMessage(msg.to,"Target dihapuskan!")
                                        break
                                    except:
                                        client.sendMessage(msg.to,"Gagal menghapus target")
                                        break
                                    
                            elif cmd == "mimiclist":
                                if settings["mimic"]["target"] == {}:
                                    client.sendMessage(msg.to,"Tidak Ada Target")
                                else:
                                    mc = "╔══[ Mimic List ]"
                                    for mi_d in settings["mimic"]["target"]:
                                        mc += "\n╠ "+client.getContact(mi_d).displayName
                                    mc += "\n╚══[ Finish ]"
                                    client.sendMessage(msg.to,mc)
                                
                            elif cmd.startswith("mimic"):
                                sep = text.split(" ")
                                mic = text.replace(sep[0] + " ","")
                                if mic == "on":
                                    if settings["mimic"]["status"] == False:
                                        settings["mimic"]["status"] = True
                                        client.sendMessage(msg.to,"Reply Message on")
                                elif mic == "off":
                                    if settings["mimic"]["status"] == True:
                                        settings["mimic"]["status"] = False
                                        client.sendMessage(msg.to,"Reply Message off")
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
# Pembatas Script #
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
                        if text.lower() == "token done":
                            tknop= codecs.open("tkn.json","r","utf-8")
                            tkn = json.load(tknop)
                            a = ['{}'.format(msg._from)][0]['tkn']
                            req = requests.get(url = '{}'.format(a))
                            b = req.text
                            client.sendMessage(msg.to, '{}'.format(b))                                    
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
                    if settings["autoRead"] == True:
                        client.sendChatChecked(to, msg_id)
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True
                    if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                        text = msg.text
                        if text is not None:
                            client.sendMessage(msg.to,text)
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
