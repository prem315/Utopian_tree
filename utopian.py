import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner s = new Scanner(System.in);
        int T = s.nextInt();
        int[] numArr = new int[T];
        for(int i = 0; i < numArr.length; i++){
            numArr[i] = s.nextInt();
        }

        for(int i:numArr){
            Utopian_Tree(i);
        }
    }

    public static void Utopian_Tree(int number){
        int height = 1; 
        for(int i =0;i<number;i++){
            if(i%2 == 0){
                height = 2*height;
            }
            else{
                height = height + 1;
            }
        }
        System.out.println(height);
    }

    
}
