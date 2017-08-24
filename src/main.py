# coding: utf-8

__author__ = 'AlexLiu'

import json
import requests
from bs4 import BeautifulSoup
import re
import urllib
import output
import list

class DoubanClient(object):
    def __init__(self):
        object.__init__(self)
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        self.outputer = output.Output()
        self.session = requests.Session()
        self.lister = list.List(self.session)
        self.session.headers.update(self.headers)

    def login(self, username, password,
              source='index_nav',
              redir='https://douban.com',
              login=u'登录'):
        url = 'https://accounts.douban.com/login'
        r = self.session.get(url, headers=self.headers)
        soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
        (captcha_id, captcha_url) = self._get_captcha(r.content, soup)

        data = {
            # 'form_email': username,
            # 'form_password': password,
            'redir': redir,
            'login': login,
            'form_email':username,
            'form_password':password,
            'remember':'on'
        }

        if captcha_id != None:
            urllib.urlretrieve(captcha_url,"captcha.jpg")
            data['captcha-id'] = captcha_id
            data['captcha-solution'] = raw_input('please input solution for [%s]' % captcha_url)

        headers = {
            'referer': 'https://accounts.douban.com/login',
            'host': 'accounts.douban.com',
            'Content-Type':'application/x-www-form-urlencoded',
            'Connection':'keep-alive',
            'Origin':'https://accounts.douban.com'
        }

        self.session.post(url, data=data, headers=headers)

    def output_kgl(self):
        self.outputer.output_kgl(self.songList)

    def output_html(self):
        self.outputer.output_html(self.songList)

    def get_fm_detail(self):
        self.songList = self.lister.get_fm_detail()



    def _get_captcha(self, content, soup):

        solution_img_node = soup.find('img', id='captcha_image')
        if solution_img_node == None:
            return None, None

        captcha_url = solution_img_node['src']
        id_node = soup.find('input', attrs={'name': 'captcha-id','type': 'hidden'})
        captcha_id = id_node['value']

        return captcha_id, captcha_url


if __name__ == "__main__":
    try:
        c = DoubanClient()
        username = raw_input('please input your username: ')
        password = raw_input('please input your password: ')
        c.login(username, password)
        c.get_fm_detail()
        c.output_html()
        c.output_kgl()
        print('success')
    except:
        print('please try again')