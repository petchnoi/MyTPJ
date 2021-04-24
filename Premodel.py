from flask import Flask,render_template,request,redirect,url_for
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pymysql
import joblib 
conn = pymysql.connect(host="localhost",user="root",passwd="12345678",database="finsurance")

with conn:
    cur=conn.cursor()
    cur.execute("select AmountOfClaim, DaysHospital, lifttime from insurancestatus")
    row=cur.fetchall()
    cur.execute("select ClaimCategory, ICD10Group, Sex from insurancestatus")
    rowd=cur.fetchall()
    cur.execute("select Status_Stamp from insurancestatus")
    rowlb=cur.fetchall()
    cur.close()

#DataFrame
df = pd.DataFrame(data=row)
df.columns =['AmountOfClaim', 'DaysHospital', 'lifttime']
dfd = pd.DataFrame(data=rowd)
dfd.columns =['ClaimCategory', 'ICD10Group', 'Sex']
lable = pd.DataFrame(data=rowlb)

lable.columns =['Status_Stamp']
d = {'Fraud': 1, 'Abuse': 2, 'Non_Fraud': 0}
lable['Status_Stamp'] = lable['Status_Stamp'].map(d)


dum = pd.get_dummies(dfd)
Ldf = pd.concat([df, dum, lable], axis=1)

#print(Ldf)


#ff = Ldf.drop(['ClaimCategory_', 'ICD10Group_','Sex_'], axis=1)
#print(dum.columns.values)

# debug
# print(Ldf)
# Ldf.to_csv (r'D:\Project\PJ\writefile\export_dataframe.csv', index = False, header=True)

#dataframetomodel
datatoM = Ldf.dropna(axis=0)

X_train = datatoM.drop('Status_Stamp', axis=1).values
Y_train = datatoM['Status_Stamp'].values

# Fit the model on training set
model = DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=10,
                       max_features=None, max_leaf_nodes=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=8, min_samples_split=8,
                       min_weight_fraction_leaf=0.0,
                       random_state=None, splitter='best')
model.fit(X_train, Y_train)

filename = 'D:/Project/PJ/model/Model_21_3_2021.sav'

#pickle.dump(model, open(filename, 'wb'))
joblib.dump(model, open(filename, 'wb'))
#dataframe2.to_csv (r'D:\testpj\test\export_dataframe.csv', index = False, header=True)
print('dddd')
