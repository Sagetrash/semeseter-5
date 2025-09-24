//[20,30,36,97,98],[41,42,43,45,46]
public class array {
    public static void main(String[] args) {
        int a[] = new int[]{20,30,36,97,98};
        int b[] = new int[]{41,42,43,45,46};
        int c[] = new int[a.length];
        for(int i = 0;i < a.length;i++){
            c[i] = a[i] + b[i];
        }
        for(int x:c){
            System.out.println(x);
        }
    }
}