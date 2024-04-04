#!/usr/bin/env python3
"""Creats Database if it doesn't exist and change to it."""
from __init__ import conn, cur
import MySQLdb
import sys


def db_create(database):
    """"Creates a connection to database.

    args:
        user (str): The user accessing the named database.
        passwd (Any): Characters used to access permission to the database.
        database (str): The name of the database we are to create.
    """

    try:
        create_db_query = f"CREATE DATABASE IF NOT EXISTS {database};"

        cur.execute(create_db_query)
        print(f"Database({database}) successfully created.")
        use_db = f"USE {database};"

        cur.execute(use_db)
        print(f"Now using ({database}) database.")
    except MySQLdb.Error as e:
        print(f"Error creating database: {e}")

    finally:
        conn.commit()
        cur.close()
        conn.close()
