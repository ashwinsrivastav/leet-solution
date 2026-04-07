    for(const string& c : words)
    { string temp;
        for(char ch : c)
        {
            temp=temp+MorseCode[ch-'a'];
        }
        sets.insert(temp);
    }
    return sets.size();
}