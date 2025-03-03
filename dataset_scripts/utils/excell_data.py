import pandas as pd

def read_excell_immobili(path='./assets/immobili-redux.xlsx'):
    df = pd.read_excel(path)
    return df