from flask import Flask,render_template,request,redirect,url_for
import pymysql
#from PredictInput import predict
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
        #Province=request.form['Province']
        Sex=request.form['Sex']
        IssueAge=request.form['IssueAge']
        Attain_Age=request.form['Attain_Age']
        ClaimStatus=request.form['ClaimStatus']
        DaysHospital=request.form['DaysHospital']
        OfClaims=request.form['OfClaims']
        ClaimCategory=request.form['ClaimCategory']
        AmountOfClaim=request.form['AmountOfClaim']
        PaybleAmount=request.form['PaybleAmount']
        Icd10=request.form['Icd10']
        ProductName=request.form['ProductName']
        policykey=request.form['policykey']
        PayerKey=request.form['PayerKey']
        PayerType=request.form['PayerType']
        PaymentMethod2=request.form['PaymentMethod2']
        HospitalCode=request.form['HospitalCode']
        InsuredID=request.form['InsuredID']
        PaybleAmount=request.form['PaybleAmount']
        with conn.cursor() as cursor:
            sql = "INSERT INTO insurancestatus (Channel, CampaignCode, PlanCode, PolicyNumber, MaritalStatus, Province, Sex, IssueAge, Attain_Age, ClaimStatus ,DaysHospital, OfClaims, ClaimCategory, AmountOfClaim, PaybleAmount, Icd10, ProductName, policykey, PayerKey, PayerType, PaymentMethod2, HospitalCode, InsuredID, PaybleAmount) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}','{21}','{22}','{23}','{24}')".format(Channel, CampaignCode, PlanCode, PolicyNumber, MaritalStatus, Province, Sex, IssueAge, Attain_Age, ClaimStatus ,DaysHospital, OfClaims, ClaimCategory, AmountOfClaim, PaybleAmount, Icd10, ProductName, policykey, PayerKey, PayerType, PaymentMethod2, HospitalCode, InsuredID, PaybleAmount)
            cursor.execute(sql)
            conn.commit()
        return redirect(url_for('showdata'))

@app.route('/delete/<string:id_data>',methods = ['GET'])
def delete(id_data):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345678",database="finsurance")
    with conn:
        cur=conn.cursor()
        cur.execute("delete from insurancestatus where id={0}".format(id_data))
        conn.commit()
    return redirect(url_for('showdata'))

@app.route('/update',methods = ['POST'])
def update():
    conn=pymysql.connect(host="localhost",user="root",passwd="12345678",database="finsurance")
    if request.method=="POST":
        id_update=request.form['id']
        fname=request.form['fname']
        lname=request.form['lname']
        phone=request.form['phone']
        with conn.cursor() as cursor:
            #sql = "update stusent set fname = {0},lame = {1}, phone =   {2} where id ={3}".format(fname,lname,phone,id_update)
            sql = "update insurancestatus set fname=%s, lame=%s, phone=%s where id=%s"
            cursor.execute(sql,(fname,lname,phone,id_update))
            #cursor.execute(sql)
            conn.commit()
        return redirect(url_for('showdata'))



@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method=="POST":
        predict = predict(request.form.get('id'),
        request.form.get('AmountOfClaim'),
        request.form.get('DaysinHospital'),
        request.form.get('Remaining'),
        request.form.get('ClaimCategory'),
        request.form.get('ICD10G'),
        request.form.get('Gender'),
        )
    predict.pred()


if __name__ == '__main__':
    app.run(debug=True)
