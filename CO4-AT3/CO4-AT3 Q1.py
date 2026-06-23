def greedy_investment(investments, budget):
    for inv in investments:
        inv['index'] = inv['return'] / inv['capital']
    
    sorted_inv = sorted(investments, key=lambda x: x['index'], reverse=True)
    
    selected = []
    total_capital = 0
    total_return = 0
    remaining_budget = budget
    
    for inv in sorted_inv:
        if inv['capital'] <= remaining_budget:
            selected.append(inv['name'])
            total_capital += inv['capital']
            total_return += inv['return']
            remaining_budget -= inv['capital']
            
    return selected, total_capital, total_return


def dp_investment(investments, budget):
    # Scale down by 10,000 to make the grid simpler and faster
    scale = 10000
    scaled_budget = budget // scale
    n = len(investments)
    
    dp = [[0 for _ in range(scaled_budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        inv_cap = investments[i-1]['capital'] // scale
        inv_ret = investments[i-1]['return']
        for w in range(scaled_budget + 1):
            if inv_cap <= w:
                dp[i][w] = max(dp[i-1][w], inv_ret + dp[i-1][w - inv_cap])
            else:
                dp[i][w] = dp[i-1][w]
                
    selected = []
    w = scaled_budget
    for i in range(n, 0, -1):
        inv_cap = investments[i-1]['capital'] // scale
        if dp[i][w] != dp[i-1][w]:
            selected.append(investments[i-1]['name'])
            w -= inv_cap
            
    selected.reverse()
    return selected, (scaled_budget - w) * scale, dp[n][scaled_budget]


if __name__ == "__main__":
    options = [
        {"name": "A", "capital": 20000, "return": 25000},
        {"name": "B", "capital": 30000, "return": 40000},
        {"name": "C", "capital": 40000, "return": 50000},
        {"name": "D", "capital": 50000, "return": 70000}
    ]
    budget = 80000

    g_portfolio, g_cap, g_ret = greedy_investment(options, budget)
    print("Greedy:", g_portfolio, "Capital:", g_cap, "Return:", g_ret)

    dp_portfolio, dp_cap, dp_ret = dp_investment(options, budget)
    print("DP:", dp_portfolio, "Capital:", dp_cap, "Return:", dp_ret)
