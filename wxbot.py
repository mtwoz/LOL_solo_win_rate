from wxpy import *

bot = Bot()
embed()

fa = bot.friends().search('K哥')[0]


@bot.register()
def rate():
    if bot.messages[len(bot.messages-1)].text == 'rate':
        fa.send('the rate is 50.00')

embed()
