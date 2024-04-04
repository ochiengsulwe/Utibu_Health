#!/usr/bin/env python3
"""Creates tables on a database."""
import MySQLdb
from __init__ import conn, cur
import sys


def create_table(table_name, columns):
    """Creates tables to a database.

    Args:
        table_name (str): The table we are to create on our database.
        columns (:obj: `list` of :obj: `str`): A list of needed table fields.
    """
    try:
        create_ = f"CREATE TABLE IF NOT EXISTS `%s` ({', '.join(columns)});"
        cur.execute(create_)
    except MySQLdb.Error as e:
        print(f"Failed to create table <{table_name}: {e}>")
    finally:
        conn.commit()
        cur.close()
        conn.clos()
