import base64
import datetime
import hashlib
import hmac

def now():
    '''
    Get current date and time

    :return: current date andtime
    '''
    return datetime.datetime.now()

def format_date(date):
    '''
    Format date object

    :param date date: date
    :return: formatted date
    '''
    return date.strftime('%Y-%m-%dT%H:%M:%S%z') + '+0200'

def sha256(message):
    '''
    Compute a hash of plain text message

    :param str message: plain text message
    :return: hashed message
    '''
    hash_object = hashlib.sha256(message.encode('utf-8'))
    return hash_object.hexdigest().encode('utf-8')

def hmac_sha256(key, message):
    '''
    Compute a Hash-based message authentication code (HMAC) using a secret key

    :param str key: secret key
    :param str message: plain text message
    :return: hmac
    '''
    byte_key = key.encode('utf-8')
    message = message.encode('utf-8')
    return hmac.new(byte_key, message, hashlib.sha256).hexdigest().encode('utf-8')

def b64encode(message):
    '''
    Encode message to a Base64 Data Encodings conforming string

    :param str message: plain text message
    :return: encoded message
    '''
    return base64.b64encode(message).decode('utf-8')
