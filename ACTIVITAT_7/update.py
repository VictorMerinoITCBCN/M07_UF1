from Connection import Connection

def update_user(id, name = None, last_name = None, age = None, email = None, phone = None):
    try:
        conn = Connection.get_connection()
        cursor = conn.cursor()

        query = "UPDATE usuari SET "
        values = []

        if name:
            query += "name = %s, "
            values.append(name)

        if last_name:
            query += "lastName = %s, "
            values.append(last_name)

        if age:
            query += "age = %s, "
            values.append(age)

        if email:
            query += "email = %s, "
            values.append(email)

        if phone:
            query += "phone = %s, "
            values.append(phone)

        query = query.rstrip(', ')
        
        query += " WHERE id = %s"
        values.append(id)

        cursor.execute(query, values)
        conn.commit()

        return {"status": 1, "msg": f"Usuari amb id: {id} actualitzat"}
    except Exception as e:
        return {"status": -1, "msg": f"Error: {e}"}
    finally:
        Connection.close()