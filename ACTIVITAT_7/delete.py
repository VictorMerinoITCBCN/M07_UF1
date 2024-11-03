from Connection import Connection

def delete_user(id):
    try:
        conn = Connection.get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM usuari WHERE id = %s"

        cursor.execute(query, (id))
        conn.commit()

        return {"status": 1, "msg": f"Usuari amb id: {id} elminat"}
    except Exception as e:
        return {"status": -1, "msg": f"Error: {e}"}
    finally:
        Connection.close()