//Accounts Book Programme - Assigment 4 of UCC module "Programming in C"

#include <stdio.h>
#include <string.h>

#define MAXNAMESIZE 30
#define MAX_ACCOUNTS 20


struct personalAccount { // initilising a new structure representing an account

    char name[MAXNAMESIZE];
    int pinNumber;
    float balance;

};


struct personalAccount accounts[MAX_ACCOUNTS];
int accountCounter = 0;

void account_initiation();
void createAccount();
void displayAccount(int index);
void array_of_accounts();
float return_balance(int pin);
float return_sum();
void largest_balance_account();
void main_menu();


int main() {

account_initiation();
main_menu();
return 0;

}


void account_initiation() {

    for (int i = 0; i < MAX_ACCOUNTS; i++) {
        accounts[i].pinNumber = i; // Initiates an account with a pin number from 0 to 20, allowing for a maximu of 20 accounts
    }

}


// Function to create a new account
void createAccount() {

    if (accountCounter >= MAX_ACCOUNTS) { // Prevents the user from registering more than 20 accounts
        printf("Account limit reached.\n");
        return 0;
    }

    printf("Please enter your full name: ");
    scanf(" %29[^\n]", accounts[accountCounter].name);

    printf("Please enter your current bank balance: ");
    scanf("%f", &accounts[accountCounter].balance);

    accounts[accountCounter].pinNumber = accountCounter;
    printf("Your pin number for this account is %d.\n",
    accounts[accountCounter].pinNumber);

    accountCounter++;

}


void displayAccount(int index) {

    printf("Account Information:\n");
    printf("Name: %s\n", accounts[index].name); // Account information is indexed so that it can relate to functionally any user account
    printf("Pin: %d\n", accounts[index].pinNumber);
    printf("Balance: %.2f\n", accounts[index].balance); // Rounds the balance

}


void array_of_accounts() {

    printf("Current accounts in the system:\n");

    for (int i = 0; i < accountCounter; i++) {
        displayAccount(i); // To display all accounts registered so far
    }

}


float return_balance(int pin) { // Returns the balance for a valid pin number

    if (pin < 0 || pin >= accountCounter) {
        printf("Invalid pin number.\n");
        return -1;
    }

    return accounts[pin].balance;

}


float return_sum() {

    float sum = 0;

    for (int i = 0; i < accountCounter; i++) { // Calculates the total balance of all accounts
        sum += accounts[i].balance;
    }

    return sum;

}


// Function to find and display the account with the largest balance
void largest_balance_account() {

    float max_balance = accounts[0].balance;
    int max_index = 0;

    for (int i = 1; i < accountCounter; i++) {
        if (accounts[i].balance > max_balance) {
            max_balance = accounts[i].balance;
            max_index = i;

        }

    }

    printf("Account with largest balance:\n");
    displayAccount(max_index); // Displays the largest account balance

}


void main_menu() { // The main menu, welcoming the user, and helps them to navigate the functions above

    char choice;

    while (1) {

        printf("\nWelcome to the bank account service.\n\n");
        printf("Please enter:\n\n'L' to log in,\n'R' to register,\n'S' to show all accounts,\n'T' to
        total balances,\n'F' for the largest balance,\n'Q' to quit: ");
        scanf(" %c", &choice);

        switch(choice) { // A switch statement for user to choose between the main menu options

            case 'L' : int pin;

                printf("Enter your pin number: ");
                scanf("%d", &pin);

                float balance = return_balance(pin);
                printf("Your balance is: %.2f\n", balance);

            case 'R' : createAccount();

            case 'S' : array_of_accounts();

            case 'T' : printf("Total balance of all accounts: %.2f\n", return_sum());

            case 'F' : largest_balance_account();

            case 'Q' : break;
            
            default : printf("Invalid choice. Please try again.\n");

        }

    }

}

