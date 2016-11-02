
import sys
import time
# This is client library if dont have this install using pip
import paho.mqtt.client as mqtt
import re
import math

import PyQt4


from PyQt4.QtGui import *
from PyQt4 import QtCore

# This is our window from QtCreator
import gui

# global variable
roll=0
pitch=0
lum=0

# Initiate MQTT Client
mqttc = mqtt.Client()

def calculate(string):
    global roll
    global lum
    global pitch
    x,y,z,temp=re.split('/',string)
    roll=round(math.atan2(-float(y),float(z))*180.0/math.pi,2)
    pitch=round(math.atan2(float(x), math.sqrt(float(y)*float(y) + float(z)*float(z)))*180.0/math.pi,2)
    lum=math.ceil(float(temp))

# Define on_connect event Handler
def on_connect(mosq, obj, rc):
    #Subscribe to a the Topic
    mqttc.subscribe("nodemcu/sensor", 0)

# Define on_subscribe event Handler
def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed to MQTT Topic")

# Define on_message event Handler
def on_message(mosq, obj, msg):
    # convert byte to string
    calculate(msg.payload.decode('utf-8'))
    
  
  

        
    


 
# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        







 
# I feel better having one of these
def main():

    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()

    # Register Event Handlers
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_subscribe = on_subscribe

    # user name has to be called before connect - my notes.
    mqttc.username_pw_set("CLOUDMQTT USERNAME", "CLOUDMQTT PASSWORD")
    mqttc.connect('CLOUDMQTT LINK', 'CLOUDMQTT PORT')

    # Update labels with data
    def update_label():
        global roll
        global lum
        global pitch
        form.roll.setText(str(roll))
        form.light.setText(str(lum))
        form.pitch.setText(str(pitch))
    
    timer = QtCore.QTimer()
    timer.timeout.connect(update_label)
    timer.start(1000)

    # Continue the network loop
    mqttc.loop_start()    
    sys.exit(app.exec_())


    
 
# python bit to figure how who started This
if __name__ == "__main__":
 main()















 
