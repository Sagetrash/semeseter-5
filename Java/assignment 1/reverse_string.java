import java.util.*;
public class reverse_string {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the String to reverse: ");
        String og_string = sc.nextLine();
        char[] charArray = og_string.toCharArray();
        String reversed = "";
        for(int i = charArray.length - 1; i >= 0; i--){
            reversed += charArray[i];
        }
        System.out.println("The reversed string is: "+reversed);

        sc.close();
    }
}