import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def create_sample_data():
    """Create a sample sales_data.csv file for demonstration"""
    
    np.random.seed(42) 
    random.seed(42)

    start_date = datetime.now() - timedelta(days=30)
    dates = [start_date + timedelta(days=i) for i in range(30)]
    

    products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam', 'Headphones', 'Tablet', 'Smartphone']
    
    data = []
    
    for date in dates:
    
        num_transactions = random.randint(3, 8)
        
        for _ in range(num_transactions):
            product = random.choice(products)
            quantity = random.randint(1, 10)
            
            price_ranges = {
                'Laptop': (800, 1500),
                'Monitor': (200, 600),
                'Tablet': (300, 800),
                'Smartphone': (400, 1200),
                'Headphones': (50, 300),
                'Keyboard': (30, 150),
                'Mouse': (20, 100),
                'Webcam': (40, 200)
            }
            
            base_price = random.uniform(*price_ranges[product])
            revenue = round(base_price * quantity, 2)
            
            data.append({
                'Date': date.strftime('%Y-%m-%d'),
                'Product': product,
                'Quantity Sold': quantity,
                'Revenue ($)': revenue
            })
    
    df = pd.DataFrame(data)
    df.to_csv('sales_data.csv', index=False)
    print("Sample sales_data.csv created successfully!")
    return df

def analyze_sales_data():
    """Perform comprehensive sales data analysis"""
    
    try:
        df = pd.read_csv('sales_data.csv')
        print("Loading sales data...")
        print(f"Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns\n")
        
        print("First 5 rows of data:")
        print(df.head())
        print("\n" + "="*60 + "\n")
        
        total_revenue = df['Revenue ($)'].sum()
        print(f"Total Revenue: ${total_revenue:,.2f}")
        
        product_quantities = df.groupby('Product')['Quantity Sold'].sum()
        best_selling_product = product_quantities.idxmax()
        best_selling_quantity = product_quantities.max()
        
        print(f"Best-Selling Product: {best_selling_product}")
        print(f"   Total Quantity Sold: {best_selling_quantity} units")
        
        daily_sales = df.groupby('Date')['Revenue ($)'].sum()
        highest_sales_day = daily_sales.idxmax()
        highest_sales_amount = daily_sales.max()
        
        print(f"Highest Sales Day: {highest_sales_day}")
        print(f"   Revenue: ${highest_sales_amount:,.2f}")
        
        print("\n" + "="*60)
        print("ADDITIONAL INSIGHTS")
        print("="*60)
        
        avg_daily_revenue = daily_sales.mean()
        print(f"Average Daily Revenue: ${avg_daily_revenue:,.2f}")
        
        product_revenue = df.groupby('Product')['Revenue ($)'].sum().sort_values(ascending=False)
        print(f"\nTop 3 Products by Revenue:")
        for i, (product, revenue) in enumerate(product_revenue.head(3).items(), 1):
            print(f"   {i}. {product}: ${revenue:,.2f}")
        
        product_summary = df.groupby('Product').agg({
            'Quantity Sold': 'sum',
            'Revenue ($)': 'sum'
        }).round(2)
        product_summary['Avg Price per Unit'] = (product_summary['Revenue ($)'] / 
                                               product_summary['Quantity Sold']).round(2)
        
        print(f"\nProduct Performance Summary:")
        print(product_summary.sort_values('Revenue ($)', ascending=False))
        
        summary_text = f"""
SALES DATA ANALYSIS SUMMARY
============================
Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Dataset Period: {df['Date'].min()} to {df['Date'].max()}
Total Records: {len(df)}

KEY METRICS:
============
Total Revenue: ${total_revenue:,.2f}
Best-Selling Product: {best_selling_product} ({best_selling_quantity} units)
Highest Sales Day: {highest_sales_day} (${highest_sales_amount:,.2f})
Average Daily Revenue: ${avg_daily_revenue:,.2f}

TOP 3 PRODUCTS BY REVENUE:
=========================
"""
        
        for i, (product, revenue) in enumerate(product_revenue.head(3).items(), 1):
            summary_text += f"{i}. {product}: ${revenue:,.2f}\n"
        
        summary_text += f"\nPRODUCT PERFORMANCE:\n"
        summary_text += "=" * 20 + "\n"
        summary_text += product_summary.sort_values('Revenue ($)', ascending=False).to_string()
        
        # Save to file
        with open('sales_summary.txt', 'w') as f:
            f.write(summary_text)
        
        print(f"\nAnalysis complete! Results saved to 'sales_summary.txt'")
        
        return {
            'total_revenue': total_revenue,
            'best_selling_product': best_selling_product,
            'best_selling_quantity': best_selling_quantity,
            'highest_sales_day': highest_sales_day,
            'highest_sales_amount': highest_sales_amount,
            'avg_daily_revenue': avg_daily_revenue,
            'product_summary': product_summary
        }
        
    except FileNotFoundError:
        print("Error: sales_data.csv not found!")
        print("Creating sample data first...")
        create_sample_data()
        print("Now running analysis on sample data...\n")
        return analyze_sales_data()
    
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        return None

def main():
    """Main function to run the sales analysis"""
    
    print("SALES DATA ANALYSIS TOOL")
    print("=" * 40)
    
    try:
        pd.read_csv('sales_data.csv')
        print("Found existing sales_data.csv")
    except FileNotFoundError:
        print("sales_data.csv not found. Creating sample data...")
        create_sample_data()
    
    print("\nStarting analysis...\n")

    results = analyze_sales_data()
    
    if results:
        print("\n" + "=" * 40)
        print("ANALYSIS COMPLETED SUCCESSFULLY!")
        print("=" * 40)
        print("\nFiles created:")
        print("   • sales_data.csv (if not existing)")
        print("   • sales_summary.txt")
        
        print(f"\nQuick Summary:")
        print(f"   Total Revenue: ${results['total_revenue']:,.2f}")
        print(f"   Best Product: {results['best_selling_product']}")
        print(f"   Best Day: {results['highest_sales_day']}")

if __name__ == "__main__":
    main()