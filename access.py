from flask import Flask,request
import requests

app = Flask(__name__)

port = 10001
@app.route('/access')
def get_internet():
    response = ''
    ips = request.args.get('ips')
    ip_list = ips.split(',')
    for ip in ip_list:
        resp = requests.get('http://%s' %ip)
        response = response + "reponse from %s=%s\n" %(ip, resp)
    return response   

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
