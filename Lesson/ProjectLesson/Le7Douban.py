#!/user/bin/python
# coding=utf-8

#!/user/bin/python
# coding=utf-8


from __future__ import print_function
from HTMLParser import HTMLParser
import requests
import os
import time

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#_MOVIE_PATH = 'html/head/meta/meta/meta/meta/meta/link/link/link/link/body/link/div/div/div/div/div/div/div/div/table'
_MOVIE_PATH ='html/head/meta/meta/meta/link/link/body/div/div/div/div/div/div/div/div/div/ul/li/li/li/li/li/li/li/li/li' \
             '/li/li/li/li/li/li/li/li/div/div/div/dl/dt'
_MOVIE_PATH2 ='html/head/meta/meta/meta/link/link/body/div/div/div/div/div/div/div/div/div/ul/li/li/li/li/li/li/li/li/li/li/div'


class Movie(object):
    def __init__(self):

        self.attrs = []

    def __str__(self):
        content = []
        for k, v in self.attrs:
            line = '{0} = {1}'.format(k, v)
            content.append(line)
        return '\r\n'.join(content)

    def downloadImg(self, imgpath, headers):
        imgurl = None
        for (k, v) in self.attrs:
            if k == 'movie_img_url':
                imgurl = v
        if imgurl is None:
            return None

        imgname = imgurl.split('/')[-1]
        imglocalpath = os.path.join(imgpath, imgname)
        img = requests.get(imgurl, headers)
        with open(imglocalpath, 'wb') as f:
            f.write(img.content)
        self.attrs.append(('movie_img_localpath', imglocalpath))
        return imglocalpath


class DouBanMovieRankParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._tags_stack = []  # 栈，后入先出

        self.movies = []
        self._new_movie = False

    def reset(self):
        HTMLParser.reset(self)
        self._tags_stack = []  # 栈，后入先出
        self._new_movie = False

    def handle_starttag(self, tag, attrs):

        def _getattr(attrname):
            for (k, v) in attrs:
                if attrname == k:
                    return v
            return None

        self._tags_stack.append(tag)
        path = '/'.join(self._tags_stack)

        # 可以用下面代码检查感兴趣内容的路径
        #print (path)

        if path == _MOVIE_PATH or path == _MOVIE_PATH2:
            self._new_movie = True
            self.movies.append(Movie())

        if self._new_movie == True and tag == 'a' and _getattr('class') == 'nbg':
            self.movies[-1].attrs.append(('movie_url', _getattr('href')))
            #self.movies[-1].attrs.append(('movie_name', _getattr('title')))

        if self._new_movie == True and tag == 'img':
            self.movies[-1].attrs.append(('movie_img_url', _getattr('src')))

        if self._new_movie == True and tag == 'a':
            self.movies[-1].attrs.append(('movie_name', _getattr('title')))

    def handle_endtag(self, tag):
        path = '/'.join(self._tags_stack)
        if path == _MOVIE_PATH:
            self._new_movie = False
        self._tags_stack.pop()

    def handle_data(self, data):

        path = '/'.join(self._tags_stack)
        # 可以用下面代码检查感兴趣内容的路径
        #print (path,data)

        if self._new_movie == True and path.endswith('/p'):
            self.movies[-1].attrs.append(('movie_intro', data))


if __name__ == '__main__':
    t1 = time.time()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115'}
    x = requests.get('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4', headers=headers)
    movieparser = DouBanMovieRankParser()
    movieparser.feed(x.content)
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    imgpath = os.path.join(parent_dir, 'doubanmovieimg')
    if not os.path.exists(imgpath):
        os.makedirs(imgpath)

    for m in movieparser.movies:
        m.downloadImg(imgpath, headers)
        print(m)
