import csv
import datetime
import pandas as pd
from aip import AipOcr
from sqlalchemy import create_engine


class CamaroCapture(object):

    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def Camaro_image(self):

        filepath='/Users/jackwang/Desktop/python/dataset/dataset.jpg'
        APP_ID = '35025764'
        API_KEY = '5XbZtSU9H5AFLUGG2wuxBaOd'
        SECRET_KEY = '05OMAm5sD0kqN2sFcPvnaokS3C2ID16E'

        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        client.setConnectionTimeoutInMillis(5000)

        with open('/Users/jackwang/Desktop/python/parkinglot/image01.jpg', 'rb') as fp:
            w = fp.read()
        res = client.licensePlate(w)
        data1 = res['words_result']['number']
        processdata01 = data1[5:7]
        arr = []
        arr.append(int(processdata01))
        print(arr)
        print('number：' + res['words_result']['number'])
        print('color：' + res['words_result']['color'])
        print('a car come in')
        t1 = datetime.datetime.now()
        predata = [data1, t1]

        with open('log01.csv', 'a+', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(predata)

        with open('/Users/jackwang/Desktop/python/parkinglot/image02.jpg', 'rb') as fp:
            w = fp.read()
        res = client.licensePlate(w)
        data2 = res['words_result']['number']
        processdata02 = data2[5:7]
        t2 = datetime.datetime.now()
        with open('test.csv', 'a+', encoding='UTF-8', newline='') as f:
            for i in arr:
                if int(processdata02) == i:
                    nowdata = (data2, t1, t2)
                    writer = csv.writer(f)
                    writer.writerow(nowdata)






class Databasetransfer(object):
    def save_parkmessage(self):
        engine = create_engine('mysql+pymysql://root:Zyn20020926@localhost/jobdb')
        df = pd.read_csv('test.csv')
        df.to_sql(name='parkmessage', con=engine, index=False, if_exists='append')

    def save_parkbill(self):
        engine = create_engine('mysql+pymysql://root:Zyn20020926@localhost/jobdb')
        df = pd.read_csv('test.csv')
        df['parktime'] = pd.to_datetime(df['outtime']) - pd.to_datetime(df['intime'])
        df["hour"] = df.parktime.map(lambda x: x.seconds / 3600)
        arr1 = []
        arr2 = []
        arr1 = df['hour'].copy()
        arr2 = df['hour'].copy()
        i = 0
        while (i < len(arr1)):
            if (arr1[i] <= 1):
                arr2[i] =12000*(arr1[i])
            elif (1 < arr1[i] <= 15):
                arr2[i] = 50000 + 15000 * (arr1[i])
            else:
                arr2[i] = 260000
            i = i + 1
        df['fee'] = arr2
        df["hour"] = df.parktime.map(lambda x: x.seconds / 3600)
        df.to_sql(name='parkbill', con=engine, index=False, if_exists='append')


if __name__=='__main__':

    db=Databasetransfer()
    capturepic=CamaroCapture()

    capturepic.Camaro_image()

    db.save_parkbill()
    db.save_parkmessage()
