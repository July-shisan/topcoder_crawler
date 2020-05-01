#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# BUAA ACT
# guohua 20200501
from Utils import *
import json
import xlwt

begin = 30055549
end = 30095032
# 测试存入txt文件
def test():
    for challengeId in range(begin, end + 1, 1):
        print(challengeId)
        challenge_detail = getChallengeDetail(challengeId)
        # time.sleep(15)
        if challenge_detail != 0:
            items = open('items.txt', 'a')
            items.write(challenge_detail)
            items.close()
            print('get challenge ', challengeId, ' successfully!')
        else:
            print('No data about challenge ', challengeId, ',')

# 爬取challenge
def getChallenge():
    # challengeId 范围
    begin = 30055549
    end = 30055570
    # 按照一定格式写入json文件，便于读入数据库
    with open('ch_detail.json', 'w') as d:
        d.write('{' + '\n')
        d.write('  "RECORDS": [' + '\n')
    for challengeId in range(begin, end + 1, 1):
        if challengeId % 10 == 0:
            print(challengeId)
        # 按照id爬取challenge_detail，获得对应response
        challenge_detail = ChallengeDetail(challengeId) # dict
        if challenge_detail != None and type(challenge_detail) == dict:
            with open('ch_detail.json', 'a') as d:
                json.dump(challenge_detail, d, indent=4)
                if challengeId != end:
                    d.write(',')
                d.write('\n')
    with open('ch_detail.json', 'a') as d:
        d.write(']' + '\n')
        d.write('}')

def getChallengeInfo():
    # 爬取challenge注册信息，发布时间信息和提交信息
    for challengeId in range(begin, end + 1, 1):
        if challengeId % 10 == 0:
            print(challengeId)
        chaReg = Challeng_Registrant(challengeId)  # list
        chaTime = Challeng_Time(challengeId)  # dict
        chaTime['challengeId'] = challengeId
        chaSub = Challeng_Submission(challengeId)  # dict
        chaSub['challengeId'] = challengeId
        if chaReg != None:
            data = {'challengeId': challengeId}
            chaReg.insert(0, data)
            with open('ch_registrant.json', 'a') as r:
                json.dump(chaReg, r)
        with open('ch_time.json', 'a') as t:
            json.dump(chaTime, t)
        with open('ch_submission.json', 'a') as s:
            json.dump(chaSub, s)

if __name__ == '__main__':
    # test()
    getChallenge()

