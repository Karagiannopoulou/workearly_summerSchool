import sys, os
import pandas as pd


file_csv = r"C:\Users\mini3\Documents\Workearly\Python\Final-Assignment-main\Final-Assignment-main\finance_liquor_sales_limitedbyYEAR.csv"
df = pd.read_csv(file_csv)

def popitem_percstorezip_sale(df):

    df['percentage'] = df['sale_dollars'] / df.groupby(['zip_code', 'store_name'])['sale_dollars'].transform('sum')

    df2 = pd.DataFrame(df[['store_name', 'zip_code', 'item_description', 'sale_dollars', 'percentage']])

    top_sales_ids = df2.groupby(['zip_code','store_name'])['percentage'].idxmax()

    top_items = df.iloc[top_sales_ids]

    return top_items.to_csv(r'C:\Users\mini3\Documents\Workearly\Python\Final-Assignment-main\Final-Assignment-main\final.csv')


if __name__ == "__main__":
    print(popitem_percstorezip_sale(df))
