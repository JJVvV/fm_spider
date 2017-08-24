# coding: utf-8
__author__ = 'AlexLiu'

class List():

    def __init__(self, session):
        self.session = session
        self.headers = headers = {
            'Host': 'douban.fm',
            'Referer':'https://douban.fm/mine/hearts',
             'Content-Type':'application/x-www-form-urlencoded',
             'Origin':'https://douban.fm',
             'X-Requested-With':'XMLHttpRequest'
        }

    def get_fm_id_list(self):

        cookies = self.session.cookies.get_dict()
        r = self.session.get('https://douban.fm/j/v2/redheart/basic', headers=self.headers, cookies=cookies)
        songList = r.json()['songs']
        self.songIdList = [song['sid'] for song in songList]
        print('******song id list*******')
        print(self.songIdList)


    def get_fm_detail(self):
        cookies = self.session.cookies.get_dict()
        dbcl2 = cookies['dbcl2']

        self.get_fm_id_list()

        songData = {
            'sids': '|'.join(self.songIdList),
            'kbps':192,
            'ck':cookies['ck']
        }

        r = self.session.post('https://douban.fm/j/v2/redheart/songs', data=songData, headers=self.headers, cookies=cookies)

        songList = r.json()
        self.songList = songList
        return self.songList
