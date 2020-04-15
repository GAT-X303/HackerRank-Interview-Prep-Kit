/*
Allan Hieng
This file will generate a random array of numbers between 1-10 and write it to a text file.
It will overwrite any file with name "randomArray.txt".
*/

import java.util.Scanner; //used for getting user input
import java.io.File; //used to created and access files
import java.io.FileWriter; //used to write to files
import java.io.IOException; //used for IOException class to handle errors
import java.util.Random; //used for generating random numbers


public class createRandomArray {
	public static void main (String[] args) {
	
		int N;

		Scanner myScanner = new Scanner(System.in); //scanner object used to get input
		File myFile = new File("randomArray.txt"); //file object used to handle opening and closing files		
		Random myRandom = new Random();	//random object used to generate random ints	


		System.out.print("Please enter size N of your random array: ");
		N = myScanner.nextInt();
		
		System.out.println("Creating random array of size " + N);
		
		try {	
			myFile.createNewFile();
		} catch (IOException e) {
			System.out.println(e);
		}


		//loops N times and writes a random number from 1 - 100 on each new line
		try {
			FileWriter myWriter = new FileWriter("randomArray.txt");

			for (int i = 0; i < N; i++){
				myWriter.write(Integer.toString(myRandom.nextInt(100)));
				myWriter.write("\n");
			}

			myWriter.close();

		} catch (IOException e) {
			System.out.println(e);
		}

		System.out.println("randomArray.txt created."); //used to show the end of the process	
	}
}
