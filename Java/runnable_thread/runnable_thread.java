import java.util.*;

public class runnable_thread{
    public static void main( String [] args){
        // System.out.println("hello world from "+ Thread.currentThread().getName());
        MyClass t1 = new MyClass();
        t1.start();
    }
}

class MyClass extends Thread{
    public void run(){
        System.out.println("hello from "+Thread.currentThread().getName());
    }
}