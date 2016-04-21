# -*- coding: utf-8 -*-
"""
Created on Thu April 21 12:54:39 2016

@author: Robin
"""
#读取，分析来自Reviews表中某一ReviewID的内容，如果是新内容，将计算其对应的情感值，并存储到SentiValues表

from SentiAnalysis import *

class SENTI:
    def __init__(self, commentSequence):
        self.commentSequence = commentSequence
        self.quality = []
        self.color = []
        self.material = []
        self.style = []
        self.function = []
        self.package = []
        self.price = []
        self.service = []
        self.logistic = []
        self.description = []
        self.others = []
        self.qualityWeight = 1 #默认“质量”权重为1
        self.colorWeight = 1 #默认“颜色”权重为1
        self.materialWeight = 1 #默认“材料”权重为1
        self.styleWeight =1 #默认“风格”权重为1
        self.functionWeight = 1 #默认“功能”权重为1
        self.packageWeight = 1 #默认“包装”去做权重为1
        self.priceWeight = 1 #默认“价格”权重为1
        self.serviceWeight = 1 #默认“卖家服务”权重为1
        self.logisticWeight = 1 #默认“物流”权重为1
        self.descriptionWeight = 1 #默认“实物与描述对比”权重为1
        self.othersWeight = 1 #默认“其他”权重为1
        self.ReviewScore = 0
        self.AllWeights = 0

    def sentiCalculation(self):
        self.ReviewSenti = commentSentiCalc(self.commentSequence)
        self.ReviewSenti.groupSentiCalc()
        #quality
        if(self.ReviewSenti.quality != []):
            for item in self.ReviewSenti.quality:
                sentiWords = u""
                sentiWordsList = item[0]
                sentiValue = item[1]
                for wordTuple in sentiWordsList:
                    sentiWords += wordTuple[1]
                self.quality.append((sentiWords, sentiValue))
            self.AllWeights += self.qualityWeight

        #color
        if(self.ReviewSenti.color != []):
            for item in self.ReviewSenti.color:
                sentiWords = u""
                sentiWordsList = item[0]
                sentiValue = item[1]
                for wordTuple in sentiWordsList:
                    sentiWords += wordTuple[1]
                self.color.append((sentiWords, sentiValue))
            self.AllWeights += self.colorWeight


        #material
        if(self.ReviewSenti.material != []):
            for item in self.ReviewSenti.material:
                sentiWords = u""
                sentiWordsList = item[0]
                sentiValue = item[1]
                for wordTuple in sentiWordsList:
                    sentiWords += wordTuple[1]
                self.material.append((sentiWords, sentiValue))
            self.AllWeights += self.materialWeight


        #style
        if(self.ReviewSenti.style != []):
            for item in self.ReviewSenti.style:
                sentiWords = u""
                sentiWordsList = item[0]
                sentiValue = item[1]
                for wordTuple in sentiWordsList:
                    sentiWords += wordTuple[1]
                self.style.append((sentiWords, sentiValue))
            self.AllWeights += self.styleWeight

        #function
        if(self.ReviewSenti.function != []):
            for item in self.ReviewSenti.function:
                sentiWords = u""
                sentiWordsList = item[0]
                sentiValue = item[1]
                for wordTuple in sentiWordsList:
                    sentiWords += wordTuple[1]
                self.function.append((sentiWords, sentiValue))
            self.AllWeights += self.functionWeight

        #package
        if(self.ReviewSenti.package != []):
            for item in self.ReviewSenti.package:
                sentiWords = u""
                sentiWordsList = item[0]
                sentiValue = item[1]
                for wordTuple in sentiWordsList:
                    sentiWords += wordTuple[1]
                self.package.append((sentiWords, sentiValue))
            self.AllWeights += self.packageWeight

        #price
        if(self.ReviewSenti.price != []):
            for item in self.ReviewSenti.price:
                sentiWords = u""
                sentiWordsList = item[0]
                sentiValue = item[1]
                for wordTuple in sentiWordsList:
                    sentiWords += wordTuple[1]
                self.price.append((sentiWords, sentiValue))
            self.AllWeights += self.priceWeight

        #service
        if(self.ReviewSenti.service != []):
            for item in self.ReviewSenti.service:
                sentiWords = u""
                sentiWordsList = item[0]
                sentiValue = item[1]
                for wordTuple in sentiWordsList:
                    sentiWords += wordTuple[1]
                self.service.append((sentiWords, sentiValue))
            self.AllWeights += self.serviceWeight

        #logistic
        if(self.ReviewSenti.logistic != []):
            for item in self.ReviewSenti.logistic:
                sentiWords = u""
                sentiWordsList = item[0]
                sentiValue = item[1]
                for wordTuple in sentiWordsList:
                    sentiWords += wordTuple[1]
                self.logistic.append((sentiWords, sentiValue))
            self.AllWeights += self.logisticWeight

        #description
        if(self.ReviewSenti.description != []):
            for item in self.ReviewSenti.description:
                sentiWords = u""
                sentiWordsList = item[0]
                sentiValue = item[1]
                for wordTuple in sentiWordsList:
                    sentiWords += wordTuple[1]
                self.description.append((sentiWords, sentiValue))
            self.AllWeights += self.descriptionWeight

        #others
        if(self.ReviewSenti.others != []):
            for item in self.ReviewSenti.others:
                sentiWords = u""
                sentiWordsList = item[0]
                sentiValue = item[1]
                for wordTuple in sentiWordsList:
                    sentiWords += wordTuple[1]
                self.others.append((sentiWords, sentiValue))
            self.AllWeights += self.othersWeight
        return(True)

    def write2SentiValues(self):
        if(self.sentiCalculation()):
            #quality
            if(self.quality != []):
                sentiWords = u""
                sentiScore = 0
                for wordTuple in self.quality:
                    sentiWords += (wordTuple[0]+u",")
                    sentiScore += wordTuple[1]
                print("QualityContent: "+sentiWords)
                print("QualityScore: %f")%(sentiScore)
                self.ReviewScore += sentiScore*self.qualityWeight

            #color
            if(self.color != []):
                sentiWords = u""
                sentiScore = 0
                for wordTuple in self.color:
                    sentiWords += (wordTuple[0]+u",")
                    sentiScore += wordTuple[1]
                print("ColorContent: "+sentiWords)
                print("ColorScore: %f")%(sentiScore)
                self.ReviewScore += sentiScore*self.colorWeight

            #material
            if(self.material != []):
                sentiWords = u""
                sentiScore = 0
                for wordTuple in self.material:
                    sentiWords += (wordTuple[0]+u",")
                    sentiScore += wordTuple[1]
                print("MaterialContent: "+sentiWords)
                print("MaterialScore: %f")%(sentiScore)
                self.ReviewScore += sentiScore*self.materialWeight

            #style
            if(self.style != []):
                sentiWords = u""
                sentiScore = 0
                for wordTuple in self.style:
                    sentiWords += (wordTuple[0]+u",")
                    sentiScore += wordTuple[1]
                print("StyleContent: "+sentiWords)
                print("StyleScore: %f")%(sentiScore)
                self.ReviewScore += sentiScore*self.styleWeight

            #function
            if(self.function != []):
                sentiWords = u""
                sentiScore = 0
                for wordTuple in self.function:
                    sentiWords += (wordTuple[0]+u",")
                    sentiScore += wordTuple[1]
                print("FunctionContent: "+sentiWords)
                print("FunctionScore: %f")%(sentiScore)
                self.ReviewScore += sentiScore*self.functionWeight

            #package
            if(self.package != []):
                sentiWords = u""
                sentiScore = 0
                for wordTuple in self.package:
                    sentiWords += (wordTuple[0]+u",")
                    sentiScore += wordTuple[1]
                print("PackageContent: "+sentiWords)
                print("PackageScore: %f")%(sentiScore)
                self.ReviewScore += sentiScore*self.packageWeight

            #price
            if(self.price != []):
                sentiWords = u""
                sentiScore = 0
                for wordTuple in self.price:
                    sentiWords += (wordTuple[0]+u",")
                    sentiScore += wordTuple[1]
                print("PriceContent: "+sentiWords)
                print("PriceScore: %f")%(sentiScore)
                self.ReviewScore += sentiScore*self.priceWeight

            #service
            if(self.service != []):
                sentiWords = u""
                sentiScore = 0
                for wordTuple in self.service:
                    sentiWords += (wordTuple[0]+u",")
                    sentiScore += wordTuple[1]
                print("ServiceContent: "+sentiWords)
                print("ServiceScore: %f")%(sentiScore)
                self.ReviewScore += sentiScore*self.serviceWeight

            #logistic
            if(self.logistic != []):
                sentiWords = u""
                sentiScore = 0
                for wordTuple in self.logistic:
                    sentiWords += (wordTuple[0]+u",")
                    sentiScore += wordTuple[1]
                print("LogisticContent: "+sentiWords)
                print("LogisticScore: %f")%(sentiScore)
                self.ReviewScore += sentiScore*self.logisticWeight

            #description
            if(self.description != []):
                sentiWords = u""
                sentiScore = 0
                for wordTuple in self.description:
                    sentiWords += (wordTuple[0]+u",")
                    sentiScore += wordTuple[1]
                print("DescriptionContent: "+sentiWords)
                print("DescriptionScore: %f")%(sentiScore)
                self.ReviewScore += sentiScore*self.descriptionWeight

            #others
            if(self.others != []):
                sentiWords = u""
                sentiScore = 0
                for wordTuple in self.others:
                    sentiWords += (wordTuple[0]+u",")
                    sentiScore += wordTuple[1]
                print("OtherContent: "+sentiWords)
                print("OtherScore: %f")%(sentiScore)
                self.ReviewScore += sentiScore*self.othersWeight
            self.ReviewScore /= self.AllWeights
            print("----------------------")
            print("ReviewScore: %s")%self.ReviewScore

if __name__=="__main__":
    sentiValue = SENTI(u"物流非常快？颜色非常好看。颜色很好看。但是质量不好。")
    sentiValue.write2SentiValues()