from typing import Dict, Union

ND = Dict[str, Union[str, 'ND']]

def _dfs(cur: str, x: Union[str, ND], ans: Dict[str, str]) -> None: # cur: [1, x]
    if isinstance(x, str): 
        ans[cur] = x  
        return 
    for nx, v in x.items():  
        if nx != "": _dfs(f"{cur}.{nx}", v, ans) 
        else: _dfs(f"{cur}", v, ans)
        
def flatten_dict(dict: ND) -> Dict[str, str]:
    ans = {}
    for x, v in dict.items(): _dfs(x, v, ans)  
    return ans

dict_input = {
    "Key1": "1",
    "Key2": {
        "a": "2",
        "b": "3",
        "c": {
            "d": "3",
            "e": {
                "": "1"
            }
        }
    }
}

flattened_output = flatten_dict(dict_input)
print(flattened_output)
