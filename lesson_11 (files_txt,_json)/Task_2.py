import json
import os



def add_entries(phonebook):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    country = input("Enter country: ")
    state = input("Enter state: ")
    city = input("Enter city: ")

    phonebook_entry = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "country": country,
        "state": state,
        "city": city
    }

    phonebook["users"].append(phonebook_entry)
    print("Entry added successfully!")
    print(phonebook)
    save_phonebook(phonebook)





def search_by_first_name (phonebook):
    print("search_by_first_name")
    first_name_to_search=input("Enter first name: ")
    for user in phonebook['users']:
        if user['first_name'] == first_name_to_search:
            print(user)

def search_by_last_name (phonebook):
    print("search_by_last_name")
    last_name_to_search=input("Enter last name: ")
    for user in phonebook['users']:
        if user['last_name'] == last_name_to_search:
            print(user)

def search_by_full_name (phonebook):
    print("search_by_full_name")
    full_name_to_search=input("Enter full name: ")
    for user in phonebook['users']:
        if user ['first_name'] + " " + user['last_name'] == full_name_to_search:
            print(user)

def search_by_phone_number (phonebook):
    print("search_by_phone_number")
    phone_number_to_search=input("Enter phone number: ")
    for user in phonebook['users']:
        if user['phone_number'] == phone_number_to_search:
            print(user)


def search_by_city_or_state(phonebook):
    print("search_by_city_or_state")
    city_or_state_to_search=input("Enter city or state to search: ")
    for user in phonebook['users']:
        if user['city'] == city_or_state_to_search or user['state'] == city_or_state_to_search:
            print(user)

def delete_record(phonebook):
    print("delete_record_by_phone_number")
    phone_number_to_search = input("Enter phone number: ")
    for user in phonebook['users']:
        if user['phone_number'] == phone_number_to_search:
            phonebook['users'].remove(user)
            save_phonebook(phonebook)


def update_record(phonebook):
    print("update_record_by_phone_number")
    phone_number_to_search = input("Enter phone number: ")

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    country = input("Enter country: ")
    state = input("Enter state: ")
    city = input("Enter city: ")

    phonebook_entry = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "country": country,
        "state": state,
        "city": city
    }
    for user in phonebook['users']:
        if user['phone_number'] == phone_number_to_search:
            index=phonebook['users'].index(user)
            phonebook['users'] [index]= phonebook_entry
            save_phonebook(phonebook)


def default():
    print("Unknown operation")

def get_phonebook():
    with open("phonebook_pattern.json", 'r') as file:
        phonebook = json.load(file)
        return phonebook

def save_phonebook (phonebook):
     with open("phonebook_pattern.json", "w") as file:
         json.dump(phonebook, file)


def exit_the_program(phonebbok6):
    exit ()


def main():
    phone_book_operations = {
        1: add_entries,
        2: search_by_first_name,
        3: search_by_last_name,
        4: search_by_full_name,
        5: search_by_phone_number,
        6: search_by_city_or_state,
        7: delete_record,
        8: update_record,
        9: exit_the_program

    }

    phonebook = get_phonebook()


    operation = int(input("""Enter number of operation: 
    Add new entries: 1 
    Search by first name: 2 
    Search by last name: 3
    Search by full name: 4
    Search by telephone number: 5
    Search by city or state: 6
    Delete a record for a given telephone number: 7
    Update a record for a given telephone number: 8
    Exit the program: 9 \n"""))
    if operation in phone_book_operations:
        function_from_dictionary = phone_book_operations[operation]  # If op. = 1, func = add_entries
        function_from_dictionary(phonebook)
    else:
        default()


if __name__ == '__main__':
    main()


