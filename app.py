from flask import Flask, render_template, request, jsonify
import psycopg2 #pip install psycopg2 
import psycopg2.extras

app = Flask(__name__)

app.secret_key = "caircocoders-ednalan"
 
DB_HOST = "localhost"
DB_NAME = "sampledb"
DB_USER = "postgres"
DB_PASS = "dba"
DB_PORT = "5432"
     
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT) 


@app.route("/")
def index():
  cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute("select * from employee order by id asc")
  employeelist = cur.fetchall()
  return render_template("index.html", employeelist=employeelist)


@app.route("/fetchdata",methods=["POST","GET"])
def fetchdata():
  cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
  if request.method == 'POST':
    id = request.form['id']
    cur.execute("select * from employee where id = %s", [id])
    rs = cur.fetchone()
    name = rs['name']
    photo = rs['photo']
    position = rs['position']
    office = rs['office']
    print(photo)
  return jsonify({'htmlresponse': render_template("response.html", name=name, photo=photo, position=position, office=office)})

if __name__ == '__Main__':
  app.run(debug=True)