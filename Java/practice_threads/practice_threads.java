public class practice_threads {
    public static void main(String[] args) {
        // Runnable test = new MyClass();
        MyClass t = new MyClass();
        MyClass t2 = new MyClass();
        t.start();
        t2.start();
        }
}

class MyClass extends Thread{
    public void run(){
        System.out.println(
            Thread.currentThread().getClass()
        );
    }
}