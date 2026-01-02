        ///insert case
        int ans1=1+helper(s1,s2,i+1,j);
        //delete
        int ans2=1+helper(s1,s2,i,j+1);
        ans=Math.min(ans1,ans2);
    }
    return dp[i][j]=ans;
}
public int minDistance(String str1, String str2) {
    dp=new int[str1.length()+1][str2.length()+1];
    for(int []arr:dp){
        Arrays.fill(arr,-1);
    }
    return helper(str1,str2,0,0);
    
}