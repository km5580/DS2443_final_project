import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split,cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing
from db_utils import get_cnx
class Model:
    get_dataframe = """
    SELECT * FROM Insurance;
    """

    def __init__(self) -> None:
        self.lg = LinearRegression()
        self.train_model()
    
    def train_model(self):
        cnx = get_cnx()
        result_dataFrame = pd.read_sql(self.get_dataframe, cnx)
        cnx.close()
        result_dataFrame[['sex', 'smoker', 'region']] = result_dataFrame[['sex', 'smoker', 'region']].astype('category')
        result_dataFrame.replace({'sex': {'female': 1, 'male': 0}}, inplace=True)
        result_dataFrame.replace({'smoker': {'yes': 1, 'no': 0}}, inplace=True)
        result_dataFrame = pd.get_dummies(result_dataFrame, columns = ["region"])
        nor_list = preprocessing.normalize([result_dataFrame["charges"]])
        nor_list = nor_list.tolist()[0]
        result_dataFrame = result_dataFrame.drop(['charges'], axis=1)
        df_charge = pd.DataFrame (nor_list, columns = ['charges'])
        result_dataFrame = result_dataFrame.join(df_charge)

        y = result_dataFrame['charges']
        x = result_dataFrame.drop(['charges'], axis = 1)
        x_train, x_test, y_train, y_test =  train_test_split(x, y, test_size=0.33, random_state=42)
        self.lg.fit(x_train, y_train)
