import java.util.Scanner;

public class basicCaluculator{
  public static void main(String[] args) {
    int answer;
    int firstNum;
    int secondNum;

    
    Scanner input = new Scanner(System.in);
    System.out.print("Enter your number here: ");
    firstNum = input.nextInt();
    
    System.out.print("Enter your second number here: ");
    secondNum = input.nextInt();

    answer = secondNum + firstNum;

    System.out.println(answer);
    
  } 
}
