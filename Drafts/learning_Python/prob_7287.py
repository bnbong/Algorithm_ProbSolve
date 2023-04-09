# 자신이 백준 온라인 저지(BOJ)에서 맞은 문제의 수와 아이디를 그대로 출력 (solvedac 비공식 라이브러리를 통해 구현한 버전)
import requests
import json

def get_raw_data_via_url(url):
    raw_data_data = requests.get(url)
    
    return raw_data_data

def decode_raw_data(data):
    decoded_data = data.content.decode('utf-8')

    return decoded_data

def get_user_and_solved_problems_from_data(raw_profile_data):
    decoded_profile_data = decode_raw_data(raw_profile_data)
    profile_data = json.loads(decoded_profile_data)

    user_name = profile_data.get('handle')
    solved_probs = profile_data.get('solvedCount')

    return user_name, solved_probs

def prob_7287():
    url = f"https://solved.ac/api/v3/user/show?handle=bnbong"

    raw_profile_data = get_raw_data_via_url(url)
    user_name = ''
    solved_probs = 0
    if raw_profile_data.status_code == requests.codes.ok:
        user_name, solved_probs = get_user_and_solved_problems_from_data(raw_profile_data)

    # expected data(example):
    #   50
    #   bnbong    
    print(solved_probs)
    print(user_name)


prob_7287()