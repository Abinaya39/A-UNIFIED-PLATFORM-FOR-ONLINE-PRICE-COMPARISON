from flask import Flask, render_template, flash, request, session, send_file
import datetime
import mysql.connector

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '789546321452145a'

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')

@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)

@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')

@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')

@app.route("/UserHome")
def UserHome():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where username='" + uname + "'")
    data = cur.fetchall()
    return render_template('UserHome.html', data=data)


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'abi' and request.form['pas'] == 'abi':
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            flash("Your are Logged In...!")
            return render_template('AdminHome.html',data=data)
        else:
            flash("Username or Password is wrong")
            return render_template('AdminLogin.html')

@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']

        username = request.form['uname']
        password = request.form['pas']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where UserName='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost',
                                           database='1productpricedb')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO regtb VALUES ('','" + name + "','" + age + "','" + mobile + "','" + email + "','" + address + "','" + username + "','" + password + "')")
            conn.commit()
            conn.close()
            flash('New User register successfully')
            return render_template('UserLogin.html')
        else:
            flash('Already registered')
            return render_template('NewUser.html')


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        uname = request.form['uname']
        pas = request.form['pas']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where UserName='" + uname + "' and Password='" + pas + "'")
        data = cursor.fetchone()
        if data is None:
            flash("Username or Password is wrong...!")
            return render_template('UserLogin.html')
        else:
            session['mob'] = data[2]
            session['add'] = data[4]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where UserName='" + uname + "' and Password='" + pas + "'")
            data = cur.fetchall()
            flash("Your are Logged In...!")
            return render_template('UserHome.html', data=data)


@app.route("/NewProduct")
def NewProduct():
    return render_template('NewProduct.html')


@app.route("/newproduct", methods=['GET', 'POST'])
def newproduct():
    if request.method == 'POST':

        productname = request.form['pname']
        type = request.form['type']
        info = request.form['info']
        price = request.form['price']
        file = request.files['image']
        file.save("static/upload/" + file.filename)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO protb1 VALUES ('','" + productname + "','" + type + "','" + info + "','" + price + "','" + file.filename + "')")
        conn.commit()
        conn.close()
        # return 'file register successfully'
        flash('New Prodect Added')
    return render_template('NewProduct.html')



@app.route("/AProductInfo")
def AProductInfo():
    conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')

    cur1 = conn1.cursor()
    cur1.execute("SELECT * FROM protb1 ")
    data = cur1.fetchall()

    return render_template('AProductInfo.html', data=data)


@app.route("/Remove", methods=['GET'])
def Remove():
    pid = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
    cursor = conn.cursor()
    cursor.execute("Delete from protb1  where pid='" + pid + "'")
    conn.commit()
    conn.close()
    conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
    # cursor = conn.cursor()
    cur1 = conn1.cursor()
    cur1.execute("SELECT * FROM protb1 ")
    data = cur1.fetchall()
    # return 'file register successfully'
    flash('Product Removed')
    return render_template('AProductInfo.html', data=data)



@app.route("/Usearch")
def Usearch():
    conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')

    cur1 = conn1.cursor()
    cur1.execute("SELECT * FROM protb1 ")
    data = cur1.fetchall()

    return render_template('Usearch.html', data=data)


@app.route("/viewproduct", methods=['GET', 'POST'])
def viewproduct():
    # searc = request.args.get('subcat')
    searc = request.form['subcat']

    conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
    cur1 = conn1.cursor()
    cur1.execute(
        "SELECT * from protb1 where Pname like '%" + searc + "%' ")
    data = cur1.fetchall()

    conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
    cur1 = conn1.cursor()
    #cur1.execute("SELECT distinct Pname FROM protb1 where Pname like '%" + searc + "%'")
    searc = searc.strip()

    if searc.isdigit():
        # Search by price
        # User enters a minimum price
        searc = searc  # example

        query = """
            SELECT pid, Pname, Type, Info, Price, Image
            FROM protb1
            WHERE CAST(Price AS UNSIGNED) >= %s
            ORDER BY CAST(Price AS UNSIGNED) ASC
        """
        param = (searc,)  # pass as a tuple

        cur1.execute(query, param)
        data1 = cur1.fetchall()

        return render_template('Usearch.html', data=data, data1=data1)

    else:
        # Search by name or type
        query = """
            SELECT pid, Pname, Type, Info, Price, Image
            FROM protb1
            WHERE Pname LIKE %s OR Type LIKE %s
            ORDER BY CAST(Price AS UNSIGNED) ASC
        """
        param = ('%' + searc + '%', '%' + searc + '%')
        cur1.execute(query, param)
        data1 = cur1.fetchall()

        return render_template('Usearch.html', data=data, data1=data1)

