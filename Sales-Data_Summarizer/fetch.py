import pandas as pd
import chardet

def read_parse(file):
    """
        Reads a CSV file and filters the relevant columns for sales data.
        
        Args:
            file (str): Path to the CSV file.
        
        Returns:
            DataFrame: Filtered data for further analysis.
    """
    try:
        with open(file, 'rb') as f:
            result = chardet.detect(f.read())
            encoding = result['encoding']
            print(f"Detected encoding: {encoding}")  # Print encoding to verify

            # First, try using the encoding detected by chardet
            try:
                df = pd.read_csv(file, encoding=encoding)
            except UnicodeDecodeError:
                # If it fails, try with ISO-8859-1 or utf-8 as fallback options
                print("Trying with 'ISO-8859-1' encoding due to decoding error.")
                df = pd.read_csv(file, encoding='ISO-8859-1')
            
            df_to_work = df[['PRODUCTCODE', 'PRICEEACH', 'SALES', 'QUANTITYORDERED', 'ORDERDATE']]  # Filter columns
            return df_to_work

    except FileNotFoundError:
        print(f"Error: The file {file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


    

def sale_per_product(df):
    sales_per_product = df.groupby('PRODUCTCODE').SALES.sum().reset_index()
    sales_per_product = sales_per_product.rename(columns={"SALES": "TOTAL_SALES"})
    return sales_per_product.sort_values(by="TOTAL_SALES", ascending=False)

def most_proftable_product(df):
    # Get the product with the highest total sales
    product_sales = df.groupby('PRODUCTCODE').SALES.sum().reset_index()
    highest_sale_product = product_sales.loc[product_sales['SALES'].idxmax()]
    
    # Find the highest sale day for that product
    highest_day_sale_prod = df.loc[df['PRODUCTCODE'] == highest_sale_product['PRODUCTCODE']].nlargest(1, 'SALES')
    return highest_day_sale_prod



file = "Inputs/sales_data_sample.csv"
print(sale_per_product(read_parse(file)))
print(most_proftable_product(read_parse(file)))
