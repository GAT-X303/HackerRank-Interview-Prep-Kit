/*
Allan Hieng
Prints an array, line by line
*/

void print_array(int *array, int num){
  int i;
  for (i = 0;i < num; i++){
    printf("%d\n",*(array + i));
  }
}
