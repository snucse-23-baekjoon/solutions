import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean ascending = true;
        boolean descending = true;

        for(int i = 1; i <= 8; i++){
            int number = scanner.nextInt();
            if(number != i){
                ascending = false;
            }
            if (number != 9 - i){
                descending = false;
            }
        }

        if(ascending){
            System.out.println("ascending");
        } else if (descending){
            System.out.println("descending");
        } else {
            System.out.println("mixed");
        }
    }
}