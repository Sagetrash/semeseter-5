import java.util.ArrayList;
import java.util.Scanner;

public class practical2 {

    public static void main(String[] args) {
        ArrayList<String> bookNames = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        bookNames.add("Book1");
        bookNames.add("Book2");1
        bookNames.add("Book3");
        bookNames.add("Book4");
        System.out.println("Current book list: " + bookNames);
        System.out.print("Enter the name of the book to remove: ");
        String bookToRemove = scanner.nextLine();
        if (bookNames.remove(bookToRemove)) {
            System.out.println(bookToRemove + " has been removed.");
        } else {
            System.out.println(bookToRemove + " was not found in the list.");
        }
        System.out.println("Updated book list: " + bookNames);
        scanner.close();
    }
}