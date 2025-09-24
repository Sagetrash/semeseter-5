import java.util.*;
public class factorial {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number to caluculate factorial:");
        long fact = sc.nextInt();
        long result = 1;
        long i = fact;
        while(i >= 1){
            result = result*i;
            i--;
        }
        System.out.println("The factorial of " + fact + " is " + result);
    }
}