import matplotlib.pyplot as plt
from load_csv import load

def projection_life(path: str) :
    
    res = load(path)
    if(type(res) == None) :
        return 
    
    res2 = load("life_expectancy_years.csv")
    if(type(res2) == None) :
        return 

    x = res["1900"].values
    y = res2["1900"].values
    
    plt.scatter(x, y)
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.savefig("graph.png")
    
    return

def main() -> int :
    
    projection_life("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    
    return 1

if (__name__ == "__main__") :
    main()