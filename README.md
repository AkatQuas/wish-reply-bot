# Wish Reply Bot

2019年猪年，过年微信自动发送祝福和回复祝福的小机器人🤖️。

## 说明

请谨慎使用，封号什么的咱不知道。

鉴于图片/表情包这类信息的分析成本太高，且准确度无法保证。当前只支持文本消息的处理。

使用前有时间的话建议先看看代码。

1. 挨（群）个（发）祝福：[auto_send_wish](auto_send_wish.py)

1. 秒回祝福：[auto_reply_wish](auto_reply_wish.py)，秒回的祝福文本简化，显得更加自然。

底层机器人来源为 [itchat](https://itchat.readthedocs.io/zh/latest/)。

## 使用体验

先跑一回群发功能，然后上人工来进行后续处理，不是很多人会秒回的，所以你来得及的。

等过了时间点，开着秒回功能，然后就可以去安心做别的事情了。

如果你是一个达人，坐着都能收到很多祝福，却又不是那么积极的主动回复，就跑秒回的功能吧。（很羡慕，我酸了 🍋。

祝福语的自动拼凑在`wish_txt.py`中的`randomWish`中实现，因为加了emoji，使得祝福变得活泼了点。祝福语文案其实很普通，不喜欢祝福语的话，可以在[这里](wish_txt.py)自行替换哦。

## 使用

```bash
git clone git@github.com:AkatQuas/wish-reply-bot.git

cd  wish-reply-bot

pip3 install -r requirements.txt
```

## 运行

给好友挨个单独发送祝福。

```bash
python3 auto_send_wish.py
```

针对好友的祝福，进行秒回。

```bash
python3 auto_reply_wish.py
```

## 效果

![](screenshot.png)

## 🐷大家春节快乐！
