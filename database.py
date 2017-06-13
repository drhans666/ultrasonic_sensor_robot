# This file should be on Your raspberry Pi

import sqlite3
import datetime
import time


# creates database and table if not provided
def create_table():
    conn = sqlite3.connect('robotbase.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS tests(datestamp TEXT, cycle INTEGER,'
              ' measure INTEGER, value REAL)')


# populates database with data
def data_entry(cycle):
    conn = sqlite3.connect('robotbase.db')
    c = conn.cursor()
    measure = 0
    # searches database for last cycle nr, so already named cycles wont be repeated
    c.execute("SELECT max(cycle) FROM tests")
    for row in c.fetchall():
        cycle_nr = (row[0])
        if cycle_nr == None:
            cycle_nr = 0
        else:
            pass
    cycle_nr = cycle_nr + 1

    # populates database with date, cycle nr, measure nr and measure value
    c.execute('BEGIN')
    for i in cycle:
        unix = time.time()
        datestamp = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        measure = measure + 1
        value = i
        c.execute("INSERT INTO tests (datestamp, cycle, measure, value) VALUES (?, ?, ?, ?)",
                  (datestamp, cycle_nr, measure, value))
    conn.commit()
    c.close()
    conn.close()
