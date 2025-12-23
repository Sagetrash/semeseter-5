class ComplexNumber {
    double real;
    double imaginary;
    public ComplexNumber(double real, double imaginary) {
        this.real = real;
        this.imaginary = imaginary;
    }

    public ComplexNumber add(ComplexNumber other) {
        double newReal = this.real + other.real;
        double newImaginary = this.imaginary + other.imaginary;
        return new ComplexNumber(newReal, newImaginary);
    }
    public void display() {
        System.out.println(this.real + " + " + this.imaginary + "i");
    }
}

public class practical {
    public static void main(String[] args) {
        ComplexNumber c1 = new ComplexNumber(2.5, 3.0);
        ComplexNumber c2 = new ComplexNumber(1.2, 4.5);

        System.out.print("Complex Number 1: ");
        c1.display();

        System.out.print("Complex Number 2: ");
        c2.display();

        ComplexNumber sum = c1.add(c2);

        System.out.print("Sum of Complex Numbers: ");
        sum.display();
    }
}