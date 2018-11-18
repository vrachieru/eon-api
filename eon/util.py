import base64
import datetime
import hashlib
import hmac

DATE_FORMAT = '%Y%m%d'
DATE_TIME_FORMAT = '%Y%m%d %H:%M:%S'

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

def parse_date(date_str):
    '''
    Parse date string

    :param str date_str: date string to parse
    :return: parsed date object
    '''
    return datetime.datetime.strptime(date_str, DATE_FORMAT)

def parse_date_time(date_time_str):
    '''
    Parse date time string

    :param str date_time_str: date string to parse
    :return: parsed date time object
    '''
    return datetime.datetime.strptime(date_time_str, DATE_TIME_FORMAT)

def sha256(message):
    '''
    Compute a hash of plain text message

    :param str message: plain text message
    :return: hashed message
    '''
    hash_object = hashlib.sha256(utf8_encode(message))

    return utf8_encode(hash_object.hexdigest())

def hmac_sha256(key, message):
    '''
    Compute a Hash-based message authentication code (HMAC) using a secret key

    :param str key: secret key
    :param str message: plain text message
    :return: hmac
    '''
    byte_key = utf8_encode(key)
    message = utf8_encode(message)
    hmac_object = hmac.new(byte_key, message, hashlib.sha256)

    return utf8_encode(hmac_object.hexdigest())

def base64_encode(message):
    '''
    Encode message to a Base64 Data Encodings conforming string

    :param str message: plain text message
    :return: encoded message
    '''
    return utf8_decode(base64.b64encode(message))

def utf8_encode(message):
    '''
    Encode message to a UTF-8 conforming string

    :param str message: plain text message
    :return: encoded message
    '''
    return message.encode('utf-8')

def utf8_decode(message):
    '''
    Decode UTF-8 conforming string

    :param str message: UTF-8 encoded text message
    :return: decoded message
    '''
    return message.decode('utf-8')