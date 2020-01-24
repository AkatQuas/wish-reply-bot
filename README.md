# Wish Reply Bot

2020年鼠年，微信自动发送祝福和回复祝福的小机器人🤖️。

## 说明

请谨慎使用，可能存在封号危险。

鉴于图片/表情包这类信息的分析成本太高，且准确度无法保证。当前只支持文本消息的处理。

使用前有时间的话建议先看看代码。

1. 挨（群）个（发）祝福：[auto_send_wish](auto_send_wish.py)

1. 秒回祝福：[auto_reply_wish](auto_reply_wish.py)，秒回的祝福文本简化，显得更加自然。

底层机器人来源为 [itchat](https://itchat.readthedocs.io/zh/latest/)。

## 使用体验

先跑一回群发功能，然后上人工来进行后续处理，不是很多人会秒回的，所以你来得及的。

等过了时间点，开着秒回功能，然后就可以去安心做别的事情了。

如果你是一个社交达人，坐着都能收到很多祝福，却又不是那么积极的主动回复，就执行秒回的功能吧。

祝福语的自动拼凑在`wish_txt.py`中的`randomWish`中实现，因为加了emoji，使得祝福变得活泼了点。祝福语文案很普通，如有需要，可以在[这里](wish_txt.py)自行替换哦。

## 使用

```bash
git clone git@github.com:AkatQuas/wish-reply-bot.git

cd  wish-reply-bot

pip3 install -r requirements.txt
```

## 运行

查看当前好友列表

```bash
python3 list-friends.py
```

给好友挨个单独发送祝福。

为了方便调试和隐私问题，建议引入该模块，然后进行传参调用，示例如下：

```python
import auto_send_wish

def main():
    auto_send_wish.sendWish(send=True, me='你的名字')

if __name__ == "__main__":
    main()
```

针对好友的祝福，进行秒回。

```bash
python3 auto_reply_wish.py
```

## 效果

![](screenshot.png)

## 大家春节快乐！
