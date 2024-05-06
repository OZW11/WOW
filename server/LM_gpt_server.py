# encoding: utf-8
import uuid
import time
import requests
from auth_util import gen_sign_headers




#参数message_to_send需要一个json数组形如:
#             [
#             {
#                 "role": "user",
#                 "content": "你能告诉我什么是人工智能吗？"
#             },
#             {
#                 "role": "assistant",
#                 "content": "人工智能是指由人制造出来的系统能够模拟人类智能行为的技术。它包括机器学习、自然语言处理、计算机视觉等多个领域。"
#             },
#             {
#                 "role": "user",
#                 "content": "那么机器学习又是什么呢？"
#             },
#             {
#                 "role": "assistant",
#                 "content": "机器学习是人工智能的一个分支，它让计算机能够通过数据分析和模式识别来学习和改进，而无需每一步都进行明确的编程。"
#             },
#             {
#                 "role": "user",
#                 "content": "机器学习有哪些应用呢？"
#             }
#             ]
def sync_vivogpt(message_to_send,APP_ID,APP_KEY):
    URI = '/vivogpt/completions'
    DOMAIN = 'api-ai.vivo.com.cn'
    METHOD = 'POST'
    params = {
        'requestId': str(uuid.uuid4())
    }
    print('requestId:', params['requestId'])

    data = {
        "messages": message_to_send,
        'model': 'vivo-BlueLM-TB',
        'sessionId': str(uuid.uuid4()),
        'extra': {
            'temperature': 0.9
        }
    }
    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)
    headers['Content-Type'] = 'application/json'

    start_time = time.time()
    url = 'https://{}{}'.format(DOMAIN, URI)
    response = requests.post(url, json=data, headers=headers, params=params)

    if response.status_code == 200:
        res_obj = response.json()
        print(f'response:{res_obj}')
        if res_obj['code'] == 0 and res_obj.get('data'):
            content = res_obj['data']['content']
            print(f'final content:\n{content}')
            return content
    else:
        print(response.status_code, response.text)
        temp=str(response.status_code)+" "+str(response.text)
        return "ERROR: {}".format(temp)
    end_time = time.time()
    timecost = end_time - start_time
    print('请求耗时: %.2f秒' % timecost)



