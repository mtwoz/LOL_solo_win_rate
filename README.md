# LOL_solo_win_rate

### 环境：python3.6（支持[wxpy](https://github.com/youfou/wxpy)）

### 库：[wxpy](https://github.com/youfou/wxpy)、[numpy](https://github.com/numpy/numpy)、[pandas](https://github.com/pandas-dev/pandas)、[requests](https://github.com/psf/requests)

### 说明：

此项目是一个结合爬虫和微信机器人的小项目。

先从[opgg](op.gg)爬到数据，保存到本地，再创建一个简单的微信机器人完成自动回复。

### 用法：

```bash
python wechat_bot.py
```

收到如下格式消息：

R + 英雄名1 + 英雄名2

例如：

R annie ahri

会自动回复这英雄1在各个位置上对位英雄2的胜率

