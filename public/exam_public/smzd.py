import requests
import self as self

from case.exam_case import host


def __init__(self, requests):
    self.requests = requests  # 设置全局参数


class Smzd:

    print("Login  start  .........................................................................................>")

    def Smzdlogin(self, token):
        """登录获取token等信息"""
        self.smzd_token = token
        # 调用登录接口
    url_login = host+"/api/v1/Login/SingleSignOnByLoginId"
    # 传入用户名和密码
    payload = {'loginId': '13671679931', 'clientType': 1, 'systemId': 56, 'loginPwd': '679931',
               'isExclusiveLogin': True, 'clientId': 'fe522376-313c-40c7-8f17-886a1bf33c62'}
    # 返回结果赋值给result
    result = requests.post(url_login, json=payload)
    # 将返回结果转为json格式
    result = result.json()
    print('登录返回参数',result)
    token = result["Data"]["Token"]
    # try:
    #     act = result["Data"]["Name"]
    # except KeyError:  # 避免取不到key报错
    #     act = '徐浩'
    #     print('登录成功')
    #       # 设置断言，返回结果中包含用户名
    #     self.assertEqual(act, '徐浩')
    # print('这个是登录成功的token'+token)
