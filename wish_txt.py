import random
import datetime

EMOJIES = ['🍻', '🎊', '🎉', '🎁', '🎈', '㊗️']


def currentPhase():
    luna_phase = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
    year = datetime.datetime.now().year
    return luna_phase[(year - 2020) % 12]


CURRENT_PHASE = currentPhase()

TEXT_WISHES = [
    "一声问候，打开新年气象；一杯美酒，斟满富贵美满；一束鲜花，绽放温馨美丽；一句快乐，带来无限欢笑；一道祝福，情谊就在其中。新春佳节，祝您快乐！",
    "已是吉言满天飞，新年再争俏。此信不争先，只把祝福报。待到烟花绚烂时，阖家齐欢笑。祝$Y$年吉祥，万事如意。",
    "以感谢为圆心，以真诚为半径，送给您一个圆圆的祝福，让爱您的人更爱您，您爱的人更懂您！祝福您和亲人和和美美，祝福您的父母健康幸福！",
    "吟诵思念的诗；高唱赞美的曲；敲响新年的钟；传出祝福的讯息。去年的时光已经远去，珍贵的情谊还在延续，一起展望美好的新年，祝新年快乐！",
    "$Y$年春节拜年早，乐乐呵呵开心年，平平安安吉祥年，团团圆圆幸福年，红红火火好运年，健健康康如意年，财源滚滚发财年。祝新年快乐，幸福无边！",
    "真挚的祝愿您：家庭顺治，生活康熙，人品雍正，事业乾隆，万事嘉庆，前途道光，财富咸丰，内外同治，千秋光绪，万众宣统！愿新春佳节快乐！",
    "阵阵炮响，开启$Y$年的吉祥；闪闪烟花，带来新年的欢畅；红红对联，辉映幸福的光芒；声声笑语，凝聚团圆的渴望；句句祝福，传递情谊的桥梁：新年来到，愿您一切都吉祥！",
    "钟声是我的问候，歌声是我的祝福，雪花是我的贺卡，美酒是我的飞吻，清风是我的拥抱，快乐是我的礼物！统统都送给您，祝您春节快乐！",
    "钟声响了，快乐在蔓延；鞭炮响了，吉祥在萦绕；礼花放了，美好在绽放；饺子熟了，福气在盈门；心儿醉了，心花在怒放；祝福发了，情谊在流淌：祝您春节快乐，心想事成，鸿运当头，万事如意！",
    "新年来到说恭喜，恭喜恭喜恭喜您。财源滚滚闯万里，鸿运当头不停息。健康快乐好福气，合家欢乐幸福年。事事顺利发大财，新年更是旺到底！新年快乐！",
    "新年来临百花香，一条信息带六香。一香送您摇钱树，二香送您贵人扶，三香送您工作好，四香送您没烦恼，五香送您钱满箱，六香送您永安康！祝春节快乐！",
    "新年礼花绽放，温馨祝福悠长：笑容荡漾脸上，好运罩在身上；平安走在路上，幸福印在心上；事业握在手上，祝福连在线上；开心幸福至上，春节快乐无上！",
    "新年临近百花香，一条信息带六香，一香送您摇钱树，二香送您贵人扶，三香送您工作好，四香送您没烦恼，五香送您钱满箱，六香送您永安康祝春节快乐！",
    "新年新开端，首选是春节。立志好人缘，天天露笑脸。一定要有钱，归隐山水间。健康常相伴，饮食加锻炼。好运在$Y$年，快乐过春节。祝：春节快乐！",
    "新年的钟声终于响起，节日的思念藏在心底，美好的春节，祝福送给您。祝愿您在新的一年里心想事成，好运连连，财源滚滚，快乐依然！",
    "也许联系有点少，思念却不曾更改您我友情依然在，千山万水难阻碍新年到，旧貌换新颜，不管居家还是出门在外，都愿您快乐安泰，过得幸福精彩！",
    "一到过春节，二目盼团圆，三更难入眠，四海亲朋念，五洲同挂牵，六合共祝愿，七色彩灯悬，八方红春联，九州喜相连，十分幸福甜。新年共祝团圆。",
    "一点一滴中把回忆积攒，一分一秒中把想念温暖，一举一动中把关怀传递，一言一行中把祝福播撒。亲爱的朋友，春节到了，愿您合家团圆，幸福安康。",
    "新年佳节到，拜年要赶早，好运跟您跑，吉祥围您绕，财源进腰包，心想事就成，春节齐欢笑！我的祝福如此早，请您一定要收到！",
    "新年将至，美妙的钟声又要敲响，让它敲响您新年的幸运之门，带给您一整年的健康平安、幸福快乐、如意吉祥。提前祝您新年快乐！",
    "新年将至红梅俏，雪中梅花分外娇。春联带来新期盼，爆竹声声喜庆传。家家户户都团圆，高高兴兴吃年饭。今年工作顺心意，来年生活更美满。好运随着钟声到，欢欢喜喜过大年。祝春节快乐！",
    "新年伊始，愿您乘着和煦的春风，朝着灿烂的明天，马不停蹄，快马加鞭！请伸出爱的手，接受我春节的祝福，让幸福绽放出灿烂的花朵！",
    "新年伊始是春节，万象更新又一年，制定人生新目标，努力奋斗创佳绩，春节，愿您告别过去的懒散，拥抱明日的辉煌，努力进取，开创幸福新生活，春节快乐！",
    "新年已来到，向您问个好；开心无烦恼，好运跟着跑；家人共团聚，天伦乐逍遥；朋友相扶持，心情不寂辽；事业风水顺，金银撑荷包。好运从天降生活步步高！",
    "又是一年新春到，新春祝福不可少；送您一片青青草，愿您人生永不老；送您一只吉祥号，愿您来年步步高；送您一声新年好，愿您好运时时扰。新春快乐！",
    "缘份是长长久久的相聚，朋友是生生世世的牵挂。新年佳节到，我用真真切切的心意，送您圆圆满满的祝福：愿您事业八面圆通，爱情花好月圆，亲朋团团圆圆，生活玉润珠圆，好运源源不断。新年快乐！",
    "愿美丽陪您散步，愿健康陪您用餐，愿幸福陪您休息，愿快乐陪您聊天，愿平安陪您工作，愿开心陪您休闲。愿我的祝福陪您迎接新的一年，预祝春节快乐！",
    "新年又要来到，忘掉忧愁烦恼；世间纷纷扰扰，心态健康重要；早上吃好吃饱，晚上洗脸洗脚；闲时弄弄花草，喝到适量就好；爱是快乐小鸟，保您青春不老。",
    "新年钟声飘扬，祝福闪亮登场；财运亨通绵长，事业顺利辉煌；好运永伴身旁，甜蜜充实心房；万事如意吉祥，合家团圆安康；$Y$年业绩猛长，获得领导赞扬！",
    "新年钟声响，金$Y$气宇昂，呈瑞送吉祥，人人体健康，个个工作爽，家家财源旺，户户粮满仓，处处安无恙，天天心情畅。",
    "祝您财源滚滚，身体棒棒，爱情甜甜，好运连连。",
    "祝您春节快乐，前程似锦，吉星高照，财运亨通，合家欢乐，飞黄腾达，福如东海，寿比南山！酒越久越醇，朋友相交越久越真；水越流越清，世间沧桑越流越淡。祝新年快乐，时时好心情！",
    "祝您新的一年，日子顺一点，幸福多一点，钞票厚一点，爱情甜一点，最后还要记一点，和我联系紧一点。新年大吉。",
]


def randomWish():
    txt_idx = random.randrange(0, len(TEXT_WISHES))
    emo_idx = random.randrange(0, len(EMOJIES))
    return TEXT_WISHES[txt_idx].replace('$Y$', CURRENT_PHASE)+(EMOJIES[emo_idx] * 2)


if __name__ == "__main__":
    print('当前年份生肖 "%s" \n' % currentPhase())
    print('---- 随机祝福语：')
    for i in range(0, 10):
        print('')
        print(randomWish())

    print('\n---- END of 随机祝福语：')
