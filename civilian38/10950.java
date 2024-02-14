import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int repeat = scanner.nextInt();
        for(int i = 0; i < repeat; i++){
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            System.out.println((a + b));
        }
    }
}