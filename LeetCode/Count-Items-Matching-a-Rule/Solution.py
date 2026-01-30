public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
    int count=0;


for(List list:items){
    if(list.contains(ruleValue)){
        count++;
        
    }
}return count;

    
}