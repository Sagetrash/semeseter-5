import java.util.*;
public class reverse {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the number:");
        int num = sc.nextInt();
        int temp_num = num;
        int sum = 0;
        while(temp_num !=0){
            int remain = temp_num%10;
            sum = sum*10+remain;
            temp_num = temp_num/10;
        }
        System.out.println(sum);
    }
    
} 