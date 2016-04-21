# -*- coding: utf-8 -*-
"""
Created on Thu April 21 12:54:39 2016

@author: Robin
"""

#commentSentiCalc类的作用是针对每一条评论commenSentence，利用groupSentiCalc函数得到对象在quality, color, material,...,others等
#11个方面的情感状况，该11个属性的表达是[([（词1的位置，词1的内容），（词2的位置， 词2的内容）...(词n的位置，词n的内容)]，该部分内容的情感值),(),...,()]

from BuildDict import sentiDictionary, featureDictionary
import jieba

class commentSentiCalc:
    def __init__(self, commentSentence):
        self.commentSentence = commentSentence
        self.sentiDic = sentiDictionary()
        self.featureDic = featureDictionary()
        self.positiveValue = 4 #正面情感词的默认分值
        self.negativeValue = -4 #负面情感词的默认分值
        #self.notValue = -1 #否定词的默认分值
        self.extremeLevel = 2 #“极其”类程度副词的默认分值
        self.veryLevel = 1.25 #“很”类程度副词的默认分值
        self.moreLevel = 1.2 #“较”类程度副词的默认分值
        self.ishLevel = 0.8 #“稍稍”类程度副词的默认分值
        self.insufficientLevel = 0.5 #“不足，稍欠”类程度副词的默认分值
        self.overLevel = 1.5 #“超”类程度副词的默认分值
        self.notvery = 0.5 #“不很”类程度副词的默认分值

    #利用标点符号将评论切分成若干块，每一块都用分词工具分好词
    def segByPunc(self):
        punctuation = [u'，', u'/', u'！', u'？', u'。', u' ', u'\'']
        wordSequenceList = []
        seg_list = jieba.cut(self.commentSentence)
        segmentedComment = [item for item in seg_list]
        segmentedCommentTuple = list(enumerate(segmentedComment))
        subWordSequenceList = []
        for wordTuple in segmentedCommentTuple:
            if(wordTuple[1] in punctuation):
                if(subWordSequenceList != []):
                    wordSequenceList.append(subWordSequenceList)
                    subWordSequenceList = []
            else:
                subWordSequenceList.append(wordTuple)
        if(subWordSequenceList != []):
            wordSequenceList.append(subWordSequenceList)
        return(wordSequenceList)

    #针对每一组词，辨识出其中的情感词，否定词和程度副词
    def sentiVec(self, wordSequence):
        positiveWords_unicode = self.sentiDic.buildSentiDic()[0]
        negativeWords_unicode = self.sentiDic.buildSentiDic()[1]
        denyWords_unicode = self.sentiDic.buildSentiDic()[2]
        levelDic_unicode = self.sentiDic.buildSentiDic()[3]
        wordNum = len(wordSequence)
        polarVec = []
        notVec = []
        levelVec = []
        for i in range(wordNum):
            if(wordSequence[i] in positiveWords_unicode):
                polarVec.append((i, 'positive', self.positiveValue)) #positive:4; negative:-4
            elif(wordSequence[i] in negativeWords_unicode):
                polarVec.append((i, 'negative', self.negativeValue))
            elif(wordSequence[i] in denyWords_unicode):
                notVec.append((i, -1))
            elif(wordSequence[i] in levelDic_unicode[0]):
                levelVec.append((i, self.extremeLevel))
            elif(wordSequence[i] in levelDic_unicode[1]):
                levelVec.append((i, self.veryLevel))
            elif(wordSequence[i] in levelDic_unicode[2]):
                levelVec.append((i, self.moreLevel))
            elif(wordSequence[i] in levelDic_unicode[3]):
                levelVec.append((i, self.ishLevel))
            elif(wordSequence[i] in levelDic_unicode[4]):
                levelVec.append((i, self.insufficientLevel))
            elif(wordSequence[i] in levelDic_unicode[5]):
                levelVec.append((i, self.overLevel))
        if(polarVec == []):
            return([])
        else:
            GroupVec = []
            polarNum = len(polarVec)
            for i in range(polarNum):
                notGroupVec = []
                levelGroupVec = []
                if(i == 0):
                    if(notVec != []):
                        for item in notVec:
                            if(item[0] < polarVec[i][0]):
                                notGroupVec.append(item)
                    if(levelVec != []):
                        for item in levelVec:
                            if(item[0] < polarVec[i][0]):
                                levelGroupVec.append(item)
                else:
                    if(notVec != []):
                        for item in notVec:
                            if(item[0] < polarVec[i][0] and item[0] > polarVec[i-1][0]):
                                notGroupVec.append(item)
                    if(levelVec != []):
                        for item in levelVec:
                            if(item[0] < polarVec[i][0] and item[0] > polarVec[i-1][0]):
                                levelGroupVec.append(item)
                GroupVec.append((polarVec[i], notGroupVec, levelGroupVec))
            return(GroupVec)

    #针对每一组词，计算出其情感值
    def sentiValueCalc(self, wordSequence):
        GroupVec = self.sentiVec(wordSequence)
        sentiValue = 0
        for polarVec, notVec, levelVec in GroupVec:
            W_level = 1
            W_not = 1
            #a big problem if there are over 1 'not' words and mover 1 'level' words
            if(levelVec != []):
                levelVec = sorted(levelVec, key =  lambda x:x[-1])
                W_level = levelVec[-1][-1]
                if(notVec != []):
                    notNum = len(notVec)
                    if(notNum % 2 != 0):
                        if(levelVec[-1][0] > notVec[-1][0]):
                            W_level = self.notvery
                        else:
                            W_level = -1*W_level        #程度副词在否定词中间或者前面都视为负，只有程度副词在所有否定词之后才视为0.5
            elif(notVec != []):
                notNum = len(notVec)
                if(notNum % 2 != 0):
                    W_not = -1
            sentiValue += polarVec[-1]*W_level*W_not
        return(sentiValue)

    #将评论分解成词块，将每一词块归类到定义的11中特征维度中，并且计算每一词块的情感值
    def groupSentiCalc(self):
        wordSequenceList = self.segByPunc()
        sentiSummary = {'quality':[], 'color':[], 'material':[], 'style':[], 'function':[], 'package':[], 'price':[], 'service':[], 'logistic':[], 'description':[], 'others':[]}
        keys = ['quality', 'color', 'material', 'style', 'function', 'package', 'price', 'service', 'logistic', 'description']
        for wordSequenceTuple in wordSequenceList:
            wordSequence = []
            for loc, seg_word in wordSequenceTuple:
                wordSequence.append(seg_word)
            groupSentiValue = self.sentiValueCalc(wordSequence)
            groupSentiTuple = (wordSequenceTuple, groupSentiValue)
            flag = -1
            for i, key in enumerate(keys):
                for item in self.featureDic.buildFeatureDic()[i]:
                    if(item in wordSequence and groupSentiTuple not in sentiSummary[key]):
                        sentiSummary[key].append(groupSentiTuple)
                        flag = 1
                        break
            if(flag == -1):
                sentiSummary['others'].append(groupSentiTuple)
        self.quality = sentiSummary['quality']
        self.color = sentiSummary['color']
        self.material = sentiSummary['material']
        self.style = sentiSummary['style']
        self.function = sentiSummary['function']
        self.package = sentiSummary['package']
        self.price = sentiSummary['price']
        self.service = sentiSummary['service']
        self.logistic = sentiSummary['logistic']
        self.description = sentiSummary['description']
        self.others = sentiSummary['others']

if __name__=="__main__":
    wordSequence1 = u"物流非常快？颜色非常好看。颜色很好看。但是质量不好。"
    comment = commentSentiCalc(wordSequence1)
    comment.groupSentiCalc()
    print(comment.color)