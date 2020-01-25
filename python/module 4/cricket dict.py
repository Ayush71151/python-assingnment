import pandas as pd
squad={'batsman':{'rohit':{'matches':'206','run':'264','avg':'47','highesyt_score':'264'},'virat':{'matches':'200','run':'214','avg':'37','highesyt_score':'164'},'pandaya':{'matches':'200','run':'214','avg':'37','highesyt_score':'164'},'dhoni':{'matches':'100','run':'200','avg':'47','highesyt_score':'150'}}}

df=pd.DataFrame(squad['batsman'])
print(df)
squad['batsman']['rohit']["highesyt_score"]='440'
s=[]
for i in squad.keys():
    for j in squad[i].keys():
     s.append(squad[i][j]["highesyt_score"])   
print('highest score is : ' ,max(s))        