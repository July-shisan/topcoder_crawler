#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from Utils import *
import json
import xlwt

begin = 30055549
end = 30095032
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


if __name__ == '__main__':
    # test()
    # getRegistrant()
    getChallenge()

