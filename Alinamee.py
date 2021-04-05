import telebot
 
bot = telebot.TeleBot('1786625589:AAG7jBRLOM-ZGuetz04hRJILkrnvQ4E_Z3o');
USERS = []
ACCOUNTS = {}
 

@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id,'Команды:' + '\n' + '/add - добавление аккаунта' + '\n' + '/list - вывод аккаунта'+ '\n' + '/all - все аккаунты')

		
@bot.message_handler(commands=['start'])
def start(message):
	if message.chat.id not in USERS:
		bot.send_message(message.chat.id, 'Привет! Этот бот поможет тебе быстро отыскать аккаунт, на который был заказан товар!' + '\n' + 'Для помощи по командам пиши /help'+ '\n' + 'ヽ(°□° )ノ', parse_mode='html')
		USERS.append(message.chat.id)
		ACCOUNTS[message.chat.id]=[]
	else:
		bot.send_message(message.chat.id, 'Извини, ты уже его активировал')
 
 
@bot.message_handler(commands=['add'])
def start_getting(message):
    bot.send_message(message.chat.id,'Введите e-mail от аккаунта!')
    bot.register_next_step_handler(message, get_login)
 
def get_login(message):
	
    global login
    login = message.text
    bot.send_message(message.chat.id,'Введите пароль от аккаунта!')
    bot.register_next_step_handler(message, get_pass)
 
def get_pass(message):
    global password
    password = message.text
    bot.send_message(message.chat.id,'Введите название товара!')
    bot.register_next_step_handler(message, get_item)
 
def get_item(message):
    global item
    item = message.text
    get_acc(message)
    bot.send_message(message.chat.id,'Успешно, для просмотра пиши /list (＾▽＾)')
 
def get_acc(message):
    ACCOUNTS[message.chat.id].append([])
    ACCOUNTS[message.chat.id][len(ACCOUNTS[message.chat.id])-1].append(login)
    ACCOUNTS[message.chat.id][len(ACCOUNTS[message.chat.id])-1].append(password)
    ACCOUNTS[message.chat.id][len(ACCOUNTS[message.chat.id])-1].append(item)
 
 
@bot.message_handler(commands=['list'])
def bots_list(message):
	output = ''
	for i in range(0, len(ACCOUNTS[message.chat.id])):
		#for acc in ACCOUNTS[message.chat.id][i]:
		output += str(ACCOUNTS[message.chat.id][i][0]) + ' - ' + str(ACCOUNTS[message.chat.id][i][1]) + ' - ' + str(ACCOUNTS[message.chat.id][i][2]) + '\n'
			#output += acc + '\n'
	file = open(str(message.chat.id) + '.txt', 'a+')	
	file.write(output+ '\n')
	file.close()
	bot.send_message(message.chat.id, output)
 

@bot.message_handler(commands=['all'])
def all_list(message):
	doc = open(str(message.chat.id) + '.txt', 'rb')
	bot.send_document(message.chat.id, doc)
	bot.send_document(message.chat.id, "FILEID")
 
if __name__ == '__main__':
	bot.polling(none_stop=True)