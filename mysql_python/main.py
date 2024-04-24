from database import cursor, db

# insert into
def add_log(text, user):
    sql = "INSERT INTO logs(text, user) VALUES (%s, %s)"
    cursor.execute(sql, (text, user))
    db.commit()
    log_id = cursor.lastrowid
    print(f"Added log {log_id}")

# select * from
def get_logs():
    sql = "SELECT * FROM logs ORDER BY created DESC"
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(row[1])

# select * from where id =
def get_log(id):
    sql = "SELECT * FROM logs WHERE id = %s"
    cursor.execute(sql, (id,))
    result = cursor.fetchone()

    for row in result:
        print(row)

# update
def update_log(id, text):
    sql = "UPDATE logs SET text = %s WHERE id = %s"
    cursor.execute(sql, (text, id))
    db.commit()
    print("Log Updated")

# delete
def delete_log(id):
    sql = "DELETE FROM logs WHERE id = %s"
    cursor.execute(sql, (id,))
    db.commit()
    print("Log Removed")


# add_log("This log one", "Aisyah")
# add_log("This log two", "Haryati")
# add_log("This log three", "Astuti")

# get_logs()
# get_log(2)

# update_log(2, "Updated log")

delete_log(2)
get_logs()
