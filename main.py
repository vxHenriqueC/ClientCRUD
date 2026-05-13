from db import init_database
from clients import (
    create_client,
    list_clients,
    search_client,
    update_client,
    delete_client
)

init_database()

while True:

    print("\n=== CLIENTFLOW ===")
    print("1 - Create client")
    print("2 - List clients")
    print("3 - Search client")
    print("4 - Update client")
    print("5 - Delete client")
    print("0 - Exit")

    option = input("Choose an option: ")

    if option == "1":

        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        company = input("Company: ")

        create_client(name, email, phone, company)

    elif option == "2":

        clients = list_clients()

        if len(clients) == 0:
            print("No clients found.")
        else:
            for client in clients:
                print(client)

    elif option == "3":

        client_id = input("Client ID: ")

        client = search_client(client_id)

        if client:
            print(client)
        else:
            print("Client not found.")

    elif option == "4":

        client_id = input("Client ID: ")

        name = input("New name: ")
        email = input("New email: ")
        phone = input("New phone: ")
        company = input("New company: ")

        update_client(client_id, name, email, phone, company)

    elif option == "5":

        client_id = input("Client ID: ")

        delete_client(client_id)

    elif option == "0":

        break