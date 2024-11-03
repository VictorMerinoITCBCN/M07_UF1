from Connection import Connection

def create_user(id, name, last_name, age, email, phone):
    try:
        conn = Connection.get_connection()
        cursor = conn.cursor()

        query = "INSERT INTO usuari (id, name, lastName, age, email, phone) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (str(id), name, last_name, age, email, phone)

        cursor.execute(query, values)
        conn.commit()

        return {"status": 1, "msg": f"Usuari amb id: {id} creat."}
    except Exception as e:
        return {"status": -1, "msg": f"Error: {e}"}
    finally:
        Connection.close()
