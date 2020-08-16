from covid import Covid

covid = Covid()
covid.get_data()

india_cases = covid.get_status_by_country_name("india")
print(india_cases["active"])
