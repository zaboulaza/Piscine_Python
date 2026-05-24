import pandas as pd

def load(path: str) -> pd.DataFrame:
    """fonction qui return le csv en forme tableau"""
    
    try :
        res = pd.read_csv(path)
    except Exception as e :
        print(f"Error: {e}")
        return None
    
    print(f"Loading dataset of dimensions {res.shape}")
    
    return res

