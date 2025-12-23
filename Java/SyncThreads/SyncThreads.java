class Counter{
    int count = 0;
    synchronized void increament(){
        count++;
        System.out.println(Thread.currentThread().getName()+ " -> "+ count);
    } 
}

class MyThread extends Thread{
    Counter c;
    public void run(){
        for(int i = 0; i < 10; i++){
            System.out.println(Thread.currentThread().getName() + " -> " + Thread.currentThread().getState());
            c.increament();
        }
    }
    MyThread(Counter c){
        this.c = c;
    }
}

public class SyncThreads {
    public static void main(String [] args){
        Counter c = new Counter();
        MyThread t1 = new MyThread(c);
        MyThread t2 = new MyThread(c);
        t1.start(); t2.start();
    }
}