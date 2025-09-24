
public class ref_variable {
    public static void main(String[] args) {
        employee emp = new employee();
        System.out.println("before intialisation");
        System.out.println(emp.id);
        System.out.println(emp.name);
        System.out.println(emp.Salary);
        System.out.println(employee.cname);

        emp.id = 1435;
        emp.name = "Ayush";
        emp.Salary = 30000;
        System.out.println("After intialisation");
        System.out.println(emp.id);
        System.out.println(emp.name);
        System.out.println(emp.Salary);

    }
    
}

class employee {
    int id;
    String name;
    float Salary;
    static String cname = "India";
}