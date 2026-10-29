# Temperature
def temperature(temp):
    if temp < 15:
        return 1
    elif temp <= 30:
        return  0
    else:
        return  2
#Humidity 
def humidity(hum):
    if hum < 30:
        return 1
    elif hum>= 30 and hum <= 60:
        return 0
    elif hum> 60 and hum <= 80:
        return 1  
    else: 
        return 2
#wind speed
def wind_speed(ws):
    if  0<=ws<= 15:
        return 0
    elif ws <= 30:
        return 1
    else:
        return 2
#AQI
def AQI(aqi):
    if  0<=aqi<=50:
        return 0
    elif aqi <= 100:
        return 1
    else:
        return  2
#UV index
def UV_Index(uv):
    if 0<=uv<=2:
        return 0
    elif  uv <= 5:
        return 1
    elif uv <= 7:
        return 2
    else:
        return 2
# Age
def age(a):
    if 0<=a<=12:
        return 1
    elif a<=59:
        return 0
    else:
        return 1
# occupation
def occupation(oc):
    if oc == "Indoor":
        return 0
    elif oc == "Mixed":
        return 1
    elif oc == "Outdoor":
        return 2
    else:
        return 0
#  Health condition         
def health_condition(hc):
    if hc == "nil":
        return 0
    elif hc == "Asthma":
        return 2
    elif hc == "respiratory related problems":
        return 2
    else:
        return 1

temp_s = temperature(float(input("temperature =")))
hum_s = humidity(int(input("Humidity =")))
ws_s = wind_speed(float(input("Wind Speed =")))
aqi_s = AQI(int(input("AQI =")))
uv_s = UV_Index(int(input("UV Ind/ex =")))
age_s = age(int(input("Age =")))
occupation_s = occupation(input("Occupation ="))
health_s = health_condition(input("Health condition ="))

total_risk = (aqi_s*4) + (temp_s*3) + (hum_s*4) + (hum_s*2) + (uv_s*2) + (ws_s) + (occupation_s) + (age_s)

if  0<=total_risk<=8:
    print("Risk is low")
elif total_risk<=18:
    print("Risk is moderate")
else:
    print("Risk is high")

  