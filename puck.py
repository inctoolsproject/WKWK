# -*- coding: utf-8 -*-

#  「 From Helloworld+Eater/ Edited by Puy 」 "
#The Beginning of this Bot Comes from Helloworld, I'm just Reworked This!
#Of Course Special Thanks To HelloWorld, And the Friends Around Me!
#ID : yapuy

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from time import sleep
from datetime import datetime, timedelta
from googletrans import Translator
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, pafy, subprocess, threading, glob, re, string, os, wikipedia, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit

#puy = LINE() 
puy = LINE("Ew0ry3Sc4W4mCz5prsDe.mDIRQD+WthuKlYOGL7ITRG.BYhCR+e/qG+Tlf7f8fLgt1JTd7pkh5jZxHBvTh0cgOc=")    # UNTUK LOGIN TOKEN #
#puy = LINE('phiezuke2@gmail.com','@phie99')      # UNTUK LOGIN MAIL LINE #
puyMid = puy.profile.mid
puyProfile = puy.getProfile()
puySettings = puy.getSettings()
puyPoll = OEPoll(puy)
botStart = time.time()

msg_dict = {}
temp_flood = {}
msg_sticker={}
wbanlist = []
translateen = []
translateid = []
translatetr = []
simisimi = []

Owner = ["u31d8aba9dff04c75242f2a2097b8adae"]
admin =["u31d8aba9dff04c75242f2a2097b8adae","ub0ff92e9820f6b82a2f0b81d6758c2fb"]

settings = {
    "autoJoin": True,
    "autoLeave": False,
    "Inroom": True,
    "Outroom": True,
    "timeRestart": "18000",
    "changeGroupPicture": [],
    "limit": 50,
    "limits": 50,
    "wordban": [],
    "autoAdd": True,
    "autoRead": False,
    "keyCommand": "",
    "ADITMADZSautoread": True,
    "welcomePesan": False,
    "mutebot2": False,
    "messageSticker": True,
    "leaveMessage": False,
    "welcomeMessage": True,
    "welcomeSticker": True,
    "unsend": True,
    "detectUnsend": True,
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "prefix": False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}

wait = {
    "Talkblacklist": {},
    "Talkwblacklist": False,
    "Talkdblacklist": False,
    "talkban": True,
    "admin":{},
    "addadmin":False,
    "delladmin":False,    
    "contact": False,
    "autoJoin": True,
    "autoAdd": True,
    "autoLeave": False,
    "autoLeave1": False,
    "detectMention": False,
    "selfbot": True,
    "ADITMADZSmessage1": "My Author (https://line.me/ti/p/~ketikidmu111)",
    "Mentiongift": False,
    "Mentionkick": True,
    "welcomeOn": True,
    "sticker": False,
    "selfbot": True,
    "unsend": True,
    "mention": "Di baca doang ish ,gk mau chat :(",
    "Respontag": "Im busy hufh",
    "welcome": "Selamat Datang",
    "leave": "Selamat Jalan",
    "comment": "Auto like by ᴄᴀʟᴏɴ ᴀʟᴍᴀʀʜᴜᴍ\nhttps://line.me/ti/p/~ketikidmu111",
    "message": "Thx For Added Me as your friend ,nice to meet you..",
    }

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())    
except:
    print("ᴄᴀʟᴏɴ ᴀʟᴍᴀʀʜᴜᴍ") 
    
adminOpen = codecs.open("admin.json","r","utf-8")
ownerOpen = codecs.open("Owner.json","r","utf-8")

settings["myProfile"]["displayName"] = puyProfile.displayName
settings["myProfile"]["statusMessage"] = puyProfile.statusMessage
settings["myProfile"]["pictureStatus"] = puyProfile.pictureStatus
coverId = puy.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)

def autoRestart():
    if time.time() - botStart > int(settings["timeRestart"]):
        time.sleep(5)
        restartBot()
        
def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    puy.sendMessage(to, '', contentMetadata, 7)        
        
