<h1>Learning Objectives</h1>
<h2>General</h2>
<ul>
  <li>Why Python programming is awesom</li>
  <li>How to connect to a MySQL database from a Python script</li>
  <li>How to SELECT rows in a MySQL table from a Python script</li>
  <li>How to INSERT rows in a MySQL table from a Python script</li>
  <li>What ORM means</li>
  <li>How to map a Python Class to a MySQL table</li>
  <li>How to create a Python Virtual Environment</li>
</ul>
<h3>Install and activate venv</h3>

<p>To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:</p>
<h4>sudo apt-get install python3.8-venv</h4>
<h4>python3 -m venv venv</h4>
<h4>source venv/bin/activate</h4>
<h3>Install MySQLdb module version 2.0.x</h3>
<p>For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04</p>
<h4>sudo apt-get install python3-dev</h4>
<h4>sudo apt-get install libmysqlclient-dev</h4>
<h4>sudo apt-get install zlib1g-dev</h4>
<h4>sudo pip3 install mysqlclient</h4>
<h4>python3</h4>
<h4> >>>import MySQLdb</h4>
<h4> >>>MySQLdb.version_info  </h4>
<h4>(2, 0, 3, 'final', 0)</h4>
<h3>Install SQLAlchemy module version 1.4.x</h3>
<h4>sudo pip3 install SQLAlchemy</h4>

<h4>python3</h4>
<h4> >>>import sqlalchemy</h4>
<h4> >>>sqlalchemy.__version__ </h4>
<h4>'1.4.22'</h4>
