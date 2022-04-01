import math
import numpy
import statistics

prizes = {}
t_sum = 0


# from tabulate import tabulate
# head = ["Ranks", "Winning_Amount", "Total_Winners", "Total_Winning Amount"]
# mydata = [[1, 2, 3, 4], [5, 6, 7, 8]]
# print(tabulate(mydata, headers=head, tablefmt="grid"))


def sumCalc(a):
    tsum = 0.0;
    # print(e_fee, total_winners, max_prize)
    for i in range(1, total_winners + 1):
        tsum += e_fee + (max_prize - e_fee) / i ** a
    return tsum


decVal = 1 / 10 ** 10
totSum = 0


def alphSearch(low, high):
    if high >= low:

        mid = (high + low) / 2
        totSum = sumCalc(mid)
        #print(totSum, mid)

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

s = [25, 100, 300, 500, 1000, 2000, 5000, 10000, 50000, 194000]
a = 0
z = 6
total_winners = math.ceil(win_percent / 100 * float(totalplayers))
winnings = round(totalplayers * .5542857)
b2 = winnings - 5
# prize_topwinners = 0.06 * float(prize_total);
#print("Total_prize: ", prize_total, " Total_Winners: ", total_winners)

# print(sumCalc(0.7))
alpha, totSum = alphSearch(0, 2)
# print("Alpha: ", alpha, " Sum: ", totSum)

for i in range(1, total_winners + 1):
    pr = round(e_fee + (max_prize - e_fee) / i ** alpha)
    prizes[i] = pr




def maprange(a, b, s):
    (a1, a2), (b1, b2) = a, b
    t = round(b1 + ((s - a1) * (b2 - b1) / (a2 - a1)))
    return t

one = prizes[1]
print("1 maps to 1 ","Prize:",one,"Range 1")
two = prizes[2]
print("2 maps to 2 ","Prize:",two,"Range 1")
three = prizes[3]
print("3 maps to 3 ","Prize:",three,"Range 1")
four = prizes[4]
print("4 maps to 4 ","Prize:",four,"Range 1")
five = prizes[5]
print("5 maps to 5 ","Prize:",five,"Range 1")


for i in range(6, winnings):
    if a < 10:
        t = maprange((6, 193995), (6, b2), s[a])
        if t >= z:
            x = math.floor(statistics.mean([prizes[z], prizes[t]]))
            print(z, " maps to ", t,"Prize:",x,"Range:", t - z + 1)
            tot_v = x*((t-z)+1)
            t_sum = t_sum + tot_v
        a += 1
        z = t + 1
#print(t_sum)


print("Sum :",t_sum+one+two+three+four+five)
# x=statistics.mean([prizes[z],prizes[26]])
# print(x)
