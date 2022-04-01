import math



# from tabulate import tabulate
# head = ["Ranks", "Winning_Amount", "Total_Winners", "Total_Winning Amount"]
# mydata = [[1, 2, 3, 4], [5, 6, 7, 8]]
# print(tabulate(mydata, headers=head, tablefmt="grid"))


def sumCalc(a):
    tsum = 0.0;
    # print(e_fee, total_winners, max_prize)
    for i in range(1, total_winners):
        tsum += e_fee + (max_prize - e_fee) / i ** a
    return tsum


decVal = 1 / 10 ** 10
totSum = 0


def alphSearch(low, high):
    if high >= low:

        mid = (high + low) / 2
        totSum = sumCalc(mid)
        print(totSum, mid)

        if math.isclose(prize_total, totSum, abs_tol=0.001):
            return mid, totSum


        elif totSum < prize_total:
            return alphSearch(low, mid - decVal, )


        else:
            return alphSearch(mid + decVal, high)

    else:
        return -1


totalplayers = int(input("No. of players: "))
e_fee = int(input("Entry Fee: "))
max_prize = int(input("Max Winning Price: "))
prize_total = e_fee * totalplayers
win_percent = float(input("Win % :  "))
# 55.42857
total_winners = math.ceil(win_percent / 100 * float(totalplayers))
# prize_topwinners = 0.06 * float(prize_total);
print("Total_prize: ", prize_total, " Total_Winners: ", total_winners)

# print(sumCalc(0.7))
alpha, totSum = alphSearch(0, 2)

print("Alpha: ", alpha, " Sum: ", totSum)
rank={}
t_prize=0
for i in range(1, total_winners):
    print(i, ": ", round(e_fee + (max_prize - e_fee) / i ** alpha))
    t_prize=t_prize+(e_fee + (max_prize - e_fee) / i ** alpha)
    key=i
    value=e_fee + (max_prize - e_fee) / i ** alpha
    rank[key]=round(value)
print(rank)
print(round(t_prize))
s=[25,100,300,500,1000,2000,5000,10000,50000,194000]
z=6
entries=int(input("enter the total entires"))
a=0
winners=round(entries*.5542857)
b2=winners-5
def maprange(a,b,s):
    (a1, a2), (b1,b2)=a,b
    t=round(b1+((s-a1)*(b2-b1)/(a2-a1)))

    return t
for i in range(6, winners):
     if(a<10):
        t=maprange((6,193995),(6 ,b2),s[a])
        if t>=z:
            # for j in m_per:
            print(z,"maps to",t,"totalWinners=",t-z+1,t-z+1*round(e_fee + (max_prize - e_fee) / i ** alpha))
        a+=1
        z=t+1

# for s in range(11):
#    print("%2g maps to %g" % (s, maprange((0, 10), (-1, 0), s)))


#
# s=[25,100,300,500,1000,2000,5000,10000,50000,194000]
# m_per=[2.857142857, 4.285714286,5.714285714,2.857142857,2.857142857,2.857142857,4.285714286,4.285714286,22.85714286,41.14285714]
# a=0
# z=6
# entries=int(input("enter the total entires"))
# t_prize=entries
# print(t_prize)
# p1=round(entries*2.857142857)/100
# p2=round(entries*1.428571429)/100
# p3=round(entries*0.857142857)/100
# p4=round(entries*0.571428571)/100
# p5=round(entries*0.285714286)/100
# # print(p1)
# # print(p2)
# # print(p3)
# # print(p4)
# # print(p5)
# d=p1+p2+p3+p4+p5
# d_prize=t_prize-d
# print(d_prize)
# winning_prize=0
# winners=round(entries*.5542857)
#
# b2=winners-5
# def maprange(a,b,s):
#     (a1, a2), (b1,b2)=a,b
#     t=round(b1+((s-a1)*(b2-b1)/(a2-a1)))
#
#     return t
# for i in range(6, winners):
#      if(a<10):
#         t=maprange((6,193995),(6 ,b2),s[a])
#         if t>=z:
#             # for j in m_per:
#             print(z,"maps to",t,"totalWinners=",t-z+1)
#         a+=1
#         z=t+1
