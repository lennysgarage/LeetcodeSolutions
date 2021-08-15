package Medium;

public class Integer_to_Roman {
    public static void main(String[] args) {
        System.out.println(new Integer_to_Roman().intToRoman(3456));
    }
    public String intToRoman(int num) {
        String[] numerals = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int[] numeralsValues = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

        StringBuilder numeralString = new StringBuilder();
        for(int i = 0; i < numerals.length; i++){
            while(num >= numeralsValues[i]) {
                num -= numeralsValues[i];
                numeralString.append(numerals[i]);
            }
        }
        return numeralString.toString();
    }
}
