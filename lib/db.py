#coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

session = False

def db_init(db_s):
	global db_string
	global session
	db_string = db_s
	engine = create_engine(db_string,echo = False,pool_size=20,pool_recycle=30)
	Seesion = sessionmaker(bind=engine,autoflush = True)
	session = Session()

def db_close():
	global session
	session.close()

def exesql(sql):
	global session

	try:
		#s.execute("set names utf8;")
		o = session.execute(sql)
	except Exception,e:
		print sql
		session.close()
		exit()
		return

	t = sql[0:3].lower()

	if t == "sel":
		return o.fetchall()
	elif t == "ins":
		session.commit()
		return o.lastrowid
	elif t == "upd":
		session.commit()
		return o.rowcount
	else :
		session.commit()
		return o.rowcount


