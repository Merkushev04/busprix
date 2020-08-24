import telepot

token = '1212716658:AAFMEBth1fyC-miiafHV8rSIRwNaMgMAGEE'
my_id = -315330767
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(-315330767, text, parse_mode="Markdown")