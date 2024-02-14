import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int repeat = Integer.parseInt(scanner.nextLine());
        int answer = 0;
        String number = scanner.nextLine();
        for(int i = 0; i < repeat; i++){
            answer += (int)(number.charAt(i)) - (int)'0';
        }
        System.out.print(answer);
    }
}