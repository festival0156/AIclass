clnt = '192.168.43.1', 50531
serv = ''            , 8765

import socket as sm
s = sm.socket(sm.AF_INET, sm.SOCK_STREAM)
s.bind(con2)
s.listen(0)
cl = r.accept()
sv = sm.socket(sm.AF_INET, sm.SOCK_STREAM)
sv.connect(serv)

c2s = list()
s2c = list()

def c2sf():
    while True:
        b = cl.recv(1)
        c2s.append(b)
        sv.send(b)
def s2cf():
    while True:
        b = sv.recv(1)
        s2c.append(b)
        cl.send(b)
