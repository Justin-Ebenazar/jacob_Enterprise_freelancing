from flask import Flask,render_template,request,redirect,flash
from flask import after_this_request


app=Flask(__name__)#DEFINING INITIALIZE

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", infos={})


@app.route('/service')
def service():
    return render_template("service.html",info=str(123))

@app.route('/fan_submit',methods=['POST','GET'])
def fan_submit():
    if request.method== 'POST':
        try:
            try:
                DeliveryChallan=int(10)
            except:
                DeliveryChallan=None
            try:
                flash("Record added successfully.")
                return redirect("/home")
            except:
                flash("Transaction failure!!! OR Check The entered mobile number.")
                return redirect("/service")
        except:
            flash("Required all values.")
            return redirect("/service")
    return render_template("home.html")

@app.route('/motor_submit',methods=['POST','GET'])
def motor_submit():
    if request.method== 'POST':
        try:
            try:
                flash("Record added successfully.")
                return redirect("/home")
            except:
                flash("Transaction failure!!!")
                return redirect("/service")
        except:
            flash("Required all values.")
            return redirect("/service")
    return render_template("home.html")

@app.route('/powertool_submit',methods=['POST','GET'])
def powertool_submit():
    if request.method== 'POST':
        try:
            try:
                flash("Record added successfully.")
                return redirect("/home")
            except:
                flash("Transaction failure!!!")
                return redirect("/service")
        except:
            flash("Required all values.")
            return redirect("/service")
    return render_template("home.html")

@app.route('/old_record',methods=['POST','GET'])
def old_record():
    return render_template('old_records.html',infos={})

@app.route('/old_record_search',methods=['POST','GET'])
def old_record_search():
    if request.method=='POST':
        Start_date=request.form['Start_date']
        End_date=request.form['End_date']
        return render_template("old_records.html",infos={})
    return redirect("/old_record")

@app.route('/record_search',methods=['POST','GET'])
def record_search():
    if request.method=='POST':
        search_element=request.form['SEARCH']
        return render_template("home.html",infos={})
    return redirect("/home")

@app.route('/add_new_item',methods=['POST','GET'])
def add_new_item():
    if request.method== 'POST':
        try:
            try:
                flash("Record added successfully.")
                return redirect("/spares_update")
            except:
                flash("Transaction failure!!!")
                return redirect("/spares_update")
        except:
            flash("Required all values.")
            return redirect("/spares_update")
    return render_template("spares_update.html")

@app.route("/delete_item/<int:id>",methods=['POST','GET'])
def delete_item(id):
    try:
        flash('Deleted successfully.')
        return redirect('/spares_update')
    except:
        flash('Item was not deleted')
        redirect('/spares_update')
    return redirect("/spares_update")

@app.route("/update_item/<int:id>",methods=['POST','GET'])
def update_item(id):
    if request.method=='POST':
        try:
            flash("Record updated successfully.")
        except:
            flash("Transaction failure!!!")
        return redirect("/spares_update")
    return render_template('spares_update_edit.html',infos={})

@app.route('/record_search_spare',methods=['POST','GET'])
def record_search_spare():
    if request.method=='POST':
        return render_template("spares_update.html",infos={})


@app.route("/repair_status/<string:id>",methods=['POST','GET'])
def repair_status(id):
    try:
        pass
    except:
        # print('hello')
        discount=0
    return render_template("repair_status_Modified.html",info={},infos={},expns={},bill={},disc={})



@app.route('/expence_del/<string:id>/<string:name>',methods=['POST','GET'])
def expence_del(id,name):
    return redirect(f'/repair_status/{id}')


@app.route('/spares_update')
def spares_update():
    return render_template('spares_update.html',infos={})

@app.route('/finance')
def finance():
    return render_template('finance.html',infos={},todays_profit=1000,month_profit=100000)

@app.route('/spares')
def spares():
    return render_template('spares.html',infos={})

@app.route('/sell_spare/<int:id>',methods=['POST','GET'])
def sell_spare(id): 
    if request.method=='POST':
        pass
    return spares()

@app.route('/lookup')
def lookup():
    return render_template('spares_lookup.html')

@app.route('/spares_look_search',methods=['POST','GET'])
def spares_look_search():
    if request.method=='POST':
        Start_date=request.form['Start_date']
        End_date=request.form['End_date']
        if(Start_date!='' and End_date!=''):
            return render_template("spares_lookup.html",infos={})
        else:
            Spare_name=request.form['spl_SEARCH']
            return render_template("spares_lookup.html",infos={})
    return redirect("/lookup")

@app.route('/spares_search',methods=['POST','GET'])
def spares_search():
    if request.method=='POST':
        return render_template("spares.html",infos={})
    
@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.secret_key="admin480"
    app.run(debug=True)
