DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
]

# 字典推导
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)

# 带有映射和判断的字典推导
country_code = {
    code: country.upper()
    for country, code in country_code.items() if code > 50
}
print(country_code)

# 集合推导
s = {country for _, country in DIAL_CODES}
print(s)