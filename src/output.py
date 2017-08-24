# coding: utf-8
__author__ = 'AlexLiu'

class Output():
    def output_html(self, list):
        fout = open('output.html', 'w')
        fout.write("<html>")
        fout.write("<head><meta charset='utf-8' /></head>")
        fout.write("<body>\n")
        for data in list:
            fout.write("<div>%s-%s</div>\n" % (self._handle_str(data['artist']), self._handle_str(data['title'])))
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

    def output_kgl(self, list, name="豆瓣红心"):
        fout = open('output.kgl', 'w')
        fout.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        fout.write("<List ListName='%s'>\n" % name)
        for data in list:
            fout.write("<File><FileName>%s-%s</FileName></File>\n" % (self._handle_str(data['artist']), self._handle_str(data['title'])))
        fout.write("</List>")
        fout.close()

    def _handle_str(self, str):
        return str.encode('utf-8').replace('&', '&amp;')