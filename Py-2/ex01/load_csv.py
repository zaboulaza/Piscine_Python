import pandas as pd

def load(path: str) -> pd.DataFrame:
    
    try :
        res = pd.read_csv(path)
    except Exception as e :
        print(f"Error: {e}")
        return None
    
    return res

def main() -> int :
    
    load("life_expectancy_years.csv")
    
    return 1

if (__name__ == "__main__") :
    main()