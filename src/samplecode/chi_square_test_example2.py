import numpy as np
import pandas as pd
import scipy.stats as stats


tent = pd.DataFrame(["zion"]*115902 + ["grandcanyon"]*154876 +\
                        ["yellowstone"]*89504 + ["yosemite"]*498389 + ["rockymountain"]*101125)
           

back_country = pd.DataFrame(["zion"]*35947 + ["grandcanyon"]*291984 + \
                         ["yellowstone"]*41694 +["yosemite"]*165206 + ["rockymountain"]*37470)

tent_table = pd.crosstab(index=tent[0], columns="count")
back_country_table = pd.crosstab(index=back_country[0], columns="count")

observed = back_country_table

tent_ratios = tent_table/len(tent)  # Get population ratios
print("Tent Ratios")
print(tent_ratios)

expected = tent_ratios * len(back_country)   # Get expected counts
print("Expected ")
print(expected)

chi_squared_stat = (((observed-expected)**2)/expected).sum()
print("chi_squared_stat ")
print(chi_squared_stat)


crit = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 4)   # Df = number of variable categories - 1

print("Critical value")
print(crit)

p_value = 1 - stats.chi2.cdf(x=chi_squared_stat,  # Find the p-value
                             df=4)
print("P value")
print(p_value)


power_divergence = stats.chisquare(f_obs= observed,   # Array of observed counts
                f_exp= expected)   # Array of expected counts

print("Power Divergence")
print(power_divergence)
