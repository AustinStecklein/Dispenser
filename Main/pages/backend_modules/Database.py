import sqlite3

def init_database():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    # Create table
    cur.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Cards' ''')
    if (cur.fetchone()[0] == 0):
        cur.execute('''CREATE TABLE Cards
                    (Name text, Cartridge text, Bullet text, Powder text, Charge text, Weight real, COAL text, Primer text, Brass text, notes text)''')
    
    cur.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='settings' ''')
    if (cur.fetchone()[0] == 0):
        cur.execute('''CREATE TABLE settings 
                    (TargetW real, CurrentW text, angle real, FSpeed real, MSpeed real, SSpeed real, settingID real)''')
        cur.execute('''INSERT INTO settings (TargetW, CurrentW, angle, FSpeed, MSpeed, SSpeed, settingID) VALUES (0, 0, 0, 0, 0, 0, 1)''')
    con.commit()
    con.close()


def getSetting(param):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute('''SELECT ''' + param + ''' FROM settings WHERE settingID = 1''')
    weight = cur.fetchone()[0]
    con.close()
    return weight

def setSetting(param, value):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute('''UPDATE settings SET ''' + param + ''' =''' + value +''' WHERE settingID = 1''') 
    con.commit()
    con.close()

def getCards():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cards = []
    cur.execute('SELECT * FROM Cards')
    for row in cur.fetchall():
        cards.append(row)
    con.close()
    return cards

def addCard(Name, Cartridge, Bullet, Powder, Charge, Weight, COAL, Primer, Brass, Notes):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute('''INSERT INTO Cards VALUES (Name, Cartridge, Bullet, Powder, Charge, Weight, COAL, Primer, Brass, Notes)''')
    con.close()

def getCard(Name):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute('''SELECT * FROM Cards WHERE ''' + Name )
    card = cur.fetchone()[0]
    con.close()
    return card
# Insert a row of data
#cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
#con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#con.close()