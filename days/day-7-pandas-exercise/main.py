import pandas as pd

df_1 = pd.read_csv("leads1.csv", sep="|")
df_2 = pd.read_csv("leads2.csv", sep="|")

common = pd.merge(df_1, df_2, on='name', how='outer', indicator=True)

hey = pd.concat([df_1,df_2]).drop_duplicates(keep=False, subset='name')

def main():
    print(hey)

if __name__ == "__main__":
    main()