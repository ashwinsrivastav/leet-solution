class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        def doessomething(minn, sum, lenn, arr):
            dic = {}
            j = 0
            for i in arr:
                dic[j] = abs(i[0] - i[1])
                j += 1
            dic = dict(sorted(dic.items(), key=lambda item: item[1]))
            print(dic)
            val = list(dic.values())
            i = 0
            while minn < lenn // 2:
                sum += val[i]
                i += 1
                minn += 1
            return sum

        sum = 0
        a = []
        b = []
        for i in costs:
            if i[0] > i[1]:
                sum += i[1]
                b.append(i)
                continue
            sum += i[0]
            a.append(i)
        minn = min(len(a), len(b))
        if len(a) == len(b):
            return sum
        elif len(a) < len(b):
            return doessomething(minn, sum, len(costs), b)
        return doessomething(minn, sum, len(costs), a)
