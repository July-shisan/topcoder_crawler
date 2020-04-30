#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from Utils import *
import json
import xlwt

def test():
    begin = 30055549
    end = 30095032
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

def getChallenge():
    begin = 30055549
    end = 30055570
    # col = ['challengeType', 'challengeName', 'challengeId', 'detailedRequirements', 'technology']
    # workbook = xlwt.Workbook()
    # sheet1 = workbook.add_sheet('sheet1')
    # for i in range(0, len(col)):
    #     sheet1.write(0, i, col[i])
    # workbook.save('challenge.xls')
    # row = 1
    with open('ch_detail.json', 'w') as d:
        d.write('{' + '\n')
        d.write('  "RECORDS": [' + '\n')
    for challengeId in range(begin, end + 1, 1):
        if challengeId % 10 == 0:
            print(challengeId)
        challenge_detail = ChallengeDetail(challengeId) # dict
        if challenge_detail != None:
            with open('ch_detail.json', 'a') as d:
                json.dump(challenge_detail, d, indent=4)
                if challengeId != end:
                    d.write(',')
                d.write('\n')
        #     for i in range(0, len(col)):
        #         if col[i] in challenge_detail.keys():
        #             sheet1.write(row, i, challenge_detail[col[i]])
        # row += 1
        # workbook.save('challenge.xls')
            # chaReg = Challeng_Registrant(challengeId) # list
            # chaTime = Challeng_Time(challengeId) # dict
            # chaTime['challengeId'] = challengeId
            # chaSub = Challeng_Submission(challengeId) # dict
            # chaSub['challengeId'] = challengeId

            # if chaReg != None:
            #     data = {'challengeId': challengeId}
            #     chaReg.insert(0, data)
            #     with open('ch_registrant.json', 'a') as r:
            #         json.dump(chaReg, r)
            # with open('ch_time.json', 'a') as t:
            #     json.dump(chaTime, t)
            # with open('ch_submission.json', 'a') as s:
            #     json.dump(chaSub, s)
    with open('ch_detail.json', 'a') as d:
        d.write(']' + '\n')
        d.write('}')


def getRegistrant():
    begin = 30055549
    end = 30095032
    for challengeId in range(begin, end + 1, 1):
        chaReg = Challeng_Registrant(challengeId)  # list
        for i in range(0, len(chaReg)):
            if type(chaReg[i]) == dict and chaReg != None:
                with open('usernamme.txt', 'a') as f:
                    f.write(str(chaReg[i]['handle']))
                    f.write('\n')
def getUser():
    user_index = ['handle', 'country', 'memberSince']
    count = 0
    with open('user.json', 'w') as d:
        d.write('{' + '\n')
        d.write('  "RECORDS": [' + '\n')
    with open("usernamme.txt", "r") as f:
        for line in f.readlines():
            username = line.strip('\n')
            if count % 10 == 0:
                print('count:', count, 'handle:', username)
            count += 1
            # print(username)
            user_base = User(username)
            if user_base != None and type(user_base) == 'dict':
                # print(user_base)
                user = {}
                skill = getUserSkill(username)
                if type(skill['result']['content']) == 'dict':
                    skill_dict = skill['result']['content']['skills']
                    skills = []
                    for key in skill_dict:
                        user_skill = skill_dict[key]['tagName']
                        skills.append(user_skill)
                        # print(user_skill)
                    for i in user_index:
                        user[i] = user_base[i]
                    user['skills'] = skills
                    with open('user.json', 'a') as d:
                        json.dump(user, d, indent=4)
                        d.write(',')
                        d.write('\n')
    with open('user.json', 'a') as d:
        d.write(']' + '\n')
        d.write('}')

if __name__ == '__main__':
    # test()
    getUser()
    # getRegistrant()
    # getChallenge()

