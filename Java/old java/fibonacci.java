import java.util.*;
public class fibonacci {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter the number:");
        int steps = sc.nextInt();
        int num1, num2, num3;
        int i = 0;
        num1 = 0; num2 = 1;
        if (steps <= 0){
            System.out.println("Invalid input");
        }else if(steps == 1){
            System.out.println("0");
        }else if(steps == 2 ){
            System.out.println("0 + 1");
        }else {
            while(i < steps - 2)
            {

                num3 = num1 + num2;
                num1 = num2;
                num2 = num3;
                if(i == 0){
                System.out.print("0 + 1 + " + num3);
                }else
                {
                System.out.print(" + " + num3);
                }
                i++;
            }
        }
    }
    
}