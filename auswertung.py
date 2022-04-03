import sys
import numpy as np
import pandas as pd
import pingouin as pg

def analyse(path):
    measurements = pd.read_csv(path, delimiter=",")
    
    mean_a = measurements[measurements.columns[1:4]].mean(axis=1)
    mean_b = measurements[measurements.columns[4:]].mean(axis=1)
    means = pd.concat(
        [measurements["Protein"], mean_a, mean_b],
        axis=1, keys=["Protein", "A", "B"]
    )
    
    logtwo = np.log2(measurements[measurements.columns[1:]])
    logtwo = pd.concat([measurements["Protein"], logtwo], axis=1)

    lt_mean_a = logtwo[logtwo.columns[1:4]].mean(axis=1)
    lt_mean_b = logtwo[logtwo.columns[4:]].mean(axis=1)
    lt_means = pd.concat(
        [measurements["Protein"], lt_mean_a, lt_mean_b],
        axis=1, keys=["Protein", "A", "B"]
    )

    p_vals = []
    
    for i in list(np.where(logtwo["Protein"])[0]):
        a_array = np.array(
            logtwo[["A1", "A2", "A3"]].loc[[i]].to_numpy()
        )[0]
        b_array = np.array(
            logtwo[["B1", "B2", "B3"]].loc[i].to_numpy()
        )[0]
        p_val = float(pg.ttest(a_array, b_array)["p-val"])
        
        p_vals.append(p_val)

    significances = []
    
    for i in p_vals:
        if i >= 0.95:
            significances.append("significant")
        else:
            significances.append("not significant")
    
    df_significances = pd.DataFrame(
        significances,
        list(measurements["Protein"]),
        columns=["Significance"]
    )

    df_pvals = pd.DataFrame(
        p_vals,
        list(measurements["Protein"]),
        columns=["p-Value"]
    )

    df_significance = pd.concat([df_pvals, df_significances], axis=1)
    
    return df_significance
        

def main():
    args = sys.argv
    
    if len(args) > 1:
        df = analyse(args[1])
        significant = df.loc[df["Significance"] == "significant"]
        
        print(significant)
    else:
        print("Fehler: fehlender Dateipfad, siehe Dokumentation!")

if __name__ == "__main__":
    main()
