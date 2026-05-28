import pandas as pd

def load(path: str) : 
    
    try :
        res = pd.read_csv(path)
    except Exception as e :
        print(f"Error: {e}")
        return None
    
    return res