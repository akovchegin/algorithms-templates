def read_input():
    row_num = int(input())
    seat_map = []
    for row in range(row_num):
        row = tuple(input().strip())
        seat_map.append(row)
    req_num = int(input())
    seat_requests = []
    for req in range(req_num):
        req = tuple(input().strip())
        seat_requests.append(req)
    return seat_map, seat_requests


def is_free(seat):
    return seat == '.'


def process_req(req):
    pass

def main(seat_map, seat_requests):
    for req in seat_requests:
        result = process_req(req)
        print(result, *seat_map)

if __name__ == '__main__':
    print(read_input())