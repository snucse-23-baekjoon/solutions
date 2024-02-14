import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        int max = scanner.nextInt();
        int min = max;

        for(int i = 1; i < number; i++){
            int temp = scanner.nextInt();
            if(temp < min){
                min = temp;
            }
            if(temp > max){
                max = temp;
            }
        }

        System.out.print(min + " " + max);
    }
}