import itchat, time, sys,os
from django.http import HttpResponse
from django.shortcuts import render_to_response
# * 获取二维码uuid
# * 获取二维码
# * 判断是否已经登陆成功

def start_itchat(request):
    request.encoding='utf-8'
    context = {}
    if 'id' in request.GET:
        id = request.GET['id']
        uuid = open_QR(id)
        path = 'images?path='+id + '.png'
        context = {'id':id,'path':path}
        print(context)
        return render_to_response('login.html',context)
    else:
        message = '你提交了空表单'
        return HttpResponse(message)

def get_qrcode(request):
    request.encoding='utf-8'
    context = {}
    if 'id' in request.GET:
        id = request.GET['id']
        uuid = open_QR(id)
        path = os.path.join('images/%s.png'% id )
        context = {id:id,path:path}
        return render_to_response('login.html',context)
    else:
        message = '你提交了空表单'
        return HttpResponse(message)

# 返回消息
def output_info(msg):
    print('[INFO] %s' % msg)

def open_QR(id):
    for get_count in range(10):
        output_info('Getting uuid')
        uuid = itchat.get_QRuuid()
        while uuid is None: uuid = itchat.get_QRuuid();time.sleep(1)
        output_info('Getting QR Code')
        if itchat.get_QR(uuid,picDir='images/%s.png'% id ): break
        elif get_count >= 9:
            output_info('Failed to get QR Code, please restart the program')
            sys.exit()
    output_info('Please scan the QR Code')
    return uuid

# uuid = open_QR()
# waitForConfirm = False
# while 1:
#     status = itchat.check_login(uuid)
#     if status == '200':
#         break
#     elif status == '201':
#         if waitForConfirm:
#             output_info('Please press confirm')
#             waitForConfirm = True
#     elif status == '408':
#         output_info('Reloading QR Code')
#         uuid = open_QR()
#         waitForConfirm = False