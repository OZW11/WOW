from socket import *
import json

if __name__ == '__main__':
    IP='127.0.0.1'
    PORT=8080
    BUFSIZE=2048
    with open('D:\\repo\\vue\\project\\server\\img.jpg','rb') as f:
        data_test_chat = f.read()

    #print(data_test_json)

    client_socket = socket(AF_INET,SOCK_STREAM)
    client_socket.connect((IP,PORT))

    while True:
        # toSend = input('test_to_send:')
        # if toSend =='':
        #     break
        
        What_to_Send =data_test_chat
        client_socket.send('imgTest'.encode('utf-8'))
        if( client_socket.recv(BUFSIZE).decode('utf-8') != 'imgTest_OK'):
            break
        client_socket.send(str(len(What_to_Send)).encode('utf-8'))

        while  client_socket.recv(BUFSIZE).decode('utf-8') == 'READY':
            have_send = client_socket.send(What_to_Send[0:BUFSIZE])
            What_to_Send = What_to_Send[have_send:]
            if len(What_to_Send) == 0:
                break

        receive = client_socket.recv(BUFSIZE)
        if not receive:
            break
        print(receive.decode('utf-8'))
    client_socket.close()













    # # ----------------------------------------------------------------











# from socket import *
# import json

# if __name__ == '__main__':
#     IP='127.0.0.1'
#     PORT=8080
#     BUFSIZE=2048
#     data_test_chat={
#         'message': [
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
#                 "content": "你能告诉我什么是人工智能吗？"
#             },
#             {
#                 "role": "assistant",
#                 "content": "人工智能是指由人制造出来的系统能够模拟人类智能行为的技术。它包括机器学习、自然语言处理、计算机视觉等多个领域。"
#             },
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
#             ]}
#     data_test_chat_json=json.dumps(data_test_chat)
#     #print(data_test_json)

#     client_socket = socket(AF_INET,SOCK_STREAM)
#     client_socket.connect((IP,PORT))

#     while True:
#         # toSend = input('test_to_send:')
#         # if toSend =='':
#         #     break
        
#         What_to_Send =data_test_chat_json.encode('utf-8')
#         client_socket.send('chat'.encode('utf-8'))
#         if( client_socket.recv(BUFSIZE).decode('utf-8') != 'chat_OK'):
#             break
#         client_socket.send(str(len(What_to_Send)).encode('utf-8'))

#         while  client_socket.recv(BUFSIZE).decode('utf-8') == 'READY':
#             have_send = client_socket.send(What_to_Send[0:BUFSIZE])
#             What_to_Send = What_to_Send[have_send:]
#             if len(What_to_Send) == 0:
#                 break

#         receive = client_socket.recv(BUFSIZE)
#         if not receive:
#             break
#         print(receive.decode('utf-8'))
#     client_socket.close()

#     # # ----------------------------------------------------------------
#     # # command说明，所有的参数要转json格式后utf-8编码发送
#     """
#     1.chat
#     要求传入message,表示之前的对话,直接返回一个单独的字符串
#     {
#         'message': [
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
#             ]}
    
#     """
#     #----------------------------------------------------
#     #














#     # # ----------------------------------------------------------------
