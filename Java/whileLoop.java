import java.util.*;
public class whileLoop {
    public static void main(String args []){
        Scanner sc = new Scanner(System.in);
        int i = 1;
        System.out.print("Enter the number you want table of:");
        int num = sc.nextInt();
        while(i<=10){
            System.out.println(num + "X" + i + "="+ i*num);
            i++;
        }
    }
}
