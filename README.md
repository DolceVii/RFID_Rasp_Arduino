# RFID_Rasp_Arduino
A code for reading RFID from Arduino via USB from Rasp. Raspberry code for read &amp; write sqlite3. 
Arduino code for reading RC522 RFID.

A system that reads RFID cards. The data are "read" by arduino and the results are sent via USB to Raspberry. 
(It was decided to do this because there is a difficulty in the raspberry library. 30% CPU LOAD.)
Raspberry reads the data from USB and checks from the sqlite database if the ID of that card corresponds to an registered account
and checks if user has access. Raspberry records the movement on the sqlite database and gives the user access to door (if it has it).

The arduino library can be downloaded from: https://github.com/miguelbalboa/rfid

Also read: https://playground.arduino.cc/Learning/MFRC522/

Help to install sqlite3 to Raspberry Pi: https://randomnerdtutorials.com/sqlite-database-on-a-raspberry-pi/

Help to install phpliteadmin to Raspberyy Pi: http://www.raspberrypirobotics.com/how-to-install-phpliteadmin-database/
