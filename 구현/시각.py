n = int(input())
cnt = 0 
for h in range(n+1) :
    if '3' in str(h) :
        cnt+=60*60
        continue
    else : 
        for m in range(60) :
            if '3' in str(m) :
                cnt+=60
                continue
            else :
                for s in range(60) : 
                    if '3' in str(s) :
                        cnt+=1
print(cnt)