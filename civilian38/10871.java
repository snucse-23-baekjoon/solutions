import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int x = scanner.nextInt();
        for(int i = 0; i < n; i++){
            int temp = scanner.nextInt();
            if(temp < x){
                System.out.print(temp + " ");
            }
        }
    }
}