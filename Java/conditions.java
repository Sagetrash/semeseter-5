import java.util.Scanner;
public class conditions {
    public static void main(String [] P) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter your Nationality:");
        String cname = sc.next();
        if (cname.equals("Indian") | cname.equals("indian")){
            System.out.println("enter your age: ");
            int age = sc.nextInt();
            if(age>=18){
                System.out.println("You can vote");
            }else {
                System.out.println("invalid age");
            }

        }else{
            System.out.println("You are not Indian");
        }
    }
}