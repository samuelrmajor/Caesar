


import pandas as pd
df = pd.read_csv("C:/Users/Sam/..pj/caesar/data.csv")
df = df.fillna(0)
def get_report(age, vip, loc, freq):
    descrip = "Age: " + age + " VIP: " + vip + " Location: " + loc + " Frequency: " + freq
    cost = 0
    revenue = 0
    for index, row in df.iterrows():
        if row["age_group"] == age or age =="none":
            if row["VIP_group"] == vip or vip == "none":
                if row["Location"] == loc or loc == "none":
                    if row["Frequency"] == freq or freq == "none":
                        cost+= float(row["Cost_2020"])
                        revenue += float(row["Rev_2020"])

    if cost <= 12000 and cost >= 8000:
        print(descrip)
        print("cost: "+ str(cost))
        print("rev:  "+ str(revenue))
        print(revenue/cost)
        print("--------------------------")
        return revenue/cost, descrip
    else:
        return 1000000000, "None"





if __name__ == '__main__':
    ages = ["none","e. 21-29 yrs","d. 30-39 yrs", "c. 40-54 yrs","b. 55-74 yrs","a. 75+ yrs"]
    # vips = ["none", "b. NonVIP <400", "a. VIP 400+"]
    vips = ["b. NonVIP <400"]
    locations = ["none", "a. Local", "b. Regional", "c. National"]
    freqs = ["none", "Weekly", "Monthly", "Infrequent"]
    count = 0
    ratio = 1000000000000000
    descrip = ""

    for age in ages:
        for vip in vips:
            for location in locations:
                for freq in freqs:
                    results = get_report(age, vip, location, freq)
                    if results[0] < ratio:
                        ratio = results[0]
                        descrip = results[1]
    print(descrip)
    print(ratio)





