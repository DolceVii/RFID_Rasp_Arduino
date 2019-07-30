# !/usr/bin/python3

import RPi.GPIO as GPIO
import sqlite3
import time
import serial
import datetime

global database
global who
global username
global data
global runok

runok = 0

database = "/var/www/html/database/raspberry.db"

username = "Άγνωστος"
who = "Άγνωστο"
now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

DoorRelay = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DoorRelay, GPIO.OUT)

def main():

    def rserial():
        global who
        global runok
        try:
            ser=serial.Serial("/dev/ttyUSB0",9600)
            ser.baudrate = 9600
            who = str(ser.readline().decode("utf-8").strip())
            who = who.lstrip("b")
            who = who.strip("'")
            who = who.rstrip("\\r\\n")
            who = who.rstrip(" ")
            ser.close()
            runok == 0
        except Exception:
            print("Error USB chek usb connection and try again")
            runok = 1
    
    def wsql():
        global who
        global username
        global runok
        if username == "None":
            username = "Άγνωστος"
        try:
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            val = ('1', who, username, now, data)
            cursor.execute ("INSERT INTO data (door, who, UserName, day, isactive) VALUES (?, ?, ?, ?, ?)", (val))
            connection.commit()
            connection.close()
            runok == 0
        except Exception:
            print("Error MySQL check Mysql server and try again")
            runok = 1

    def rsql():
        global who
        global data
        global username
        global runok
        try:
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute('SELECT count(*) FROM active WHERE activerfid = 1 AND userrfid = ?', (who,))
            data = cursor.fetchone()[0]
            cursor.execute('SELECT UserName FROM active WHERE userrfid = ?', (who,))
            username = cursor.fetchone()
            username = str(username)
            username = username.replace("('","")
            username = username.replace("',)","")
            connection.close()
            runok == 0
        except Exception:
            print("Erorr SQL connection check and try again")
            runok = 1

    while True:
        global username
        if runok == 0:
            rserial()
        if runok == 0:
            rsql()
        if runok == 0:
            wsql()
        
            if username == "None":
                username = "Άγνωστος"
            
            if data == 1:
                print("The user: " + username + ", with ID: " + who + ", has access!")
                GPIO.output(DoorRelay, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(DoorRelay, GPIO.LOW)
            else:
                print("The user: " + username + ", with ID: " + who + ", has no access!")
                GPIO.output(DoorRelay, GPIO.LOW)
            
            time.sleep(3)

if __name__== "__main__":
    main()
