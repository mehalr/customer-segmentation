import pickle
import pandas as pd
import numpy as np
col = ['ID', 'Age', 'Work_Experience', 'Family_Size', 'Gender_0', 'Gender_1',
       'Ever_Married_0', 'Ever_Married_1', 'Ever_Married_2', 'Graduated_0',
       'Graduated_1', 'Graduated_2', 'Profession_0', 'Profession_1',
       'Profession_2', 'Profession_3', 'Profession_4', 'Profession_5',
       'Profession_6', 'Profession_7', 'Profession_8', 'Profession_9',
       'Spending_Score_0', 'Spending_Score_1', 'Spending_Score_2', 'Var_1_0',
       'Var_1_1', 'Var_1_2', 'Var_1_3', 'Var_1_4', 'Var_1_5', 'Var_1_6',
       'Var_1_7', 'week', 'month', 'year', 'quarter']


def check(data):
    data = data.dict()
    numeric = {}
    for i in ['ID', 'Age', 'Work_Experience', 'Family_Size']:
        numeric[i] = int(data[i])
    df = pd.DataFrame(columns=col, index=None)
    df = df.append(numeric, ignore_index=True)
    for j in ['gender', 'married', 'graduated', 'profession', 'spending', 'category']:
        df[data[j]] = 1
    df['week'] = int(df['ID']) % 7
    df['month'] = int(df['ID']) % 30
    df['year'] = int(df['ID']) % 365
    df['quarter'] = int(df['ID']) % 90
    df = df.replace(np.nan, 0)
    Pkl_Filename = "LGBM.pkl"
    with open(Pkl_Filename, 'rb') as file:
        LGBM = pickle.load(file)
    pred = LGBM.predict(df)
    print(pred)
    return pred[0]