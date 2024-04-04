#!/usr/bin/env pyhton3
"""Establishes connection to database."""
import MySQLdb


conn = MySQLdb.connect(host="localhost",
                       user="username",
                       passwd="password"
        )

cur = conn.cursor()

