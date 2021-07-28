#!/usr/bin/env python3

import cx_Oracle
from flask import Flask, render_template, request, url_for, redirect,session,g
import os


con = cx_Oracle.connect('MATRIMONY/admin123@localhost')
cursor = con.cursor()

def get_data():    
      cursor.execute("SELECT * FROM UserDetails")
      userdata = cursor.fetchall()
      # for data in userdata:
      #       print(data[0],data[1])
      return userdata
            

def uservalidate(username,password):
       userdata = get_data()
       flag = False
       #print(len(userdata))
       for data in userdata:
              if(data[0]==username and data[1]==password):
                     flag = True
                     break
       return flag


def checkuser(username):
       userdata = get_data()
       flag = False
       for data in userdata:
              if(data[0] == username):
                     #print("account already exist")
                     flag = True
                     break
       return flag
             

def add_data(username,password):
    print(username, password)
    cursor.execute("INSERT INTO UserDetails VALUES('{}','{}')".format(username,password))
    con.commit()


def uploadData():
       if request.method == 'POST':
         email = request.form.get('username')
         password = request.form.get('password')
         add_data(email,password)
         #print('User added')
         

def RegisterFormData(fname,age,gender,highest_education,profession,salary,city,native_place,height,complexion,mother_tounge,religion,physical_status,father,mother,father_occ,mother_occ,num_of_brothers,num_of_sisters,about_famly,register_as,email,mobile_number,address):
      # cursor.execute("INSERT INTO TESTMALE VALUES('firstname','secondname','male')")
       if gender == 'male':
              # print(fname,lname,gender,dob,age,religion,country,father,mother,father_occ,mother_occ,mother_tounge,qualification,occupation,salary,address,pincode,state,addhar,mobile_number,alternate_number)
              # cursor.execute("INSERT INTO MALE VALUES('afasdf','j','male','3-23-2001',25,'kajhlsj','jsalhkjfk','father','mother','Mechanic','Housewife','Tamil','Student','MAnager',25000,'as,jdgfkssaf',63,'Pondy',7325876,29468,8747)")
              cursor.execute("INSERT INTO MALE VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(fname,age,gender,highest_education,profession,salary,city,native_place,height,complexion,mother_tounge,religion,physical_status,father,mother,father_occ,mother_occ,num_of_brothers,num_of_sisters,about_famly,register_as,email,mobile_number,address))
       elif gender == 'female':
              # print(fname,lname,gender,dob,age,religion,country,father,mother,father_occ,mother_occ,mother_tounge,qualification,occupation,salary,address,pincode,state,addhar,mobile_number,alternate_number)
              cursor.execute("INSERT INTO FEMALE VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(fname,age,gender,highest_education,profession,salary,city,native_place,height,complexion,mother_tounge,religion,physical_status,father,mother,father_occ,mother_occ,num_of_brothers,num_of_sisters,about_famly,register_as,email,mobile_number,address))
       con.commit()

# def uploadform(email,fname,age,dob,father,mother,gender,phone,qualification):
#        cursor.execute("INSERT INTO NEWUSER VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(email,fname,age,dob,father,mother,gender,phone,qualification))
#        con.commit()

app = Flask(__name__)

app.secret_key = 'abcd123'

@app.route('/')
def home():
       if g.user:
              profile = True
              return render_template("home2.html",profile = profile)
       return render_template('home2.html')

@app.route('/logedin')
def index():
   return render_template('index.html')

@app.route('/login', methods = ['POST','GET'])
def login():
       alert = True
       profile = False
       username = request.form.get('username')
       password = request.form.get('password')
       check =  uservalidate(username,password)
       if request.method == 'POST':
              session.pop('user',None)
              if check:
                     session['user'] = username
                     profile = True
                     return render_template("home2.html",profile = profile)
                     #return redirect(url_for('home2'))
              else:
                     return render_template('MainLogin.html',alert = alert)                    
       return render_template('MainLogin.html')

@app.route('/home2')
def home2():
   return render_template("home2.html")

@app.route('/newUser',methods = ['POST', 'GET'])
def newUser():
       alert = False
       accountAdded = False
       if request.method == 'POST':
              fname = request.form.get('dob')
              age = request.form.get('age')
              gender = request.form.get('gender')
              height = request.form.get('height')
              complexion = request.form.get('complexion')
              highest_education = request.form.get('highest_education')
              profession = request.form.get('profession')
              salary = request.form.get('salary')
              working_place = request.form.get('working_place')
              native_place = request.form.get('native_place')
              mother_tounge = request.form.get('mother_tounge')
              religion = request.form.get('religion')
              caste = request.form.get('caste')
              material_status = request.form.get('material_status')
              physical_status = request.form.get('physical_status')
              father = request.form.get('father')
              mother = request.form.get('mother')
              father_occ = request.form.get('father_occ')
              mother_occ = request.form.get('mother_occ')
              num_of_brothers = request.form.get('num_of_brothers')
              num_of_sisters = request.form.get('num_of_sisters')
              about_famly = request.form.get('about_famly')
              photos=request.form.get("photos")
              register_as = request.form.get('register_as')
              mobile_number = request.form.get('mobile_number')
              alt_mobile_number = request.form.get('alt_mobile_number')
              email_id = request.form.get('email_id')
              address = request.form.get('address')
              # RegisterFormData(fname,age,gender,highest_education,profession,salary,city,native_place,height,complexion,mother_tounge,religion,physical_status,father,mother,father_occ,mother_occ,num_of_brothers,num_of_sisters,about_famly,register_as,email,mobile_number,address)
              #user Details
              username = request.form.get('username')
              password = request.form.get('password')
              checkuser(username)
              usercheck = checkuser(username)
              if usercheck:
                     alert = True
                     return render_template('newUser.html',alert = alert)
              elif usercheck == False:
                     uploadData()
                     accountAdded = True
                     return render_template('newUser.html',accountAdded = True)
       return render_template('newUser.html')    


@app.route('/MatchFinder',methods=["POST","GET"])
def match_finder():
   if g.user:
          profile = True
          if request.method =="POST":
                     gender = request.form.get("gender")
                     from_age = request.form.get("from_age")
                     to_age = request.form.get("to_age")
                     from_height = request.form.get("from_height")
                     to_height = request.form.get("to_height")
                     mother_tounge = request.form.get("mother_tounge")
                     religion = request.form.get("religion")
                     caste = request.form.get("caste")
                     material_status = request.form.get("material_status")
                     print(gender)
          return render_template('match_finder.html',profile=profile)
   return redirect(url_for('login'))

@app.route('/searchResult')
def search_result():
       if g.user:
              return render_template("search_result.html",profile = True)
       return redirect(url_for('login'))

@app.route('/interest')
def interest():
       if g.user:
              return render_template('interestPage.html',profile = True)
       return redirect(url_for('login'))

@app.route('/myProfile')
def myProfile():
       if g.user:
              return render_template ('My_profile.html')

@app.before_request
def before_request():
       g.user = None
       if 'user' in session:
              g.user = session['user']
                      
@app.route('/dropsession')
def dropsession():
   session.pop('user',None)
   return redirect(url_for('login'))


# @app.route('/form', methods = ['POST', 'GET'])
# def register():
#        fname = request.form.get('fname')
#        age = request.form.get('age')
#        gender = request.form.get('gender')
#        highest_education = request.form.get('highest_education')
#        profession = request.form.get('profession')
#        salary = request.form.get('salary')
#        # city = request.form.get('city')
#        native_place = request.form.get('native_place')
#        height = request.form.get('height')
#        complexion = request.form.get('complexion')
#        mother_tounge = request.form.get('mother_tounge')
#        religion = request.form.get('religion')
#        physical_status = request.form.get('physical_status')
#        father = request.form.get('father')
#        mother = request.form.get('mother')
#        father_occ = request.form.get('father_occ')
#        mother_occ = request.form.get('mother_occ')
#        num_of_brothers = request.form.get('num_of_brothers')
#        num_of_sisters = request.form.get('num_of_sisters')
#        about_famly = request.form.get('about_famly')
#        register_as = request.form.get('register_as')
#        email = request.form.get('email')
#        mobile_number = request.form.get('mobile_number')
#        address = request.form.get('address')
#        # RegisterFormData(fname,age,gender,highest_education,profession,salary,city,native_place,height,complexion,mother_tounge,religion,physical_status,father,mother,father_occ,mother_occ,num_of_brothers,num_of_sisters,about_famly,register_as,email,mobile_number,address)
       
#        return "success"


       


if __name__ == '__main__':
    app.run(debug= True)
