population = 380123456
sec_year = 60 * 60 * 24 * 365
b_rate = sec_year / 6
d_rate = sec_year / 12
m_rate = sec_year / 40

year_1 = population + b_rate + m_rate - d_rate
year_2 = year_1 + b_rate + m_rate - d_rate
year_3 = year_2 + b_rate + m_rate - d_rate

print(year_3)
