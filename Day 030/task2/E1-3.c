//  Exercise 1-3. Modify the temperature conversion program to print a heading above the table. 

#include <stdio.h>


#include <stdio.h>

int main() {
    int fahr;     
    int celsius;  
    int lower;    
    int upper;    
    int step;     // how much to increase each time

    lower = 0;     // start at 0 degrees Fahrenheit
    upper = 300;   // go up to 300 degrees
    step = 20;     // go up by 20 each time

    fahr = lower;  /


    printf("Fahrenheit\tCelsius\n");  

    while (fahr <= upper) {
        celsius = 5 * (fahr - 32) / 9;   
        printf("%d\t\t%d\n", fahr, celsius);  
        fahr = fahr + step; 
    }

    return 0;  // because main is an int function
}
