// *
// **
// ***
// ****

// import java.util.*;
// public class pattern {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("enter the number of rows:");
//         int steps = sc.nextInt();
//         for (int row = 1; row <= steps; row++){
//             for(int col = 1; col <= row; col++){
//                 System.out.print("* ");
//             }
//             System.out.println();
//         }
//     }
// }



//     *
//    **
//   ***
//  ****   
import java.util.*;
public class pattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter the number of rows:");
        int steps = sc.nextInt();
        for(int row = 1; row <= steps; row ++){
            for(int spc = steps - row; spc >= 0; spc--){
                System.out.print(" ");
            }
            for(int star = 1; star <= row; star++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}