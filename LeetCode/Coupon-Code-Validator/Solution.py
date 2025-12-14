1class Solution:
2    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
3        a=set(list(["electronics", "grocery", "pharmacy", "restaurant"])); l=[]; el,gr,ph,re=[],[],[],[]
4        for i in range(len(code)):
5            if code[i].replace("_","0").isalnum():
6                if businessLine[i] in a:
7                    if isActive[i]:
8                        if businessLine[i]=="electronics":
9                            el.append(code[i])
10                        elif businessLine[i]=="grocery":
11                            gr.append(code[i])
12                        elif businessLine[i]=="pharmacy":
13                            ph.append(code[i])
14                        else:
15                            re.append(code[i])
16        l.extend(sorted(el));l.extend(sorted(gr));l.extend(sorted(ph));l.extend(sorted(re))
17        return l
18
19