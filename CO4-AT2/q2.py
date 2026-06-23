def allocate_resources(products, budget):
    # Scale down the budget and investments by 10,000 for cleaner matrix indices
    scale = 10000
    W = budget // scale
    
    # Extract names, scaled costs, and profits
    names = list(products.keys())
    costs = [products[p][0] // scale for p in names]
    profits = [products[p][1] for p in names]
    n = len(names)

    # Initialize DP table with zeros: (n + 1) rows x (W + 1) columns
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Build the table bottom-up
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if costs[i-1] <= w:
                # Max of (excluding current product, including current product)
                dp[i][w] = max(dp[i-1][w], profits[i-1] + dp[i-1][w - costs[i-1]])
            else:
                # Exclude current product if it exceeds current sub-budget
                dp[i][w] = dp[i-1][w]

    # Max profit is at the bottom-right corner of the matrix
    max_profit = dp[n][W]

    # Backtracking to find which products were selected
    selected_products = []
    w = W
    for i in range(n, 0, -1):
        # If value changed from the row above, the product was included
        if dp[i][w] != dp[i-1][w]:
            product_name = names[i-1]
            selected_products.append(product_name)
            w -= costs[i-1] # Deduct scaled investment cost

    # Reverse list to show selection in chronological order
    selected_products.reverse() 
    
    return max_profit, selected_products


# --- Execution Example ---
if __name__ == "__main__":
    # Product Data: { Name: (Investment_Cost, Profit) }
    product_options = {
        "A": (20000, 25000),
        "B": (30000, 40000),
        "C": (40000, 50000),
        "D": (50000, 65000)
    }
    total_budget = 100000

    max_prof, selection = allocate_resources(product_options, total_budget)

    print("=== OPTIMAL RESOURCE ALLOCATION ===")
    print(f"Selected Products : {', '.join(selection)}")
    print(f"Maximum Profit    : Rs. {max_prof:,}")
    print("====================================")
