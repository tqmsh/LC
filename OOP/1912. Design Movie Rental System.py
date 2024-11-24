# pq: init O(n), add O(logn), pq[0]: O(1), k top O(klogn), remove O(logn), arbituary O(n)
# sortedContainer: init O(nlogn), add O(logn), a[0]: O(1), k top O(k), remove O(logn), arbitrary O(logn)
from collections import defaultdict
from sortedcontainers import SortedList
from typing import List, Tuple, Dict

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[Tuple[int, int, int]]): 
        # Faster k top, k = 5
        self.search_ans: defaultdict[int, SortedList[Tuple[int, int]]] = defaultdict(SortedList)  # movie -> (price, shop)
        self.report_ans: SortedList[Tuple[int, int, int]] = SortedList()  # (price, shop, movie)
        self.shop_movie_to_price: Dict[Tuple[int, int], int] = {}  # (shop, movie) -> price
        for shop, movie, price in entries:
            self.search_ans[movie].add((price, shop))
            self.shop_movie_to_price[(shop, movie)] = price  # 初始化，构建商店和电影的映射
        
    def search(self, movie: int) -> List[int]: 
        return [shop for _, shop in self.search_ans[movie][:5]]  # 前五最便宜的

    def rent(self, shop: int, movie: int) -> None: 
        price = self.shop_movie_to_price[(shop, movie)]
        self.search_ans[movie].remove((price, shop))  # 从可租列表中移除
        self.report_ans.add((price, shop, movie))  # 添加到已租赁列表中

    def drop(self, shop: int, movie: int) -> None: 
        price = self.shop_movie_to_price[(shop, movie)]
        self.search_ans[movie].add((price, shop))  # 重新加入可租列表
        self.report_ans.remove((price, shop, movie))  # 从已租赁列表中移除

    def report(self) -> List[List[int]]: 
        return [[shop, movie] for _, shop, movie in self.report_ans[:5]]  # 返回前五个最便宜的租赁信息

# 🟥 边缘测试: 处理特殊情况，如电影或商店不存在时返回空列表

# 测试用例
if __name__ == "__main__":
    # Initialization
    Obj = MovieRentingSystem(3, [(0, 1, 5), (0, 2, 6), (0, 3, 7), (1, 1, 4), (1, 2, 7), (2, 1, 5)])
    
    # Test #1: 搜索功能 (movie ID 1)
    print(Obj.search(1))  # 预期输出: [1, 0, 2] (按价格排序，如果价格相同按商店编号排序)

    # Test #2: 租赁功能 (从商店 0 租赁电影 1)
    Obj.rent(0, 1)
    print(Obj.search(1))  # 预期输出: [1, 2] (商店 0 不再有电影 1)

    # Test #3: 租赁功能 (从商店 1 租赁电影 2)
    Obj.rent(1, 2)
    print(Obj.report())  # 预期输出: [[0, 1], [1, 2]] (已租赁的电影)

    # Test #4: 归还功能 (归还商店 1 的电影 2)
    Obj.drop(1, 2)
    print(Obj.search(2))  # 预期输出: [0, 1] (商店 0 和 1 现在都有电影 2)

    # Test #5: 归还后的报告功能
    print(Obj.report())  # 预期输出: [[0, 1]] (只有商店 0 的电影 1 被租赁)

    # 🟥 Test #6: 边缘情况 (搜索不存在的电影)
    print(Obj.search(99))  # 预期输出: [] (电影 ID 99 不存在)

    # 🟥 Test #7: 边缘情况 (没有租赁时的报告)
    new_Obj = MovieRentingSystem(2, [(0, 4, 10), (1, 4, 12)])
    print(new_Obj.report())  # 预期输出: [] (还没有任何电影被租赁)

    # Test #8: 归还未租赁的电影 (应当保持状态而不报错)
    try:
        new_Obj.drop(0, 4)
        print("归还未租赁的电影操作成功处理。")
    except ValueError:
        print("归还未租赁的电影时发生错误。")
