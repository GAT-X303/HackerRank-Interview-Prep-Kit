/*
Allan Hieng
Swaps values of 2 pointers
*/

void swap(int *a, int *b){
  int temp = *a;

  *a = *b;
  *b = temp;
}
