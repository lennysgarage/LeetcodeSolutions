package Easy;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Count_Items_Matching_a_Rule {
    public static void main(String[] args) {
        List<List<String>> items = new ArrayList<>();
        items.add(Arrays.asList("phone","blue","pixel"));
        items.add(Arrays.asList("computer","silver","lenovo"));
        items.add(Arrays.asList("phone","gold","iphone"));
        System.out.println(Arrays.toString(Arrays.stream(items.toArray()).toArray()));
        Count_Items_Matching_a_Rule a = new Count_Items_Matching_a_Rule();
        System.out.println(a.countMatches(items, "color", "silver"));
    }

    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int numItems = 0;
        for(int i = 0; i < items.toArray().length; i++){
            switch(ruleKey) {
                case "type":
                    if (items.get(i).get(0).equals(ruleValue)) {
                        numItems++;
                    }
                    break;
                case "color":
                    if (items.get(i).get(1).equals(ruleValue)) {
                        numItems++;
                    }
                    break;
                case "name":
                    if (items.get(i).get(2).equals(ruleValue)) {
                        numItems++;
                    }
                    break;
            }
        }
        return numItems;
    }
}
