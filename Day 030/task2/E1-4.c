// Exercise 1-4. Write a program to print the corresponding Celsius to Fahrenheit table

#include <stdio.h>

int main() {
    int celsius;   
    int fahr;      
    int lower;     
    int step;      
    lower = 0;     
    upper = 300;   
    step = 20;     

    celsius = lower;  /


    printf("Celsius\tFahrenheit\n");

    while (celsius <= upper) {
        fahr = (9 * celsius) / 5 + 32;   // convert to Fahrenheit
        printf("%d\t\t%d\n", celsius, fahr);  // print both values
        celsius = celsius + step;  // move to the next step
    }

    return 0;
}
