package Easy;

import java.util.Arrays;
import java.util.HashMap;

public class Two_Sum {

    public static void main(String[] args) {
        Two_Sum s = new Two_Sum();
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] sums = s.twoSum(nums, target);
        System.out.println(Arrays.toString(sums));

    }

    public int[] twoSum(int[] nums , int target) {
        HashMap<Integer, Integer> missingValue = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length; i++){
            if (missingValue.get(nums[i]) != null ){ // Then we have the value
                return new int[]{missingValue.get(nums[i]), i};
            } else {
                missingValue.put(target-nums[i], i);
            }
        }
        return new int[]{-1, -1};
    }
}
