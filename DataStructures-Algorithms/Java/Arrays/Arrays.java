/**
Allan Hieng
This file will be using Arrays.
It will do the following:
1. Create a random array of size N
2. Output the random array of size N onto a text file
3. Use Bubblesort
**/

import java.util.Scanner; //used for getting user input
import java.io.File; //used to created and access files
import java.io.FileWriter; //used to write to files
import java.io.IOException; //used for IOException class to handle errors

public class Arrays {
	public static void main (String[] args) {
		
		//start of the program where it asks for size N of array and creates it
		//an unsorted array is returned and a txt file ver is created
		System.out.println("This is doing Arrays with Java!");

		int N;

		Scanner myScanner = new Scanner(System.in); //scanner object used to get input

		createRandomArray myRandomArray = new createRandomArray();

		System.out.print("Please enter size N of your random array: ");
		N = myScanner.nextInt();

		int[] unsortedArray = myRandomArray.createArray(N);
		//
		int[] bubbleArray = bubbleSort(unsortedArray, N);
	}

	//function used to write the sorted array to a txt file
	public static void writeArray(int[] sortedArray, int N, String textname){

		System.out.println("Creating " + textname + " ...");

		File myFile = new File(textname); //file object used to handle opening and closing files

		try {	
			myFile.createNewFile();
		} catch (IOException e) {
			System.out.println(e);
		}
	
		//loops N times and writes the sorted array
		try {
			FileWriter myWriter = new FileWriter(textname);

			for (int i = 0; i < N; i++){

				myWriter.write(Integer.toString(sortedArray[i]));
				myWriter.write("\n");
			}

			myWriter.close();

		} catch (IOException e) {
			System.out.println(e);
		}

		System.out.println(textname + " created.");

	}

	//bubble sort for descending order
	public static int[] bubbleSort(int[] unsortedArray, int N){

		System.out.println("Starting bubble sort...");
		
		int temp;

		int sortedArray[] = unsortedArray;

		for (int i = 0; i < N; i++){
			for (int j = 0; j < N; j++){
				if (sortedArray[i] > sortedArray[j]){
					temp = sortedArray[i];
					sortedArray[i] = sortedArray[j];
					sortedArray[j] = temp;
				}
			}
		}

		System.out.println("Bubble sort done.");

		writeArray(sortedArray, N, "bubblesorted.txt");

		return sortedArray;
	}

}
