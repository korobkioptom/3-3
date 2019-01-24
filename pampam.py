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
dicta = {'1':1,'2':2,'3':3,'4':4}
def slovarnik (text):
	for number in text:
		if number in dicta.keys():
			print  (dicta[number])			 
			x_number = dicta[number]
			otpravka = requests.post(telegram.format(bot_token)+'sendmessage?chat_id=606375631&text={number} messages ago you wrote {text}'.format(text=text, number=x_number))
	return x_number	

print  (slovarnik(last_messaga()))	