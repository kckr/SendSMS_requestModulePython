import json
import re

import requests



def sms():
    s = requests.Session()
    data = {"username": "****", "password": "****"}  # Kirjautumistiedot
    url = "https://vip.sonera.fi/login"
    url2 = "https://vip.sonera.fi/admin/home/sendSms"
    login = s.post(url, data=data)

    receiver = '0469536673'
    message = 'Did you receive it?'

    data2 = {"cocoon-ajax": "true", "forms_submit_id": "send", "message": message, "to": receiver,
             "searchuser_input": ""}

    b = s.get(url2)  # using existing session for 2nd url

    re_text = re.sub(r'\s+', ' ', b.text)


    start = re_text.find('method="POST" action=')
    end = re_text.find('.continue')
    koodi = re_text[start + 22:end]  # extracting the code for send message .continue link
    print(koodi)


    form_data = {"to": receiver, "message": message, "searchuser_input": "", "dojo.transport": "xmlhttp",
                 "cocoon-ajax": "true", "forms_submit_id": "send"}

    url3 = "https://vip.sonera.fi/admin/home/" + koodi + '.continue'
    print(url3)
    r = s.post(url3, data=form_data)




sms()
