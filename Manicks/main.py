from flask import Flask,render_template,request,redirect,flash
import pymysql as ps
import datetime as dt
import webview

#DATABASE CCONNECCTION
try:
    con=ps.connect(host="localhost",user="root",password="h13143m17",database="shop",cursorclass=ps.cursors.DictCursor)
except:
    con=ps.connect(host="localhost",user="root",password="12345678",database="shop",cursorclass=ps.cursors.DictCursor)
cursor=con.cursor()


today=dt.datetime.now()
day=today.strftime("20%y-%m-%d")

app=Flask(__name__)#DEFINING INITIALIZE
window=webview.create_window("justin",app)

@app.route('/')
@app.route('/home')
def home():
    cursor.execute("select * from service where not DeliveryStatus='on'")
    datas=cursor.fetchall()
    return render_template("home.html",infos=datas)

@app.route('/service')
def service():
    datas=0
    try:
        cursor.execute("select * from service")
        datas=int(cursor.fetchall()[-1]['P_id'])
    except:
        datas=0
    return render_template("service.html",info=str(datas+1))

@app.route('/fan_submit',methods=['POST','GET'])
def fan_submit():
    if request.method== 'POST':
        try:
            Name=request.form['NAME']
            Mobile=int(request.form['MOBILE'])
            if len(str(Mobile))!=10:
                flash("Moile Number is wrong")
                return redirect('/service')
            Color=request.form['COLOR']
            Fantype=request.form['FANTYPE']
            Dategiven=request.form['DATEOFGIVEN']
            if Dategiven=='':
                Dategiven=day
            Advance=int(request.form['ADVANCE'])
            Missingparts=request.form['MISSINGPARTS']
            try:
                cursor.execute(f"insert into service (C_name,C_mobile,P_color,F_type,DateGiven,Advance,Machine,MachineParts) values ('{Name.lower()}',{Mobile},'{Color}','{Fantype}','{Dategiven}',{Advance},'Fan','{Missingparts}');")
                con.commit()
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
            Name=request.form['NAME']
            Mobile=int(request.form['MOBILE'])
            if len(str(Mobile))!=10:
                flash("Moile Number is wrong")
                return redirect('/service')
            Color=request.form['COLOR']
            MotorHP=request.form['HP']
            Dategiven=request.form['DATEOFGIVEN']
            if Dategiven=='':
                Dategiven=day
            Advance=int(request.form['ADVANCE'])
            Missingparts=request.form['MISSINGPARTS']
            try:
                cursor.execute(f"insert into service (C_name,C_mobile,P_color,M_hp,DateGiven,Advance,Machine,MachineParts) values ('{Name.lower()}',{Mobile},'{Color}','{MotorHP}','{Dategiven}',{Advance},'Motor','{Missingparts}');")
                con.commit()
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
            Name=request.form['NAME']
            Mobile=int(request.form['MOBILE'])
            if len(str(Mobile))!=10:
                flash("Moile Number is wrong")
                return redirect('/service')
            Color=request.form['COLOR']
            PowertoolType=request.form['POWERTOOLS']
            Dategiven=request.form['DATEOFGIVEN']
            if Dategiven=='':
                Dategiven=day
            Advance=int(request.form['ADVANCE'])
            Modelno=int(request.form['MODELNO'])

            PowertoolCompany=request.form['COMPANY']
            Missingparts=request.form['MISSINGPARTS']
            try:
                cursor.execute(f"insert into service (C_name,C_mobile,P_color,P_type,DateGiven,Advance,P_company,P_model,Machine,MachineParts) values ('{Name.lower()}',{Mobile},'{Color}','{PowertoolType}','{Dategiven}',{Advance},'{PowertoolCompany}','{Modelno}','PowerTool','{Missingparts}');")
                con.commit();
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
    cursor.execute("select * from service where DeliveryStatus='on'")
    datas=cursor.fetchall()
    return render_template('old_records.html',infos=datas)

@app.route('/old_record_search',methods=['POST','GET'])
def old_record_search():
    if request.method=='POST':
        search_element=request.form['SEARCH']
        Start_date=request.form['Start_date']
        End_date=request.form['End_date']
        cursor.execute(f"select * from service where P_id='{search_element}' or C_name='{search_element}' or DateGiven between '{Start_date}' and '{End_date}' and DeliveryStatus='on'")
        datas=cursor.fetchall()
        return render_template("old_records.html",infos=datas)
    return redirect("/old_record")

@app.route('/record_search',methods=['POST','GET'])
def record_search():
    if request.method=='POST':
        search_element=request.form['SEARCH']
        cursor.execute(f"select * from service where P_id='{search_element}' or C_name='{search_element}'")
        datas=cursor.fetchall()
        return render_template("home.html",infos=datas)
    return redirect("/home")

@app.route('/add_new_item',methods=['POST','GET'])
def add_new_item():
    if request.method== 'POST':
        try:
            Name=request.form['SPARENAME']
            UseCase=request.form['USECASE']
            Available=int(request.form['SPAREAVAILABLE'])
            Cost=int(request.form['SPARECOST'])
            try:
                cursor.execute(f"insert into spares(S_name,S_stock,S_use,S_Cost) values('{Name}',{Available},'{UseCase}',{Cost})")
                con.commit();
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
        cursor.execute(f"delete from spares where S_id='{id}'")
        con.commit()
        flash('Deleted successfully.')
        return redirect('/spares_update')
    except:
        flash('Item was not deleted')
        redirect('/spares_update')
    return redirect("/spares_update")

