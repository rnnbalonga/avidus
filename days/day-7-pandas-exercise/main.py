import pandas as pd

df_1 = pd.read_csv("leads1.csv", sep="|")
df_2 = pd.read_csv("leads2.csv", sep="|")

common = pd.merge(df_1, df_2, on='name', how='outer', indicator=True)

hey = pd.concat([df_1,df_2]).drop_duplicates(keep=False, subset='name')

# Find rows that are only in df1 but not in df2
diff_df1 = common[common['_merge'] == 'left_only']

# Find rows that are only in df2 but not in df1
diff_df2 = common[common['_merge'] == 'right_only']

def main():
    print("leads1 only customers")
    for name in diff_df1['name']:
        print(name)

if __name__ == "__main__":
    main()