#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
from random import randint
import datetime

con = lite.connect('coins.db')

def initialize(con):
    with con:
        
        cur = con.cursor()    
        cur.execute("CREATE TABLE IF NOT EXISTS Coins(Id INT, Bought INT, Sold INT, DateBought TEXT, DateSold TEXT)")    

def check_hex(con, num):
    with con:    
    
        cur = con.cursor()
        cur.execute("SELECT * FROM Coins WHERE Id=?", '1')

        try:
            first_row = cur.next()

            for row in [first_row] + res.fetchall():
                print '\t%s: %s' % (row[0], row[1])
        except StopIteration as e:
            return True

def gen_hex(con):
    hex_string = str(randint(0,1000000))

    if check_hex(con, hex_string):
        return hex_string
    else:
        return gen_hex(con)

def retreive(con):
    with con:    
    
        cur = con.cursor()
        cur.execute("SELECT * FROM Coins")

        rows = cur.fetchall()

        for row in rows:
            print row[2]


def add_coin(con, paid, date = str(datetime.datetime.now())):
    with con:    
    
        cur = con.cursor()

        id_string = gen_hex(con)

        cur.execute("INSERT INTO Coins VALUES("+id_string+","+str(paid)+",0,'"+date+"','0')")

def sold(con, amount, the_id, date = str(datetime.datetime.now())):
    with con:    
    
        cur = con.cursor()
        cur.execute("UPDATE Coins SET Sold=?, DateSold=? WHERE Id=?", (amount, date, the_id)) 

initialize(con)
sold(con, 130, 359650)
retreive(con)