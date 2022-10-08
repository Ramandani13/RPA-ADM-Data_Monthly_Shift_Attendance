import pyautogui as pag
from time import sleep
from datetime import datetime,timedelta

def input_tanggal():
	hariini = (datetime.now().strftime("%m-%Y"))
	bln = pag.prompt(title="Masukan Tanggal", default=hariini)
	return bln


sleep(3)
edge = pag.locateCenterOnScreen("edge.png")
print(edge)
pag.moveTo(edge)
pag.click(clicks=2, interval=0.25)


sleep(2)
user = pag.locateCenterOnScreen("userid.png")
print(user)
pag.moveTo(user)
pag.moveTo(user.x , user.y + 30)
pag.click()
pag.write("vu08a12")

password = pag.locateCenterOnScreen("password.png")
print(password)
pag.moveTo(password)
pag.moveTo(password.x , password.y + 30)
pag.click()
pag.write("yamaha06*")

loginbutton = pag.locateCenterOnScreen("login.png")
print(loginbutton)
pag.moveTo(loginbutton)
pag.click()

sleep(2)
reportcenter = pag.locateCenterOnScreen("report-center.png")
print(reportcenter)
pag.moveTo(reportcenter)
pag.click()

sleep(1)
reportcenter = pag.locateCenterOnScreen("reportnew.png")
print(reportcenter)
pag.moveTo(reportcenter)
pag.click()

sleep(1)
rptam = pag.locateCenterOnScreen("rptam.png")
pag.moveTo(rptam)
pag.moveTo(rptam.x - 70 , rptam.y )
pag.click()

sleep(2)
if __name__ == "__main__":
	tglawal = input_tanggal()

sleep(1)
dated = pag.locateCenterOnScreen("date.png")
pag.moveTo(dated)
pag.moveTo(dated.x + 150, dated.y)
pag.click()
pag.press("backspace", presses=10)
pag.write(tglawal)

sleep(2)
dated = pag.locateCenterOnScreen("date.png")
pag.moveTo(dated)
pag.moveTo(dated.x + 190, dated.y + 40)
pag.click()

sleep(1)
alll = pag.locateCenterOnScreen("2222.png")
pag.moveTo(alll)
pag.moveTo(alll.x - 60, alll.y)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("confirm.png")
pag.moveTo(confir)
pag.click()

sleep(1)
export = pag.locateCenterOnScreen("export.png")
pag.moveTo(export)
pag.click()

sleep(25)
cel = pag.locateCenterOnScreen("cel.png")
pag.moveTo(cel)
pag.click()

sleep(2)
ok = pag.locateCenterOnScreen("ok.png")
pag.moveTo(ok)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("exit.png")
pag.moveTo(confir)
pag.click()