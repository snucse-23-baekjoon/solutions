import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        for(int i = 0; i < number; i++){
            int h = scanner.nextInt();
            int w = scanner.nextInt();
            int n = scanner.nextInt();
            if(h < n){
                if (n % h == 0){
                    System.out.println((100 * h + (n / h)));
                } else {
                    System.out.println((100 * (n % h) + (1 + n / h)));
                }
            } else if (h == n){
                System.out.println((100 * h + 1));
            } else {
                System.out.println((100 * n + 1));
            }
        }
    }
}