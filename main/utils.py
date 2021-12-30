from ldap3 import Server, Connection


def create_connection(hostname, port, user, password):
    server = Server(hostname, port=port)
    conn = Connection(server, user, password, auto_bind=True)
    return conn
