def main_second():
    n = int(input())
    orders = [tuple(map(int, input().split(' '))) for _ in range(n)]
    orders.sort(key=lambda x: (x[0], x[1]))
    q = int(input())
    requests = [tuple(map(int, input().split(' '))) for _ in range(q)]
    print(orders)
    print(requests)
    answer = ''
    for request in requests:
        if request[2] == 1:
            total_cost = find_total_cost(orders, request[0], request[1])
            answer += str(total_cost) + " "
        elif request[2] == 2:
            total_duration = find_total_duration(orders, request[0], request[1])
            answer += str(total_duration) + " "
    print(answer[:-1])

def binary_search(arr, x, is_start):
    result = []
    left, right = 0, len(arr) - 1
    if is_start:
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] == x:
                result.append(mid)  # Добавляем индекс, если нашли элемент
                # Проверяем дополнительные вхождения элемента слева
                i = mid - 1
                while i >= 0 and arr[i][0] == x:
                    result.append(i)
                    i -= 1
                # Проверяем дополнительные вхождения элемента справа
                i = mid + 1
                while i < len(arr) and arr[i][0] == x:
                    result.append(i)
                    i += 1
                print("RESULT: ",result)
                return min(result)
            elif arr[mid][0] < x:
                left = mid + 1
            else:
                right = mid - 1
    else:
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] == x:
                result.append(mid)  # Добавляем индекс, если нашли элемент
                # Проверяем дополнительные вхождения элемента слева
                i = mid - 1
                while i >= 0 and arr[i][0] == x:
                    result.append(i)
                    i -= 1
                # Проверяем дополнительные вхождения элемента справа
                i = mid + 1
                while i < len(arr) and arr[i][0] == x:
                    result.append(i)
                    i += 1
                print("RESULT: ",result)
                return max(result)
            elif arr[mid][0] < x:
                left = mid + 1
            else:
                right = mid - 1

    return 0 # Возвращаем -1, если элемент не найден


def find_total_cost(orders, start_time, end_time):
    start_index = binary_search(orders, start_time, True)
    end_index = binary_search(orders, end_time, False)
    if(start_index>end_index):
        end_index = len(orders)
    print("S/E:", start_index, end_index+1)
    total_cost = sum(order[2] for order in orders[start_index:end_index+1] if start_time <= order[0] <= end_time)
    return total_cost

def find_total_duration(orders, start_time, end_time):
    start_index = binary_search(orders, start_time, True)
    end_index = binary_search(orders, end_time, False) # Исправление: уменьшаем на 1
    if (start_index > end_index):
        end_index = len(orders)
    print("S/E:", start_index, end_index + 1)
    total_duration = sum(order[1] - order[0] for order in orders[start_index:end_index+1] if start_time <= order[1] <= end_time)
    return total_duration

def main():
    n = int(input())
    orders = [tuple(map(int, input().split(' '))) for _ in range(n)]

    q = int(input())
    requests = [tuple(map(int, input().split(' '))) for _ in range(q)]

    results = []
    for request in requests:
        if request[2] == 1:
            total_cost = sum(order[2] for order in orders if request[0] <= order[0] <= request[1])
            results.append(total_cost)
        elif request[2] == 2:
            total_duration = sum(order[1] - order[0] for order in orders if request[0] <= order[1] <= request[1])
            results.append(total_duration)

    answer = ' '.join(map(str, results))
    print(answer)


if __name__ == "__main__":
    main()