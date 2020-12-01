class Logger(object):

    def __init__(self):
        self.level=0

    def setLevel(self,level):
        if level>=0:
            self.level=level

    def log(self, message,level):
        if level <= self.level:
            message=u''+message
            import datetime
            #import codecs
            #with codecs.open('log.txt', 'a','utf-16') as stream:
            #    stream.write(str(datetime.datetime.now()) + '|' + str(message) + str('|')+'\n')
            f = open('log.txt', 'a')
            f.write(str(datetime.datetime.now()) + '|' + str(message) + str('|')+'\n')
            f.close()