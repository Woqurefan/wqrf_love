from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import json
from myapp.models import *
from django.db.models import Q
import random
from difflib import SequenceMatcher

# Create your views here.

def search(request):
    wechart_value = request.GET['wechart_value']
    user = DB_userInfo.objects.filter(wechat=wechart_value)
    want = user[0].user_info.all()
    res = {}
    res['userInfo'] = list(user.values())[0]
    res['want'] = list(want.values())[0]
    return HttpResponse(json.dumps(res),content_type='application/json')

def add_user(request):
    userInfo_value = json.loads(request.POST.get('userInfo_value'))
    want_value = json.loads(request.POST.get('want_value'))
    new_user = DB_userInfo(**userInfo_value)
    new_user.save()
    want_value['user_info'] = new_user
    new_want = DB_want(**want_value)
    new_want.save()
    return HttpResponse('')

def del_user(request):
    id = request.GET['id']
    DB_userInfo.objects.filter(id=id).delete()
    return HttpResponse('')


def get_user(request):
    id = request.GET['id']
    user = DB_userInfo.objects.filter(id=id)
    content = '【个人信息】：\n'
    for key in user.values()[0].keys():
        content += key+' : '+ str(user.values()[0][key]) + '\n'

    content += '\n【择偶要求】：\n'
    want = user[0].user_info.all()
    for key in want.values()[0].keys():
        content += key+' : '+ str(want.values()[0][key]) + '\n'

    res={"content":content}
    return HttpResponse(json.dumps(res),content_type='application/json')



def match_user(request):
    uid = request.GET['uid']
    user_info = DB_userInfo.objects.filter(id=uid)[0]  # 会员个人信息
    user_want = user_info.user_info.all()[0] # 会员择偶信息
    others_info = DB_userInfo.objects.filter(~Q(sex=user_info.sex)).all() #其他性别会员个人信息
    data = []
    for other_info in others_info:
        other_want = other_info.user_info.all()[0]
        tmp = {}
        tmp['weChat'] = other_info.wechat
        tmp['Ouid'] = other_info.id
        tmp['Iscore'] = get_score(user_want,other_info)
        tmp['Oscore'] = get_score(other_want,user_info)
        tmp['probability'] = (tmp['Iscore']+tmp['Oscore'])/2  #别吐槽，算法以后再优化！
        data.append(tmp)
    # 排序
    data = sorted(data,key=lambda x:x["probability"],reverse=True)
    # 整理并返回
    res = {"match_result":data}
    return HttpResponse(json.dumps(res),content_type='application/json')

def get_score(want,info):
    score_height = (info.height - want.height)*10
    score_money = (info.money - want.money) /1000
    education_levels = ['下忍','中忍','上忍','影','小学','初中','高中','专','本','研','博']
    want_edu =  [i for i in range(len(education_levels)) if education_levels[i] in want.education] #算下标
    info_edu =  [i for i in range(len(education_levels)) if education_levels[i] in info.education] #算下标
    try:
        score_education = (info_edu - want_edu)*50
    except:
        score_education = -100
    score_age = (want.age - info.age)*20
    score_adress = SequenceMatcher(None, want.adress, info.adress).ratio()*100
    score = score_height*0.2 + score_money*0.2 + score_education*0.2 + score_age*0.2 + score_adress*0.2
    return float('%.1f'%score)

