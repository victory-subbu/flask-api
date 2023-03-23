import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()

options.add_argument("start-maximized")
options.add_argument("disable-extensions")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
from flask import Flask,request
app=Flask(__name__)

@app.route("/attendance/<rollnumber>/<password>",methods=["POST","GET"])
def attendance(rollnumber,password):
    
    options = Options()

    options.add_argument("start-maximized")
    options.add_argument("disable-extensions")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    
    driver.get("https://vce.ac.in/")
#window_before = driver.window_handles[0]
    vce_roll = rollnumber
    vce_pass = password
    username= driver.find_element(By.NAME, "LoginID").send_keys(vce_roll)
    password = driver.find_element(By.NAME, "Password").send_keys(vce_pass)
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    driver.forward()
    driver.get("https://vce.ac.in/student_info.aspx")
    driver.find_element(By.LINK_TEXT, "View").click()
    window_before = driver.window_handles[0]
    driver.switch_to.window(driver.window_handles[1])
    x=driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]/table[9]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[5]/td[4]/font[1]")
    print(x.text)

    return {"result": x.text}





    
    

if __name__== '__main__':
    app.run(debug=False,port=2000,threaded=True,host="0.0.0.0")