def tongchuso(n):
    if(n==0):
        return 0 # diemdung
    else:
        return n%10+tongchuso(n//10)
n=int(input("nhap n "))
print("tong chu so", tongchuso(n))
df=pd.read_csv("Life expectancy.csv")
fig=px.line(df,x="Year",y="life expectancy")
fig.show()
