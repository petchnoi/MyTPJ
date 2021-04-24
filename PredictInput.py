import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

class predictI():
        
        def __init__(self, AmountOfClaim , DaysinHospital , Remaining , ClaimCategory , ICD10G , Gender):
            #self.lr = DecisionTreeClassifier()
            self.AmountOfClaim = AmountOfClaim
            self.DaysinHospital = DaysinHospital
            self.Remaining = Remaining
            self.ClaimCategory = ClaimCategory
            self.ICD10G = ICD10G
            self.Gender = Gender
            self.predictI = ''
    

        def pred(self):
            inputdata =[[]]
            #inputdata =[[self.AmountOfClaim,self.DaysinHospital,self.Remaining,self.ClaimCategory,self.ICD10G,self.Gender]]
            inputdata[0].extend([int(self.AmountOfClaim)])
            inputdata[0].extend([int(self.DaysinHospital)])
            inputdata[0].extend([int(self.Remaining)])
            
            #debug
            print("---------")
            print(self.AmountOfClaim)
            print(self.DaysinHospital)
            print(self.Remaining)
            print("---------")
            print(self.ClaimCategory)
            print(self.ICD10G)
            print(self.Gender)
            print("---------")


            # #ClaimCategory
            if self.ClaimCategory == 'Accident' :
                inputdata[0].extend([1,0,0,0,0])
            elif self.ClaimCategory == 'Dental' :
                inputdata[0].extend([0,1,0,0,0])
            elif self.ClaimCategory == 'Dental':
                inputdata[0].extend([0,0,1,0,0])
            elif self.ClaimCategory == 'Health':
                inputdata[0].extend([0,0,0,1,0])
            elif self.ClaimCategory == 'PA':
                inputdata[0].extend([0,0,0,0,1])

            #ICD10G
            if self.ICD10G == 'A00-B99' :
                inputdata[0].extend([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif self.ICD10G == 'C00-D48' :
                inputdata[0].extend([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif self.ICD10G == 'E00-E90':
                inputdata[0].extend([0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif self.ICD10G == 'F00-F99':
                inputdata[0].extend([0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0])
            elif self.ICD10G == 'G00-G99':
                inputdata[0].extend([0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0])
            elif self.ICD10G == 'H00-H59' :
                inputdata[0].extend([0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0])
            elif self.ICD10G == 'I00-I99':
                inputdata[0].extend([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0])
            elif self.ICD10G == 'J00-J99':
                inputdata[0].extend([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0])
            elif self.ICD10G == 'K00-K93':
                inputdata[0].extend([0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])
            elif self.ICD10G == 'L00-L99' :
                inputdata[0].extend([0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0])
            elif self.ICD10G == 'M00-M99':
                inputdata[0].extend([0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0])
            elif self.ICD10G == 'N00-N99':
                inputdata[0].extend([0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0])
            elif self.ICD10G == 'O00-O99':
                inputdata[0].extend([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])
            elif self.ICD10G == 'P00-P96' :
                inputdata[0].extend([0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0])
            elif self.ICD10G == 'Q00-Q99':
                inputdata[0].extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0])
            elif self.ICD10G == 'R00-R99':
                inputdata[0].extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
            elif self.ICD10G == 'S00-T98':
                inputdata[0].extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif self.ICD10G == 'U00-U99' :
                inputdata[0].extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif self.ICD10G == 'V01-Y98':
                inputdata[0].extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif self.ICD10G == 'W00-W99':
                inputdata[0].extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif self.ICD10G == 'X00-X99':
                inputdata[0].extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif self.ICD10G == 'Y00-Y98' :
                inputdata[0].extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif self.ICD10G == 'Z00-Z99':
                inputdata[0].extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            if self.Gender == 'Female' :
                inputdata[0].extend([1,0])
            elif self.Gender == 'Male' :
                inputdata[0].extend([0,1])
            
            
            
            filename = 'D:/Project/PJ/model/Model_21_3_2021.sav'
            # print(inputdata)
            #inputdata.to_csv (r'D:\Project\PJ\writefile\export_dataframeddd.csv', index = False, header=True)
            # print("sd")
            
            print("usemodel")


            print(inputdata)
            loaded_model = joblib.load(open(filename, 'rb'))
            result = loaded_model.predict(inputdata)
            # self.predictI = self.lr.predict(inputdata)[0]
            print("getresult")
            print(result)
            print("______________")
            return result