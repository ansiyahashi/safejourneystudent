from DBConnection import Db
import serial

# serialPort = serial.Serial(port="COM3")
serialPort = serial.Serial('COM3', 9600)
serialString = ""                           # Used to hold data coming over UART
mm=""
counter=0
studentlogid=""
while(True):
        serialString = serialPort.read().decode('utf-8')
        mm=mm+serialString
        if len(mm)==12:
            print(mm)
            if counter == 0:  # first student rfid scanned

                db = Db()
                qry = "select * from myapp_student where rfid='" + mm + "'"
                print(qry)
                mm = ""
                res = db.selectOne(qry)
                if res is not None:
                    stud_id=res['id']
                    qry1="SELECT * FROM `myapp_attendance` WHERE `date`=CURDATE() AND `STUDENT_id`='"+str(stud_id)+"'"
                    res1=db.selectOne(qry1)
                    if res1 is None:
                        db.insert("INSERT INTO `myapp_attendance`(`date`,`status`,`STUDENT_id`,`time`) VALUES(CURDATE(),'present','"+str(stud_id)+"',CURTIME())")
                    else:
                        db.update("UPDATE `myapp_attendance` SET `time`=CURTIME() WHERE id='"+str(res1['id'])+"'")