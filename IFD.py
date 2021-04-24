from flask import Flask,render_template,request,redirect,url_for
import pymysql
from PredictInput import predictI
app = Flask(__name__)
#conn=pymysql.connect(host="localhost",user="root",passwd="12345678",database="teststdb")

@app.route('/')
def showdata():
    conn=pymysql.connect(host="localhost",user="root",passwd="12345678",database="finsurance")
    with conn:
        cur=conn.cursor()
        cur.execute("select * from insurancestatus")
        row=cur.fetchall()
        cur.close()
        return render_template('index.html',data=row)


@app.route('/sform')
def sform():
    conn=pymysql.connect(host="localhost",user="root",passwd="12345678",database="finsurance")
    return render_template('addData.html')

@app.route('/insert',methods = ['POST'])
def insert():
    conn=pymysql.connect(host="localhost",user="root",passwd="12345678",database="finsurance")
    if request.method=="POST":

        Channel=request.form['Channel']
        CampaignCode=request.form['CampaignCode']
        PlanCode=request.form['PlanCode']
        PolicyNumber=request.form['PolicyNumber']
        MaritalStatus=request.form['MaritalStatus']
        Province=request.form['Province']
        Sex=request.form['Sex']
        IssueAge=request.form['IssueAge']
        Attain_Age=request.form['Attain_Age']
        ClaimStatus=request.form['ClaimStatus']
        DaysHospital=request.form['DaysHospital']
        OfClaims=request.form['OfClaims']
        ClaimCategory=request.form['ClaimCategory']
        AmountOfClaim=request.form['AmountOfClaim']
        PaybleAmount=request.form['PaybleAmount']
        ICD10Group=request.form['ICD10Group']
        ProductName=request.form['ProductName']
        policykey=request.form['policykey']
        PayerKey=request.form['PayerKey']
        PayerType=request.form['PayerType']
        PaymentMethod2=request.form['PaymentMethod2']
        HospitalCode=request.form['HospitalCode']
        InsuredID=request.form['InsuredID']
        Status_Stamp=request.form['Status_Stamp']

        print(InsuredID)
        print(Status_Stamp)        
        with conn.cursor() as cursor:
            sql = "INSERT INTO insurancestatus (Channel, CampaignCode, PlanCode, PolicyNumber, MaritalStatus, Province, Sex, IssueAge, Attain_Age, ClaimStatus ,DaysHospital, OfClaims, ClaimCategory, AmountOfClaim, PaybleAmount, ICD10Group, ProductName, policykey, PayerKey, PayerType, PaymentMethod2, HospitalCode, InsuredID, Status_Stamp) VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)"
            record = (Channel, CampaignCode, PlanCode, PolicyNumber, MaritalStatus, Province, Sex, IssueAge, Attain_Age, ClaimStatus ,DaysHospital, OfClaims, ClaimCategory, AmountOfClaim, PaybleAmount, ICD10Group, ProductName, policykey, PayerKey, PayerType, PaymentMethod2, HospitalCode, InsuredID, Status_Stamp)
            cursor.execute(sql, record)
            conn.commit()
        return redirect(url_for('showdata'))



# @app.route('/delete/<string:id_data>',methods = ['Get'])
# def delete(id_data):
#     conn=pymysql.connect(host="localhost",user="root",passwd="12345678",database="finsurance")
#     with conn:
#         cur=conn.cursor()
#         cur.execute("delete from insurancestatus where InsuredID ={7} ".format(id_data))
#         conn.commit()
#     return redirect(url_for('showdata'))

@app.route('/update',methods = ['POST'])
def update():
    conn=pymysql.connect(host="localhost",user="root",passwd="12345678",database="finsurance")
    if request.method=="POST":
        Channel=request.form['Channel']
        CampaignCode=request.form['CampaignCode']
        PlanCode=request.form['PlanCode']
        PolicyNumber=request.form['PolicyNumber']
        MaritalStatus=request.form['MaritalStatus']
        Province=request.form['Province']
        Sex=request.form['Sex']
        IssueAge=request.form['IssueAge']
        Attain_Age=request.form['Attain_Age']
        ClaimStatus=request.form['ClaimStatus']
        DaysHospital=request.form['DaysHospital']
        OfClaims=request.form['OfClaims']
        ClaimCategory=request.form['ClaimCategory']
        AmountOfClaim=request.form['AmountOfClaim']
        PaybleAmount=request.form['PaybleAmount']
        ICD10Group=request.form['ICD10Group']
        ProductName=request.form['ProductName']
        policykey=request.form['policykey']
        PayerKey=request.form['PayerKey']
        PayerType=request.form['PayerType']
        PaymentMethod2=request.form['PaymentMethod2']
        HospitalCode=request.form['HospitalCode']
        InsuredID=request.form['InsuredID']
        Status_Stamp=request.form['Status_Stamp']
        with conn.cursor() as cursor:
            sql = "INSERT INTO insurancestatus (Channel, CampaignCode, PlanCode, PolicyNumber, MaritalStatus, Province, Sex, IssueAge, Attain_Age, ClaimStatus ,DaysHospital, OfClaims, ClaimCategory, AmountOfClaim, PaybleAmount, ICD10Group, ProductName, policykey, PayerKey, PayerType, PaymentMethod2, HospitalCode, InsuredID, Status_Stamp) VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)"
            record = (Channel, CampaignCode, PlanCode, PolicyNumber, MaritalStatus, Province, Sex, IssueAge, Attain_Age, ClaimStatus ,DaysHospital, OfClaims, ClaimCategory, AmountOfClaim, PaybleAmount, ICD10Group, ProductName, policykey, PayerKey, PayerType, PaymentMethod2, HospitalCode, InsuredID, Status_Stamp)
            cursor.execute(sql, record)
            conn.commit()
        return redirect(url_for('showdata'))

@app.route('/predict')
def predictpage():
    return render_template('predict.html')


@app.route('/predict',methods = ['GET','POST'])
def predict():
    print("HHHHHHHH")
    if request.method=="POST":
        predict = predictI(
        request.form.get('AmountOfClaim'),
        request.form.get('DaysinHospital'),
        request.form.get('Remaining'),
        request.form.get('ClaimCategory'),
        request.form.get('ICD10G'),
        request.form.get('Gender'),
        )
        #predict.pred()
        res = predict.pred()
        print(res)
        toward = res[0]
        if toward == 1:
            word = 1
        elif toward == 2:
            word = 2
        elif toward == 0:
            word = 0
        print("word")
        return render_template('respage.html',res=word)
    return redirect(url_for('showdata'))

@app.route('/dashboard')
def dashboard():
    return render_template('dash.html')

if __name__ == '__main__':
    app.run(debug=True)
