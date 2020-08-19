#贝叶斯算法的应用
from numpy import *
import operator
from os import listdir
import numpy as npy
import numpy
class Bayes:
    def __init__(self):
        self.length=-1  #判断是否已进行训练
        self.labelcount=dict()  #存储标签
        self.vectorcount=dict() #存储向量
    def fit(self,dataSet:list,labels:list):  #fit是训练，为了简历类别与向量的关联
        if(len(dataSet)!=len(labels)):
            raise ValueError("您输入的测试数组跟类别数组长度不一致")
        self.length=len(dataSet[0])#测试数据特征值的长度
        labelsnum=len(labels)#类别所有的数量
        norlabels=set(labels)#不重复类别的数量
        for item in norlabels:
            thislabel=item
            self.labelcount[thislabel]=labels.count(thislabel)/labelsnum#求的当前类别占类别总数的比例
        for vector,label in zip(dataSet,labels):
            if(label not in self.vectorcount):
                self.vectorcount[label]=[]
            self.vectorcount[label].append(vector)
        print("训练结束")
        return self
    def btest(self,TestData,labelsSet):
        if(self.length==-1):
            raise ValueError("您还没有进行训练，请先训练")
        #计算testdata分别为各个类别的概率
        lbDict=dict()
        for thislb in labelsSet:
            p=1
            alllabel=self.labelcount[thislb]
            allvector=self.vectorcount[thislb]
            vnum=len(allvector)
            allvector=numpy.array(allvector).T
                vector=list(allvector[index])
                p*=vector.count(TestData[index])/vnum
            lbDict[thislb]=p*alllabel
        thislabel=sorted(lbDict,key=lambda x:lbDict[x],reverse=True)[0]
        return thislabel

#加载数据
def datatoarray(fname):
    arr=[]
    fh=open(fname)
    for i in range(0,32):
        thisline=fh.readline()
        for j in range(0,32):
            arr.append(int(thisline[j]))
    return arr
#建立一个函数取文件名前缀
def seplabel(fname):
    filestr=fname.split(".")[0]
    label=int(filestr.split("_")[0])
    return label
#建立训练数据
def traindata():
    labels=[]
    trainfile=listdir("D:/Python35/traindata")
    num=len(trainfile)
    #长度1024（列），每一行存储一个文件
    #用一个数组存储所有训练数据，行：文件总数，列：1024
    trainarr=zeros((num,1024))
    for i in range(0,num):
        thisfname=trainfile[i]
        thislabel=seplabel(thisfname)
        labels.append(thislabel)
        trainarr[i,:]=datatoarray("D:/Python35/traindata/"+thisfname)
    return trainarr,labels
bys=Bayes() #实例化
#训练数据
train_data,labels=traindata()
bys.fit(train_data,labels)
#测试
thisdata=datatoarray("D:/Python35/testdata/8_90.txt")
labelsall=[0,1,2,3,4,5,6,7,8,9]
#识别单个手写体数字
'''
rst=bys.btest(thisdata,labelsall)
print(rst)
'''
#识别多个手写体数字（批量测试）
testfileall=listdir("D:/Python35/testdata")
num=len(testfileall)
x=0
for i in range(0,num):
    thisfilename=testfileall[i]
    thislabel=seplabel(thisfilename)
    #print(thislabel)
    thisdataarray=datatoarray("D:/Python35/testdata/"+thisfilename)
    label=bys.btest(thisdataarray,labelsall)
    #print("该数字是:"+str(thislabel)+",识别出来的数字是："+str(label))
    if(label!=thislabel):
        x+=1
        print("此次出错")
print(x)
print("错误率是："+str(float(x)/float(num)))
#小作业：用贝叶斯算法实现课程销量的预测



















