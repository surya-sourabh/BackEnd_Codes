import math



# from tabulate import tabulate
# head = ["Ranks", "Winning_Amount", "Total_Winners", "Total_Winning Amount"]
# mydata = [[1, 2, 3, 4], [5, 6, 7, 8]]
# print(tabulate(mydata, headers=head, tablefmt="grid"))
import statistics


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

s = [25, 100, 300, 500, 1000, 2000, 5000, 10000, 50000, 194000]
a = 0
z = 6
total_winners = math.ceil(win_percent / 100 * float(totalplayers))
winnings = round(totalplayers * .5542857)
b2 = winnings - 5
# prize_topwinners = 0.06 * float(prize_total);
print("Total_prize: ", prize_total, " Total_Winners: ", total_winners)

# print(sumCalc(0.7))
alpha, totSum = alphSearch(0, 2)

print("Alpha: ", alpha, " Sum: ", round(totSum))


def maprange(a, b, s):
    (a1, a2), (b1, b2) = a, b
    t = round(b1 + ((s - a1) * (b2 - b1) / (a2 - a1)))
    return t


t_prize=0
for i in range(1, total_winners  ):
    print(i, ": ",round(e_fee + (max_prize - e_fee) / i ** alpha))
    t_prize = t_prize + (e_fee + (max_prize - e_fee) / i ** alpha)
    print(round(t_prize))
#mean = statistics.mean(e_fee + (max_prize - e_fee)/ i ** alpha)
#print(mean)
for i in range(6, winnings):
        if a < 10:
          t = maprange((6, 193995), (6, b2), s[a])
          if t >= z:
              print(i)
              print(z, " maps to ", t, "winners=" , t - z + 1 ,"prize",i)
              sum = (t-z+1)*round(e_fee + (max_prize - e_fee) / i ** alpha)
              print('prize for players for the above rank',sum)

          a += 1
          z = t + 1
#mean = statistics.mean(sum)
#print(mean)
#def maprange(a, b, s):
#    (a1, a2), (b1, b2) = a, b
 #   return b1 + ((s - a1) * (b2 - b1) / (a2 - a1))

# for s in range(11):
#    print("%2g maps to %g" % (s, maprange((0, 10), (-1, 0), s))

#55.42857
