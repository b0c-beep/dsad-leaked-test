import numpy as np
import pandas as pd

def main():
    #1 --------------------------------------------------------------------------------------------------
    matrix = np.loadtxt("matrice_32.txt")
    print(matrix)

    #2 --------------------------------------------------------------------------------------------------
    vector = np.random.uniform(-3, 3, 50)
    print(vector)

    serie = pd.Series(vector, index=[f"R_{i+1}" for i in range(len(vector))])
    print(serie)

    #3 --------------------------------------------------------------------------------------------------
    bid = np.random.uniform(-5, 5, (11, 6))
    print(bid)

    df = pd.DataFrame(bid, columns=[f"V{i}" for i in range(1, 7)], index=[f"R{i}" for i in range(1, 12)])
    print(df)

    #4 --------------------------------------------------------------------------------------------------
    mat = np.full((7,7), 9)
    print(mat)

    mat[:, :] = 0
    mat[1:-1, 1:-1] = 1

    print(mat)

    #5 --------------------------------------------------------------------------------------------------
    dictionar_studenti = {
        f"Stud_{i}": np.random.randint(1, 11)
        for i in range(1, 7)
    }
    print(dictionar_studenti)

    df_dict = pd.DataFrame(dictionar_studenti, index=["Nota"])
    print(df_dict)

    #6 --------------------------------------------------------------------------------------------------
    pd.Series(np.random.randint(1, 100, 5), name='Valori').to_csv("Seria_1.csv", index=False)
    pd.Series(np.random.randint(100, 200, 5), name='Valori').to_csv("Seria_2.csv", index=False)

    s1 = pd.read_csv("Seria_1.csv").squeeze()
    s2 = pd.read_csv("Seria_2.csv").squeeze()

    print(s1)
    print(s2)

    dict_serie = {
        "C_1": s1,
        "C_2": s2
    }

    print(dict_serie)

    df_dict_serie = pd.DataFrame(dict_serie)
    print(df_dict_serie)

    #7 --------------------------------------------------------------------------------------------------
    data = {
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
        'Open': [140.0, 142.5, 141.0, 145.0],
        'High': [145.0, 144.0, 143.0, 148.0],
        'Low': [139.0, 140.0, 140.0, 144.0],
        'Close': [144.5, 141.0, 142.0, 147.0]
    }
    pd.DataFrame(data).to_csv('NVDA.csv', index=False)

    df_nvda = pd.read_csv("NVDA.csv")
    numarator = df_nvda['Close'] - df_nvda['Open']
    numitor = df_nvda['High'] - df_nvda['Low']

    df_nvda['RV'] = numarator / numitor
    df_nvda.to_csv("NVDA_RV.csv", index=False)

    print(df_nvda)

    #8 --------------------------------------------------------------------------------------------------
    fac = {
        f"An_{i}": {
            f"Stud{j}": np.random.randint(1, 11, 3)
            for j in range(1, 8)
        }
        for i in range(1, 4)
    }

    df_fac = pd.DataFrame(fac)
    print(df_fac)

    #9 --------------------------------------------------------------------------------------------------
    big_mat = np.ones((7,7))

    big_mat[:, 0] = 444
    big_mat[0, :] = 444
    big_mat[:, -1] = 444
    big_mat[-1, :] = 444

    for i in range(big_mat.shape[0]):
        for j in range(big_mat.shape[1]):
            if i == j:
                big_mat[i, j] = 55

    big_mat[int(big_mat.shape[0] / 2), int(big_mat.shape[1] / 2)] = 111


    print(big_mat)

if __name__ == '__main__':
    main()