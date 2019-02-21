

# Python Script to Validate a CSV - Jesu Darison 
# 2018-08-30

### STEP :1 ------------Install Python3
### Python3.6 Needs to be installed in the system to execute the code 
# yum -y groupinstall development
# yum -y install zlib-devel

# wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz
# tar xJf Python-3.6.3.tar.xz
# cd Python-3.6.3
# ./configure   or sudo ./configure --enable-optimizations
# make   or sudo make altinstall
# make install
#type - python3.6 -V to check the version 


### STEP :2 ---------------Create a virutal environment for the project 
#Create the virtual Environment
#python3 -m venv env
#source /root/flask/Python-3.6.3/env/bin/activate

#which python
#python3 -m pip install pandas
#1. python3 -m pip install --allow-external mysql-connector-python mysql-connector-python
#2. apt-get install build-essential
#3. apt-get install python3-dev
#4. pip install mysqlclient

#deactivate 

## STEP :3 ----------------Execute the python file from within the virutal Environment
#To run the script from the virtual environment:
#source /root/flask/Python-3.6.3/env/bin/activate
#/root/flask/Python-3.6.3/env/bin/python  flask_app.py 
#deactivate


##sudo ufw status   / ufw allow 3306/tcp
###systemctl restart mysql or service mysql restart -> restarts mysql
# CREATE USER 'newuser'@'your_droplet_ip' IDENTIFIED BY 'password';
# GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'your_droplet_ip';
# FLUSH PRIVILEGES;
# sudo service mysql restart


##MYSQL settings
# sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf     (and change 127.0.0.1 to 192.168.1.100 ( local ip address ))
# #bind-address            =  127.0.0.1
# bind-address            =  192.168.1.100


# sudo /etc/init.d/mysql restart

# root@192.168.1.100:~$ mysql -u root -p

# CREATE USER 'root'@'%' IDENTIFIED BY 'password';
# GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
# FLUSH PRIVILEGES;
# If you want to have access only from specific ip address , change 'root'@'%' to 'root'@'( ip address or hostname)'

# CREATE USER 'root'@'192.168.1.100' IDENTIFIED BY 'password';
# GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.1.100' WITH GRANT OPTION;
# FLUSH PRIVILEGES;

# Then you can connect:
# nobus@xray:~$ mysql -h 192.168.1.100 -u root -p

from flask import Flask
import requests
from pyexchange import Exchange2010Service, ExchangeNTLMAuthConnection
import MySQLdb
from datetime import timedelta
from flask import jsonify,render_template


#app = Flask(__name__,static_folder='/Users/jgerardf/Downloads/jesu_angular_app/static')
app = Flask(__name__)


def mysql_connection(query):  
    # Open database connection
    db = MySQLdb.connect("74.208.94.46","root","Ct5g4yiniv","Jesu" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to DELETE required records  
    sql = query
    try:
    # Execute the SQL command
        cursor.execute(sql)
        data = cursor.fetchall()
        # items = []
        # for row in data:
        #      for key in cursor.description:
        #          items.append({key[0]:value for value in row})
        items = [dict(zip([key[0] for key in cursor.description], row)) for row in data]
        d = {'items':items}
        #print(data)
    # Commit your changes in the database
        db.commit()
    except:
    # Rollback in case there is any error
        db.rollback()
        db.close()

    # disconnect from server
    db.close()

    return d

def mysql_connection_bkup(query):  
    # Open database connection
    db = MySQLdb.connect("127.0.0.1","root","root","Jesu" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to DELETE required records  
    sql = query
    try:
    # Execute the SQL command
        cursor.execute(sql)
        data = cursor.fetchall()
        # items = []
        # for row in data:
        #      for key in cursor.description:
        #          items.append({key[0]:value for value in row})
        items = [dict(zip([key[0] for key in cursor.description], row)) for row in data]
        d = {'items':items}
        #print(data)
    # Commit your changes in the database
        db.commit()
    except:
    # Rollback in case there is any error
        db.rollback()
        db.close()

    # disconnect from server
    db.close()

    return d

##  Routes declarations :
@app.route("/index")
def index():
  
    #return "welcome to ecommerce app"
    return render_template('index.html', name=index)

@app.route("/getProducts")
def getProducts():
    data = mysql_connection_bkup('''select * from vestment_products;''')
    return jsonify(data)


@app.route("/insertProducts")
def insertProducts():
    sql_query ="""insert into vestment_products
    values
    ('1','one','http://tech.firstpost.com/wp-content/uploads/2014/09/Apple_iPhone6_Reuters.jpg','description of product 1','132','100'),
    ('2','one','http://tech.firstpost.com/wp-content/uploads/2014/09/Apple_iPhone6_Reuters.jpg','description of product 2','432','200'),               ('3','one','http://tech.firstpost.com/wp-content/uploads/2014/09/Apple_iPhone6_Reuters.jpg','description of product 3','632','100'),
    ('4','one','http://tech.firstpost.com/wp-content/uploads/2014/09/Apple_iPhone6_Reuters.jpg','description of product 4','732','300'),
    ('5','one','http://tech.firstpost.com/wp-content/uploads/2014/09/Apple_iPhone6_Reuters.jpg','description of product 5','832','600');"""
    data = mysql_connection_bkup(sql_query)
    return "succesfully inserted"



if __name__ == "__main__":
    #app.run(host='74.208.94.46', debug=True, port=80)
    app.run(debug=True)





#####

##DB creds
##Connect using ssh instead of standard
##74.208.94.46 - Mysql Host
##root- username
## pass - n/A
## ssh host - ip
##ssh user - root
## ssh pass - N/A
##SQL queries:
 
#  create table vestment_products
#  (
#  product_id                varchar(255),
#  product_name              varchar(255),
#  product_image             varchar(255),
#  product_description       varchar(255),
#  product_price             varchar(255),
#  product_quantity          varchar(255));
                           
						   
# insert into vestment_products
# values
# ('1','one','http://tech.firstpost.com/wp-content/uploads/2014/09/Apple_iPhone6_Reuters.jpg','description of product 1','132','100'),
# ('2','one','http://tech.firstpost.com/wp-content/uploads/2014/09/Apple_iPhone6_Reuters.jpg','description of product 2','432','200'),               ('3','one','http://tech.firstpost.com/wp-content/uploads/2014/09/Apple_iPhone6_Reuters.jpg','description of product 3','632','100'),
# ('4','one','http://tech.firstpost.com/wp-content/uploads/2014/09/Apple_iPhone6_Reuters.jpg','description of product 4','732','300'),
# ('5','one','http://tech.firstpost.com/wp-content/uploads/2014/09/Apple_iPhone6_Reuters.jpg','description of product 5','832','600');



# insert into vestment_products
# values
# ('1','one','/static/images/m1.png','description of product 1','132','100'),
# ('2','one','/static/images/m2.png','description of product 2','432','200'),               
# ('3','one','/static/images/m3.png','description of product 3','632','100'),
# ('4','one','/static/images/m4.png','description of product 4','732','300'),
# ('5','one','/static/images/m1.png','description of product 5','832','600');