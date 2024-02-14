import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int number = Integer.parseInt(scanner.nextLine());
        for(int i = 0; i < number; i++){
            String quiz = scanner.nextLine();
            int score = 0, temp = 0;
            for(int j = 0; j < quiz.length(); j++){
                if(quiz.charAt(j) == 'O'){
                    temp++;
                }else{
                    temp = 0;
                }
                score += temp;
            }
            System.out.println(score);
        }

    }
}