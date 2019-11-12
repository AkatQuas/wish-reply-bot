import itchat

def listFriend():
  itchat.login(enableCmdQR=2)
  flist = itchat.get_friends(update=True)
  print(flist[0])
  print(flist[0]['MemberList'])

  itchat.run(debug=True)

if __name__ == "__main__":
    listFriend()