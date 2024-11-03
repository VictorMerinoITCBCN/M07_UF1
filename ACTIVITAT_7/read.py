from Connection import Connection

def read_users():
    try:
        conn = Connection.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM usuari"

        cursor.execute(query)
        response = cursor.fetchall()

        return {"status": 1, "msg": f"{len(response)} usuaris seleccionats","users": response}
    except Exception as e:
        return {"status": -1, "msg": f"Error: {e}"}
    finally:
        Connection.close()