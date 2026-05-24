from load_csv import load
import matplotlib.pyplot as plt

def aff_lige() :
    
    res = load("life_expectancy_years.csv")
    if (type(res) is None) :
        return

    x = res.columns[1:]
    y = (res[res["country"] == "France"]).drop("country", axis=1).values.flatten()
    # print(res.columns)
    
    # x = [1, 2, 3, 4, 5, 6]
    # y = [10, 20, 30, 40, 50, 60]
    
    plt.plot(x, y) # trace une courbe
    
    plt.title("France LIfe expectancy Projections")
    plt.xlabel("Year") # legende axe x
    plt.xticks(x[::40])
    plt.ylabel("Life expectancy") # legnede axe y
    # plt.legend() # nom de la courbe si plusieur 
    plt.savefig("graph.png")
    
    return

def main() -> int :
    
    aff_lige()
    
    return 1

if (__name__ == "__main__") :
    main()