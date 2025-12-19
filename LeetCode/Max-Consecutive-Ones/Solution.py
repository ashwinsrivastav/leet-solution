    for(int i=0; i<nums.length; i++){
        if(nums[i] == 0){
            if(count > max) max = count;
            count = 0;
        }
        else count++;
    }

    return count>max ? count : max;
}