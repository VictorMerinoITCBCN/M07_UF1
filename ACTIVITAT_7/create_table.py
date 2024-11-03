from Connection import Connection

def create_user_table():
    try:
        conn = Connection.get_connection()
        cursor = conn.cursor()

        query = """CREATE TABLE IF NOT EXISTS usuari (
            id uuid PRIMARY KEY,
            name varchar(255),
            lastName varchar(255),
            age int,
            email varchar(255),
            phone int
        )
        """

        cursor.execute(query)
        conn.commit()

        return {"status": 1, "msg": f"Taula Usuari creada."}
    except Exception as e:
        return {"status": -1, "msg": f"Error: {e}"}
    finally:
        Connection.close()