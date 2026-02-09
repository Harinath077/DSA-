class Solution {
    void merge(int[] arr, int low, int mid, int high){
        int left = low;
        int right = mid + 1;
        ArrayList<Integer> temp = new ArrayList<>();
        // merging two sorted arrays
        while( left <= mid && right <= high){
            if(arr[left] <= arr[right]){
                temp.add(arr[left]);
                left ++;
            }
            else{
                temp.add(arr[right]);
                right ++;
            }
        }
        // left part
        while( left <= mid){
            temp.add(arr[left]);
            left ++;
        }
        // right part
        while( right <= high){
            temp.add(arr[right]);
            right ++;
        }
        // copy the elements from temp to original array
        for(int i = 0 ; i < temp.size(); i++){
            arr[low + i] = temp.get(i);
        }
    }
    void mergeSort(int[] arr, int low, int high){
        if( low >= high){
            return;
        }
        int mid = low + (high - low ) / 2;
        mergeSort(arr, low, mid);
        mergeSort(arr, mid + 1, high);
        merge(arr, low, mid, high);
    }

    // Public helper method
    
    public int[] sortArray(int[] arr) {
        mergeSort(arr, 0, arr.length - 1);
        return arr;
    }
}