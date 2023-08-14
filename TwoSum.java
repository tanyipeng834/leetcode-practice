import java.util.HashMap;

class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numsDict = new HashMap<>();
        // Allocate for 2 intefers in the array
        int[] result = new int[2];
        for (int i = 0; i < nums.length; i++) {
            int r = target - nums[i];
            if (numsDict.containsKey(r)) {
                result[0] = i;
                result[1] = numsDict.get(r);
                return result;

            }
            numsDict.put(nums[i], i);

        }

        return result;
    }

    public static void main(String[] args) {
        TwoSum solution = new TwoSum();
        int[] results = { 2, 2 };
        solution.twoSum(results, 6);
    }
}