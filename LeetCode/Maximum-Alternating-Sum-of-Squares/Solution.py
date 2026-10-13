  for(int i = 0; i < half; i++){
    leftsum += minpq.top();
    minpq.pop();
  }
  long long rightsum = totalsum - leftsum;
  long long maxsum = rightsum - leftsum;
  return maxsum;
}