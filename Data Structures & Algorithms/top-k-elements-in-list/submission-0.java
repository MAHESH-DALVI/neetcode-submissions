class Solution {
    public int[] topKFrequent(int[] nums, int k) {
      // step 1. count frequncey 
      HashMap<Integer, Integer> map = new HashMap();

      for(int num : nums) {
        map.put(num , map.getOrDefault(num,0)+1);
      }  
      // 2. Max Heap 
      PriorityQueue<Integer> pq = new PriorityQueue<>(
        (a,b) -> map.get(b)- map.get(a)
        );

        // step 3. Add all unique numbers into heap 
        pq.addAll(map.keySet());
        
        // steo 4. Extrect top k elements 
         int[] result = new int[k];

         for (int i=0; i<k; i++) {
            result[i] = pq.poll();
         }
          return result;
    }
}
