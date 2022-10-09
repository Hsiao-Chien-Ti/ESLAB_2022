import socket 
import json
import numpy as np
import matplotlib.pyplot as plot
HOST = '192.168.0.155'     # IP address
PORT = 65431            # Port to listen on (use ports > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Starting server at: ", (HOST, PORT))
    conn, addr = s.accept()
    with conn:
        print("Connected at", addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            print("Received from socket server:", data)
            if (data.count('{') != 1):
                # Incomplete data are received.
                choose = 0
                buffer_data = data.split('}')
                while buffer_data[choose][0] != '{':
                    choose += 1
                data = buffer_data[choose] + '}'
                
            obj = json.loads(data)
            t = obj['s']
            
            plot.subplot(2, 3, 1)
            plot.scatter(t, obj['x'], c='blue') # x, y, z, gx, gy, gz
            plot.xlabel("sample num")
            plot.ylabel("x")
            plot.title("x vs sample num")
            
            plot.subplot(2, 3, 2)
            plot.scatter(t, obj['y'], c='blue') # x, y, z, gx, gy, gz
            plot.xlabel("sample num")
            plot.ylabel("y")
            plot.title("y vs sample num")
            
            plot.subplot(2, 3, 3)
            plot.scatter(t, obj['z'], c='blue') # x, y, z, gx, gy, gz
            plot.xlabel("sample num")
            plot.ylabel("z")
            plot.title("z vs sample num")
            
            plot.subplot(2, 3, 4)
            plot.scatter(t, obj['gx'], c='blue') # x, y, z, gx, gy, gz
            plot.xlabel("sample num")
            plot.ylabel("gx")
            plot.title("gx vs sample num")
            
            plot.subplot(2, 3, 5)
            plot.scatter(t, obj['gy'], c='blue') # x, y, z, gx, gy, gz
            plot.xlabel("sample num")
            plot.ylabel("gy")
            plot.title("gy vs sample num")
            
            plot.subplot(2, 3, 6)
            plot.scatter(t, obj['gz'], c='blue') # x, y, z, gx, gy, gz
            plot.xlabel("sample num")
            plot.ylabel("gz")
            plot.title("gz vs sample num")
            
            plot.pause(0.1)