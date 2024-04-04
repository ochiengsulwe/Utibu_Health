#!/usr/bin/env python3
"""Updates existing table fields."""
from __init__ import conn, cur


def update_table(table, condition=None, **kwargs):
    """Updates the value of table `table` fields unpacked from `**kwargs`.

    Args:
        table (str): Table element we are updating.
        **kwargs (Any): key/value representing the column and value.
                        Key represents the table column, and
                            Value is the object attribute value mapped to the
                                table.
        condition (:obj:`str` optional): A condition set to just update table
                                            if the condition is true.
    """
    try:
        set_clause = ", ".join([f"{key} = {value}" for key, value in
                                kwargs.items()])
        update_query = f"UPDATE `{table}` SET {set_clause}"
        if condition:
            update_query += f" WHERE {condition}"

        cur.execute(update_query)
    except MySQLdb.Error as e:
        print(f"Encounted and Error Updating table: {e}")
    finally:
        conn.commit()
        cur.close()
        conn.close()
