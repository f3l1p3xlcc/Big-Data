import requests
import json
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='user', password='pass', database='database')
cursor = mariadb_connection.cursor()

fechahora = '2019-02-21 16:00:00';
    
response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=V8XPNGS08JKJTUUI')
assert response.status_code == 200
json_data = json.loads(response.text)
json_data1 = json_data['Time Series (5min)'][fechahora]['4. close']
print(json_data1)

response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=GOOGL&interval=5min&apikey=V8XPNGS08JKJTUUI')
assert response.status_code == 200
json_data = json.loads(response.text)
json_data2 = json_data['Time Series (5min)'][fechahora]['4. close']
print(json_data2)

response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=5min&apikey=V8XPNGS08JKJTUUI')
assert response.status_code == 200
json_data = json.loads(response.text)
json_data3 = json_data['Time Series (5min)'][fechahora]['4. close']
print(json_data3)

response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=INTC&interval=5min&apikey=V8XPNGS08JKJTUUI')
assert response.status_code == 200
json_data = json.loads(response.text)
json_data4 = json_data['Time Series (5min)'][fechahora]['4. close']
print(json_data4)

response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AMGN&interval=5min&apikey=V8XPNGS08JKJTUUI')
assert response.status_code == 200
json_data = json.loads(response.text)
json_data5 = json_data['Time Series (5min)'][fechahora]['4. close']
print(json_data5)

try:
    cursor.execute("INSERT INTO precios (BESALCO, CCU, CONCHATORO, ENELCHILE, FALABELLA, ILC, MULTIFOODS, PARAUCO, SMSAAM, VAPORES) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (float(json_data1), float(json_data2), float(json_data3), float(json_data4), float(json_data5), 1.6, 1.7, 1.8, 1.9, 1.1))
except mariadb.Error as error:
    print("Error: {}".format(error))

mariadb_connection.commit()
print("The last inserted id was: ", cursor.lastrowid)

mariadb_connection.close()


