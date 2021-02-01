# LOL_solo_win_rate

### 环境：python3.6（支持[wxpy](https://github.com/youfou/wxpy)）

### 库：[wxpy](https://github.com/youfou/wxpy)、[numpy](https://github.com/numpy/numpy)、[pandas](https://github.com/pandas-dev/pandas)、[requests](https://github.com/psf/requests)

### 说明：

此项目是一个结合爬虫和微信机器人的小项目。

R：先从[opgg](op.gg)爬到数据，保存到本地，再创建一个简单的微信机器人完成自动回复。

O：收到请求自动从[opgg](op.gg)上获取最新数据，在通过微信机器人完成自动回复。

### 用法：

```bash
python wechat_bot.py
```

收到如下格式消息：

> 暂时只支持英文消息，具体单词见下表。

1. R + 英雄名1 + 英雄名2

   例如：

   R annie ahri

   会自动回复英雄1在各个位置上对位英雄2的胜率

   **该数据来自本地保存的opgg数据 (1.30)，并非最新数据**

2. O + 英雄名1 + 英雄名2 + 位置

   例如：

   O aatrox camille top

   会自动回复英雄1在指定位置上对位英雄2的胜率
   
   **该数据来自opgg，为最新数据**



### 中英文对应：

#### 位置：

| 中文 | English |
| ---- | ------- |
| 上   | top     |
| 野   | jungle  |
| 中   | mid     |
| 下   | bottom  |
| 辅   | support |



#### 英雄：

