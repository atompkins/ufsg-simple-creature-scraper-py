import sqlite3

con = sqlite3.connect('data.sqlite', isolation_level=None)

def init_sql():
  con.execute('''CREATE TABLE IF NOT EXISTS data (
      id               integer primary key
    , name             text    null
    , class            text    null
    , level            integer null
    , attack           integer null
    , defense          integer null
    , armor            integer null
    , damage           integer null
    , hp               integer null
  )''')

def close_sql():
  con.close()

def sql_writer(list):
  con.executemany('''REPLACE INTO data (
      id
    , name
    , class
    , level
    , attack
    , defense
    , armor
    , damage
    , hp
  )
  VALUES (
      ?
    , ?
    , ?
    , ?
    , ?
    , ?
    , ?
    , ?
    , ?
  )''', list)