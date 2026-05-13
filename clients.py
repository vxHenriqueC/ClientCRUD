from db import get_connection


def create_client(name, email, phone, company):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO clients (name, email, phone, company)
        VALUES (?, ?, ?, ?)
    """, (name, email, phone, company))

    connection.commit()
    connection.close()

    print("Client created successfully!")


def list_clients():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM clients")

    clients = cursor.fetchall()

    connection.close()

    return clients


def search_client(client_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM clients WHERE id = ?",
        (client_id,)
    )

    client = cursor.fetchone()

    connection.close()

    return client


def update_client(client_id, name, email, phone, company):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE clients
        SET name = ?, email = ?, phone = ?, company = ?
        WHERE id = ?
    """, (name, email, phone, company, client_id))

    connection.commit()
    connection.close()

    print("Client updated successfully!")


def delete_client(client_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM clients WHERE id = ?",
        (client_id,)
    )

    connection.commit()
    connection.close()

    print("Client deleted successfully!")