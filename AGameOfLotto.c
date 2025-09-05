//Lotto Programme - Assigment 2 of UCC module "Programming in C"

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int size_of_ray, lowest, greatest;

void welcome_user() {

    printf("Welcome to a lotto game! Please enter the length of the lotto list: ");
    scanf("%d", &size_of_ray);

    printf("Please enter the lowest number possible for the random combination: ");
    scanf("%d", &lowest);

    printf("Please enter the greatest number possible for the random combination: ");
    scanf("%d", &greatest);

    /*A while loop allows the user to continue only when the size of array is smaller than
    10, and greater than 0,
    as well as greatest vale greater than smallest minus lowest possible value to be
    generated is smaller
    than the size of the array.*/

    while ((lowest >= greatest) || (size_of_ray <= 0) || (size_of_ray > 10) || (greatest - lowest
    > size_of_ray)) {

    printf("\nError. Maximum length allowed is 10, and has to be greater than 0,\nso that
    it is larger then the difference between the largest and smallest number in the
    array.\nPlease enter the length of the lotto list: ");
    scanf("%d", &size_of_ray);

    printf("Please enter the lowest number possible for the random combination: ");
    scanf("%d", &lowest);

    printf("Please enter the greatest number possible for the random combination: ");
    scanf("%d", &greatest);

    }
}


void unique_list(int lotto[]) {

    srand(time(NULL)); // The srand() function ensures a unique list to be genearted every time the programme is run.
    for (int i = 0; i < size_of_ray; i++) { // A for loop that generates a unique list of random numbers in entred range.
        lotto[i] = rand() % ((greatest + 1) - lowest) + lowest;

    }
}


void printlist(int list[], int n) {

    for (int i = 0; i < n-1; i++) {
        printf("%d, ", list[i]); // Prints the comma seperated pseudo-random values in a list.
    }

    printf("%d", list[n-1]); // Prints the last pseudo-random number without being followed by a comma.
}

int* sortlist(int list[], int n) { // Bubble sort algorithm that sorts the pseudo-random list of numbers from smallest to biggest.

    int i, j, temp;
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) { // Switches the two numbers if a number in a list is bigger than the number following it.
            if (list[j] > list[j + 1]) {
                temp = list[j];
                list[j] = list[j + 1];
                list[j + 1] = temp;
            }
        }
    }
    
return list;

}

int main() {

    welcome_user();

    int lotto[size_of_ray];

    unique_list(lotto);

    printf("\nYour lotto list: ");
    printlist(sortlist(lotto, size_of_ray), size_of_ray);
    
    return 0;
}

