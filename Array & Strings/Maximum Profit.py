def max_profit(prices):
    if prices == []: return None # 🟥 Edge Case, 空数列
    mx1 = mx2 = 0; mx1_name = mx2_name = ""; 
    mn = float('inf'); mn_name = ""
    for city, price in prices.items():
        if price > mx1: 
            mx1, mx2 = price, mx1 
            mx1_name, mx2_name = city, mx1_name
        elif price > mx2: 
            mx2 = price   
            mx2_name = city
        if price < mn:
            mn = min(mn, price)
            mn_name = city
    if mx1_name == mn_name: # 🟥 Edge Case, 一样的数据
        return [mx2_name, mn_name]
    return [mx1_name, mn_name]  

prices = {'London': 72, 'New York': 72, 'Tokyo': 72, 'Miami': 72}
print(max_profit(prices))