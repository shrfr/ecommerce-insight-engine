from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_insights(df, keyword):
    summary = df[["product_price", "product_star_rating", "product_num_ratings"]].describe().to_string()
    top5 = df.nlargest(5, "product_star_rating")[
        ["product_title", "product_price", "product_star_rating"]
    ].to_string()

    prompt = f"""
    You are a business analyst. Analyze this Amazon India product data for the keyword "{keyword}".
    
    Statistical Summary:
    {summary}
    
    Top 5 Rated Products:
    {top5}
    
    Provide:
    1. Price range analysis — what price segment dominates?
    2. Rating trends — are higher priced products rated better?
    3. Top 3 business insights a seller should know
    4. One recommendation for a new seller entering this category
    
    Keep it concise and actionable. Use plain English.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    sys.path.append(".")
    from etl.fetch import fetch_products
    from etl.clean import clean_products
    raw = fetch_products("laptop")
    df = clean_products(raw)
    insights = generate_insights(df, "laptop")
    print(insights)