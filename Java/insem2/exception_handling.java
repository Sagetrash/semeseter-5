public class exception_handling {
    public static void main(String[] args) {
        System.out.println("null pointer exception");
        String str = null;

        try{

        System.out.println(str.toUpperCase());
        
    } catch(NullPointerException n){

            System.err.println("null cant be uppercased");
        
        }
    }
    
} 