@app.route("/Add")
def Add():
    id = request.args.get('pid')
    session['pid'] = id
    print(id)
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb1 where pid='" + str(id) + "' ")
    data = cur.fetchall()
    return render_template('AddCart.html', data=data)


@app.route("/addcart", methods=['GET', 'POST'])
def addcart():
    if request.method == 'POST':
        import datetime
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        pid = session['pid']
        uname = session['uname']
        qty = int(request.form['qty'])

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM protb1  where  pid='" + pid + "'")
        data = cursor.fetchone()

        if data:
            productid = data[0]
            ProductName = data[1]
            Producttype = data[2]
            info = data[3]
            price = data[4]
            #quanty = int(data[4])
            Image = data[5]

        else:
            return 'No Record Found!'

        tprice = float(price) * float(qty)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO carttb VALUES ('','" + uname + "','" + ProductName + "','" + Producttype + "','" + str(
                price) + "','" + str(qty) + "','" + str(tprice) + "','" +
            Image + "','" + date + "','0','','" + session['mob'] + "','" + session['add'] + "', 'waiting','"+ info +"')")
        conn.commit()
        conn.close()

        flash('Add To Cart  Successfully')
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM protb1  where pid='" + pid + "' ")
        data = cur.fetchall()
        return render_template('AddCart.html', data=data)


@app.route("/Cart")
def Cart():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='0' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT  sum(Qty) as qty ,sum(Tprice) as Tprice   FROM  carttb where UserName='" + uname + "' and Status='0' ")
    data1 = cursor.fetchone()
    if data1:
        tqty = data1[0]
        tprice = data1[1]
    else:
        return 'No Record Found!'

    return render_template('Cart.html', data=data, tqty=tqty, tprice=tprice)


@app.route("/RemoveCart")
def RemoveCart():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
    cursor = conn.cursor()
    cursor.execute(
        "delete from carttb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('Product Remove Successfully!')

    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='0' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT  sum(Qty) as qty ,sum(Tprice) as Tprice   FROM  carttb where UserName='" + uname + "' and Status='0' ")
    data1 = cursor.fetchone()
    if data1:
        tqty = data1[0]
        tprice = data1[1]

    return render_template('Cart.html', data=data, tqty=tqty, tprice=tprice)

@app.route("/payment", methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        import datetime
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        uname = session['uname']
        cname = request.form['cname']
        Cardno = request.form['cno']
        Cvno = request.form['cvno']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT  sum(Qty) as qty ,sum(Tprice) as Tprice   FROM  carttb where UserName='" + uname + "' and Status='0' ")
        data1 = cursor.fetchone()
        if data1:
            tqty = data1[0]
            tprice = data1[1]

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT  count(*) As count  FROM booktb ")
        data = cursor.fetchone()
        if data:
            bookno = data[0]
            print(bookno)

            if bookno == 'Null' or bookno == 0:
                bookno = 1
            else:
                bookno += 1

        else:
            return 'Incorrect username / password !'

        bookno = 'BOOKID' + str(bookno)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
        cursor = conn.cursor()
        cursor.execute(
            "update   carttb set status='1',Bookid='" + bookno + "' where UserName='" + uname + "' and Status='0' ")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO booktb VALUES ('','" + uname + "','" + bookno + "','" + str(tqty) + "','" + str(
                tprice) + "','" + cname + "','" + Cardno + "','" + Cvno + "','" + date + "')")
        conn.commit()
        conn.close()
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='1' ")
        data1 = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where username='" + uname + "'")
        data2 = cur.fetchall()
        flash("Payment Successful....!")

    return render_template('UBookInfo.html', data1=data1, data2=data2)


@app.route("/UBookInfo")
def UBookInfo():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='1' ")
    data1 = cur.fetchall()
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  booktb where username='" + uname + "'")
    data2 = cur.fetchall()
    return render_template('UBookInfo.html', data1=data1, data2=data2)


@app.route("/ABookInfo")
def ABookInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where Status='1' ")
    data1 = cur.fetchall()
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productpricedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  booktb ")
    data2 = cur.fetchall()
    return render_template('ABookInfo.html', data1=data1, data2=data2)



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

