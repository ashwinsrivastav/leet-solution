// Iterate through the string and generate all substrings of length 3
for (int i = 0; i < s.size() - 2; ++i) {
    string sub = s.substr(i, 3); // Extract the substring
    set<char> uniqueChars(sub.begin(), sub.end()); // Convert substring to set to check for uniqueness
    // If a substring has exactly 3 unique characters, it's a good substring
    if (uniqueChars.size() == 3) {
        count++;
    }
}

return count; //why this is giving error