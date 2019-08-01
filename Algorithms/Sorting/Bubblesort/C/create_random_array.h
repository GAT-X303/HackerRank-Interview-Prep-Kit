/*
Allan Hieng
Creates a random array that has numbers under 10.
*/

int *create_random_array(int num){
  int *array = (int*)malloc(num*sizeof(int)); //malloc used to keep area in memory 
  int i;
  for (i = 0; i < num; i++){
    *(array + i) = rand()%10;
  }
  return array;
}
