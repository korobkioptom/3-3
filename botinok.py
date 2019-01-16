import requests

bot_token = '710715631:AAHvw3WnM4W_weBbZPDoZyxr_Srk3K8y1zM'
telegram = 'https://api.telegram.org/bot{}/'
def get_updates (bot_token):
	res = requests.get(telegram.format(bot_token))
	return res.json()
	pass

def last_messaga (json_answer):
	text_answer = json_answer['result'][-1]['message']['text']
	chat_id = json_answer['result'][-1]['chat']['id']
	return text_answer, chat_id
	pass
print  (last_messaga(get_updates(bot_token)))	