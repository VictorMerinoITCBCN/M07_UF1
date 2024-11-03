import psycopg2

class Connection:
    
    _connection = None

    @staticmethod
    def connect():
        if Connection._connection: return

        host = "localhost"
        port = "5432"
        db = "postgres"
        user = "victor"
        password = "super"
        try:
            Connection._connection = psycopg2.connect(
                dbname = db,
                user = user,
                host = host,
                password = password,
                port = port
            )
        except Exception as e:
            print(f"Error connecting to the data base: {e}")

    @staticmethod
    def get_connection():
        if not Connection._connection: Connection.connect()
        
        return Connection._connection
    
    @staticmethod
    def close():
        if Connection._connection:
            Connection._connection.close()
            Connection._connection = None
        else: 
            print("There is no active connection.")