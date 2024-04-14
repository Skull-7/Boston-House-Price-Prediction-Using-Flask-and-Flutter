import pickle
import numpy as np
import pandas as pd
from flask import Flask,jsonify
app=Flask(__name__)
model=pickle.load(open(r"model.pkl","rb"))
@app.route("/")
def Test_call():
    return "The API is successfull running \n Status Code=200"
@app.route("/predict/<float:CRIM>/<float:ZN>/<float:INDUS>/<float:CHAS>/<float:NOX>/<float:RM>/<float:AGE>/<float:DIS>/<float:RAD>/<float:TAX>/<float:PTRATIO>/<float:B>/<float:LSTAT>",methods=["POST","GET"])
def predict(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT):
    array=np.array([pd.Series([CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT])])
    # data_var=np.array([CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT])
    # return(str(model.predict(data_var)))
    return(str(round(model.predict(array)[0][0],2)))
if __name__ == '__main__':
    app.run(debug=True)