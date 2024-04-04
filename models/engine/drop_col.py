#!/usr/bin/env python3
"""Drops table column(s) or the whole table."""
from __init__ import cur, conn


def drop_(table, *args):
    """Deletes specified column(s) from the specified table.

        If `args` is missing, it will drop the whole table. This should be done
            with caution.

    Args:
        table (str): The table from which column(s) is to be deleted.
        *args (str): The table column(s) to be droped.
    """
    try:
        if not args:
            drop_query = f"DROP TABLE IF EXISTS {table}"
        else:
            columns = ", ".join(args)
            drop_query = f"ALTER TABLE {table} DROP COLUMN {columns}"

        cur.execute(drop_query)
    except MySQLdb.Error as e:
        print(f"An Error ocurred: {e}")

    finally:
        conn.commit()
        cur.close()
        conn.close()
