import sqlite3

def init_database():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    # Create table
    cur.execute('''CREATE TABLE Cards
                    (Name text, Cartridge text, Bullet text, Powder text, Charge text, Weight real, COAL text, Primer text, Brass text, notes text)''')
    cur.execute('''CREATE TABLE settings 
                    (TargetW real, CurrentW real, angle real, FSpeed real, MSpeed real, SSpeed real)''')
    con.commit()
    con.close()


def getSetting(param):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    weight =  cur.execute('''SELECT ''' + param + ''' FROM settings ''')
    con.close()
    return weight

def setSetting(param, value):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    weight =  cur.execute('''UPDATE settings SET ''' + param + '''=''' + value)
    con.close()

def getCards():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cards = []
    for row in cur.execute('SELECT * FROM Cards'):
        cards.append(row)
    con.close()
    return cards

def addCard(Name, Cartridge, Bullet, Powder, Charge, Weight, COAL, Primer, Brass, Notes):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("INSERT INTO Cards VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (Name, Cartridge, Bullet, Powder, Charge, Weight, COAL, Primer, Brass, Notes))
    con.close()

# Insert a row of data
#cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
#con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#con.close()