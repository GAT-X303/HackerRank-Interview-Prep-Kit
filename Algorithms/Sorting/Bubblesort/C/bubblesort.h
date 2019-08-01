/*
Allan Hieng
Bubble sort down in descending order. Iterates in an n^2 fashion and compares the dereferenced values of
the unsorted array
*/

#include "swap.h"

void bubblesort(int *array, int num){
  int i,j;
  for (i = 0; i < num; i++){
    for (j = 0; j < num; j++){
      if ((*(array + i)) > (*(array + j))){
        swap((array + i), (array + j));
      }
    }
  }
}
