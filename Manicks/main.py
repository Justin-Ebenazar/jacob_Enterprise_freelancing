from flask import Flask,render_template,request,redirect,flash
import pymysql as ps


#DATABASE CCONNECCTION
con=ps.connect(host="localhost",user="root",password="********",database="shop",cursorclass=ps.cursors.DictCursor)
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
            print(Id,Name,Mobile,Color,Fantype,Dategiven,Advance)
            try:
                cursor.execute(f"insert into service (P_id,C_name,C_mobile,P_color,F_type,DateGiven,Advance,Machine) values ('{Id}','{Name}',{Mobile},'{Color}','{Fantype}','{Dategiven}',{Advance},'Fan');")
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
            try:
                cursor.execute(f"insert into service (P_id,C_name,C_mobile,P_color,M_hp,DateGiven,Advance,Machine) values ('{Id}','{Name}',{Mobile},'{Color}','{MotorHP}','{Dategiven}',{Advance},'Motor');")
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
            try:
                cursor.execute(f"insert into service (P_id,C_name,C_mobile,P_color,P_type,DateGiven,Advance,P_company,P_model,Machine) values ('{Id}','{Name}',{Mobile},'{Color}','{PowertoolType}','{Dategiven}',{Advance},'{PowertoolCompany}','{Modelno}','PowerTool');")
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
        cursor.execute(f"select * from service where P_id='{search_element}' or C_name='{search_element}' or C_mobile={int(search_element)}")
        datas=cursor.fetchall()
        return render_template("home.html",infos=datas)
    return redirect("/home")






@app.route('/service')
def service():
    return render_template('service.html')

if __name__=="__main__":
    app.secret_key="admin480"
    app.run(debug=True)