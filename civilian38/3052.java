import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean[] left = new boolean[42];

        for(int i = 0; i < 10; i++){
            int number = scanner.nextInt();
            left[number % 42] = true;
        }

        int sum = 0;
        for(int i = 0; i < 42; i++){
            if(left[i]){
                sum++;
            }
        }

        System.out.println(sum);
    }
}