def sendMentionFooter(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Meka Finee "
    if mids == []:
        raise Exception("Lost Time")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Lost Time")
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
    puy.sendMessage(to, textx, {'AGENT_NAME':'Menu Command', 'AGENT_LINK': 'https://www.instagram.com/phie_cobain', 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + puy.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)    
    #'AGENT_LINK': 'line://ti/p/~{}'.format(puy.getProfile().userid),
    
def sendMusic(send_to,music_id,title,artist,thumbnail,link):
 puy.sendMessage(send_to, '',
  {'text': title,
  'subText': artist,
  'id': music_id,
  'previewUrl': thumbnail,
  'linkUri': link,
  'i-linkUri': link,
  'a-linkUri': link,
  'i-installUrl': link,
  'a-installUrl': link,
  'a-packageName': 'jp.linecorp.linemusic.android',
  'type': 'mt',
  'countryCode': 'JP',
  'ORGCONTP': 'MUSIC'},
  19)    
    
def sendMessageWithFooter(to, text, name, url, iconlink):
        contentMetadata = {
            'AGENT_NAME': name,
            'AGENT_LINK': url,
            'AGENT_ICON': iconlink
        }
        return puy.sendMessage(to, text, contentMetadata, 0)
    
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                puy.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        userid = "https://line.me/ti/p/~" + puy.profile.userid
                        puy.sendFooter(tmp, "Spam is over , Now Bots Actived !", str(userid), "http://dl.profile.line-cdn.net/"+puy.getContact(puyMid).pictureStatus, puy.getContact(puyMid).displayName)
                    except Exception as error:
                        logError(error)            
            
def backupData():
    try:
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
#        backup = unsend
#        f = codecs.open('unsend.json','w','utf-8')
#        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False            
            
def logError(text):
    puy.log("[ ERROR ] {}".format(str(text)))
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
        raise Exception("Lost Time")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Lost Time")
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
    puy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if settings["prefix"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
def helpmessage():
    if settings['prefix'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpMessage =   "   「 Helper 」     " + "\n" + \
                    " " "1) " + key + " About" + "\n" + \
                    " " "2) " + key + " bye" + "\n" + \
                    " " "3) " + key + " get token" + "\n\n" + \
                    " " "「 Get Reader 」" + "\n" + \
                    " " "1) " + key + " check reader On/Off - [For SetRead]" + "\n" + \
                    " " "2) " + key + " get reader reset - [For Reset point]" + "\n" + \
                    " " "3) " + key + " get reader - [For CheckRead]" + "\n\n" + \
                    " " "「 All Can Used 」" + "\n" + \
                    " " "1) " + key + "  Asking [query]" + "\n" + \
                    " " "2) " + key + "  Hasil Dari [query]/[contoh : Hasil dari 22x22]" + "\n" + \
                    " " "3) " + key + "  Timezone [query]" + "\n" + \
                    " " "4) " + key + "  Smule [query]" + "\n" + \
                    " " "5) " + key + "  Bitcoin" + "\n" + \
                    " " "6) " + key + "  Twitter [query]" + "\n" + \
                    " " "7) " + key + "  Memelist" + "\n" + \
                    " " "8) " + key + "  Randomlose" + "\n" + \
                    " " "9) " + key + "  Playstore [query]" + "\n" + \
                    " " "10) " + key + " Get Motivation" + "\n" + \
                    " " "11) " + key + " get Suggestion to [query]" + "\n" + \
                    " " "12) " + key + " Groupinfo [number of groups]" + "\n" + \
                    " " "13) " + key + " Grouplist" + "\n" + \
                    " " "14) " + key + " get Memberlist to [number of groups]" + "\n" + \
                    " " "15) " + key + " Mention to [number of groups]" + "\n" + \
                    " " "16) " + key + " get devianart [query]" + "\n" + \
                    " " "17) " + key + " get Image [query]" + "\n" + \
                    " " "18) " + key + " get Quotes" + "\n" + \
                    " " "19) " + key + " get 1Cak" + "\n" + \
                    " " "20) " + key + " get video [query]" + "\n" + \
                    " " "21) " + key + " get Wikipedia [query]" + "\n" + \
                    " " "22) " + key + " getmeme dwight*Hei*Rin" + "\n" + \
                    " " "23) " + key + " get lockscreen [query]" + "\n" + \
                    " " "24) " + key + " get creepypasta" + "\n" + \
                    " " "25) " + key + " get gif [query]" + "\n\n" + \
                    "  「Use < " + key + " > For the Prefix」" + "\n" + \
                    "  「*CREATED BY : @!*」"
    return helpMessage
                    
def ownermessage():
    if settings['prefix'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    ownerMessage =  " " "「 Only Owner Can Used 」" + "\n" + \
                    " " "1) " + key + " SetPrefix:" + "\n" + \
                    " " "2) " + key + " Prefix on" + "\n" + \
                    " " "3) " + key + " Prefix off" + "\n" + \
                    " " "4) " + key + " Logout" + "\n" + \
                    " " "5) " + key + " check errorlog" + "\n" + \
                    " " "6) " + key + " reset errorlog" + "\n" + \
                    " " "7) " + key + " Update" + "\n" + \
                    " " "8) " + key + " Mention to [number of Groups]" + "\n" + \
                    " " "9) " + key + " Memberlist to [number of groups]" + "\n" + \
                    " " "10) " + key + " Bukaqr to [number of Groups]" + "\n" + \
                    " " "11) " + key + " Tutupqr to [number of Groups]" + "\n" + \
                    " " "12) " + key + " Crash to [number of Groups]" + "\n" + \
                    " " "13) " + key + " Leave to [number of Groups]" + "\n\n" + \
                    "  「Use < " + key + " > For the Prefix」" + "\n" + \
                    "  「*CREATED : @!*」"
    return ownerMessage
    
def puyBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return

        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                puy.findAndAddContactsByMid(op.param2)
                sendMessageWithFooter(op.param1, "Thx for add")

        if op.type == 13:
            print ("[ 13 ] Invite Into Group")
            if puyMid in op.param3:
                if settings["autoJoin"] == True:
                    puy.acceptGroupInvitation(op.param1)
                dan = puy.getContact(op.param2)
                tgb = puy.getGroup(op.param1)
                sendMention(op.param1, "[ INVITATION ]\n Thx For Invited Me".format(str(tgb.name)),[op.param2])
                #puy.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                puy.sendContact(op.param1, op.param2)

#ADD ADMIN
            if msg._from in admin:
             if wait["addadmin"] == True:
               if msg.contentMetadata["mid"] in admin:
                   puy.sendMessage(msg.to,"Dia udah menjadi admin")
                   wait["addadmin"] = True
               else:
                   admin.append(msg.contentMetadata["mid"])
                   wait["addadmin"] = True
                   puy.sendMessage(msg.to,"Berhasil menambahkan dia menjadi admin.")
            if wait["delladmin"] == True:
               if msg.contentMetadata["mid"] in admin:
                   admin.remove(msg.contentMetadata["mid"])
                   puy.sendMessage(msg.to,"Berhasil menghapus dia dari admin.")
               else:
                   wait["delladmin"] = True
                   puy.sendMessage(msg.to,"Dia bukan admin.")                
                
        if op.type == 15:
            print ("[ 15 ]  NOTIFIED LEAVE GROUP")
            if settings["leaveMessage"] == True:
                if "{gname}" in settings['leavePesan']:
                    gName = puy.getGroup(op.param1).name
                    msg = settings['leavePesan'].replace("{gname}", gName)
                    msgSticker = settings["messageSticker"]["listSticker"]["leaveSticker"]
                    if msgSticker != None:
                        sid = msgSticker["STKID"]
                        spkg = msgSticker["STKPKGID"]
                        sver = msgSticker["STKVER"]
                        sendSticker(op.param2, sver, spkg, sid)
                    if "@!" in settings['leavePesan']:
                        msg = msg.split("@!")
                        return sendMention(op.param2, op.param2, msg[0], msg[1])
                    return sendMention(op.param2, op.param2, "Hallo ", msg)
                msgSticker = settings["messageSticker"]["listSticker"]["leaveSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
                sendMention(op.param1, op.param2, "Bye", "\n{}".format(str(settings['leavePesan'])))
                
        if op.type == 17:
            print ("[ 17 ]  NOTIFIED ACCEPT GROUP INVITATION")
            if settings["welcomeMessage"] == True:
                group = puy.getGroup(op.param1)
                contact = puy.getContact(op.param2)
                msgSticker = settings["messageSticker"]["listSticker"]["welcomeSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
                if "{gname}" in settings['welcomePesan'].lower():
                    gName = group.name
                    msg = settings['welcomePesan'].replace("{gname}", gName)
                    if "@!" in msg:
                        msg = msg.split("@!")
                        return sendMention(op.param1, op.param2, msg[0], msg[1])
                    sendMention(op.param1, op.param2, "Hi", msg)
                else:
                    sendMention(op.param1, op.param2, "Hi","\n{}".format(str(settings['welcomePesan'])))
                    contact = puy.getContact(op.param2)
                    puy.sendImageWithURL(op.param1,image)
                    arg = "   Group Name : {}".format(str(group.name))
                    arg += "\n   User Join : {}".format(str(contact.displayName))
                    print (arg)                
                
        if op.type == 19:
            print ("[ 19 ] NOTIFIED KICKOUT FROM GROUP")
            group = puy.getGroup(op.param1)
            contact = puy.getContact(op.param2)
            victim = puy.getContact(op.param3)
            dap = "   Group Name : {}".format(str(group.name))
            dapp = "\n   Executor : {}".format(str(contact.displayName))
            dappp = "\n   Victim : {}".format(str(victim.displayName))
            puy.sendMessage(op.param1, "「 Notify Kickout From Group 」\n\nPelaku Kick : {}\nK{}".format(str(contact.displayName),"orban Kick : {}".format(str(victim.displayName))))
            puy.sendContact(op.param1, op.param2)
            puy.sendContact(op.param1, op.param3)
            print (dap)                
                
        if op.type == 65:
            if settings["detectUnsend"] == False:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                                ginfo = puy.getGroup(at)
                                ariftj = puy.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "Sticker Dihapus\n"
                                ret_ += "Pengirim : {}".format(str(ariftj.displayName))
                                ret_ += "\nNama Grup : {}".format(str(ginfo.name))
                                ret_ += "\nWaktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict[msg_id]["text"]))
                                puy.sendMessage(at, str(ret_))
                                puy.sendImage(at, msg_dict[msg_id]["data"])
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)                
                
        if op.type in [22, 24]:
            print ("[ 22 And 24 ] NOTIFIED INVITE INTO ROOM & NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                sendMention(op.param2, "@! hmm?")
                puy.leaveRoom(op.param1)
                                
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg.to in simisimi:
                   try:
                       if msg.text is not None:
                           simi = msg.text
                           r = requests.get("http://leert.corrykalam.gq/chatbot.php?text="+simi)
                           data = r.text
                           data = json.loads(data)
                           if data["status"] == 200:
                               puy.sendMessage(msg.to, str(data["answer"]))
                   except Exception as error:
                       pass

               if msg.to in translatetr:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='tr')
                           A = hasil.text
                           puy.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

               if msg.to in translateen:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='en')
                           A = hasil.text
                           puy.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

               if msg.to in translateid:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='id')
                           A = hasil.text
                           puy.sendMessage(msg.to, A)
                   except Exception as error:
                       pass                                
                                
        if op.type == 25:
            try:
                print ("[ 25 ] PUBLIC")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                prefix = settings["keyCommand"].title()
                if settings["prefix"] == False:
                    prefix = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != puy.profile.mid:
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
                              if wait["selfbot"] == True:
                                helpMessage = helpmessage()
                                poey = "ub0ff92e9820f6b82a2f0b81d6758c2fb"
                                creator = puy.getContact(poey)
                                sendMention(to, str(helpMessage), [poey])
                                
                            if cmd == "helpstaff":
                              if wait["selfbot"] == True:
                                ownerMessage = ownermessage()
                                poey = "ub0ff92e9820f6b82a2f0b81d6758c2fb"
                                creator = puy.getContact(poey)
                                sendMention(to, str(ownerMessage), [poey])                                
                            
                            if cmd == "pause":
                              if msg._from in admin:
                                  wait["selfbot"] = False
                                  puy.sendMessage(msg.to, "Server diberhentikan sementara")                            
                            
                            if cmd == "#help":
                              if wait["selfbot"] == True:
                                helpMessage = helpmessage()
                                puy.sendMessage(to, str(helpMessage),{'AGENT_ICON':'http://dl.profile.line-cdn.net/0hkY3juiptNHYOExk5wsdLITJWOht5PTI-diUpGX8RPhZ0IydzMSV_FC0VaxV0I3JyMCZ4Ei8VOEQh','AGENT_LINK':'https://line.me/ti/p/~ketikidmu111','AGENT_NAME':'Help Message'})
                            
                            elif cmd == "tokengen":
                                sendMentionFooter(to, "「 GET TOKEN 」\n\n1) DESKTOPWIN\n2) WIN10\n3) DESKTOPMAC\n4) IOSPAD\n5) CHROME\n\nUsage : get token chrome\n@! - Selamat Mencoba.", [sender])
                            elif cmd == "get token":
                                sendMentionFooter(to, "「 GET TOKEN 」\n\n1) DESKTOPWIN\n2) WIN10\n3) DESKTOPMAC\n4) IOSPAD\n5) CHROME\n\nUsage : get token chrome\n@! - Selamat Mencoba.", [sender])
                                
                            elif cmd == "sp":
                                start = time.time()
                                puy.sendMessage(to, "Counting...")
                                speed = time.time() - start
                                ping = speed * 1000
                                puy.sendMessage(to, "The result is {} ms".format(str(speedtest(ping))))
                                
                            elif cmd == ".speed":
                              if msg._from in Owner:
                                start = time.time()
                                puy.sendMessage(to, "...")
                                elapsed_time = time.time() - start
                                puy.sendMessage(to, "{}".format(str(elapsed_time)))
                                
                            elif cmd == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                puy.sendMessage(to, "Server has been Active for {} puy".format(str(runtime)))                                
                                
                            elif cmd.startswith("speed"):
                                get_profile_time_start = time.time()
                                get_profile = puy.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = puy.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                #get_contact = puy.getContact(clientMid)
                                get_contact_time = time.time() - get_contact_time_start
                                #puy.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                                puy.sendMessage(to, "%.6f" % (get_group_time/3))                                
                                
                            elif cmd == "restart":
                              if sender in Owner:
                                tz = pytz.timezone("Asia/Jakarta")
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
                                Timed = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                #if msg.to not in read['readPoint']:
                                    #dap.sendMessage(msg.to, "「 NOTIFIED BOT SPEED 」\n\n" + Timed)
                                #sendMention(to, "@! \nPUY berhasil diperbarui.\n\nPada :\n" + Timed, [sender])
                                puy.sendMessage(to, "Server berhasil diperbarui.\n\nPada :\n" + Timed)
                                restartBot()
                              else:
                                  puy.sendMessage("Permission Denied")

                            elif cmd.startswith("about"):
                                try:
                                    arr = []
                                    Ownerz = "ub0ff92e9820f6b82a2f0b81d6758c2fb"
                                    creator = puy.getContact(Ownerz)
                                    contact = puy.getContact(puyMid)
                                    grouplist = puy.getGroupIdsJoined()
                                    contactlist = puy.getAllContactIds()
                                    blockedlist = puy.getBlockedContactIds()
                                    ret_ = " "
                                    ret_ += " Bot Name : {}".format(contact.displayName)
                                    ret_ += "\n  In Groups : {}".format(str(len(grouplist)))
                                    ret_ += "\n  Friends : {}".format(str(len(contactlist)))
                                    ret_ += "\n  Blocked Account : {}".format(str(len(blockedlist)))                                    
                                    #ret_ += "\n  [ About Selfbot ]"
                                    #ret_ += "\n  Version : Premium"
                                    #ret_ += "\n  Creator : {}".format(creator.displayName)
                                    #ret_ += "\n  Creator : @!".format(Owner)
                                    puy.sendMessage(to, str(ret_))
                                    #puy.sendMessage(to, "「 Read Text Below 」")
                                    sendMention(to, "「 About Server 」\n\nThe Beginning of this Bot Comes from PH-13, I'm just Reworked This!\n\nOf Course Special Thanks To ALLAH SWT, And the Friends Around Me!\n\n*Creator : @!", [Ownerz])
                                except Exception as e:
                                    puy.sendMessage(msg.to, str(e))
                                  
                            elif cmd.startswith("#me"):
                                contact = puy.getContact(puyMid)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                name = contact.displayName
                                puy.sendMessage(to, contentMetadata={'countryCode': 'ID', 'i-installUrl': 'line://ti/p/~ketikidmu111', 'a-packageName': 'com.spotify.music', 'linkUri': 'line://ti/p/~ketikidmu111', 'subText': 'Hei', 'a-installUrl': 'line://ti/p/~ketikidmu111', 'type': 'mt', 'previewUrl': image, 'a-linkUri': 'line://ti/p/~ketikidmu111', 'text': name, 'id': 'mt000000000a6b79f9', 'i-linkUri': 'line://ti/p/~yapuy'}, contentType=19)                                  
                                  
                            elif cmd == "me":
                                contact = puy.getContact(sender)
                                userid = "https://line.me/ti/p/~" + puy.profile.userid
                                sendMention(to, "@!", [sender])
                                #puy.sendContact(to, sender)
                                #puy.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                                puy.sendMusic(to, puy.getContact(sender).displayName, "http://dl.profile.line-cdn.net/"+puy.getContact(sender).pictureStatus, str(userid), "Khie Bot", puy.getContact(sender).displayName)
                                
                            elif cmd == "check errorlog":
                                with open('logError.txt', 'r') as er:
                                        error = er.read()
                                puy.sendMessage(to, str(error))                                          
                                
                            elif cmd == "change to self":
                                mode = "25"
                                puy.sendMessage(receiver, 'Has ben Changed to Self Mode')
                            elif cmd == "change to public":
                                mode = "26"
                                puy.sendMessage(receiver, 'Has ben Changed to Public Mode')
                                

              ## LURKING ##                      
                            elif text.lower() == 'get reader on':
                                tz = pytz.timezone("Asia/Jakarta")
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
                                if msg.to in read['readPoint']:
                                        try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                        except:
                                            pass
                                        read['readPoint'][msg.to] = msg.id
                                        read['readMember'][msg.to] = ""
                                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                        read['ROM'][msg.to] = {}
                                        with open('read.json', 'w') as fp:
                                            json.dump(read, fp, sort_keys=True, indent=4)                                                                                                                                                                                                                                                                                                                                                           
                                            #sendMention(to, "@!\n「 Getreader Diaktifkan 」\nWaktu :\n" + readTime, [sender])
                                            puy.sendMessage(to, "「 Getreader Diaktifkan 」\n\nWaktu :\n" + readTime)
                                else:
                                    try:
                                        del read['readPoint'][msg.to]
                                        del read['readMember'][msg.to]
                                        del read['readTime'][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][msg.to] = msg.id
                                    read['readMember'][msg.to] = ""
                                    read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                    read['ROM'][msg.to] = {}
                                    with open('read.json', 'w') as fp:
                                        json.dump(read, fp, sort_keys=True, indent=4)
                                        #sendMention(to, "@!\n「 Getreader Diaktifkan 」\n" + readTime, [sender])
                                        puy.sendMessage(to, "「 Getreader Diaktifkan 」\n\n" + readTime)
                            
                            elif text.lower() == 'get reader off':
                                tz = pytz.timezone("Asia/Jakarta")
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
                                if msg.to not in read['readPoint']:
                                    #sendMention(to, "「 Getreader telah dimatikan  」\n@!\nWaktu :\n" + readTime, [sender])
                                    puy.sendMessage(to, "「 Getreader telah dimatikan  」\n\nWaktu :\n" + readTime)
                                else:
                                    try:
                                        del read['readPoint'][msg.to]
                                        del read['readMember'][msg.to]
                                        del read['readTime'][msg.to]
                                    except:
                                          pass
                                    #sendMention(to, "「 Getreader telah dimatikan  」\n@!\n" + readTime, [sender])
                                    puy.sendMessage(to, "「 Getreader belum diaktifkan  」\n\n" + readTime)
        
                            elif text.lower() == 'get reader reset':
                                tz = pytz.timezone("Asia/Jakarta")
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
                                    except:
                                        pass
                                    #sendMention(to, "「 Mengulangi riwayat pembaca 」 :\n@!\n" + readTime, [sender])
                                    puy.sendMessage(to, "「 Getreader telah direset 」\n\n" + readTime)
                                else:
                                    #sendMention(to, "「 Getreader belum diaktifkan 」\n@!", [sender])
                                    puy.sendMessage(to, "「 Getreader belum diaktifkan 」\n\n" + readTime)

                            elif text.lower() == 'get reader':
                                tz = pytz.timezone("Asia/Jakarta")
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
                                        puy.sendMessage(receiver,"   「 Daftar Pembaca 」\nNone")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = puy.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '「 Daftar Pembaca 」\n\n'
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
                                        puy.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    puy.sendMessage(receiver,"*Belum diaktifkan\nKetik 「 get reader on 」 untuk mengaktifkan.")
              ## LURKING ##
              
##SETTINGS MESSAGE##
                            elif cmd.startswith('Set pesan: '):
                              if msg._from in Owner:
                                spl = msg.text.replace('Set pesan: ','')
                                if spl in [""," ","\n",None]:
                                    puy.sendMessage(msg.to, "Gagal menerapkan Messages")
                                else:
                                    wait["message"] = spl
                                    puy.sendMessage(msg.to, "Pesan Messages diterapkan menjadi :\n\n{}".format(str(spl)))
                            elif cmd.startswith('Set wlcmsg: '):
                              if msg._from in Owner:
                                spl = msg.text.replace('Set wlcmsg: ','')
                                if spl in [""," ","\n",None]:
                                    puy.sendMessage(msg.to, "Gagal menerapkan Welcome Messages")
                                else:
                                    wait["welcome"] = spl
                                    puy.sendMessage(msg.to, "Welcome Messages diterapkan menjadi :\n\n{}".format(str(spl)))
                            elif cmd.startswith('Set leave: '):
                              if msg._from in Owner:
                                spl = msg.text.replace('Set leave: ','')
                                if spl in [""," ","\n",None]:
                                    puy.sendMessage(msg.to, "Gagal menerapkan Leave Messages")
                                else:
                                    wait["leave"] = spl
                                    puy.sendMessage(msg.to, "Leave Messages diterapkan menjadi :\n\n{}".format(str(spl)))
                            elif cmd.startswith('Set respon: '):
                              if msg._from in Owner:
                                spl = msg.text.replace('Set respon: ','')
                                if spl in [""," ","\n",None]:
                                    puy.sendMessage(msg.to, "Gagal menerapkan Respon Messages")
                                else:
                                    wait["Respontag"] = spl
                                    puy.sendMessage(msg.to, "Respon Messages diterapkan menjadi :\n\n{}".format(str(spl)))
                            elif cmd.startswith('Set spam: '):
                              if msg._from in Owner:
                                spl = msg.text.replace('Set spam: ','')
                                if spl in [""," ","\n",None]:
                                    puy.sendMessage(msg.to, "Gagal menerapkan Spam")
                                else:
                                    Settings["ADITMADZSmessage1"] = spl
                                    puy.sendMessage(msg.to, "Spam Messages diterapkan menjadi :\n\n{}".format(str(spl)))
                            elif cmd.startswith('Set sider: '):
                              if msg._from in Owner:
                                spl = msg.text.replace('Set sider: ','')
                                if spl in [""," ","\n",None]:
                                    puy.sendMessage(msg.to, "Gagal menerapkan Sider Messages")
                                else:
                                    wait["mention"] = spl
                                    puy.sendMessage(msg.to, "Sider Messages diterapkan menjadi :\n\n{}".format(str(spl)))
                            elif cmd == "cek pesan":
                              if msg._from in Owner:
                                puy.sendMessage(msg.to, "Pesan Msg mu :\n\n " + str(wait["message"]) + " ")
                            elif cmd == "cek welcome":
                              if msg._from in Owner:
                                puy.sendMessage(msg.to, "Welcome Msg mu :\n\n " + str(wait["welcome"]) + " ")
                            elif cmd == "cek leave":
                              if msg._from in Owner:
                                puy.sendMessage(msg.to, "Leave Msg mu :\n\n " + str(wait["leave"]) + " ")
                            elif cmd == "cek respon":
                              if msg._from in Owner:
                                puy.sendMessage(msg.to, "Respon Msg mu :\n\n " + str(wait["Respontag"]) + " ")
                            elif cmd == "cek spam":
                              if msg._from in Owner:
                                puy.sendMessage(msg.to, "Spam Msg mu :\n\n " + str(Setmain["ADITMADZSmessage1"]) + " ")
                            elif cmd == "cek sider":
                              if msg._from in Owner:
                                puy.sendMessage(msg.to, "Sider Msg mu :\n\n " + str(wait["mention"]) + " ")
                               
                            elif cmd == "autojoin on":
                              if msg._from in Owner:
                                settings["autoJoin"] = True
                                sendMention(to, "[ Notified Auto Join ]\nBerhasil mengaktifkan Auto Join @!", [sender])
                            elif cmd == "autojoin off":
                              if msg._from in Owner:
                                settings["autoJoin"] = False
                                sendMention(to, "[ Notified Auto Join ]\nBerhasil menonaktifkan Auto Join @!", [sender])
                            elif cmd == "detectunsend on":
                              if msg._from in Owner:
                                settings["detectUnsend"] = True
                                sendMention(to, "[ Notified Detect Unsend ]\nBerhasil mengaktifkan Detect Unsend\n@!", [sender])
                            elif cmd == "detectunsend off":
                              if msg._from in Owner:
                                settings["detectUnsend"] = False
                                sendMention(to, "[ Notified Detect Unsend ]\nBerhasil menonaktifkan Detect Unsend\n@!", [sender])                                
                            elif cmd == "autoleave on":
                              if msg._from in Owner:
                                settings["autoLeave"] = True
                                sendMention(to, "[ Notified Auto Leave ]\nBerhasil mengaktifkan Auto leave @!", [sender])
                            elif cmd == "autoleave off":
                              if msg._from in Owner:
                                settings["autoLeave"] = False
                                sendMention(to, "[ Notified Auto Leave ]\nBerhasil menonaktifkan Auto leave @!", [sender])
                            elif cmd == "autoadd on":
                              if msg._from in Owner:
                                wait["autoAdd"] = True
                                puy.sendMessage(to,"Auto add diaktifkan")
                            elif cmd == "autoadd off":
                              if msg._from in Owner:
                                wait["autoAdd"] = False
                                puy.sendMessage(to,"Auto add dinonaktifkan")                                
                            elif cmd == "status":
                                try:
                                    ret_ = "\n   [ BOT STATUS ]\n"
                                    if settings["autoJoin"] == True: ret_ += "\n   [ ON ] Auto Join"
                                    else: ret_ += "\n   [ OFF ] Auto Join"
                                    if settings["autoLeave"] == True: ret_ += "\n   [ ON ] Auto Leave Room"
                                    else: ret_ += "\n   [ OFF ] Auto Leave Room"
                                    ret_ += ""
                                    sendMessageWithFooter(to, str(ret_))
                                except Exception as e:
                                    sendMessageWithFooter(to, str(e))
##SETTINGS MESSAGE##
                                
               ## RINDA SC ##                                    
                            elif cmd.startswith("bye"):
                                heij = puy.getGroupIdsJoined()
                                #G = puy.getGroup(heij)
                                #puy.sendMessage(to, "Gbye {}".format(str(G.name)))
                                puy.sendMessage(to, "Gbye")
                                #puy.getGroupIdsJoined()
                                puy.leaveGroup(to)

                            elif cmd.startswith("get wikipedia "):
                                query = cmd.replace("get wikipedia ","")
                                try:
                                    sep = msg.text.split(" ")
                                    wiki = msg.text.replace(sep[0] + " ","")
                                    wikipedia.set_lang("id")
                                    pesan=" 「Judul」 "
                                    pesan+=wikipedia.page(wiki).title
                                    pesan+="\n 「Teks」 "
                                    pesan+=wikipedia.summary(wiki, sentences=1)
                                    pesan+="\n 「Alamat url」 "+wikipedia.page(wiki).url
                                    pesan+="\n"
                                    puy.sendMessage(to, pesan)
                                except:
                                        try:
                                            pesan="Teks terlalu panjang, Klik url untuk lebih lengkap\n"
                                            pesan+=wikipedia.page(wiki).url
                                            #puy.sendMessage(to, pesan)
                                            puy.sendMessage(to, " Wikipedia Search 「 " + query + " 」  " + pesan)
                                        except Exception as e:
                                            #puy.sendMessage(to, "Wikipedia [ " + query + " ] " + str(e))
                                            puy.sendMessage(msg.to, " Wikipedia Search 「 " + query + " 」 " + str(e))
                                
                            elif cmd.startswith("searchporn "):
                                kata = cmd.replace("searchporn ", "")
                                with _session as web:
                                    try:
                                        r = web.get("https://api.redtube.com/?data=redtube.Videos.searchVideos&output=json&search={}".format(urllib.parse.quote(kata)))
                                        data = r.text
                                        data = json.loads(data)
                                        ret_ = "Porns Link\n"
                                        no = 1
                                        anu = data["videos"]
                                        if len(anu) >= 5:
                                            for s in range(5):
                                                hmm = anu[s]
                                                title = hmm['video']['title']
                                                duration = hmm['video']['duration']
                                                views = hmm['video']['views']
                                                link = hmm['video']['embed_url']
                                                ret_ += "\n\n{}. Title : {}\n    Duration : {}\n    Views : {}\n    Link : {}".format(str(no), str(title), str(duration), str(views), str(link))
                                                no += 1
                                        else:
                                            for s in anu:
                                                hmm = s
                                                title = hmm['video']['title']
                                                duration = hmm['video']['duration']
                                                views = hmm['video']['views']
                                                link = hmm['video']['embed_url']
                                                ret_ += "\n\n{}. Title : {}\n    Duration : {}\n    Views : {}\n    Link : {}".format(str(no), str(title), str(duration), str(views), str(link))
                                                no += 1
                                        puy.sendMessage(to, str(ret_))
                                    except:
                                        puy.sendMessage(to, "Porn Not Found !")                                
                                
                            elif cmd.startswith("biografi "):
                                query = cmd.replace("biografi ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("https://farzain.xyz/api/biografi.php?apikey=YcUTTUvO2xe75rxWhsqSkWkZsIeTn9&id={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = " 「 Search Biografi 」\n"
                                    for bio in data:
                                        num += 1
                                        ret_ += "\n{}. {}".format(str(num), str(bio["title"]))                                        
                                    ret_ += "\n\nExample: Biography {}|1".format(settings["keyCommand"],search)
                                    puy.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data):
                                        bio = data[num - 1]
                                        result = requests.get("https://farzain.xyz/api/biografi.php?apikey=YcUTTUvO2xe75rxWhsqSkWkZsIeTn9&id={}".format(str(search)))
                                        data = result.text
                                        data = json.loads(data)
                                        ret_ = " 「 Details Biografi 」\n"                                        
                                        ret_ += "\n    {}".format(str(bio["link"]))
                                        puy.sendImageWithURL(to, str(bio["img"]))
                                        puy.sendMessage(to, str(ret_))                                
                                
                            elif cmd.startswith("vidcall"):
                              if msg._from in Owner:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    group = puy.getGroup(to)
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        for var in range(0,50):                                         
                                            puy.acquireGroupCallRoute(to)                                            
                                            members = [ls for ls in lists]
                                            puy.inviteIntoGroupCall(to, contactIds=members)
                                        try:
                                            puy.sendMessage(to,"Ready to Vidcall in Private chat with "+puy.getContact(ls).displayName)
                                        except Exception as error:
                                            logError(error)
                                
                            elif cmd.startswith("randomlose"):
                                group = puy.getGroup(to)
                                try:
                                    members = [mem.mid for mem in group.members]
                                except:
                                    members = [mem.mid for mem in group.members]
                                message = random.choice(members)
                                sendMention(to, "「 RandomLoseMem 」\n\n• The Loser is :", [sender])
                                puy.sendContact(to, message)
                                
                            elif cmd.startswith("guessed"):
                                sendMention(to, "「 Guess 」\n\n• Getting random number 1-50", [sender])
                                time.sleep(1)
                                sendMention(to, "「 Guess 」\n\n• 30 Seconds...", [sender])
                                time.sleep(1)
                                sendMention(to, "「 Guess 」\n\n• 20 Seconds...", [sender])
                                time.sleep(1)
                                sendMention(to, "「 Guess 」\n\n• 10 Seconds...", [sender])
                                path = random.randint(0,50)
                                time.sleep(1)
                                sendMention(to, "「 Guess 」\n\n• Lucky number is : ", [sender] + str(path))
                                
                            elif cmd.startswith("infomovie "):
                                query = cmd.replace("infomovie ","")   
                                r = requests.get("https://farzain.xyz/api/film.php?id={}".format(str(query)))
                                data1 = r.text
                                data1 = json.loads(data1)
                                hasil="Imdb Result:\n"
                                hasil += "\nTitle: {}".format(str(data1["Title"]))
                                hasil += "\nYear: {}".format(str(data1["Year"]))
                                hasil += "\n Rating: {}".format(str(data1["Rated"]))
                                hasil += "\nRelease: {}".format(str(data1["Released"]))
                                hasil += "\nDuration: {}".format(str(data1["Runtime"]))
                                hasil += "\nDirector: {}".format(str(data1["Director"]))
                                hasil += "\nWritter: {}".format(str(data1["Writer"]))
                                hasil += "\nActor: {}".format(str(data1["Actors"]))
                                hasil += "\n\n{}".format(str(data1["Plot"]))
                                hasil += "\n\nAwards: {}".format(str(data1["Awards"]))
                                puy.sendImageWithURL(to,str(data1["Poster"]))
                                puy.sendMessage(to, str(hasil))                                
                                
                            elif cmd.startswith("get meme "):
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
                                puy.sendMessage(msg.to, "Search Meme 「 " + query + " 」")
                                puy.sendImageWithURL(msg.to, memes)
                                
                            elif cmd.startswith("memelists"):
                                hasil = "「 Meme list 」\n"
                                hasil += "\n  1. Distracted Boyfriend "
                                hasil += "\n  2. Two Buttons "                           
                                hasil += "\n  3. Expanding Brain "
                                hasil += "\n  4. Batman Slapping Robin "
                                hasil += "\n  5. Roll Safe Think About It "
                                hasil += "\n  6. One Does Not Simply "
                                hasil += "\n  7. Waiting Skeleton "
                                hasil += "\n  8. Blank Nut Button "
                                hasil += "\n  9. Boardroom Meeting Suggestion "
                                hasil += "\n  10. Is This A Pigeon "
                                hasil += "\n  11. Ancient Aliens "
                                hasil += "\n  12. Left Exit 12 Off Ramp "
                                hasil += "\n  13. X, X Everywhere "
                                hasil += "\n  14. The Most Interesting Man In The World "
                                hasil += "\n  15. Futurama Fry "
                                hasil += "\n  16. Inhaling Seagull "
                                hasil += "\n  17. Trump Bill Signing "
                                hasil += "\n  18. Oprah You Get A "
                                hasil += "\n  19. Y'all Got Any More Of That "
                                hasil += "\n  20. Buzz "
                                hasil += "\n\n Used : getmeme buzz*hei*puy "
                                puy.sendMessage(msg.to, str(hasil))
                  
                            elif cmd == 'memelist':
                                puy.sendMessage(to,"10 Guy = tenguy\nAfraid to Ask Andy = afraid\nAn Older Code Sir, But It Checks Out = older\nAncient Aliens Guy = aag\nAt Least You Tried = tried\nBaby Insanity Wolf = biw\nBad Luck Brian = blb\nBut That's None of My Business = kermit\nButthurt Dweller = bd\nCaptain Hindsight = ch\nComic Book Guy = cbg\nCondescending Wonka = wonka\nConfession Bear = cb\nConspiracy Keanu = keanu\nDating Site Murderer = dsm\nDo It Live! = live\nDo You Want Ants? = ants\nDoge = doge\nDrake Always On Beat = alwaysonbeat\nErmahgerd = ermg\nFirst World Problems = fwp\nForever Alone = fa\nFoul Bachelor Frog = fbf\nFuck Me, Right? = fmr\nFuturama Fry = fry\nGood Guy Greg = ggg\nHipster Barista = hipster\nI Can Has Cheezburger? = icanhas\nI Feel Like I'm Taking Crazy Pills = crazypills\nI Immediately Regret This Decision! = regret\nI Should Buy a Boat Cat = boat\nI Would Be So Happy = sohappy\nI am the Captain Now = captain\nInigo Montoya = inigo\nInsanity Wolf = iw\nIt's A Trap! = ackbar\nIt's Happening = happening\nIt's Simple, Kill the Batman = joker\nJony Ive Redesigns Things = ive\nLaughing Lizard = ll\nMatrix Morpheus = morpheus\nMilk Was a Bad Choice = badchoice\nMinor Mistake Marvin = mmm\nNothing To Do Here = jetpack\nOh, Is That What We're Going to Do Today? = red\nOne Does Not Simply Walk into Mordor = mordor\nOprah You Get a Car = oprah\nOverlay Attached Girlfriend = oag\nPepperidge Farm Remembers = remembers\nPhilosoraptor = philosoraptor\nProbably Not a Good Idea = jw\nSad Barack Obama = sad-obama\nSad Bill Clinton = sad-clinton\nSad Frog / Feels Bad Man = sadfrog\nSad George Bush = sad-bush\nSad Joe Biden = sad-biden\nSad John Boehner = sad-boehner\nSarcastic Bear = sarcasticbear\nSchrute Facts = dwight\nScumbag Brain =  sb\nScumbag Steve = ss\nSealed Fate = sf\nSee? Nobody Cares = dodgson\nShut Up and Take My Money! = money\nSo Hot Right Now = sohot\nSocially Awesome Awkward Penguin = awesome-awkward\nSocially Awesome Penguin = awesome\nSocially Awkward Awesome Penguin = awkward-awesome\nSocially Awkward Penguin = wkward\nStop Trying to Make Fetch Happen = fetch\nSuccess Kid = success\nSuper Cool Ski Instructor = ki\nThat Would Be Great = officespace\nThe Most Interesting Man in the World = interesting\nThe Rent Is Too Damn High = toohigh\nThis is Bull, Shark = bs\nWhy Not Both? = Both\nWinter is coming = winter\nX all the Y = xy\nX, X Everywhere = buzz\nXzibit Yo Dawg = yodawg\nY U NO Guy = yuno\nY'all Got Any More of Them = yallgot\nYou Should Feel Bad = bad\nYou Sit on a Throne of Lies = elf\nYou Were the Chosen One! = chosen\n\nUsage : Rinda getmeme sohot*Hello*Rin")
                  
                            elif cmd.startswith("rinda get quotes"):
                                r=requests.get("https://talaikis.com/api/quotes/random")
                                data=r.text
                                data=json.loads(data)
                                hasil = "  [ Search Random Quote ]\n\n"
                                hasil += "Genre : " +str(data["cat"])
                                hasil += "\n\n" +str(data["quote"])
                                hasil += "\n\n From : " +str(data["author"])+ " "
                                puy.sendMessage(msg.to, str(hasil))
                  
                            elif cmd.startswith("get video "):
                                try:
                                    sep = msg.text.split(" ")
                                    textToSearch = msg.text.replace(sep[0] + " ","")
                                    query = urllib.parse.quote(textToSearch)
                                    url = "https://www.youtube.com/results?search_query=" + query
                                    response = urllib.request.urlopen(url)
                                    html = response.read()
                                    soup = BeautifulSoup(html, "html.parser")
                                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                    dl=("https://www.youtube.com" + results['href'])
                                    vid = pafy.new(dl)
                                    stream = vid.streams
                                    for s in stream:
                                        vin = s.url
                                        hasil = " 「 Video Search 」\n"
                                        hasil += "\n [Judul] : {}".format(str(vid.title))
                                        hasil += "\n [Nama channel] : {}".format(str(vid.author))
                                        hasil += "\n [Durasi vidio] : " + str(vid.duration) + " Quality : " + s.quality + " "
                                        hasil += "\n [Nilai] : " + str(vid.rating)
                                        hasil += "\n [Penonton] : " + str(vid.viewcount) + "x"
                                        hasil += "\n [Published] : " + str(vid.published)
                                        hasil += "\n [Pencarian : Youtube]"
                                        hasil += "\n\n Video Below"
                                    puy.sendMessage(msg.to,hasil)
                                    puy.sendVideoWithURL(msg.to,vin)
                                    print("[YOUTUBE]MP4 Succes")
                                except Exception as e:
                                    puy.sendMessage(to, str(e))
                  
                            elif cmd.startswith("leave to"):
                                number = cmd.replace("leave to","")
                                groups = puy.getGroupIdsJoined()
                                try:
                                    group = groups[int(number)-1]
                                    G = puy.getGroup(group)
                                    try:
                                        puy.leaveGroup(G.id)
                                    except:
                                        puy.leaveGroup(G.id)
                                    puy.sendMessage(to, "Leave To Group : " + G.name)
                                except Exception as error:
                                    puy.sendMessage(to, str(error))
                  
                            elif cmd.startswith(".whois "):
                                spl = re.split(".whois ",msg.text,flags=re.IGNORECASE)
                                if spl[0] == "":
                                    msg.contentType = 13
                                    msg.text = None
                                    msg.contentMetadata = {"mid":spl[1]}
                                    puy.sendMessage(msg)                  
                  
                            elif 'Autotrans en-' in msg.text:
                              #if msg._from in admin:
                                spl = msg.text.replace('Autotrans en-','')
                                if spl == 'on':
                                    if msg.to in translateen:
                                         msgs = "Auto Translate sudah aktif"
                                    else:
                                         translateen.append(msg.to)
                                         ginfo = puy.getGroup(msg.to)
                                         msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                    puy.sendMessage(msg.to, "Aktif\n" + msgs)
                                elif spl == 'off':
                                      if msg.to in translateen:
                                           translateen.remove(msg.to)
                                           ginfo = puy.getGroup(msg.to)
                                           msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                      else:
                                           msgs = "Auto Translate Sudah Tidak Aktif"
                                      puy.sendMessage(msg.to, "Aktif\n" + msgs)
                  
                            elif cmd.startswith("img food: "):
                              #if msg._from in admin:
                                query = msg.text.replace("img food: ","")
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    for food in data:
                                        puy.sendImageWithURL(msg.to, str(food["url"]))                  
                  
                            elif cmd.startswith("setspamtag: "):
                              if wait["selfbot"] == True:
                               if msg._from in admin:
                                    proses = text.split(":")
                                    strnum = text.replace(proses[0] + ":","")
                                    num =  int(strnum)
                                    Setmain["ADITMADZSlimit"] = num
                                    puy.sendMessage(msg.to,"Jumlah Spamtag telah diterapkan menjadi <" +strnum + ">")
                  
                            elif cmd.startswith("acaratv: "):
                              #if msg._from in admin:
                                try:
                                    separate = msg.text.split(" ")
                                    channel = msg.text.replace(separate[0] + " ","")
                                    r = requests.get("https://farzain.xyz/api/premium/acaratv.php?apikey=al11241519&id="+channel)
                                    data = r.text
                                    data = json.loads(data)
                                    puy.sendMessage(msg.to, "Acara TV Di "+channel+ ":\n" + str(data["url"]))
                                except Exception as error:
                            	    pass
                                    
                            elif cmd.startswith("gimage: "):
                              #if msg._from in admin:
                                try:
                                    separate = msg.text.split(" ")
                                    keyword = msg.text.replace(separate[0] + " ","")
                                    r = requests.get("https://farzain.xyz/api/gambarg.php?id="+keyword)
                                    data = r.text
                                    data = json.loads(data)
                                    puy.sendImageWithURL(msg.to, str(data["url"]))
                                except Exception as error:
                            	    pass
                                    
                            elif cmd.startswith("fs: "):
                              #if msg._from in admin:
                                try:
                                    separate = msg.text.split(" ")
                                    nama = msg.text.replace(separate[0] + " ","")
                                    nmor = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21"]
                                    plih = random.choice(nmor)
                                    nmor2 = ["1","2","3","4","5","6","7"]
                                    plih2 = random.choice(nmor2)
                                    url = ("https://farzain.xyz//api//premium//fansign//fs%20("+plih+").php?text="+nama+"&apikey=al11241519","http://farzain.xyz/api/premium/fansign/cos/cos%20("+plih2+").php?text="+nama+"&apikey=al11241519")
                                    plihurl = random.choice(url)
                                    puy.sendImageWithURL(msg.to, plihurl)
                                except Exception as error:
                                    pass                                    
                  
                            elif cmd.startswith("Film "):
                                proses = msg.text.split("*")
                                get = msg.text.replace(proses[0] + ":","")
                                getfilm = get.split()
                                title = getfilm[0]
                                tahun = getfilm[1]
                                r = requests.get('http://www.omdbapi.com/?t='+title+'&y='+tahun+'&plot=full&apikey=4bdd1d70')
                                start = time.time()
                                data=r.text
                                data=json.loads(data)
                                hasil = "Informasi \n" +str(data["Title"])+ " (" +str(data["Year"])+ ")"
                                hasil += "\n\n " +str(data["Plot"])
                                hasil += "\n\n Director : " +str(data["Director"])
                                hasil += "\n Actors   : " +str(data["Actors"])
                                hasil += "\n Release : " +str(data["Released"])
                                hasil += "\n Genre    : " +str(data["Genre"])
                                hasil += "\n Runtime   : " +str(data["Runtime"])
                                path = data["Poster"]
                                puy.sendImageWithURL(msg.to, str(path))
                                puy.sendMessage(msg.to,hasil)                  
                  
                            elif cmd == "grouplist":
                                groups = puy.getGroupIdsJoined()
                                ret_ = "   [ Group List ]"
                                no = 0
                                for gid in groups:
                                    group = puy.getGroup(gid)
                                    no += 1
                                    ret_ += "\n{}. {} = {} Members".format(str(no), str(group.name), str(len(group.members)))
                                ret_ += "\n   [ Total {} Groups ]".format(str(len(groups)))
                                puy.sendMessage(to, str(ret_))
                  
                            elif cmd == "invite:gcreator":
                                if msg.toType == 2:                
                                       ginfo = puy.getGroup(receiver)
                                       try:
                                           gcmid = ginfo.creator.mid
                                       except:
                                           gcmid = "Error"
                                       if settings["lang"] == "JP":
                                           puy.inviteIntoGroup(receiver,[gcmid])
                                           puy.sendMessage(receiver, "Invited")
                                       else:
                                           puy.inviteIntoGroup(receiver,[gcmid])
                                           puy.sendMessage(receiver, "Pembuat grupnya sudah ada di Grup.")                  
                  
                            elif cmd.startswith("get memberlist to"):
                              #if msg._from in Owner:
                                number = cmd.replace("get memberlist to","")
                                groups = puy.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number)-1]
                                    G = puy.getGroup(group)
                                    no = 0
                                    ret_ = " 「 Member List 」\n"
                                    for mem in G.members:
                                        no += 1
                                        ret_ += "\n " + str(no) + ". " + mem.displayName
                                    puy.sendMessage(to,"Member in Group : \n"+ str(G.name) + "\n\n" + ret_ + "\n\nTotal ada %i Members" % len(G.members))
                                except: 
                                    pass
                  
                            elif cmd.startswith("groupinfo "):
                              #if msg._from in Owner:
                                number = cmd.replace("groupinfo ","")
                                groups = puy.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number)-1]
                                    G = puy.getGroup(group)
                                    path = "http://dl.profile.line-cdn.net/" + G.pictureStatus
                                    try:
                                        gCreator = G.creator.displayName
                                    except:
                                        gCreator = "Tidak ditemukan"
                                    if G.invitee is None:
                                        gPending = "0"
                                    else:
                                        gPending = str(len(G.invitee))
                                    if G.preventedJoinByTicket == True:
                                        gQr = "Tertutup"
                                        gTicket = "Tidak ada"
                                    else:
                                        gQr = "Terbuka"
                                        gTicket = "https://line.me/R/ti/g/{}".format(str(puy.reissueGroupTicket(G.id)))
                                    timeCreated = []
                                    timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                    ret_ += " 「 Group Info 」 \n"
                                    ret_ += "\n Nama Group : {}".format(G.name)
                                    ret_ += "\n ID Group : \n{}".format(G.id)
                                    ret_ += "\n Pembuat Grup : {}".format(gCreator)
                                    ret_ += "\n Waktu Dibuat : {}".format(str(timeCreated))
                                    ret_ += "\n Jumlah Member : {}".format(str(len(G.members)))
                                    ret_ += "\n Jumlah Pending : {}".format(gPending)
                                    ret_ += "\n Group Qr : {}".format(gQr)
                                    ret_ += "\n Group Ticket : {}".format(gTicket)
                                    ret_ += "\n\n 「 Kontak Pembuat dibawah 」"
                                    puy.sendImageWithURL(to, path)
                                    puy.sendMessage(to, str(ret_))
                                    puy.sendContact(to, G.creator.mid)
                                except:
                                    pass
                  
                            elif cmd.startswith("tutupqr to"):
                              if msg._from in Owner:
                                number = cmd.replace("tutupqr to","")
                                groups = puy.getGroupIdsJoined()
                                try:
                                    group = groups[int(number)-1]
                                    G = puy.getGroup(group)
                                    try:
                                        G.preventedJoinByTicket = True
                                        puy.updateGroup(G)
                                    except:
                                        G.preventedJoinByTicket = True
                                        puy.updateGroup(G)
                                    puy.sendMessage(to, " 「 Close Qr 」 InGroup : " + G.name)
                                except Exception as error:
                                    puy.sendMessage(to, str(error))
                  
                            elif cmd.startswith("bukaqr to"):
                              if msg._from in Owner:
                                number = cmd.replace("bukaqr to","")
                                groups = puy.getGroupIdsJoined()
                                try:
                                    group = groups[int(number)-1]
                                    G = puy.getGroup(group)
                                    try:
                                        G.preventedJoinByTicket = False
                                        puy.updateGroup(G)
                                        gurl = "https://line.me/R/ti/g/{}".format(str(puy.reissueGroupTicket(G.id)))
                                    except:
                                        G.preventedJoinByTicket = False
                                        puy.updateGroup(G)
                                        gurl = "https://line.me/R/ti/g/{}".format(str(puy.reissueGroupTicket(G.id)))
                                    puy.sendMessage(to, " 「 Close Qr 」 InGroup : " + G.name + "\n  Url : " + gurl)
                                except Exception as error:
                                    puy.sendMessage(to, str(error))
                  
                            elif cmd.startswith("mention to"):
                              #if msg._from in Owner:
                                number = cmd.replace("mention to","")
                                groups = puy.getGroupIdsJoined()
                                try:
                                    group = groups[int(number)-1]
                                    G = puy.getGroup(group)
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
                                    puy.sendMessage(to, "Send Mention To Group : " + G.name)
                                except Exception as error:
                                    puy.sendMessage(to, str(error))
                  
                            elif cmd.startswith("crash to"):
                              if msg._from in Owner:
                                number = cmd.replace("crash to","")
                                groups = puy.getGroupIdsJoined()
                                try:
                                    group = groups[int(number)-1]
                                    G = puy.getGroup(group)
                                    try:
                                        puy.sendContact(group, "uc7d319b7d2d38c35ef2b808e3a2aeed9',")
                                    except:
                                        puy.sendContact(group, "uc7d319b7d2d38c35ef2b808e3a2aeed9',")
                                    puy.sendMessage(to, "Send Crash To Group : " + G.name)
                                except Exception as error:
                                    puy.sendMessage(to, str(error))
                  
                            elif cmd.startswith("github "):
                                query = cmd.replace("github ","")
                                b = urllib.parse.quote(query)
                                #puy.sendMessage(to,"「 Searching 」\n" "Type: GitHub Search\nStatus: Processing...")
                                puy.sendMessage(to, " " + a + "\nhttps://github.com/search?utf8=✓&q="+query)
                                
                            elif cmd.startswith("playstore "):
                                query = cmd.replace("playstore ","")
                                puy.sendMessage(to, "「 Title : "+query+"」\nhttps://play.google.com/store/search?q="+query)
                  
                            elif cmd.startswith("twitter "):
                                query = cmd.replace("twitter ","")
                                b = urllib.parse.quote(query)
                                #puy.sendMessage(to,"「 Searching 」\n" "Type:Search Info\nStatus: Processing")
                                puy.sendMessage(to, "https://www.twitter.com/"+query)
                                #puy.sendMessage(to,"「 Searching 」\n" "Type:Search Info\nStatus: Success")
                  
                            elif cmd.startswith("smule "):
                                query = cmd.replace("smule ","")
                                b = urllib.parse.quote(query)
                                #puy.sendMessage(to,"Searching to id smule..")
                                puy.sendMessage(to, "Nama : "+b+"\nId smule : http://smule.com/"+query)                  
                  
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
                                   ret_ += " => Link : {}".format(str(url))
                                   #puy.sendMessage(to, str(ret_))
                                   puy.sendMessage(msg.to, "「 Question is *" + query + "* 」  " + str(ret_))
                  
                            elif cmd.startswith("fc "):
                                sep = msg.text.split(" ")
                                anu = msg.text.replace(sep[0] + " "," ")                
                                with requests.session() as web:
                                    web.headers["user-agent"] = random.choice(settings["userAgent"])
                                    r = web.get("https://farzain.xyz/api/premium/fs.php?apikey=apikey_saintsbot&id={}".format(urllib.parse.quote(anu)))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["status"] == "success":
                                        ret_ = data["url"]
                                        puy.sendImageWithURL(msg.to,ret_)
                                    else:
                                        puy.sendMessage(msg.to, "Error")                  
                  
                            elif cmd.startswith("sendfile"):
                              #if sender in admin:
                                sep = text.split(" ")
                                file = text.replace(sep[0] + " ","")
             #                  sendMention(to,"[ Send File ]\nType: Send Files\nI Am Send Your Files @!Please Wait",[sender])
                                time.sleep(1)
                                puy.sendFile(to,file)
                  
                            elif cmd.startswith("get creepypasta"):
                                r=requests.get("http://hipsterjesus.com/api")
                                data=r.text
                                data=json.loads(data)
                                hasil = " 「 Creepypasta 」\n\n" 
                                hasil += str(data["text"])
                                puy.sendMessage(msg.to, str(hasil))
                  
                            elif cmd.startswith("announcetext "):
                               Text = cmd.replace("announcetext ","")
                               Link = "http://line.me/ti/p/uv8Cqx77tB"
                               Logo = "http://dl.profile.line-cdn.net/" + puy.getGroup(to).pictureStatus
                               stype = 1
                               announce = ChatRoomAnnouncementContents(displayFields=5,text=Text,link=Link,thumbnail=Logo)
                               puy.createChatRoomAnnouncement(to,stype,announce)
                               sendMention(receiver, sender, "? Create Announce ?\nType : Lock\n•", "\nSuccess Create Announce Lock "+str(Text)+" in Group : "+str(puy.getGroup(to).name))                  
                  
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
                                    #puy.sendMessage(to, str(ret_))
                                    puy.sendMessage(to, " 「 Timezone " + query + " 」  " + str(ret_))
                                except Exception as error:
                                    puy.sendMessage(to, str(error))
                  
                            elif cmd.startswith("get image "):
                                try:
                                    query = cmd.replace("get image ","")
                                    #search = cmd.replace("puy image ","")
                                    r = requests.get("https://xeonwz.herokuapp.com/images/google.api?q={}".format(query))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["content"] != []:
                                        items = data["content"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        puy.sendMessage(to, " Search Image 「 " + query + " 」  ")
                                        puy.sendImageWithURL(to, str(path))
                                except Exception as error:
                                     logError(error)
                                     var= traceback.print_tb(error.__traceback__)
                                     puy.sendMessage(to,str(var))
                  
                            elif cmd.startswith("get 1cak"):
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
                                #puy.sendImageWithURL(msg.to, str(image))
                                puy.sendMessage(msg.to, str(hasil))
                                
                            elif cmd.startswith("get devianart "):
                                query = cmd.replace("get devianart ","")
                                try:
                                    search = cmd.replace("get devianart ","")
                                    r = requests.get("https://xeonwz.herokuapp.com/images/deviantart.api?q={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["content"] != []:
                                        items = data["content"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        puy.sendMessage(msg.to, "Search Image 「 " + query + " 」")
                                        puy.sendImageWithURL(to, str(path))                                        
                                except Exception as error:
                                     logError(error)
                                     var= traceback.print_tb(error.__traceback__)
                                     puy.sendMessage(to,str(var))
                                
                            elif cmd.startswith("hasil dari "):
                                query = cmd.replace("hasil dari ","")
                                puy1 = requests.get("https://www.calcatraz.com/calculator/api?c={}".format(urllib.parse.quote(query)))
                                data=puy1.text
                                data=json.loads(data)
                                puy.sendMessage(msg.to, query + " = " + str(data))
                                
                            elif cmd.startswith("cekig:"):
                              #if msg._from in admin:
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://farzain.xyz/api/ig_profile.php?apikey=arTdnVbJkW1EuzDNQrIxQDvHtJIDcQ&id={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "[ Profile Instagram ]"
                                        ret_ += "\n Nama : {}".format(str(data["info"]["full_name"]))
                                        ret_ += "\n Username : {}".format(str(data["info"]["username"]))
                                        ret_ += "\n Bio : {}".format(str(data["info"]["bio"]))
                                        ret_ += "\n URL Bio : {}".format(str(data["info"]["url_bio"]))
                                        ret_ += "\n Pengikut : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\n Diikuti : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\n Total Post : {}".format(str(data["count"]["post"]))
                                        ret_ += "\n[ https://www.instagram.com/{} ]".format(search)
                                        path = data["info"]["profile_pict"]
                                        puy.sendMessage(to, str(ret_))
                                        puy.sendImageWithURL(to, str(path))
                                except Exception as e:
                                    puy.sendMessage(msg.to, str(e))                                
                                
                            elif cmd.startswith("get motivation"):
                                puy1 = requests.get("https://talaikis.com/api/quotes/random")
                                data=puy1.text
                                data=json.loads(data)
                                puy.sendMessage(to, " 「 Motivation 」 \n" + str(data["quote"]))
                                
                            elif cmd.startswith("bitcoin"):
                                puy1 = requests.get("https://xeonwz.herokuapp.com/bitcoin.api")
                                data=puy1.text
                                data=json.loads(data)
                                hasilnya = "「 Bitcoin 」\n" 
                                hasilnya += "\n Price : " +str(data["btc"])
                                hasilnya += "\n Expensive : " +str(data["high"])
                                hasilnya += "\n Cheap : " +str(data["low"])
                                puy.sendMessage(msg.to, str(hasilnya))
                                
                            elif 'Simi ' in msg.text:
                              #if msg._from in admin:
                                spl = msg.text.replace('Simi ','')
                                if spl == 'on':
                                    if msg.to in simisimi:
                                         msgs = "Simi-simi sudah aktif"
                                    else:
                                         simisimi.append(msg.to)
                                         ginfo = puy.getGroup(msg.to)
                                         msgs = "Simi-simi Diaktifkan\nDi Group : " +str(ginfo.name)
                                    puy.sendMessage(msg.to, "Diaktifkan\n" + msgs)
                                elif spl == 'off':
                                      if msg.to in simisimi:
                                           simisimi.remove(msg.to)
                                           ginfo = puy.getGroup(msg.to)
                                           msgs = "Simi-simi Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                      else:
                                           msgs = "Simi-simi Sudah Tidak Aktif"
                                      puy.sendMessage(msg.to, "Dinonaktifkan\n" + msgs)                                
                                
                            elif cmd.startswith("urban "):
                                sep = cmd.split(" ")
                                judul = cmd.replace(sep[0] + " ","")
                                url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                                with requests.session() as s:
                                    s.headers["User-Agent"] = random.choice(settings["userAgent"])
                                    puy1 = s.get(url)
                                    data = puy1.text
                                    data = json.loads(data)
                                    y = "Result Urban :"
                                    y += "\nTags: "+ data["tags"][0]
                                    y += ","+ data["tags"][1]
                                    y += ","+ data["tags"][2]
                                    y += ","+ data["tags"][3]
                                    y += ","+ data["tags"][4]
                                    y += ","+ data["tags"][5]
                                    y += ","+ data["tags"][6]
                                    y += ","+ data["tags"][7]
                                    y += "\n\n~Author : "+str(data["list"][0]["author"])
                                    y += "\n~Word : "+str(data["list"][0]["word"])
                                    y += "\n~Link : "+str(data["list"][0]["permalink"])
                                    y += "\n~Definition : "+str(data["list"][0]["definition"])
                                    y += "\n~Example : "+str(data["list"][0]["example"])
                                    puy.sendMessage(to, str(y))                                
                                
                            elif cmd.startswith("instagram "):
                                try:
                                    search = cmd.replace("instagram ","")
                                    r=requests.get("http://rahandiapi.herokuapp.com/instainfo/"+search+"?key=betakey")
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_="    [ Instagram Result ]\n"
                                        ret_ += "\nName: {}".format(str(data["result"]["name"]))
                                        ret_ += "\nUsername: {}".format(str(data["result"]["username"]))                 
                                        ret_ += "\n\n {}".format(str(data["result"]["bio"]))            
                                        ret_ += "\n\nFollowers: {}".format(str(data["result"]["follower"]))
                                        ret_ += "\nFollowing: {}".format(str(data["result"]["following"]))                                 
                                        ret_ += "\nTotal Post: {}".format(str(data["result"]["mediacount"]))
                                        ret_ += "\nhttps://www.instagram.com/{}".format(search)
                                        path = data["result"]["url"]
                                        puy.sendImageWithURL(to, str(path))
                                        puy.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                                    var= traceback.print_tb(error.__traceback__)
                                    puy.sendMessage(to,str(var))                                
                                
                            elif cmd.startswith("get suggestion to "):
                                query = cmd.replace("get suggestion to ","")
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
                                puy.sendMessage(msg.to, " This is Suggestion to 「 " + query + " 」  " + str(ret_))
                                
                            elif cmd.startswith("get gif "):
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
                                        ret_ = "\n\nget gif {}*number".format(str(search))
                                    puy.sendMessage(to,hasil+ret_)
                                elif len(count) == 2:
                                    try:
                                        num = int(count[1])
                                        b = data["results"][num - 1]
                                        c = str(b["id"])
                                        hasil = " Gif ID : "+str(c)
                                        hasil += ""
                                        puy.sendMessage(msg.to,hasil)
                                        dl = str(b["media"][0]["loopedmp4"]["url"])
                                        puy.sendVideoWithURL(msg.to,dl)
                                    except Exception as e:
                                        puy.sendMessage(to," "+str(e))

                            elif cmd.startswith("fmylife"):
                              if msg._from in Owner:
                                result = requests.get("http://www.fmylife.com/random")
                                data = BeautifulSoup(result.content, 'html5lib')                                                                             
                                for sam in data.findAll('figure', attrs={'class':'text-center visible-xs'}):                                        
                                    path = str(sam.find('img')['data-src'])                                    
                                puy.sendImageWithURL(to, str(path))                                        
                                        
                            elif cmd.startswith("news today"):
                                try:
                                    api_key = "a53cb61cee4d4c518b69473893dba73b"
                                    r = _session.get("https://newsapi.org/v2/top-headlines?country=id&apiKey={}".format(str(api_key)))
                                    data = r.text
                                    data = json.loads(data)
                                    ret_ = "Top News\n"
                                    no = 1
                                    anu = data["articles"]
                                    if len(anu) >= 5:
                                        for s in range(5):
                                            syit = anu[s]
                                            sumber = syit['source']['name']
                                            author = syit['author']
                                            judul = syit['title']
                                            url = syit['url']
                                            ret_ += "\n\n{}. Title : {}\n    Sumber : {}\n    Penulis : {}\n    Link : {}".format(str(no), str(judul), str(sumber), str(author), str(url))
                                            no += 1
                                    else:
                                        for s in anu:
                                            syit = s
                                            sumber = syit['source']['name']
                                            author = syit['author']
                                            judul = syit['title']
                                            url = syit['url']
                                            ret_ += "\n\n{}. Judul : {}\n    Sumber : {}\n    Penulis : {}\n    Link : {}".format(str(no), str(judul), str(sumber), str(author), str(url))
                                            no += 1
                                    puy.sendMessage(to, str(ret_))
                                except:
                                    puy.sendMessage(to, "Top news Not Found !")                                        
                                        
                            elif cmd.startswith("get lockscreen "):
                              #if msg._from in Owner:
                                query = cmd.replace("get lockscreen ","")
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
                                    ret_ += "\n\nMore : get lockscreen {}*(number) to Details.".format(str(search))
                                    puy.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        sam = data["result"][num - 1]
                                        result = requests.get("https://api.eater.tech/wallp/{}".format(str(search)))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            puy.sendImageWithURL(to, str(sam["link"]))
                                
                            elif cmd.startswith("searchcharacter "):
                                kata = cmd.replace("searchcharacter ", "")
                                with _session as web:
                                    try:
                                        r = web.get("http://ariapi.herokuapp.com/api/anime/search?q={}".format(urllib.parse.quote(kata)))
                                        data = r.text
                                        data = json.loads(data)
                                        anu = data["result"]["character"][0]
                                        title = anu['title']
                                        link = anu['link']
                                        ret_ = "     「 Character 」"
                                        ret_ += "\n\nTitle : {}\nLink : {}".format(str(title), str(link))
                                        puy.sendMessage(to, str(ret_))
                                    except:
                                        puy.sendMessage(to, "No result found")                                
                                
                            elif cmd.startswith("square"):
                                number = cmd.replace("square","")
                                squares = puy.getJoinedSquares().squares
                                ret_ = "「 Square 」\n"
                                try:
                                    square = squares[int(number)-1]
                                    path = "http://dl.profile.line-cdn.net/" + square.profileImageObsHash
                                    ret_ += "\n1. Name : {}".format(str(square.name))
                                    ret_ += "\n2. Description: {}".format(str(square.desc))
                                    ret_ += "\n3. ID Square : {}".format(str(square.mid))
                                    ret_ += "\n4. Link : {}".format(str(square.invitationURL))
                                    puy.sendImageWithURL(to, path)
                                    puy.sendMessage(to, str(ret_))
                                except Exception as error:
                                    puy.sendMessage(to, str(error))
                                
                            elif cmd.startswith("bc: "):
                              if msg._from in Owner:
                                sep = text.split(" ")
                                pesan = text.replace(sep[0] + " ","")
                                saya = puy.getGroupIdsJoined()
                                for group in saya:
                                   puy.sendMessage(group,"" + str(pesan))

                            elif cmd.startswith("#cuaca: "):
                                separate = text.split(" ")
                                location = text.replace(separate[0] + " ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = random.choice(settings["userAgent"])
                                    r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                    data = r.text
                                    data = json.loads(data)
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    if "result" not in data:
                                        ret_ = "「Status Cuaca」"
                                        ret_ += "\n┃🇮🇩┃ Lokasi : " + data[0].replace("Temperatur di kota ","")
                                        ret_ += "\n┃🇮🇩┃ Suhu : " + data[1].replace("Suhu : ","") + " C"
                                        ret_ += "\n┃🇮🇩┃ Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                        ret_ += "\n┃🇮🇩┃ Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                        ret_ += "\n┃🇮🇩┃ Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                        ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                        ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    puy.sendMessage(msg.to, str(ret_))                                                                                                                                                             
                            elif cmd.startswith("#igpost"):
                                separate = msg.text.split(" ")
                                user = msg.text.replace(separate[0] + " ","")
                                profile = "https://www.instagram.com/" + user
                                with requests.session() as x:
                                    x.headers['user-agent'] = random.choice(settings['userAgent'])
                                    end_cursor = ''
                                    for count in range(1, 999):
                                        print('PAGE: ', count)
                                        r = x.get(profile, params={'max_id': end_cursor})
                        
                                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                                        j    = json.loads(data)
                        
                                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                                            if node['is_video']:
                                                page = 'https://www.instagram.com/p/' + node['code']
                                                r = x.get(page)
                                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                                print(url)
                                                puy.sendVideoWithURL(msg.to,url)
                                            else:
                                                print (node['display_src'])
                                                puy.sendImageWithURL(msg.to,node['display_src'])
                                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)                                                                                  
                            elif cmd.startswith("lirik "):
                              #if msg._from in admin:
                                try:
                                    sep = msg.text.split(" ")
                                    query = msg.text.replace(sep[0] + " ","")
                                    cond = query.split(":")
                                    search = cond[0]
                                    api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                    data = api.text
                                    data = json.loads(data)
                                    if len(cond) == 1:
                                        num = 0
                                        ret_ = "  [ List Lirik ]  "
                                        for lyric in data["results"]:
                                            num += 1
                                            ret_ += "\n {}. {}".format(str(num), str(lyric["single"]))
                                        ret_ += "\n [ Total {} Lagu ] ".format(str(len(data["results"])))
                                        ret_ += "\n\nUntuk Melihat Details Musik, Silahkan Ketik \nâ˜¬ã€Œ {}Lirik {}:nomor ".format(str(),str(search))
                                        ret_ += "\ {}Playlist {}:nomor ".format(str(),str(search))
                                        puy.sendMessage(msg.to, str(ret_))
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
                                            puy.sendMessage(msg.to, str(lyric))
                                except Exception as error:
                                    pass
                                         
                            elif cmd.startswith("#lokasi "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "╔═══[ ʟᴏᴄᴀᴛɪᴏɴ sᴛᴀᴛᴜs ]"
                                        ret_ += "\n╠❂➣ ʟᴏᴄᴀᴛɪᴏɴ : " + data[0]
                                        ret_ += "\n╠❂➣  ɢᴏᴏɢʟᴇ ᴍᴀᴘs : " + link
                                        ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                        puy.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                                         
                            elif cmd.startswith("get imageart "):
                                try:                                   
                                    search = cmd.replace("get imageart ","")
                                    puy1 = requests.get("https://xeonwz.herokuapp.com/images/deviantart.api?q={}".format(search))
                                    data = puy1.text
                                    data = json.loads(data)
                                    if data["content"] != []:
                                        items = data["content"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        puy.sendMessage(to,"Image in #%s From #%s." %(str(a),str(b)))
                                        puy.sendImageWithURL(to, str(path))
                                        log.info("Art #%s from #%s." %(str(a),str(b)))                                    
                                except Exception as error:
                                    logError(error)
                                    traceback.print_tb(error.__traceback__)
               ## RINDA SC ##
#=======================================================  ADMIN  ===============================================================#
                            elif ("+admin " in msg.text):
                              if wait["selfbot"] == True:
                                if msg._from in admin:
                                   key = eval(msg.contentMetadata["MENTION"])
                                   key["MENTIONEES"][0]["M"]
                                   targets = []
                                   for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                   for target in targets:
                                           try:
                                               admin.append(target)
                                               puy.sendMessage(msg.to,"Berhasil menambahkan admin")
                                           except:
                                               pass

                            elif ("-admin " in msg.text):
                                if msg._from in admin:
                                   key = eval(msg.contentMetadata["MENTION"])
                                   key["MENTIONEES"][0]["M"]
                                   targets = []
                                   for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                   for target in targets:
                                       #if target not in puy:
                                           try:
                                               admin.remove(target)
                                               puy.sendMessage(msg.to,"Berhasil menghapus admin")
                                           except:
                                               pass

                            elif cmd == "+admin:on" or text.lower() == 'addadmin:on':
                                if msg._from in admin:
                                    wait["addadmin"] = True
                                    puy.sendMessage(msg.to,"Sent a Contact")

                            elif cmd == "-admin:on" or text.lower() == 'admin:remove':
                                if msg._from in admin:
                                    wait["delladmin"] = True
                                    puy.sendMessage(msg.to,"Sent a Contact")

                            elif cmd == "refresh admin" or text.lower() == 'refreshhh':
                                if msg._from in admin:
                                    wait["addadmin"] = False
                                    wait["delladmin"] = False
                                    puy.sendMessage(msg.to,"Admin has been Refreshed")

                            elif cmd == "admin contact" or text.lower() == 'virüssz':
                                if msg._from in admin:
                                    ma = ""
                                    for i in admin:
                                        ma = puy.getContact(i)
                                        puy.sendMessage(msg.to, None, contentMetadata={'mid': 'sezer'}, contentType=13)
#=======================================================  ADMIN FINISHED ===============================================================#               
## GET TOKEN ##
                        if text.lower() == 'get token win10':
                          try:
                              aa = puy.getContact(sender).displayName
                              ab = puy.getGroup(msg.to).name
                              ac = puy.getContact(sender).mid
                              req = requests.get('https://api.eater.pw/WIN10')
                              a = req.text
                              b = json.loads(a)
                              tknop= codecs.open("tkn.json","r","utf-8")
                              tkn = json.load(tknop)
                              tkn['{}'.format(msg._from)] = []
                              tkn['{}'.format(msg._from)].append({
                              'qr': b['result'][0]['linkqr'],
                              'tkn': b['result'][0]['linktkn']
                                  })
                              qrz = b['result'][0]['linkqr']
                              puy.sendMessage(to, '「 WIN 10 」\n'+aa+', Buka Link dibawah dan Tekan Login\n\nYour ID : '+ac+'\nInGroup : '+ab+'\n{}'.format(qrz))
                              #dap.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                              with open('tkn.json', 'w') as outfile:
                                  json.dump(tkn, outfile)
                              tknop= codecs.open("tkn.json","r","utf-8")
                              tkn = json.load(tknop)
                              a = tkn['{}'.format(msg._from)][0]['tkn']
                              req = requests.get(url = '{}'.format(a))
                              b = req.text
                              #sendMention(to, '- TIPE TOKEN : WIN10\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                              #puy.sendMessage(to, '「 WIN 10 」\n\nUntuk : '+aa+'\nDari Grup : '+ab+'\nMid Kamu : '+ac+'.')
                              puy.sendMessage(receiver, '{}'.format(b))
                          except Exception as e:
                                 puy.sendMessage(to, str(e))
                             
                        if text.lower() == 'get token chrome':
                          try:
                              aa = puy.getContact(sender).displayName
                              ab = puy.getGroup(msg.to).name
                              ac = puy.getContact(sender).mid
                              req = requests.get('https://api.eater.pw/CHROMEOS')
                              a = req.text
                              b = json.loads(a)
                              tknop= codecs.open("tkn.json","r","utf-8")
                              tkn = json.load(tknop)
                              tkn['{}'.format(msg._from)] = []
                              tkn['{}'.format(msg._from)].append({
                              'qr': b['result'][0]['linkqr'],
                              'tkn': b['result'][0]['linktkn']
                                  })
                              qrz = b['result'][0]['linkqr']
                              puy.sendMessage(to, '「 CHROMEOS 」\n'+aa+', Buka Link dibawah dan Tekan Login\n\nYour ID : '+ac+'\nInGroup : '+ab+'\n{}'.format(qrz))
                              with open('tkn.json', 'w') as outfile:
                                  json.dump(tkn, outfile)
                              tknop= codecs.open("tkn.json","r","utf-8")
                              tkn = json.load(tknop)
                              a = tkn['{}'.format(msg._from)][0]['tkn']
                              req = requests.get(url = '{}'.format(a))
                              b = req.text
                              #sendMention(to, '- TIPE TOKEN : WIN10\n- For : '+aa+'\n\n- TOKEN : \n{}'.format(b), [sender])
                              #puy.sendMessage(receiver,'「 CHROME 」\n\nUntuk : '+aa+'\nDari Grup : '+ab+'\nMid Kamu : '+ac+'.')
                              puy.sendMessage(receiver, '{}'.format(b))
                          except Exception as e:
                                 puy.sendMessage(to, str(e))
                               
                        if text.lower() == 'get token iospad':
                          try:
                              aa = puy.getContact(sender).displayName
                              ab = puy.getGroup(msg.to).name
                              ac = puy.getContact(sender).mid
                              req = requests.get('https://api.eater.pw/IOSIPAD')
                              a = req.text
                              b = json.loads(a)
                              tknop= codecs.open("tkn.json","r","utf-8")
                              tkn = json.load(tknop)
                              tkn['{}'.format(msg._from)] = []
                              tkn['{}'.format(msg._from)].append({
                              'qr': b['result'][0]['linkqr'],
                              'tkn': b['result'][0]['linktkn']
                                  })
                              qrz = b['result'][0]['linkqr']
                              puy.sendMessage(to, '「 IOSIPAD 」\n'+aa+', Buka Link dibawah dan Tekan Login\n\nYour ID : '+ac+'\nInGroup : '+ab+'\n{}'.format(qrz))
                              #dap.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                              with open('tkn.json', 'w') as outfile:
                                  json.dump(tkn, outfile)
                              tknop= codecs.open("tkn.json","r","utf-8")
                              tkn = json.load(tknop)
                              a = tkn['{}'.format(msg._from)][0]['tkn']
                              req = requests.get(url = '{}'.format(a))
                              b = req.text
                              #sendMention(to, '- TIPE TOKEN : WIN10\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                              #puy.sendMessage(receiver,'「 IOSPAD 」\n\nUntuk : '+aa+'\nDari Grup : '+ab+'\nMid Kamu : '+ac+'\n\n-「 TOKEN 」  : \n{}\n\n*「 From BotEater / Edited By PUY 」'.format(b))
                              puy.sendMessage(receiver, '{}'.format(b))
                          except Exception as e:
                                 puy.sendMessage(to, str(e))
                                
                        if text.lower() == 'get token desktopwin':
                          try:
                              aa = puy.getContact(sender).displayName
                              ab = puy.getGroup(msg.to).name
                              ac = puy.getContact(sender).mid
                              req = requests.get('https://api.eater.pw/DESKTOPWIN')
                              a = req.text
                              b = json.loads(a)
                              tknop= codecs.open("tkn.json","r","utf-8")
                              tkn = json.load(tknop)
                              tkn['{}'.format(msg._from)] = []
                              tkn['{}'.format(msg._from)].append({
                              'qr': b['result'][0]['linkqr'],
                              'tkn': b['result'][0]['linktkn']
                                  })
                              qrz = b['result'][0]['linkqr']
                              puy.sendMessage(to, '「 DESKTOPWIN 」\n'+aa+', Buka Link dibawah dan Tekan Login\n\nYour ID : '+ac+'\nInGroup : '+ab+'\n{}'.format(qrz))
                              #dap.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                              with open('tkn.json', 'w') as outfile:
                                  json.dump(tkn, outfile)
                              tknop= codecs.open("tkn.json","r","utf-8")
                              tkn = json.load(tknop)
                              a = tkn['{}'.format(msg._from)][0]['tkn']
                              req = requests.get(url = '{}'.format(a))
                              b = req.text
                              #sendMention(to, '- TIPE TOKEN : WIN10\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                              #puy.sendMessage(receiver,'「 DESKTOPWIN 」\n\nUntuk : '+aa+'\nDari Grup : '+ab+'\nMid Kamu : '+ac+'\n\n-「 TOKEN 」  : \n{}\n\n*「 From BotEater / Edited By PUY 」'.format(b))
                              puy.sendMessage(receiver, '{}'.format(b))
                          except Exception as e:
                                 puy.sendMessage(to, str(e))
                            
                        if text.lower() == 'get token desktopmac':
                          try:
                              aa = puy.getContact(sender).displayName
                              ab = puy.getGroup(msg.to).name
                              ac = puy.getContact(sender).mid
                              req = requests.get('https://api.eater.pw/DESKTOPMAC')
                              a = req.text
                              b = json.loads(a)
                              tknop= codecs.open("tkn.json","r","utf-8")
                              tkn = json.load(tknop)
                              tkn['{}'.format(msg._from)] = []
                              tkn['{}'.format(msg._from)].append({
                              'qr': b['result'][0]['linkqr'],
                              'tkn': b['result'][0]['linktkn']
                                  })
                              qrz = b['result'][0]['linkqr']
                              puy.sendMessage(to, '「 DESKTOPMAC 」\n'+aa+', Buka Link dibawah dan Tekan Login\n\nYour ID : '+ac+'\nInGroup : '+ab+'\n{}'.format(qrz))
                              #dap.sendMessage(msg.to, 'Buka Link dibawah dan Tekan Login\n{}'.format(qrz))
                              with open('tkn.json', 'w') as outfile:
                                  json.dump(tkn, outfile)
                              tknop= codecs.open("tkn.json","r","utf-8")
                              tkn = json.load(tknop)
                              a = tkn['{}'.format(msg._from)][0]['tkn']
                              req = requests.get(url = '{}'.format(a))
                              b = req.text
                              #sendMention(to, '- TIPE TOKEN : WIN10\n- For : @!\n\n- TOKEN : \n{}'.format(b), [sender])
                              #dap.sendMessage(to,'「 CHROMEOS 」\nUntuk: '+aa+'\nFrom Group: '+ab+'\nMid User: '+ac+'\n\n- TOKEN : \n{}'.format(b))
                              #puy.sendMessage(receiver,'「 DESKTOPMAC 」\n\nUntuk : '+aa+'\nDari Grup : '+ab+'\nMid Kamu : '+ac+'\n\n-「 TOKEN 」  : \n{}\n\n*「 From BotEater / Edited By PUY 」'.format(b))
                              puy.sendMessage(receiver, '{}'.format(b))
                          except Exception as e:
                                 puy.sendMessage(to, str(e))                              
## GET TOKEN ##
                                
        ## PREFIX ##          
                        elif cmd.startswith("setprefix:"):
                          if msg._from in Owner:
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            if " " in key:
                                puy.sendMessage(to, "\nTanpa spasi.\n")
                            else:
                                settings["keyCommand"] = str(key).lower()
                                sendMessageWithFooter(to, "text [ {} ]".format(str(key).lower()))        
                        if text.lower() == "myprefix":
                            puy.sendMessage(to, "Prefix diterapkan menjadi [ {} ]\n".format(str(settings["keyCommand"])))
                        elif text.lower() == "prefix":
                            puy.sendMessage(to, "Prefix saat ini [ {} ]".format(str(settings["keyCommand"])))
                        elif text.lower() == "prefix on":
                          if msg._from in Owner:
                            settings["prefix"] = True
                            puy.sendMessage(to, "[ Notified Prefix Key ]\nBerhasil mengaktifkan Prefix")
                        elif text.lower() == "prefix off":
                          if msg._from in Owner:
                            settings["prefix"] = False
                            puy.sendMessage(to, "[ Notified Prefix Key ]\nBerhasil menonaktifkan Prefix")
        ## PREFIX ##                            
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
                                    group = puy.findGroupByTicket(ticket_id)
                                    puy.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    puy.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))                                             
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if puyMid in mention["M"]:
                                    if settings["autoRespon"] == True:
                                        sendMention(sender, " @!, don't tag", [sender])
                                    break
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
                    #if text =='mute':
                        if sender != puy.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    #if settings["autoRead"] == True:
                        #puy.sendChatChecked(to, msg_id)
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)                    
## INI KALAU MAU DI HAPUS SILAHKAN ## 
        if op.type == 25 and 26:
            try:
                print ("[ 26 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 2:
                    if msg.toType == 0:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
                            if msg.text:
                                if msg.text.lower().lstrip().rstrip() in wbanlist:
                                    if msg.text not in puyMid:
                                        try:
                                            puy.kickoutFromGroup(msg.to,[sender])
                                        except Exception as e:
                                            print(e)
                            if receiver in temp_flood:
                                if temp_flood[receiver]["expire"] == True:
                                   if cmd == "open":
                                        temp_flood[receiver]["expire"] = False
                                        temp_flood[receiver]["time"] = time.time()
                                        puy.sendMessage(to,"Bot Actived")
                                   return
                                elif time.time() - temp_flood[receiver]["time"] <= 5:
                                    temp_flood[receiver]["flood"] += 1
                                    if temp_flood[receiver]["flood"] >= 20:
                                        temp_flood[receiver]["flood"] = 0
                                        temp_flood[receiver]["expire"] = True
                                        ret_ = "I will be off for 30 seconds, type open to re-enable"
                                        userid = "https://line.me/ti/p/~" + puy.profile.userid
                                        puy.sendFooter(to, "Flood Detect !\n"+str(ret_), str(userid), "http://dl.profile.line-cdn.net/"+puy.getContact(puyMid).pictureStatus, puy.getContact(puyMid).displayName)
                                else:
                                     temp_flood[receiver]["flood"] = 0
                                temp_flood[receiver]["time"] = time.time()
                            else:
                                temp_flood[receiver] = {
    	                            "time": time.time(),
    	                            "flood": 0,
    	                            "expire": False
                                }
                                                                     
                    elif msg.contentType == 16:
                        if settings["checkPost"] == True:
                            try:
                                ret_ = "\n  [ Details Post ]  "
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = puy.getContact(sender)
                                    auth = "\n  Author : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n  Author : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n  URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n  Object URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n  Object URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n  Object URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n  Object URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "text" in msg.contentMetadata:
                                    text = "\n  the contents of writing : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n"
                                puy.sendMessage(to, str(ret_))
                            except:
                                puy.sendMessage(to, "\nInvalid post\n")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                            
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
        ops = puyPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                puyBot(op)
                puyPoll.setRevision(op.revision)
    except Exception as error:
        logError(error)
        
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
