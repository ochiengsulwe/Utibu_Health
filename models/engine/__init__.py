#!/usr/bin/env pyhton3
"""Establishes connection to database."""
import MySQLdb


conn = MySQLdb.connect(host="localhost",
                       user="ochi",
                       password="ochi001"
        )

cur = conn.cursor()

