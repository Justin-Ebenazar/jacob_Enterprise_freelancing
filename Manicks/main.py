from flask import Flask,render_template,request,redirect,flash
import pymysql as ps


#DATABASE CCONNECCTION
con=ps.connect(host="localhost",user="root",password="********",database="shop",cursorclass=ps.cursors.DictCursor)
cursor=con.cursor()

app=Flask(__name__)#DEFINING INITIALIZE

@app.route('/')
@app.route('/home',methods=['POST','GET'])
def home():
    cursor.execute("select * from service")
    datas=cursor.fetchall()
    if request.method== 'POST':
        try:
            i=request.form['idval']
            n=request.form['name']
            p=int(request.form['phno'])
            t=request.form['type']
            b=request.form['brand']
            f=request.form['purpose']
            m=request.form['parts']
            h=request.form['hp']
            c=request.form['color']
            a=int(request.form['advanc'])
            d=request.form['dog']
            pay=request.form['status']
            if t in ['Fan','Powertools']:
                h=0
            cursor.execute(f"insert into service (id,cname,phno,mtype,brand,purpose,mhp,dog,msparts,advance,color,payment) values('{i}','{n}',{p},'{t}','{b}','{f}','{h}','{d}','{m}',{a},'{c}','{pay}')")
            con.commit()
            flash('Record Added Successfully.')
            return render_template("home.html",infos=datas)
        except:
            flash('Record Adding Failier!!!')
            return render_template("service.html")
    return render_template("home.html",infos=datas)

@app.route('/service')
def service():
    return render_template('service.html')
if __name__=="__main__":
    app.secret_key="admin480"
    app.run(debug=True)