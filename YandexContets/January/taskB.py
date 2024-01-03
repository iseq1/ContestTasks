from datetime import datetime, timedelta

def main():
    n = int(input())
    log = []

    for i in range(n):
        cin = input().split()
        day, hour, minute, order_id = map(int, cin[:4])
        status = cin[4]
        log.append((datetime(2024, 1, 1, hour, minute) + timedelta(days=day - 1), order_id, status))

    log.sort(key=lambda x: (x[1], x[0]))
    # print(log)
    answer = {}

    accepted_time = datetime(2024, 1, 1, 0, 0)

    for timestamp, order_id, status in log:
        if status == 'A':
            accepted_time = timestamp
        elif status in ('C', 'S'):
            time_in_order = (timestamp - accepted_time).total_seconds() // 60
            answer[order_id] = answer.get(order_id, 0) + int(time_in_order)
            accepted_time = datetime(2024, 1, 1, 0, 0)

    print(' '.join(str(value) for value in answer.values()))

if __name__ == "__main__":
    main()
