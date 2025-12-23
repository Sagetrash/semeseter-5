import java.util.*;

public class runnable_thread {
    public static void main(String[] args) {
        Runnable task = new Myclass1();
        Thread t1 = new Thread(task);
        Thread t2 = new Thread(task);
        
        t1.start();
        // System.out.println(t1.isAlive());
        t2.start();
        // System.out.println(t2.isAlive());

    }
}

class Myclass1 implements Runnable{
    @Override
    public void run(){
        for(int i=0 ; i<5;i++ ){
            System.out.println(i+". "+ Thread.currentThread().getName() + "is running");
            try{
                Thread.sleep(100);
            }catch (InterruptedException e){
                e.printStackTrace();
            }
        }
    }
}