| 中文                  | English      |
| --------------------- | ------------ |
| 暗裔剑魔/亚托克斯     | aatrox       |
| 九尾妖狐/阿狸         | ahri         |
| 离群之刺/阿卡丽       | akali        |
| 牛头酋长/阿利斯塔     | alistar      |
| 殇之木乃伊/阿木木     | amumu        |
| 冰晶凤凰/艾尼维亚     | anivia       |
| 黑暗之女/安妮         | annie        |
| 残月之肃/厄斐琉斯     | aphelios     |
| 寒冰射手/艾希         | ashe         |
| 铸星龙王/索尔         | aurelionsol  |
| 沙漠皇帝/阿兹尔       | azir         |
| 星界游神/巴德         | bard         |
| 蒸汽机器人/布里茨     | blitzcrank   |
| 复仇焰魂/布兰迪       | brand        |
| 弗雷尔卓德之心        | braum        |
| 皮城女警/凯特琳       | caitlyn      |
| 青钢影/卡密尔         | camille      |
| 魔蛇之拥/卡西奥佩娅   | cassiopeia   |
| 虚空恐惧/科加斯       | chogath      |
| 英勇投弹手/库奇       | corki        |
| 诺克萨斯之手/德莱厄斯 | darius       |
| 皎月女神/黛安娜       | diana        |
| 祖安狂人/蒙多         | drmundo      |
| 荣耀行刑官/德莱文     | draven       |
| 时间刺客/艾克         | ekko         |
| 蜘蛛女皇/伊莉丝       | elise        |
| 痛苦之拥/伊芙琳       | evelynn      |
| 探险家/伊泽瑞尔       | ezreal       |
| 远古恐惧/费德提克     | fiddlesticks |
| 无双剑姬/菲奥娜       | fiora        |
| 潮汐海灵/菲兹         | fizz         |
| 正义巨像/加里奥       | galio        |
| 海洋之灾/普朗克       | gangplank    |
| 德玛西亚之力/盖伦     | garen        |
| 迷失之牙/纳尔         | gnar         |
| 酒桶/古拉加斯         | gragas       |
| 法外狂徒/格雷福斯     | graves       |
| 战争之影/赫卡里姆     | hecarim      |
| 大发明家/黑默丁格     | heimerdinger |
| 海兽祭司/俄洛伊       | illaoi       |
| 刀锋舞者/艾瑞莉娅     | irelia       |
| 翠神/艾翁             | ivern        |
| 风暴之怒/迦娜         | janna        |
| 德玛西亚皇子/嘉文四世 | jarvaniv     |
| 武器大师/贾克斯       | jax          |
| 未来守护者/杰斯       | jayce        |
| 戏命师/烬             | jhin         |
| 暴走萝莉/金克斯       | jinx         |
| 虚空之女/卡莎         | kaisa        |
| 复仇之矛/卡利斯塔     | kalista      |
| 天启者/卡尔玛         | karma        |
| 死亡颂唱者/卡尔萨斯   | karthus      |
| 虚空行者/卡萨丁       | kassadin     |
| 不祥之刃/卡特琳娜     | katarina     |
| 正义天使/凯尔         | kayle        |
| 影流之镰/凯隐         | kayn         |
| 狂暴之心/凯南         | kennen       |
| 虚空掠夺者/卡兹克     | khazix       |
| 永猎双子/千珏         | kindred      |
| 暴怒骑士/克烈         | kled         |
| 深渊巨口/克格莫       | kogmaw       |
| 诡术妖姬/乐芙兰       | leblanc      |
| 盲僧/李青             | leesin       |
| 曙光女神/蕾欧娜       | leona        |
| 含羞蓓蕾/莉莉娅       | lillia       |
| 冰霜女巫/丽桑卓       | lissandra    |
| 圣枪游侠/卢锡安       | lucian       |
| 仙灵女巫/露露         | lulu         |
| 光辉女郎/拉克斯       | lux          |
| 熔岩巨兽/墨菲特       | malphite     |
| 虚空先知/玛尔扎哈     | malzahar     |
| 扭曲树精/茂凯         | maokai       |
| 无极剑圣/易大师       | masteryi     |
| 赏金猎人/厄运小姐     | missfortune  |
| 铁铠冥魂/莫德凯撒     | mordekaiser  |
| 堕落天使/莫甘娜       | morgana      |
| 唤潮鲛姬/娜美         | nami         |
| 沙漠死神/内瑟斯       | nasus        |
| 深海泰坦/诺提勒斯     | nautilus     |
| 万花通灵/妮蔻         | neeko        |
| 狂野女猎手/奈德丽     | nidalee      |
| 永恒梦魇/魔腾         | nocturne     |
| 雪原双子/努努         | nunu         |
| 狂战士/奥拉夫         | olaf         |
| 发条魔灵/奥莉安娜     | orianna      |
| 山隐之焰/奥恩         | ornn         |
| 不屈之枪/潘森         | pantheon     |
| 圣锤之毅/波比         | poppy        |
| 血港鬼影/派克         | pyke         |
| 元素女皇/*琪亚娜*     | qiyana       |
| 德玛西亚之翼/奎因     | quinn        |
| 幻翎/洛               | rakan        |
| 披甲龙龟/拉莫斯       | rammus       |
| 虚空遁地兽/雷克塞     | reksai       |
| 镕铁少女/芮尔         | rell         |
| 荒漠屠夫/雷克顿       | renekton     |
| 傲之追猎者/雷恩加尔   | rengar       |
| 放逐之刃/瑞文         | riven        |
| 机械公敌/兰博         | rumble       |
| 符文法师/瑞兹         | ryze         |
| 沙漠玫瑰/莎弥拉       | samira       |
| 北地之怒/瑟庄妮       | sejuani      |
| 涤魂圣枪/赛娜         | senna        |
| 星籁歌姬/萨勒芬妮     | seraphine    |
| 腕豪/瑟提             | sett         |
| 恶魔小丑/萨科         | shaco        |
| 暮光之眼/慎           | shen         |
| 龙血武姬/希瓦娜       | shyvana      |
| 炼金术士/辛吉德       | singed       |
| 亡灵战神/赛恩         | sion         |
| 战争女神/希维尔       | sivir        |
| 水晶先锋/斯卡纳       | skarner      |
| 琴瑟仙女/娑娜         | sona         |
| 众星之子/索拉卡       | soraka       |
| 诺克萨斯统领/斯维因   | swain        |
| 解脱者/塞拉斯         | sylas        |
| 暗黑元首/辛德拉       | syndra       |
| 河流之王/塔姆         | tahmkench    |
| 岩雀/塔莉垭           | taliyah      |
| 刀锋之影/泰隆         | talon        |
| 瓦洛兰之盾/塔里克     | taric        |
| 迅捷斥候/提莫         | teemo        |
| 魂锁典狱长/锤石       | thresh       |
| 麦林炮手/崔斯塔娜     | tristana     |
| 巨魔之王/特朗德尔     | trundle      |
| 蛮族之王/泰达米尔     | tryndamere   |
| 卡牌大师/崔斯特       | twistedfate  |
| 瘟疫之源/图奇         | twitch       |
| 兽灵行者/乌迪尔       | udyr         |
| 无畏战车/厄加特       | urgot        |
| 惩戒之箭/韦鲁斯       | varus        |
| 暗夜猎手/薇恩         | vayne        |
| 邪恶小法师/维迦       | veigar       |
| 虚空之眼/维克兹       | velkoz       |
| 皮城执法官/蔚         | vi           |
| 破败之王/佛耶戈       | viego        |
| 机械先驱/维克托       | viktor       |
| 猩红收割者/弗拉基米尔 | vladimir     |
| 不灭狂雷/沃利贝尔     | volibear     |
| 祖安怒兽/*沃里克*     | warwick      |
| 齐天大圣/悟空         | wukong       |
| 逆羽/霞               | xayah        |
| 远古巫灵/泽拉斯       | xerath       |
| 德邦总管/赵信         | xinzhao      |
| 疾风剑豪/亚索         | yasuo        |
| 封魔剑魂/永恩         | yone         |
| 牧魂人/约里克         | yorick       |
| 魔法猫咪/悠米         | yuumi        |
| 生化魔人/扎克         | zac          |
| 影流之主/劫           | zed          |
| 爆破鬼才/吉格斯       | ziggs        |
| 时光守护者/基兰       | zilean       |
| 暮光星灵/佐伊         | zoe          |
| 荆棘之兴/婕拉         | zyra         |

