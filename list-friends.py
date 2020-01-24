import itchat


def listFriend():
    itchat.login(enableCmdQR=2)
    flist = itchat.get_friends(update=True)
    for f in flist:
        print(
            '名称 "%s"，备注 "%s", DisplayName "%s", ReamrkName "%s"' %
            (f['NickName'], f['Alias'], f['DisplayName'], f['RemarkName'])
        )

    itchat.run(debug=True)


if __name__ == "__main__":
    listFriend()
