package Medium;


public class Partitioning_Into_Minimum_Number_Of_Deci_Binary_Numbers {
    public static void main(String[] args) {
        System.out.println(Partitioning_Into_Minimum_Number_Of_Deci_Binary_Numbers.minPartitions("32"));
    }

    public static int minPartitions(String n) {
        int max = 0;
        for (int i =0 ; i < n.length(); i++){
            int digit = Character.getNumericValue(n.charAt(i));
            if ( digit > max ) {
                max = digit;
            }
        }
        return max;

    }
}
