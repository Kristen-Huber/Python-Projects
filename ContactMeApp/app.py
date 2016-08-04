from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'Kris110940'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Kris110940'
app.config['MYSQL_DATABASE_DB'] = 'contactMe'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _message = request.form['inputMessage']

        # validate the received values
        if _name and _email and _message:

            # All Good, let's call MySQL

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_createUser',(_name,_email,_message))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'Thank you!'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(port=5002)