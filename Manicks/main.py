from flask import Flask,render_template,request,redirect,flash
import pymysql as ps


#DATABASE CCONNECCTION
con=ps.connect(host="localhost",user="root",password="h13143m17",database="shop",cursorclass=ps.cursors.DictCursor)
cursor=con.cursor()

app=Flask(__name__)#DEFINING INITIALIZE

@app.route('/')
@app.route('/home')
def home():
    cursor.execute("select * from service")
    datas=cursor.fetchall()
    return render_template("home.html",infos=datas)

@app.route('/fan_submit',methods=['POST','GET'])
def fan_submit():
    if request.method== 'POST':
        try:
            Id=request.form.get('ID')
            Name=request.form['NAME']
            Mobile=int(request.form['MOBILE'])
            Color=request.form['COLOR']
            Fantype=request.form['FANTYPE']
            Dategiven=request.form['DATEOFGIVEN']
            Advance=int(request.form['ADVANCE'])
            Missingparts=request.form['MISSINGPARTS']
            try:
                cursor.execute(f"insert into service (P_id,C_name,C_mobile,P_color,F_type,DateGiven,Advance,Machine,MachineParts) values ('{Id}','{Name}',{Mobile},'{Color}','{Fantype}','{Dategiven}',{Advance},'Fan','{Missingparts}');")
                con.commit();
                flash("Record added successfully.")
                return redirect("/home")
            except:
                flash("Tranction failure!!!")
                return render_template("service.html")
        except:
            flash("Required all values.")
            return render_template("service.html")
    return render_template("home.html")

@app.route('/motor_submit',methods=['POST','GET'])
def motor_submit():
    if request.method== 'POST':
        try:
            Id=request.form.get('ID')
            Name=request.form['NAME']
            Mobile=int(request.form['MOBILE'])
            Color=request.form['COLOR']
            MotorHP=request.form['HP']
            Dategiven=request.form['DATEOFGIVEN']
            Advance=int(request.form['ADVANCE'])
            Missingparts=request.form['MISSINGPARTS']
            try:
                cursor.execute(f"insert into service (P_id,C_name,C_mobile,P_color,M_hp,DateGiven,Advance,Machine,MachineParts) values ('{Id}','{Name}',{Mobile},'{Color}','{MotorHP}','{Dategiven}',{Advance},'Motor','{Missingparts}');")
                con.commit();
                flash("Record added successfully.")
                return redirect("/home")
            except:
                flash("Tranction failure!!!")
                return render_template("service.html")
        except:
            flash("Required all values.")
            return render_template("service.html")
    return render_template("home.html")

@app.route('/powertool_submit',methods=['POST','GET'])
def powertool_submit():
    if request.method== 'POST':
        try:
            Id=request.form.get('ID')
            Name=request.form['NAME']
            Mobile=int(request.form['MOBILE'])
            Color=request.form['COLOR']
            PowertoolType=request.form['POWERTOOLS']
            Dategiven=request.form['DATEOFGIVEN']
            Advance=int(request.form['ADVANCE'])
            Modelno=int(request.form['MODELNO'])
            PowertoolCompany=request.form['COMPANY']
            Missingparts=request.form['MISSINGPARTS']
            try:
                cursor.execute(f"insert into service (P_id,C_name,C_mobile,P_color,P_type,DateGiven,Advance,P_company,P_model,Machine,MachineParts) values ('{Id}','{Name}',{Mobile},'{Color}','{PowertoolType}','{Dategiven}',{Advance},'{PowertoolCompany}','{Modelno}','PowerTool','{Missingparts}');")
                con.commit();
                flash("Record added successfully.")
                return redirect("/home")
            except:
                flash("Tranction failure!!!")
                return render_template("service.html")
        except:
            flash("Required all values.")
            return render_template("service.html")
    return render_template("home.html")

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
            try:
                cursor.execute(f"insert into spares(S_name,S_stock,s_use) values('{Name}',{Available},'{UseCase}');")
                con.commit();
                flash("Record added successfully.")
                return redirect("/spares_update")
            except:
                flash("Tranction failure!!!")
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
        flash('Item didnot deleted')
        redirect('/spares_update')
    return redirect("/spares_update")

@app.route("/update_item/<int:id>",methods=['POST','GET'])
def update_item(id):
    if request.method=='POST':
        print("hello")
        Name=request.form['SPARENAME']
        UseCase=request.form['USECASE']
        Available=int(request.form['SPAREAVAILABLE'])
        try:
            cursor.execute(f"update spares set  S_name='{Name}' , S_stock={Available} , S_use='{UseCase}' where S_id={id};")
            con.commit();
            flash("Record updated successfully.")
        except:
            flash("Tranction failure!!!")
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
        


@app.route('/spares_update')
def spares_update():
    cursor.execute("select * from spares")
    datas=cursor.fetchall()
    return render_template('spares_update.html',infos=datas)

@app.route('/service')
def service():
    return render_template('service.html')

if __name__=="__main__":
    app.secret_key="admin480"
    app.run(debug=True)