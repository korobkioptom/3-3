import requests

bot_token = '710715631:AAHvw3WnM4W_weBbZPDoZyxr_Srk3K8y1zM'
telegram = 'https://api.telegram.org/bot{}/'

def get_updates ():
	res = requests.get(telegram.format(bot_token)+'getupdates')
	#print (res.json())
	return res.json()
#print (get_updates())

def last_messaga ():
	updates = get_updates()
	chat_id = updates['result'][-1]
	text = chat_id['message']['text']
	return text

print  (last_messaga())	

def post_messsaga (text_messagi):
	chat_id_bot = '606375631'
	otpravka = requests.post(telegram.format(bot_token)+'sendmessage?chat_id=606375631&text={}'.format(text_messagi))
	return text_messagi
post_messsaga('123bot')









#def main():
#	pass

#if __name__ == '__main__':
#	main()
