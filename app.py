from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/input',methods=['GET','POST'])
def input():
    if request.method=="POST":
        msg=[]
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

        return render_template('output.html', msg=msg)




if __name__=='__main__':
    app.run(debug=True)