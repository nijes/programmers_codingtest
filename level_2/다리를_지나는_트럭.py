def solution(bridge_length, weight, truck_weights):
    time, weights = 0, 0
    bridge = [0]*bridge_length
    while truck_weights:
        # 1칸씩 이동
        weights -= bridge.pop(0)
        # 다음 트럭 건너도 무게 초과X
        if weights + truck_weights[0] <= weight:
            weights += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        # 무게 초과
        else:
            bridge.append(0)
        time += 1
    return time + bridge_length