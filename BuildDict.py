# -*- coding: utf-8 -*-
"""
Created on Thu April 21 12:54:39 2016

@author: Robin
"""
#sentiDictionary类用于构造情感词典
#featureDictionary类用于构造特征维度词典

class sentiDictionary:
    def __init__(self):
        pass;

    def readWords(self, filePath):
        wordList = []
        with open(filePath) as f:
            for word in f.readlines():
                wordList.append(word.strip('\n'))
        return(wordList)

    def buildSentiDic(self, positiveFile='positive.txt', negativeFile='negative.txt', levelFile='level_adv.txt', denyFile='deny_adv.txt'):
        positiveWords_utf8 = self.readWords(positiveFile)
        negativeWords_utf8 = self.readWords(negativeFile)
        levelWords_utf8 = self.readWords(levelFile)
        denyWords_utf8 = self.readWords(denyFile)
        positiveWords_unicode = []
        for word_utf8 in positiveWords_utf8:
            positiveWords_unicode.append(word_utf8.decode('utf8'))
        negativeWords_unicode = []
        for word_utf8 in negativeWords_utf8:
            negativeWords_unicode.append(word_utf8.decode('utf8'))
        denyWords_unicode = []
        for word_utf8 in denyWords_utf8:
            denyWords_unicode.append(word_utf8.decode('utf8'))
        levelWords_unicode = []
        for word_utf8 in levelWords_utf8:
            levelWords_unicode.append(word_utf8.decode('utf8'))
        level1_unicode = levelWords_unicode[1:70]       #extreme 69
        level2_unicode = levelWords_unicode[71:113]     #very 42
        level3_unicode = levelWords_unicode[114:151]    #more 37
        level4_unicode = levelWords_unicode[152:181]    #bit 29
        level5_unicode = levelWords_unicode[182:194]    #insufficiently 12
        level6_unicode = levelWords_unicode[195:]       #over 30
        level_unicode = (level1_unicode, level2_unicode, level3_unicode, level4_unicode, level5_unicode, level6_unicode)
        positiveWords_unicode[0] = positiveWords_unicode[0][1:]
        negativeWords_unicode[0] = negativeWords_unicode[0][1:]
        denyWords_unicode[0] = denyWords_unicode[0][1:]
        self.positiveWords_unicode = positiveWords_unicode
        self.negativeWords_unicode = negativeWords_unicode
        self.denyWords_unicode = denyWords_unicode
        self.levelWords_unicode = level_unicode
        return(positiveWords_unicode, negativeWords_unicode, denyWords_unicode, level_unicode)

class featureDictionary:
    def __init__(self):
        pass;
    def buildFeatureDic(selfself):
        quality = [u"质量", u"做工"]
        color = [u"颜色"]
        material = [u"面料", u"手感"]
        style = [u"款式", u"效果"]
        function = [u"遮阳", u"防晒"]
        package = [u"包装"]
        price = [u"价格", u"实惠", u"便宜"]
        service = [u"店家", u"卖家", u"服务态度", u"服务"]
        logistic = [u"发货", u"物流", u"快递", u"速度"]
        description = [u"图片", u"描述"]
        return(quality, color, material, style, function, package, price, service, logistic, description)

if(__name__ == "__main__"):
    feature = sentiDictionary()
    feature.buildSentiDic()
    print(feature.positiveWords_unicode)

