import libs.vk as vk
import modules.settings as settings
import sys
session = vk.Session()
session = vk.AuthSession(settings.app_id, settings.vk_send_login, settings.vk_send_pass, scope='messages')
vk_api_send = vk.API(session,v = '5.85')
class zakupka:
    message = ''
    link = ''
    link_doc = ''
    date_end = ''
    adres=''
    def __init__(self, id, org_name,description,price,date):
        self.id = id
        self.org_name = org_name
        self.date = date
        self.description = description
        self.price = price
        self.link = "http://www.zakupki.gov.ru/epz/order/notice/zk44/view/common-info.html?regNumber="+id
        self.link_doc = "http://www.zakupki.gov.ru/epz/order/notice/zk44/view/documents.html?regNumber="+id
    def construct_message(self):
        self.message = "💡 " + self.description + "\n💰Цена контракта: " + self.price + "р.\n🏛Организация: " + self.org_name+"\n📭"+self.adres + "\n⏳" + self.date+ "\n⏳Дата окончания: " + self.date_end +"\n🔑"+self.link

#"Id: " + self.id + "\n
def send(zakupka):
    try:
        vk_api_send.messages.send(user_id = settings.user_id,message = zakupka.message)
        vk_api_send.messages.send(user_id=123363583, message=zakupka.message)

        #,attachment = {"type":"link","link": {"url":zakupka.link,"title":"Гос закупка","description":"hjhsajh hdja sjd"}}
    except:
        print("Ошибка отправки сообщения в ВК: ", sys.exc_info()[0])
def sendm(message):
    try:
        vk_api_send.messages.send(user_id = settings.user_id,message = message)
    except:
        print("Ошибка отправки сообщения в ВК: ", sys.exc_info()[0])