import socket as s

con2 = '', 5557
with s.socket(s.AF_INET, s.SOCK_STREAM) as sock:
	sock.bind(con2)
	sock.listen(5)
	print('Server started @ ' + str(con2[0]) + ':' + str(con2[1]))
	cl, addr = sock.accept()
	print('Client connected IP:', addr)

	running = True
	while running:
		ch = cl.recv(1)
		def zero(soc):
			from subprocess import check_output
			cmd = soc.recv()
