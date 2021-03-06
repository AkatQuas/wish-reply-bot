import itchat
import time
import re
from wish_txt import randomWish

# fri_example = {'MemberList': <ContactList: []>, 'Uin': 0, 'UserName': '@7b2aecac35f3a242127aea293369', 'NickName': '孙**', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=684094795&username=@7b2aecaa24e4182127aea293369&skey=@crypt_66146f3f_f864ea8bb809ed78cd9adeda0da', 'ContactFlag': 3, 'MemberCount': 0, 'RemarkName': '孙**', 'HideInputBarFlag': 0, 'Sex': 1, 'Signature': '悟.....', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'S', 'PYQuanPin': 'syung', 'RemarkPYInitial': 'SYP', 'RemarkPYQuanPin': 'syuepg', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 2147715109, 'Province': '', 'City': '', 'Alias': '', 'SnsFlag': 49, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': 'a38', 'EncryChatRoomId': '', 'IsOwner': 0}


def totalWish(nick, me):
    str = "亲爱的{}：您好，值此新春佳节，{}在这里给您敬送新春祝福：\n{}"
    return str.format(nick, me,  randomWish())


def sendWish(send=False, me='我'):
    itchat.auto_login(enableCmdQR=2)
    flist = itchat.get_friends(update=True)
    i = 0
    for fri in flist:
        nick = fri['RemarkName'] or fri['NickName']
        username = fri['UserName']
        total = totalWish(nick, me)
        if send:
            itchat.send(total, toUserName=username)
        else:
            print(total)

        i += 1
        if i % 3 == 1:
            time.sleep(1.15)
        elif i % 3 == 2:
            time.sleep(1.55)
        else:
            time.sleep(1.25)

    itchat.run(debug=True)


if __name__ == '__main__':
    sendWish()
