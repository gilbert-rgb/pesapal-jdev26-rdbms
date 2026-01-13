import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rdbms.storage import save_table, load_table

class Database:
    def create_table(self, name, columns, primary_key=None, unique=None):
        table = {
            "name": name,
            "columns": columns,
            "rows": [],
            "primary_key": primary_key,
            "unique": unique or []
        }
        save_table(name, table)
        return f"Table '{name}' created"

    def insert(self, table_name, row):
        table = load_table(table_name)
        if not table:
            return "Table not found"

        # Primary key check
        pk = table["primary_key"]
        if pk:
            for r in table["rows"]:
                if r[pk] == row[pk]:
                    return "Primary key violation"

        # Unique check
        for col in table["unique"]:
            for r in table["rows"]:
                if r[col] == row[col]:
                    return f"Unique constraint violation on {col}"

        table["rows"].append(row)
        save_table(table_name, table)
        return "Row inserted"

    def select_all(self, table_name):
        table = load_table(table_name)
        if not table:
            return "Table not found"
        return table["rows"]

    def update(self, table_name, column, value, where_col, where_val):
        table = load_table(table_name)
        if not table:
            return "Table not found"
        updated = False
        for row in table["rows"]:
            if row[where_col] == where_val:
                row[column] = value
                updated = True
        save_table(table_name, table)
        return "Row updated" if updated else "No matching row"

    def delete(self, table_name, where_col, where_val):
        table = load_table(table_name)
        if not table:
            return "Table not found"
        table["rows"] = [r for r in table["rows"] if r[where_col] != where_val]
        save_table(table_name, table)
        return "Row deleted"

    def join(self, table1, table2, col1, col2):
        t1 = load_table(table1)
        t2 = load_table(table2)
        if not t1 or not t2:
            return "Table not found"
        result = []
        for r1 in t1["rows"]:
            for r2 in t2["rows"]:
                if r1[col1] == r2[col2]:
                    result.append({**r1, **r2})
        return result


# --- SQL Parsers ---
def parse_create_table(command):
    command = command.replace(";", "")
    before, inside = command.split("(", 1)
    table_name = before.split()[2]
    columns_part = inside.replace(")", "")
    columns_def = columns_part.split(",")

    columns = []
    primary_key = None
    unique = []

    for col in columns_def:
        parts = col.strip().split()
        col_name = parts[0]
        columns.append(col_name)
        if "PRIMARY" in parts:
            primary_key = col_name
        if "UNIQUE" in parts:
            unique.append(col_name)

    return table_name, columns, primary_key, unique


def parse_insert(command):
    command = command.replace(";", "")
    parts = command.split("VALUES")
    table_name = parts[0].split()[2]

    values_part = parts[1].strip().strip("()")
    raw_values = values_part.split(",")

    values = []
    for v in raw_values:
        v = v.strip()
        if v.startswith('"') and v.endswith('"'):
            values.append(v.strip('"'))
        else:
            values.append(int(v))
    return table_name, values
