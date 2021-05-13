from flask import Flask,render_template,request,send_file
#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
import pandas as pd

import pygal



msg=[]
    


app=Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/input',methods=['GET','POST'])
def input():
    if request.method=="POST":
        detail=request.form
        builtup=int(detail['builtup'])
        cost=int(detail['cost'])
        print(builtup,cost)
        msg.append(builtup)
        msg.append(cost)
        tot=cost*builtup
        msg.append(tot)
        msg.append(0.164*tot)
        msg.append(0.123*tot)
        msg.append(0.0742*tot)
        msg.append(0.246*tot)
        msg.append(0.165*tot)
        msg.append(0.228*tot)
        msg.append(0.4*builtup)
        msg.append(0.816*builtup)
        msg.append(0.608*builtup)
        msg.append(4*builtup)
        msg.append(0.18*builtup)
        msg.append(8*builtup)
        msg.append(1.3*builtup)
        msg.append(0.27*tot)
        msg.append(0.184*tot)
        msg.append(0.111*tot)
        msg.append(0.169*tot)
        msg.append(0.178*tot)
        msg.append(0.139*tot)





        results = [
    (msg[3],'Cement'),
    (msg[4],'Sand'),
    (msg[5],'Aggregate'),
    (msg[6],'Steel'),
    (msg[7],'Finishers'),
    (msg[8],'Fittings'),
 
    ]

        pie_chart = pygal.Pie(height=500)
        pie_chart.title = 'Approx. cost on various work of materials'
        for r in results:
            pie_chart.add(r[1], r[0])
        pie_chart.value_formatter = lambda x: "%.15f" % x
        piech=pie_chart.render_data_uri()
    

        bar_chart = pygal.Bar(height=500)  # instance of Bar class
        bar_chart.title = 'construction'  # title of bar chart
        bar_chart.add('cost', [msg[16],msg[17],msg[18],msg[19],msg[20],msg[21]])  # add fibo data to chart
        bar_chart.x_labels = 'Month 1','Month 2','Month 3','Month 4','Month 5','Month 6'
        chart = bar_chart.render_data_uri()  

      
        html = render_template(
        'output.html',
        msg=msg,
        piech=piech,
        chart=chart   
    )
    return (html)


if __name__=='__main__':
    app.run(debug=True)