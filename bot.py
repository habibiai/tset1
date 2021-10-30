import requests
import schedule
import time


token = '2011055195:AAEnokVkXloIOOo4l7ESL6VCBzQAWAR1WzI'
id = '-1001753665143'

def send_message(msg):

    payload = {
        'chat_id': id,
        'text':msg,
        'parse_mode':'HTML'
    }
    return requests.post('https://api.telegram.org/bot{token}/sendMessage'.format(token=token),data=payload).content

print('start send message')
# res = send_message("from python script")
# print("response",res)


def report():
    my_balance = 10  ## Replace this number with an API call to fetch your account balance
    my_message = "Current balance is: {}".format(my_balance)  ## Customize your message
    send_message(my_message)


schedule.every(5).seconds.do(report)

while True:
    schedule.run_pending()
    time.sleep(1)