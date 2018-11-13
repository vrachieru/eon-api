import json
import requests

from .util import *

class EON():

    _HOST = 'myline-eon.ro'
    _USER_AGENT = 'okhttp/3.10.0'
    _CONTENT_TYPE = 'application/json; charset=UTF-8'

    _SHARED_KEY = 'zrAnQjN0bDjlTsKYmbpexjaBNY6wrCzuIqGWNgqoaJzlLrYiqd'

    def __init__(self, username, password):
        '''
        Create a new client instance.

        :param str username: username
        :param str password: password
        '''
        self._token = None
        self._token = self.login(username, password)

    def login(self, username, password):
        '''
        Log into the service

        :param str username: username
        :param str password: password
        :return: authentication token
        '''
        response = self.request(
            'POST', 
            '/mobapi/v3/public/user/authorize',
            {
                'username': username,
                'password': password
            }
        )

        return response.headers['XAuth']

    def get_inbox(self, page_size=10, start_index=0):
        '''
        Get inbox messages

        :param int page_size: size of paged results
        :param int start_index: results offset
        :return: 
        '''
        response = self.request(
            'GET',
            '/mobapi/v3/inbox/list?pageSize={page_size}&startIndex={start_index}'.format(**locals())
        )

        return response.json()

    def get_inbox_message(self, message_id):
        '''
        Get inbox message

        :param int message_id: message id
        :return: message
        '''
        response = self.request(
            'GET',
            '/mobapi/v3/inbox/message/{message_id}'.format(**locals())
        )

        return response.json()

    def request(self, method, path, payload=None):
        '''

        :param str method: http verb
        :param str path: api path
        :param dict payload: request payload
        :return: the REST response
        '''
        method = method.upper()
        date = format_date(now())

        return requests.request(
            method = method,
            url = 'https://' + self._HOST + path,
            headers = self.inject_xauth({
                'autorizare': self.get_authorization_header(method, path, self._HOST, date),
                'host': self._HOST,
                'x-date': date,
                'Content-Type': self._CONTENT_TYPE,
                'User-Agent': self._USER_AGENT
            }),
            data = json.dumps(payload)
        )

    def inject_xauth(self, headers):
        '''
        Inject the authorization header into subsequent requests after login

        :param dict headers: request headers
        :return: the unified header dict
        '''
        if self._token != None:
            headers.update({'XAuth': self._token})

        return headers

    def get_authorization_header(self, method, path, host, date):
        '''
        Get authorization header based on request metadata

        :param str method: http verb
        :param str path: api path
        :param str host: host
        :param str date: formatted date
        :return: the authorization header
        '''
        canonical_request = '{method}\n{path}\ncontent-type:{content_type}\nhost:{host}\nx-date:{date}'.format(
            **{
                **locals(),
                'content_type': self._CONTENT_TYPE
            }
        )

        canonical_request_hash = sha256(canonical_request)
        payload = date + '\n' + b64encode(canonical_request_hash)

        nonce = hmac_sha256(self._SHARED_KEY, date).decode('utf-8')
        signature = b64encode(hmac_sha256(nonce, payload))

        return 'SignedHeaders=content-type.host.x-date,Signature=' + signature