@app.route("/update_item/<int:id>",methods=['POST','GET'])
def update_item(id):
    if request.method=='POST':
        Name=request.form['SPARENAME']
        UseCase=request.form['USECASE']
        Available=int(request.form['SPAREAVAILABLE'])
        Cost=int(request.form['SPARECOST'])
        try:
            cursor.execute(f"update spares set  S_name='{Name}' , S_stock={Available} , S_use='{UseCase}' , S_Cost={Cost} where S_id={id};")
            con.commit();
            flash("Record updated successfully.")
        except:
            flash("Transaction failure!!!")
        return redirect("/spares_update")
    cursor.execute(f"select * from spares where S_id={id}")
    datas=cursor.fetchone()
    return render_template('spares_update_edit.html',infos=datas)

@app.route('/record_search_spare',methods=['POST','GET'])
def record_search_spare():
    if request.method=='POST':
        search_element=request.form['SEARCH']
        cursor.execute(f"select * from spares where S_name='{search_element}'")
        datas=cursor.fetchall()
        return render_template("spares_update.html",infos=datas)
        
@app.route("/repair_status/<string:id>",methods=['POST','GET'])
def repair_status(id):
    DiscountAmt=0
    if request.method=='POST':
        try:
            DeliveryStatus=request.form.get('delivered_or_not','off')
            if DeliveryStatus=='on':
                cursor.execute(f"update service set DateDelivered='{day}' where P_id='{id}'")
                con.commit()
            RepairStatus=request.form.get('repaired_or_not','off')
            cursor.execute(f"update service set RepairStatus='{RepairStatus}', DeliveryStatus='{DeliveryStatus}' where P_id='{id}' ")
            con.commit()
        except:
            pass
        try:
            EXPNSPARE=request.form['EXPNSPARE']
            COST=int(request.form['COST'])
            STOCK=0
            try:
                try:
                    cursor.execute(f"select S_Cost,S_stock from spares where S_name='{EXPNSPARE}'")
                    cost_and_stock=cursor.fetchone()
                    COST=cost_and_stock['S_Cost']
                    STOCK=int(cost_and_stock['S_stock'])
                except:
                    if(COST==0):
                        flash("Require cost value for new Spare.")
                if (COST!=0):
                    cursor.execute(f"insert into expences values('{id}','{EXPNSPARE}',{COST},{DiscountAmt})")
                    con.commit()
                    cursor.execute(f"update spares set S_stock={STOCK-1} where S_name='{EXPNSPARE}'")
                    con.commit()
                    
                # flash("Added Sucessfully")
            except:
                flash("Cannot add item.")
        except:
            pass
        try:
            DiscountAmt=int(request.form['DISCOUNTAMOUNT'])
            cursor.execute(f"update expences set Discount={DiscountAmt} where P_id='{id}' ")
            con.commit()
        except:
            pass
    cursor.execute(f"select * from service where P_id='{id}'")
    datas=cursor.fetchone()

    cursor.execute(f"select * from spares")
    datas1=cursor.fetchall()

    cursor.execute(f"select * from expences where P_id='{id}'")
    datas2=cursor.fetchall()

    cursor.execute(f"select coalesce(sum(Cost),0) as tot from expences where P_id='{id}'")
    total=cursor.fetchone()
    try:
        cursor.execute(f"update service set Totalbill={total['tot']} where P_id='{id}'")
        con.commit()
    except:
        pass
    discount=0
    try:
        discount=datas2[0]['Discount']
    except:
        discount=0
    return render_template("repair_status_Modified.html",info=datas,infos=datas1,expns=datas2,bill=total,disc=discount)



@app.route('/expence_del/<string:id>/<string:name>',methods=['POST','GET'])
def expence_del(id,name):
    try:
        cursor.execute(f"delete from expences where P_id='{id}' and S_name='{name}'")
        con.commit()
    except:
        # flash("Cannot delete item.")
        pass
    return repair_status(id)


@app.route('/spares_update')
def spares_update():
    cursor.execute("select * from spares")
    datas=cursor.fetchall()
    return render_template('spares_update.html',infos=datas)

@app.route('/finance')
def finance():
    cursor.execute("select P_id,C_name,Machine,DateDelivered,Totalbill from service where DeliveryStatus='on'")
    datas=cursor.fetchall()
    todays_income=0
    month_income=0

    for data in datas:
        if data['DateDelivered'][8:]==day[8:]:
            todays_income+=data['Totalbill']
        if data['DateDelivered'][5:7]==day[5:7]:
            month_income+=data['Totalbill']
        
    return render_template('finance.html',infos=datas,todays_profit=todays_income,month_profit=month_income)

@app.route('/spares')
def spares():
    cursor.execute("select * from spares")
    datas=cursor.fetchall()
    return render_template('spares.html',infos=datas)

@app.route('/sell_spare/<int:id>',methods=['POST','GET'])
def sell_spare(id): 
    if request.method=='POST':
        qunantity=int(request.form['quantity'])
        try:
            cursor.execute(f"select S_stock,S_Cost,S_id from spares where S_id={id}")
            datas=cursor.fetchone()
            total_stock=datas['S_stock']
            price=datas['S_Cost']*qunantity
            cursor.execute(f"update spares set S_stock={total_stock-qunantity} where S_id={id}")
            con.commit()
            cursor.execute(f"insert into service (DeliveryStatus,DateDelivered,Totalbill) values('on','{day}',{price})")
            con.commit()
            return redirect('/spares')
        except:
            print("hello")      
    return spares()

@app.route('/lookup')
def lookup():
    return render_template('spares_lookup.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.secret_key="admin480"
    app.run(debug=True)
    #webview.start()
