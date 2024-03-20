# Loops & - for and while 
# Conditionals
# Repeat & Check


# Initializing our blcokchain list
blockchain = [] 


def get_last_blockchain_list():
    """ Return the last value of the current blockchain."""
    return blockchain[-1]


def add_list(transactions_amount, last_transaction=[1]):
    """ Apppend a new value as well as the last blockchain value to the blockchain. """
    """ add last """
    blockchain.append([last_transaction, transactions_amount])

def get_transaction_value():
    """ Return the input of the user (a new transaction amount) as a float(0.9) """
    user_input = float(input("Your Transaction amount please:. "))
    return user_input   

def get_user_choise():
    user_input = input("You Choice: ")
    return user_input

def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print("Output block")
        print(block)
    

tx_amount = get_transaction_value()
add_list(tx_amount)

while True:
    print("Please choose ")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    user_choice = get_user_choise()
    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_list = (tx_amount, get_last_blockchain_list())
    else:
        print_blockchain_elements()
        
      


print("Done!")
