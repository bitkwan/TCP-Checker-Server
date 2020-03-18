# TCP-Checker-Server
# Sebastian S

import subprocess,os
from flask import Flask,request,json
app = Flask(__name__)

token_l = "LOCAL_TOKEN"
server_ip = "0.0.0.0"
server_port = 8123
debug_toggle = False

@app.route('/quote')
def check():
	server = request.args.get('s')
	port = request.args.get('p')
	token = request.args.get('t')
	if token != token_l:
		arr = {'status':0, 'msg': 'wrong token'}
	elif server is None:
		arr = {'status':0, 'msg': 'empty server'}
		#return arr
	elif port is None:
		arr = {'status':0, 'msg': 'empty port'}
	else:
		cmd = 'tcping -x 2 -w 5 {} {}'.format(server, port)
		#print(cmd)
		out_bytes = os.popen(cmd).read()
		#print(out_bytes)
		if "open" in out_bytes:
			arr = {'status':1}
		elif "closed" in out_bytes:
			arr = {'status':1}
		elif "refused" in out_bytes:
			arr = {'status':1}
		else:
			arr = {'status':-1}
	return "result("+json.dumps(arr)+")"

if __name__ == '__main__':
    app.run(host=server_ip,port=server_port,debug=debug_toggle)
