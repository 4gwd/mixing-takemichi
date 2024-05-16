import telebot
import random
import time

API_KEY = '6885093503:AAFr2jlB_67uAZJsiBq0vLyL3_dr09K85b0'

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message,f'''𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐑𝐚𝐧𝐝𝐨𝐦𝐢𝐳𝐞𝐝 𝐂𝐨𝐦𝐛𝐨 𝐁𝐨𝐭 🫶🏻

𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐅𝐢𝐥𝐞 𝐅𝐨𝐫 𝐌𝐢𝐱𝐢𝐧𝐠

𝐃𝐞𝐯 𝐁𝐨𝐓 𝐁𝐲 ⇾ 𝐓𝐀𝐊𝐄𝐌𝐈𝐂𝐇𝐈 ~ @Q_2_M''')

@bot.message_handler(content_types=['document'])
def handle_document(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        text = downloaded_file.decode('utf-8')
        cards = text.split('\n')
        
        bot.send_message(message.chat.id, "𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭, 𝐈'𝐦 𝐌𝐢𝐱𝐢𝐧𝐠 𝐂𝐨𝐦𝐛𝐨 𝐍𝐨𝐰...")
        
        time.sleep(5)
        
    
        random.shuffle(cards)
        
        with open('𝐃𝐎𝐍𝐄_𝐌𝐢𝐱𝐢𝐧𝐠_𝐁𝐲_𝐓𝐀𝐊𝐄𝐌𝐈𝐂𝐇𝐈.txt', 'w') as new_file:
            new_file.write('\n'.join(cards))
        
        with open('𝐃𝐎𝐍𝐄_𝐌𝐢𝐱𝐢𝐧𝐠_𝐁𝐲_𝐓𝐀𝐊𝐄𝐌𝐈𝐂𝐇𝐈.txt', 'rb') as mixed_file:
            bot.send_document(message.chat.id, mixed_file)
    
    except Exception as e:
        bot.reply_to(message, f'حدث خطأ: {str(e)}')

print('𝐓𝐡𝐞 𝐁𝐨𝐭 𝐈𝐬 𝐖𝐨𝐫𝐤𝐢𝐧𝐠 𝐍𝐨𝐰')
bot.polling()
