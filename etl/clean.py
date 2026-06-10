import pandas as pd

def clean_products(raw_products):
    df = pd.DataFrame(raw_products)
    
    # Keep only useful columns
    df = df[["product_title", "product_price", 
             "product_star_rating", "product_num_ratings",
             "product_url", "product_photo"]]
    
    # Clean price column
    df["product_price"] = (
        df["product_price"]
        .str.replace("₹", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    df["product_price"] = pd.to_numeric(df["product_price"], errors="coerce")
    df["product_star_rating"] = pd.to_numeric(df["product_star_rating"], errors="coerce")
    df["product_num_ratings"] = pd.to_numeric(df["product_num_ratings"], errors="coerce")
    
    df.dropna(subset=["product_price"], inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    return df

# Test it
if __name__ == "__main__":
    from fetch import fetch_products
    raw = fetch_products("laptop")
    df = clean_products(raw)
    print(df.head())
    print(df.dtypes)