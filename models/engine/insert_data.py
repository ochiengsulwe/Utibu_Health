#!/usr/bin/env python3
"""Inserts values for table fields."""
from __init__ import conn, cur


def insert_data(table, **kwargs):
    """Populates `table` fields from unpacked`**kwargs`.

    Args:
        table (str): Table element we are updating.
        **kwargs (Any): key/value representing the column and value.
                        Key represents the table column, and
                            Value is the object attribute value mapped to the
                                table.
    """
    try:
        columns = ", ".join(kwargs.keys())
        values = ", ".join([f"'{value}'" for value in kwargs.values()])
        insert_query = f"INSERT INTO {table} ({columns}) VALUES({values})"
        cur.execute(insert_query)
    except MySQLdb.Error as e:
        print(f"Encounted and Error Inserting to table: {e}")
    finally:
        conn.commit()
        cur.close()
        conn.close()
