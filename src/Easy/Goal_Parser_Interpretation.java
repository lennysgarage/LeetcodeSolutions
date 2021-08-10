package Easy;

public class Goal_Parser_Interpretation {
    public String interpret(String command) {
        StringBuilder newCommand = new StringBuilder();
        int i = 0;
        while (i < command.length()) {
            if (command.charAt(i) == 'G') {
                newCommand.append("G");
                i++;
            }
            else if (command.charAt(i+1) == 'a'){
                newCommand.append("al");
                i+= 4;
            } else {
                newCommand.append("o");
                i+= 2;
            }
        }
        return newCommand.toString();
    }
}
