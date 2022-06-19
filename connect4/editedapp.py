from flask import Flask,request,render_template
from flask_cors import cross_origin
import pickle
import pandas as pd

model = pickle.load(open('flight_rf.pkl','rb'))

app = Flask(__name__)

@app.route('/')
@cross_origin()
def home():
	return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method=='POST':
        dep_time = request.form['Dep_Time']

        Journey_day = pd.to_datetime(dep_time,format="%Y-%m-%dT%H:%M").day
        Journey_month = pd.to_datetime(dep_time,format="%Y-%m-%dT%H:%M").month

        Departure_hour = pd.to_datetime(dep_time,format="%Y-%m-%dT%H:%M").hour
        Departure_min = pd.to_datetime(dep_time,format="%Y-%m-%dT%H:%M").minute

        arrival_time = request.form['Arrival_Time']
        Arrival_hour =  pd.to_datetime(arrival_time,format="%Y-%m-%dT%H:%M").hour
        Arrival_min =  pd.to_datetime(arrival_time,format="%Y-%m-%dT%H:%M").minute

        Total_stops = int(request.form['stops'])

        dur_hour = abs(Arrival_hour-Departure_hour)
        dur_min = abs(Arrival_min-Departure_min)

        airline=request.form['airline']
        if(airline=='Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Trujet = 0 
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0

        elif(airline=='IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Trujet = 0 
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0

        elif(airline=='Air_India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Trujet = 0 
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0

        elif(airline=='Multiple_carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Trujet = 0 
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0

        elif(airline=='SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Trujet = 0 
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0

        elif(airline=='Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Trujet = 0 
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0

        elif(airline=='GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Trujet = 0 
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0

        elif(airline=='Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Trujet = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0

        elif(airline=='Jet_Airways_Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Trujet = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0

        elif(airline=='Multiple_carriers_Premium_economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Trujet = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0

        elif(airline=='Vistara_Premium_economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Trujet = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1

        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Trujet = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0

        Source = request.form["Source"]
        if(Source == 'Hong Kong'):
            s_HongKong = 1 
            s_Singapore= 0
            a_Taiwan = 0
            s_Shanghai = 0

        elif(Source == 'Singapore'):
            s_HongKong  = 0 
            s_Singapore = 1
            a_Taiwan  = 0
            s_Shanghai = 0

        elif(Source == 'Taiwan'):
            s_HongKong  = 0 
            s_Singapore = 0
            a_Taiwan  = 1
            s_Shanghai = 0

        elif(Source == 'Shanghai'):
            s_HongKong  = 0 
            s_Singapore = 0
            a_Taiwan  = 0
            s_Shanghai = 1

        else:
            s_HongKong  = 0 
            s_Singapore = 0
            a_Taiwan  = 0
            s_Shanghai = 0


        Destination = request.form["Destination"]
        if(Destination == 'Taiwan'):
            d_Taiwan = 1
            d_HongKong = 0
            d_Japan= 0
            d_Singapore = 0

        elif(Destination == 'HongKong'):
            d_Taiwan = 0
            d_HongKong = 1
            d_Japan= 0
            d_Singapore = 0

        elif(Destination == 'Japan'):
            d_Taiwan = 0
            d_HongKong = 0
            d_Japan= 1
            d_Singapore = 0

        elif(Destination == 'Singapore'):
           d_Taiwan = 0
           d_HongKong = 0
           d_Japan= 0
           d_Singapore = 1

        else:
            d_Taiwan = 0
            d_HongKong = 0
            d_Japan= 0
            d_Singapore = 0

        output = model.predict([[Total_stops,
            Journey_day,
            Journey_month,
            Departure_hour,
            Departure_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Jet_Airways,
            IndiGo,
            Air_India,
            Multiple_carriers,
            SpiceJet,
            Vistara,
            GoAir,
            Trujet,
            Multiple_carriers_Premium_economy,
            Jet_Airways_Business,
            Vistara_Premium_economy,
            s_HongKong,
            s_Singapore,
            a_Taiwan,
            s_Shanghai,
            d_Taiwan,
            d_HongKong,
            d_Japan,
            d_Singapore,]])

        output = round(output[0],2)
        return render_template('home.html', predictions='You will have to pay approx Sgd$ .{}'.format(output))

if __name__ == '__main__':
	app.run(debug=True)

                                 
                                 


                                 











                                 
                                 
            
            

        
            
                              
            
        




        
