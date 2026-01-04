public int solve(int x){
    int sum=0;
    int count=0;
    for(int i=1; i*i<=x; i++){
            if(x%i==0){
                if(i*i==x)return 0;
                sum+=i;
                sum+=x/i;
                count+=2;
        }
    }
                
    return count==4 ? sum : 0;
    
}