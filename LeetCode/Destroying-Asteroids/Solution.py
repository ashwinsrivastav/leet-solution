class Solution { 
    static final int MAX = 100001, sz = 1 << 5;
    public boolean asteroidsDestroyed(long mass, int[] A) {
        int[] mins = new int[sz];
        long[] sums = new long[sz];
        Arrays.fill(mins, MAX);

        for (int a : A) {
            int k = 31 - Integer.numberOfLeadingZeros(a);
            mins[k] = Math.min(mins[k], a);
            sums[k] += a;
        }

        for (int i = 0; i < sz; i++) {
            if (sums[i] == 0) continue;
            if (mass < mins[i]) return false;
            mass += sums[i];
        }

        return true;
    }
}