import const
import requests
import zmq, time

def cotation():
    response = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
    json = response.json()['USDBRL']
    return json['ask']

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(f"tcp://*:{const.PORT}")
while True:
    msg = "TIME " + time.asctime() + " R$" + cotation()
    socket.send(msg.encode())
    time.sleep(300)
