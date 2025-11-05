import pandas as pd

df_1 = pd.read_csv("leads1.csv")
df_2 = pd.read_csv("leads2.csv")

def main():
    print(df_1)

if __name__ == "__main__":
    main()