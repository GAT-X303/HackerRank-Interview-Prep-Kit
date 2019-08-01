/*
Allan Hieng
Bubblesort implementation
*/

#include <stdlib.h>
#include <stdio.h>
#include "create_random_array.h"
#include "print_array.h"
#include "bubblesort.h"

int main(){

  int num;
  int *array;

  //user prompt
  printf("Please enter size of array: ");
  scanf("%d", &num);
  //

  array = create_random_array(num); //creates the array
  printf("Unsorted array\n");
  print_array(array, num); //prints the unsorted array
  bubblesort(array, num); //sorts the array
  printf("Sorted array\n");
  print_array(array, num); //prints the sorted array

  return 0;
}
