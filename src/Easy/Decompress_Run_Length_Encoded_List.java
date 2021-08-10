package Easy;

public class Decompress_Run_Length_Encoded_List {
    public int[] decompressRLElist(int[] nums) {
        int size = 0;
        for(int i = 0; i < nums.length; i+=2){
            size += nums[i];
        }
        /* Want to find how big the array will have to be */


        int[] result = new int[size];
        int curr = 0; // Tracks placement of the next element
        for(int i = 0; i < nums.length; i+=2) {
            int freq = nums[i];
            int val = nums[i+1];

            /* Add each pair of elements sublists into the decompressed list */
            for (int j = 0; j < freq; j++){
                result[curr] = val;
                curr++;
            }
        }

        return result;
    }
}
