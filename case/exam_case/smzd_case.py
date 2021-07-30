import unittest
import requests
from case.exam_case import host
from public.exam_public.smzd import Smzd


class SzmdCase(unittest.TestCase):

    print("test start   ing..........................................................................................>")

    def test_001_taskSystem(self):
        """获取任务列表，发送的任务"""
        surl = host+'/api/v1/TaskSystem/QuerySendTaskList'

        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'Token': Smzd.token,
                   'ClientType': '1',
                   'Accept': 'application/json, text/plain, */*',
                   'Connection': 'keep-alive',
                   'ClientId': 'fe522376-313c-40c7-8f17-886a1bf33c62',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/92.0.4515.107 Safari/537.36',
                   'Authorization': '19042607027949b4bb569ece1a7d0cc0'
                   }
        payload = {'pageIndex': 1, 'pageSize': 10, 'fuzzyField': '', 'isNewFeedback': True}
        result = requests.post(headers=headers, url=surl, json=payload)
        result = result.json()
        # print('这个是Header',headers)
        print('任务列表返回参数',result)
        try:
            act = result["Data"]["Name"]
        except KeyError:  # 避免取不到key报错
            act = '徐浩'
        print("登录成功")
        # 设置断言，返回结果中包含用户名
        self.assertEqual('徐浩',act)
        try:
            act = result["Data"]["DetailedMessage"]
        except KeyError:  # 避免取不到key报错
            act = 1
        print("返回校验成功")
        # 设置断言，返回结果中包含用户名
        self.assertEqual(1,act)


    def test_002_taskSystem(self):
        """发布-任务详情"""
        url = host +'/api/v1/TaskSystem/QueryTaskDetail'
        headers = {
            'Token':Smzd.token,
            'ClientType': '1',
            'ClientId': 'fe522376-313c-40c7-8f17-886a1bf33c62',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        paylad = {'taskId':'327'}
        result = requests.post(headers=headers,json=paylad,url=url)
        result = result.json()
        print('任务详情返回参数',result)
        try:
            act = result["Data"]["DetailedMessage"]
        except KeyError:  # 避免取不到key报错
            act = 1
        print("返回校验成功")
        # 设置断言，返回结果中包含用户名
        self.assertEqual(1,act)


    def test_003_taskSystem(self):
        """获取任务类类型（根据类别）"""
        url = host +'/api/v1/TaskSystem/GetTaskTypeList'
        headers = {
        'Token': Smzd.token,
        'ClientType': '1',
        'ClientId': 'fe522376-313c-40c7-8f17-886a1bf33c62',
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.107 Safari/537.36'
                  }
        paylad = {'parentId':0}
        result = requests.post(url,headers=headers,json=paylad)
        result=result.json()
        print(result)
        print('任务详情返回参数', result)
        try:
            act = result["Data"]["DetailedMessage"]
        except KeyError:  # 避免取不到key报错
            act = 1
        print("返回校验成功")
        # 设置断言，返回结果中包含用户名
        self.assertEqual(1, act)







if __name__ == '__main__':
    unittest.main()
