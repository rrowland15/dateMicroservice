import zmq
import re
import datetime


def read_request():
    # Wait for user to send request
    message_rcvd = False
    while not message_rcvd:
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://127.0.0.1:5555") # tcp socket 2
        metadata = socket.recv().decode('utf-8')
        print(metadata)
        pattern = '''\d{4}\:\d{2}\:\d{2}'''
        date = re.search(pattern,metadata)
        print(date)
        pattern2 = '''\s{1}(\d{2}\:\d{2}\:\d{2})'''
        time = re.search(pattern2,metadata)
        print(time)
        if date:
            context = zmq.Context()
            socket = context.socket(zmq.REQ)
            socket.connect("tcp://127.0.0.1:5557")
            result = date.group()
            result = result.split(":")
            result2 = time.group()
            result2 = result2.split(":")
            date_object = (result[0] + "-" + result[1] + "-" + result[2] + " " + result2[0] + ":" + result2[1] + ":" + result2[2])
            print(date_object)
            socket.send_string(str(date_object))
        else:
            socket.send_string("None")

read_request()

