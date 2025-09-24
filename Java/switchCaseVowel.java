import java.util.*;
public class switchCaseVowel {
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a character:");
        String ch = sc.next();
        if(ch.equals("a") | ch.equals("e") | ch.equals("i") | ch.equals("o") | ch.equals("u")){
            System.out.println("You entered a vowel:" + ch);
        }else {System.out.println("you did not enter a vowel");}
    }

}
