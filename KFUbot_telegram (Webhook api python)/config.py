# -*- coding: utf-8 -*-
token = '441412717:AAG-li-UKdvMccRhJsbj8WXflDKFLFGkxPw'
WEBHOOK_HOST = '212.237.19.218'
WEBHOOK_PORT = 443  # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = '0.0.0.0'  # На некоторых серверах придется указывать такой же IP, что и выше

WEBHOOK_SSL_CERT = '/home/webhook_cert.pem'  # Путь к сертификату
WEBHOOK_SSL_PRIV = '/home/webhook_pkey.pem'  # Путь к приватному ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (token)







