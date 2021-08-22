from sqhandler import SqHandler

s = SqHandler()

s.execute("CREATE TABLE lager(a TEXT)")
s.execute('INSERT INTO lager VALUES ("HAlllo")')
back = s.execute("SELECT a from lager", read=True)
print(back)
