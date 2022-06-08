# AKSHIT OP >>

""" matrix = [
    [0, 10, 15, 20],
    [5, 0, 9, 10  ],
    [6, 13, 0, 12 ],
    [8, 8, 9, 0   ]] """
    
matrix = [
    [0,24,11,10,9],
    [8,0,2,5,11  ],
    [26,12,0,8,7 ],
    [11,23,24,0,6],
    [5,4,8,11,0  ]]

results = {}

def tsp_solve(root, path_set):
    
    hash_key = f"{root},{sorted(path_set)}"
    
    if hash_key in results.keys():
        return results[hash_key]
    
    else:
        if len(path_set) > 1:
            temp_results = []
            for path_node in path_set:
                temp_result = matrix[root][path_node] + tsp_solve(path_node, [i for i in path_set if i != path_node])
                temp_results.append(temp_result)
            level_result = min(temp_results)
        else:
            level_result = matrix[root][path_set[0]] + matrix[path_set[0]][0]

        results[f"{root},{sorted(path_set)}"] = level_result
        return level_result
                
def trace_path(root, path_set, store):
    if len(path_set)==1:
        store.append(path_set[0]+1)
    else:
        path_costs = [matrix[root][path]+results[f"{path},{sorted([j for j in path_set if j!=path])}"] for path in path_set]
        paths = [(path,sorted([j for j in path_set if j!=path])) for path in path_set]
        selected_path = min(zip(path_costs, paths))[1]
        store.append(selected_path[0]+1)
        trace_path(selected_path[0], selected_path[1], store)
    
results={}
tsp_solve(0, [i for i in range(1,len(matrix))])
ans_arr = []
trace_path(0, [i for i in range(1,len(matrix))], ans_arr)
print("1 -->", end=" ")
print(" --> ".join(map(str, ans_arr)), end=" ")
print("--> 1", end="")