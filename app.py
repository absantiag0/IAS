from flask import *
#import pymysql #$ python3 -m pip install PyMySQL


app = Flask(__name__)

#MySQL Connection
# Connect to the database
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='',
#                              database='IAS',
#                              cursorclass=pymysql.cursors.DictCursor)

# settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
#   try:
#     if 'FullName' in session:
    #   return redirect('/home')
    # else:
    return render_template('home.html')
#   except Exception as error:
#     flash(str(error))
#     return render_template('index.html')
#     return render_template('index.html',usuarios = data)

@app.route('/Registro',methods=['GET'])
def Registro():
    return render_template('Registro.html')
    
@app.route('/Menu',methods=['GET'])
def Menu():
    return render_template('Menu.html')

@app.route('/salir',methods=['GET'])
def salir():
    return redirect('/')


if __name__=='__main__':
    app.run(port = 4000, debug =True)
    
