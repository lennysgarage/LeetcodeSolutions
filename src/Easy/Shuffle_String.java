package Easy;

public class Shuffle_String {
    public String restoreString(String s, int[] indices) {
        char[] letters = new char[indices.length];

        for (int i = 0; i < indices.length; i++){
            letters[indices[i]] = s.charAt(i);
        }
        return String.valueOf(letters);
    }
}
