import matplotlib.pyplot as plt
# import string as str
from load_csv import load

def aff_pop() :
    
    res = load("population_total.csv")
    if (type(res) is None) :
        return
    # print(res)
    
    x = res.columns[1:]
    mask = x <= "2050"
    y = (res[res["country"] == "France"]).drop("country", axis=1)
    y = y.replace({'M': ''}, regex=True).astype(float) * 1_000_000
    y = y.values.flatten()
    xx = res.columns[1:]
    mask2 = xx <= "2050"

    yy = (res[res["country"] == "Belgium"]).drop("country", axis=1)
    yy = yy.replace({'M': ''}, regex=True).astype(float) * 1_000_000
    yy = yy.values.flatten()
    
    plt.plot(xx[mask2], yy[mask2], label="Belgium", color="blue")
    plt.plot(x[mask], y[mask], label="France", color="green")
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.xticks(x[mask][::40])
    plt.ylabel("Population")
    plt.yticks([20_000_000, 40_000_000, 60_000_000], ["20M", "40M", "60M"])
    plt.legend(loc="lower right")
    plt.savefig("graph.png")
    
    return


def main() -> int :
    
    aff_pop()
    return 1

if (__name__ == "__main__") :
    main()