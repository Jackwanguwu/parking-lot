import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sqlalchemy import create_engine
import pymysql
from sqlalchemy import text
from pyecharts import  options as opts
from  pyecharts.charts import Line
from  pyecharts.globals import ThemeType
import matplotlib.pyplot as plt

class statistics(object):
    def databaseconnecter(self):

        DIALECT = 'mysql'
        DRIVER = 'pymysql'
        USERNAME = 'root'
        PASSWORD = 'Zyn20020926'
        HOST = '127.0.0.1'
        PORT = '3306'
        DATABASE = 'jobdb'

        SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD,
                                                                               HOST, PORT,
                                                                               DATABASE)

        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        with engine.connect() as con:
            df = pd.read_sql_table('parkbill', con=con)
            df = df.dropna()
        return df
    def linechart(self):

        df=self.databaseconnecter()
        df['intime'] = pd.to_datetime(df['intime'])
        df = df.set_index('intime')

        df = df.drop(['outtime', 'parktime', 'hour', 'carnumber'], axis=1)
        df_daily = df.resample('D').sum()

        index = df_daily.index.astype(str)
        columns_fee_loc = df_daily.loc[:, ['fee']]

        x = index # x 轴数据
        y = df_daily['fee']  # y 轴数据
        plt.figure(facecolor='lightgray')
        plt.figure(figsize=(8, 6))
        plt.fill_between(x, y, color='lightblue', alpha=0.3)
        plt.plot(x, y)

        plt.title('折线图')
        plt.xlabel('横轴')
        plt.ylabel('纵轴')
        plt.grid(True)
        plt.plot(x, y, color=(0.5, 0.2, 0.8))
        plt.show()




c=statistics()

c.linechart()



