public class object_method {
    public static void main(String[] args) {
        Student st = new Student();
        st.setvalue(1435, "ayush", 30000);
        System.out.println(st.id);
        System.out.println(st.name);
        System.out.println(st.fee);
    }
}

class Student {
    int id;
    String name;
    float fee;
    public void setvalue(int id, String name, float fee){
        this.id = id;
        this.name = name;
        this.fee = fee;
    }
}