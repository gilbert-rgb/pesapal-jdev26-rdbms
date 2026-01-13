import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rdbms.engine import Database, parse_create_table, parse_insert
from rdbms.storage import load_table

db = Database()

print("MiniRDBMS started. Type 'exit' to quit.")

# Check if a command file is provided
if len(sys.argv) > 1:
    file_path = sys.argv[1]
    with open(file_path, "r") as f:
        commands = f.read().splitlines()
else:
    commands = []

i = 0
while True:
    if i < len(commands):
        command = commands[i].strip()
        print(f"db> {command}")
        i += 1
    else:
        command = input("db> ").strip()

    if command.lower() == "exit":
        break

    if command.upper().startswith("CREATE TABLE"):
        name, columns, pk, unique = parse_create_table(command)
        print(db.create_table(name, columns, pk, unique))

    elif command.upper().startswith("INSERT"):
        table_name, values = parse_insert(command)
        table_meta = load_table(table_name)
        if not table_meta:
            print("Table not found")
            continue
        row = dict(zip(table_meta["columns"], values))
        print(db.insert(table_name, row))

    elif command.upper().startswith("SELECT"):
        table_name = command.split()[3]
        print(db.select_all(table_name))

    elif command.upper().startswith("UPDATE"):
        parts = command.replace(";", "").split()
        table_name = parts[1]
        column = parts[3].split("=")[0]
        value = parts[3].split("=")[1].replace('"', '')
        where_col = parts[5].split("=")[0]
        where_val = int(parts[5].split("=")[1])
        print(db.update(table_name, column, value, where_col, where_val))

    elif command.upper().startswith("DELETE"):
        parts = command.replace(";", "").split()
        table_name = parts[2]
        where_col = parts[4].split("=")[0]
        where_val = int(parts[4].split("=")[1])
        print(db.delete(table_name, where_col, where_val))

    elif command.upper().startswith("JOIN"):
        parts = command.split()
        table1 = parts[1]
        table2 = parts[2]
        col1 = parts[4].split(".")[1]
        col2 = parts[4].split("=")[1].split(".")[1]
        print(db.join(table1, table2, col1, col2))

    else:
        print("Unsupported command")
