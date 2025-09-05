//Caesar Cypher - Assigment 3 from UCC "Module Programming in C"

#include<stdio.h>
#define MAXNAME 10

FILE *uf;
char input_file[MAXNAME];
char output_file[MAXNAME];
char ray[100];

int indexi = 0;
int i;
int n;
int ch;
int counter;

int main() { // Three prompts below asks the user to enter the file name, the number n by which each character
    // will be shifted in the ASCII table to the user-named output file.

    printf("Welcome to Ceaser Shift Programme!\n\nPlease enter a name of file: ");
    scanf(" %s", input_file);

    printf("Please enter a value for an integer n: ");
    scanf(" %d", &n);

    printf("Please enter a name of an output file: ");
    scanf(" %s", output_file);

    uf = fopen(input_file, "w");
    fprintf(uf, "This is a string of characters to be cyphered.");
    fclose(uf);

    uf = fopen(input_file, "r");

    if (uf == NULL) { // Runs the while loop below only if the file exists.
        printf("Error opening file!\n");
        return 1;
    }

    while ((ch = fgetc(uf)) != EOF) { // Reads character by character from a file to stream until
        // end of file (EOF) until the end of file is encountered.
        // Ceaser shifts the ASCII value of each character by three places in the table.
        ray[indexi++] = ch+n; // I used an array to store and keep track of all characters read from input file until EOF is reached.
        counter++;
    }

    for(i=0; i<counter; i++) {
        printf("%c", ray[i]); // Displays, character by character, the contents of the input file stored in ray onto the terminal.
    }

    fclose(uf);

    uf = fopen(output_file, "w");
    fprintf(uf, "%s", ray); // The stored contents of the input file are written to the output file.
    fclose(uf);
    return 0;
}

