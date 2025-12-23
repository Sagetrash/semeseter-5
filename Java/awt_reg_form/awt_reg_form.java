import java.awt.*;

class awt_reg_form {
    public static void main(String[] args) {
        Frame f = new Frame();
        f.setTitle("My first Frame");

        Label titleLabel = new Label("registration Form");
        titleLabel.setBounds(200,30,100,30);
        f.add(titleLabel);

        // NAME
        Label nameLabel = new Label("NAME:");
        nameLabel.setBounds(150,70,100,30);
        f.add(nameLabel);
        TextField nameTextField = new TextField();
        nameTextField.setBounds(250,70,100,30);
        f.add(nameTextField);
        
        //FatherName
        int y = 105;
        Label fatherNameLabel = new Label("FATHER NAME:");
        fatherNameLabel.setBounds(150,y,100,30);
        f.add(fatherNameLabel);
        TextField fatherNameTextField = new TextField();
        fatherNameTextField.setBounds(250,y,100,30);
        f.add(fatherNameTextField);
        f.add(fatherNameLabel);
        y = y + 35;
        
        // AGE
        Label ageLabel = new Label("Age:");
        ageLabel.setBounds(150,y,100,30);
        f.add(ageLabel);
        TextField ageTextField = new TextField();
        ageTextField.setBounds(250,y,100,30);
        f.add(ageTextField);
        f.add(ageLabel);


        //CHECKBOX
        y=y+35;
        Label hobbiesLabel = new Label("hobbies:");
        hobbiesLabel.setBounds(150,y,50,30);
        f.add(hobbiesLabel);

        Checkbox cricketCheckbox = new Checkbox();
        cricketCheckbox.setBounds(250,y,20,20);
        f.add(cricketCheckbox);
        Label cricketLabel = new Label("cricket");
        cricketLabel.setBounds(270,y,70,20);
        f.add(cricketLabel);

        f.setSize(500,500);
        f.setLayout(null);
        f.setVisible(true);
    }
}