from django.db import models

# Create your models here.
class DB_userInfo(models.Model):
    wechat = models.CharField(max_length=20,default='')  #微信号，字符串类型，最大长度20，默认值为空字符串
    sex = models.CharField(max_length=20,default='')  #性别，字符串类型，man / women
    age = models.IntegerField(default=0)  #年龄，整形
    money = models.IntegerField(default=0)  #年收入，整形
    adress = models.CharField(max_length=20,default='')  #地址，字符串类型，最大长度20，默认值为空字符串
    height = models.IntegerField(default=0)  #身高厘米，整形
    weight = models.IntegerField(default=0)  #体重斤，整形
    appearance = models.IntegerField(default=0) #外表，满分10分，整形
    character = models.CharField(max_length=20,default='')  #性格，字符串描述，关键字匹配算法
    education = models.CharField(max_length=20,default='')  #学历，字符串描述，关键字匹配算法

    def __str__(self):
        return self.wechat


class DB_want(models.Model): #注意，其中按照人类习惯，，如年龄稍小加分就比稍大高，但没有正好高。
    height =  models.IntegerField(default=0)  #身高厘米，整形
    money = models.IntegerField(default=0)  #年收入，整形
    education = models.CharField(max_length=20,default='')  #学历，字符串描述，关键字匹配算法
    age = models.IntegerField(default=0)  #年龄，整形
    adress = models.CharField(max_length=20,default='')  #地址，字符串类型，最大长度20，默认值为空字符串

    user_info = models.ForeignKey(DB_userInfo,on_delete=models.CASCADE,related_name='user_info') #设置外键

    def __str__(self):
        return str(self.user_info)

