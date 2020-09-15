# Алгоритм Дейкстры

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:      # Перебрать все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed:    # Если этот узел с наименьшей стоимостью из уже 
                                                            # виденных и он еще не был обработан
            lowest_cost = cost                              # Он назначен новым узлом с наименьшей стоимостью
            lowest_cost_node = node
    return lowest_cost_node

if __name__ == "__main__":
    #Создание всех узлов и стоимости связей между ними
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph["a"] = {}
    graph["a"]["fin"] = 1
    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5
    graph["fin"] = {}

    #Создание стоимостей 
    infinity = float("inf")
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = infinity

    #Создание хеш-таблицы родителей
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["in"] = None
    
    processed = []

    node = find_lowest_cost_node(costs) # Найти узел с наименьшей стоимостью
                                        # среди необработанных

    while node is not None:             # Если обработаны все узлы, цикл while завершен
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors.keys():      # Перебрать всех соседей текущего узла
            new_cost = cost + neighbors[n]

            if costs[n] > new_cost:     # Если к соседу можно добраться быстрее через текущий узел
                costs[n] = new_cost     # Обновить стоимость для этого узла
                parents[n] = node       # Этот узел становится новым родителем для соседа
        processed.append(node)          # Узел помечен как обработанный
        print(processed)
        node = find_lowest_cost_node(costs) # Найти след. узел для обработки и повторить цикл
        
