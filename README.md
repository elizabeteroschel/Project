#MY BOOK SHELF 
My Book Shelf is a full-stack web application for searching books and get 

##Contents
* [Features](#features)
* [Technologies & Stack](#techstack)
* [Set-up & Installation](#configuration)
* [About the Developer](#about)

##  <a name="techstack"></a> Technologies and Stack
**Backend:**
Python, Flask, SQLAlchemy, PostgreSQL <br>
**Frontend:**
Babel, Bootstrap, Google Fonts, HTML5, CSS3 <br>
**Datasete:**
Good Reads (Kaggle)

## <a name="configuration"></a> Set-up & Installation
Install a code editor such as [VS code](https://code.visualstudio.com/download) or [Sublime Text](https://www.sublimetext.com/).<br>
Install [Python3](https://www.python.org/downloads/mac-osx/)<br>
Install [pip](https://pip.pypa.io/en/stable/installing/), the package installer for Python <br>
Install [postgreSQL](https://www.postgresql.org/) for the relational database.<br>

Clone or fork repository:
```bash
git clone https://github.com/elizabeteroschel/mybookshelf.git
```
Create and activate a virtual environment inside the mybooksheldirectory:
```bash
virtualenv env
source env/bin/activate
```

Install dependencies:
```bash
pip3 install -r requirements.txt
```

With PostgreSQL, create the mybookshelf database:
```bash
createdb mybookshelf
```

Create all tables and relations in the database and seed all data:
```bash
python3 seed.py
```
Run the app from the command line:
```bash
$ python3 server.py
```

## <a name="features"></a> Features 
User registration, log-in, & log-out
<br>
<br>
![](https://gph.is/g/aNbgjzd)
<br>


## <a name="about"></a>About the Developer
My Book Shelf creator Elizabete Roschel graduated from the University of São Jose, São Paulo  with a degree in Veterinary medicine. This is her first full-stack project. She can be found on [LinkedIn](https://www.linkedin.com/in/elizabete-freire-roschel-b2902215a/) and on [Github](https://github.com/elizabeteroschel).