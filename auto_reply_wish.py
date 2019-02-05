import itchat
import re

# msg = {'MsgId': '857022760643954', 'FromUserName': '@3d8e9b650d61f7fe4d20e212664a3d8b22efbc63ad0b47d88d76e939fe67', 'ToUserName': '@3d8e9b650d61f7fe4d2e3800e212664a3d8bbc63ad0b47d88d76e939fe67', 'MsgType': 1, 'Content': '我', 'Status': 3, 'ImgStatus': 1, 'CreateTime': 1549164836, 'VoiceLength': 0, 'PlayLength': 0, 'FileName': '', 'FileSize': '', 'MediaId': '', 'Url': '', 'AppMsgType': 0, 'StatusNotifyCode': 0, 'StatusNotifyUserName': '', 'RecommendInfo': {'UserName': '', 'NickName': '', 'QQNum': 0, 'Province': '', 'City': '', 'Content': '', 'Signature': '', 'Alias': '', 'Scene': 0, 'VerifyFlag': 0, 'AttrStatus': 0, 'Sex': 0, 'Ticket': '', 'OpCode': 0}, 'ForwardFlag': 0, 'AppInfo': {'AppID': '', 'Type': 0}, 'HasProductId': 0, 'Ticket': '', 'ImgHeight': 0, 'ImgWidth': 0, 'SubMsgType': 0, 'NewMsgId': 8570227606436702954, 'OriContent': '', 'EncryFileName': '', 'User': <User: {'MemberList': <ContactList: []>, 'UserName': '@3d8e9b650d61f7fe4d200e212664a3d8b22efbc63ad0b47d88d76e939fe67', 'City': '', 'DisplayName': '', 'PYQuanPin': '', 'RemarkPYInitial': '', 'Province': '', 'KeyWord': '', 'RemarkName': '', 'PYInitial': '', 'EncryChatRoomId': '', 'Alias': '', 'Signature': '富士山下钟无艳 人来人往喜帖街', 'NickName': 'Akat💯', 'RemarkPYQuanPin': '', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=407606596&username=@3d8e9b650d61f7fe4d2e0e212664a3d8b22efb7d88d76e939fe67&skey=@crypt_66146f3f_1e91c386a46a32ee49d9b59c78961', 'UniFriend': 0, 'Sex': 1, 'AppAccountFlag': 0, 'VerifyFlag': 0, 'ChatRoomId': 0, 'HideInputBarFlag': 0, 'AttrStatus': 0, 'SnsFlag': 129, 'MemberCount': 0, 'OwnerUin': 0, 'ContactFlag': 0, 'Uin': 1785286379, 'StarFriend': 0, 'Statues': 0, 'WebWxPluginSwitch': 0, 'HeadImgFlag': 1}>, 'Type': 'Text', 'Text': '我'}

REG_PATTERN = re.compile('.*(快乐|祝福|春节|新年|幸福|祝愿|吉祥|猪年|健康|财源|万事|平安)+.*')

def totalWish(nick):
    return nick+'，您的祝福我收到啦，谢谢您叻。\n值此新春佳节，我也祝您新年快乐，万事如意！🎉🎉🎊🎊'

def chatrun():

    @itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
    def text_reply(msg):
        msg_sender = msg['FromUserName']
        content = msg['Content']
        text = msg['Text']
        nick = msg['User']['RemarkName'] or msg['User']['NickName']

        if checkIfWish(text):
            return totalWish(nick)

    itchat.auto_login(enableCmdQR=2, hotReload=True)
    itchat.run(debug=True)

def checkIfWish(text):
    res = re.match(REG_PATTERN, text )
    if res:
        return True
    else:
        return False

if __name__ == '__main__':
    chatrun()
