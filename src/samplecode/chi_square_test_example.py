import numpy as np


parks = ['Zion','Grand Canyon','Yellow Stone', 'Yosemite','Rocky Mountain']
tent_overnight = [115902,154876,89504,498389,101125]
back_country_overnight = [35947,291984,41694,165206,37470]


sum_by_park = [x+y for x,y in zip(tent_overnight,back_country_overnight)]
sum_tent = sum(tent_overnight)
sum_back_country = sum(back_country_overnight)

total_sum = sum(sum_by_park)

print(sum_tent)
print(sum_back_country)
print(total_sum)
print("parks")
print(parks)
print("tent_overnight")
print(tent_overnight)
print("back_country_overnight")
print(back_country_overnight)
print("sum_by_park")
print(sum_by_park)

i_exp =[]
tent_ex = []
back_ex = []

for i in range(0,len(parks)):
    exp_value = (sum_by_park[i]) * (sum_tent/total_sum)
    j = ((tent_overnight[i]-exp_value)**2)/exp_value
    tent_ex.append(j)

for i in range(0,len(parks)):
    exp_value = (sum_by_park[i]) * (sum_back_country/total_sum)
    j = ((back_country_overnight[i]-exp_value)**2)/exp_value
    back_ex.append(j)

degree_of_freedom = (2-1)*(len(parks)-1)

print("Tent")
print(tent_ex)
print("Back")
print(back_ex)
print("degrees of freedom {}".format(degree_of_freedom))

chi_square_statistic_tent = sum(tent_ex)
chi_square_statistic_backcountry = sum(back_ex)

print("Chi Square Statistic Tent")
print(chi_square_statistic_tent)

print("Chi Square Statistic Backcountry")
print(chi_square_statistic_backcountry)

