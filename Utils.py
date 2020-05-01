#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# BUAA ACT
# guohua 20200501
from urllib.request import Request, urlopen
import urllib.error as err
import json

# challenge url
CHALLENGE_BASE_URL = "http://api.topcoder.com/v2/challenges/"
REGISTRANT_URL = "http://api.topcoder.com/v2/challenges/registrants/"
PHRASE_URL = "http://api.topcoder.com/v2/challenges/phases/"
SUBMISSION_URL = "http://api.topcoder.com/v2/challenges/submissions/"

# user url
USER_URL = "http://api.topcoder.com/v2/users/"
SKILL_URL = "http://api.topcoder.com/v3/members/"

def getChallengeDetail(challengeId):
    request = Request(CHALLENGE_BASE_URL + str(challengeId))
    try:
        response_body = urlopen(request).read()
    except err.URLError as e:
        print(challengeId, ': URLError:', e.reason)
        return 0
    except:
        print(challengeId, ': Unknown Error!')
        return 0
    else:
        response_body = json.loads(response_body)
        index = ['challengeType', 'challengeName', 'challengeId', 'detailedRequirements', 'technology']
        challenge_detail = response_body['challengeType']
        for x in index:
            if not response_body[x]:
                challenge_detail += ';'
            else:
                challenge_detail += ';' + str(response_body[x])
        challenge_detail += '\n'
        return challenge_detail
# challenge base info
def ChallengeDetail(challengeId):
    request = Request(CHALLENGE_BASE_URL + str(challengeId))
    try:
        response_body = urlopen(request).read()
    except err.URLError as e:
        print('challengedetail', challengeId, ': URLError:', e.reason)
        return 0
    except:
        print(challengeId, ': Unknown Error!')
        return 0
    else:
        response_body = json.loads(response_body)
        return response_body

# challenge registrants info
def Challeng_Registrant(challengeId):
    request = Request(REGISTRANT_URL + str(challengeId))
    try:
        response_body = urlopen(request).read()
    except err.URLError as e:
        print('register', challengeId, ': URLError:', e.reason)
        return 0
    except:
        print(challengeId, ': Unknown Error!')
        return 0
    else:
        response_body = json.loads(response_body)
        return response_body

# challenge time info
def Challeng_Time(challengeId):
    request = Request(PHRASE_URL + str(challengeId))
    try:
        response_body = urlopen(request).read()
    except err.URLError as e:
        print('cha_time', challengeId, ': URLError:', e.reason)
        return 0
    except:
        print(challengeId, ': Unknown Error!')
        return 0
    else:
        response_body = json.loads(response_body)
        return response_body

# challenge submission info
def Challeng_Submission(challengeId):
    request = Request(SUBMISSION_URL + str(challengeId))
    try:
        response_body = urlopen(request).read()
    except err.URLError as e:
        print('cha_sub', challengeId, ': URLError:', e.reason)
        return 0
    except:
        print(challengeId, ': Unknown Error!')
        return 0
    else:
        response_body = json.loads(response_body)
        return response_body

def User(username):
    request = Request(USER_URL + username)
    try:
        response_body = urlopen(request).read()
    except err.URLError as e:
        print(username, ': UserBase URLError:', e.reason)
        return 0
    except:
        print(username, ':UserBase Unknown Error!')
        return 0
    else:
        response_body = json.loads(response_body)
        return response_body

def getUserSkill(username):
    request = Request(SKILL_URL + username + "/skills")
    try:
        response_body = urlopen(request).read()
    except err.URLError as e:
        print(username, ':skill URLError:', e.reason)
        return 0
    except:
        print(username, ':skill Unknown Error!')
        return 0
    else:
        response_body = json.loads(response_body)
        return response_body
