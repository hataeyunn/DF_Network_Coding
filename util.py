import math
from node import Node

omega = 0.9  # set weight factor
topology_term = 10


def delay_function(bidir, K, alpha, d_limit, num_node):
    k_bar_t = omega * bidir + (1 - omega) * (K - bidir);
    if bidir <= K:
        return (1 / math.pow(alpha, k_bar_t)) * (1 / pow(num_node - 1, k_bar_t + 1)) * d_limit
    else:
        return (1 / (num_node - 1)) * d_limit


def distance(in_position, out_position):
    return math.sqrt(pow(in_position['x'] - out_position['x'], 2) + pow(in_position['y'] - out_position['y'], 2))


def make_position(x, y):
    return {'x': x, 'y': y}


def make_topology(num_relay_row, num_relay_col, num_client):
    left_client = []
    right_client = []
    result = []
    left_relay = []
    right_relay = []
    for i in range(0, num_client):
        if i % 2 == 0:
            left_client.append(num_relay_row * num_relay_col + i)
        else:
            right_client.append(num_relay_row * num_relay_col + i)

    for j in range(0, num_relay_col):
        for i in range(0, num_relay_row):
            if j == num_relay_col - 1:  # 최상단
                if i == 0:
                    result.append(Node(True, make_position((i + 1) * topology_term, j * topology_term),
                                       [(j - 1) * num_relay_row + i, j * num_relay_row + i + 1
                                        ] + left_client,
                                       j * num_relay_row + i))
                    left_relay.append(j * num_relay_row + i)
                elif i == num_relay_row - 1:
                    result.append(Node(True, make_position((i + 1) * topology_term, j * topology_term),
                                       [(j - 1) * num_relay_row + i, j * num_relay_row + i - 1
                                        ] + right_client,
                                       j * num_relay_row + i))
                    right_relay.append(j * num_relay_row + i)

                else:
                    result.append(Node(True, make_position((i + 1) * topology_term, j * topology_term),
                                       [(j - 1) * num_relay_row + i, j * num_relay_row + i - 1,
                                        j * num_relay_row + i + 1],
                                       j * num_relay_row + i))
            elif j == 0:  # 최하단
                if i == 0:
                    result.append(Node(True, make_position((i + 1) * topology_term, j * topology_term),
                                       [j * num_relay_row + i + 1, (j + 1) * num_relay_row + i] + left_client,
                                       j * num_relay_row + i))
                    left_relay.append(j * num_relay_row + i)

                elif i == num_relay_row - 1:
                    result.append(Node(True, make_position((i + 1) * topology_term, j * topology_term),
                                       [j * num_relay_row + i - 1, (j + 1) * num_relay_row + i
                                        ] + right_client,
                                       j * num_relay_row + i))
                    right_relay.append(j * num_relay_row + i)

                else:
                    result.append(Node(True, make_position((i + 1) * topology_term, j * topology_term),
                                       [j * num_relay_row + i - 1,
                                        j * num_relay_row + i + 1, (j + 1) * num_relay_row + i],
                                       j * num_relay_row + i))
            else:  # 중간
                if i == 0:
                    result.append(Node(True, make_position((i + 1) * topology_term, j * topology_term),
                                       [(j - 1) * num_relay_row + i, j * num_relay_row + i + 1,
                                        (j + 1) * num_relay_row + i
                                        ] + left_client,
                                       j * num_relay_row + i))
                    left_relay.append(j * num_relay_row + i)

                elif i == num_relay_row - 1:
                    result.append(Node(True, make_position((i + 1) * topology_term, j * topology_term),
                                       [(j - 1) * num_relay_row + i,
                                        j * num_relay_row + i - 1,
                                        (j + 1) * num_relay_row + i] + right_client,
                                       j * num_relay_row + i))
                    right_relay.append(j * num_relay_row + i)

                else:
                    result.append(Node(True, make_position((i + 1) * topology_term, j * topology_term),
                                       [(j - 1) * num_relay_row + i, j * num_relay_row + i - 1,
                                        j * num_relay_row + i + 1,
                                        (j + 1) * num_relay_row + i],
                                       j * num_relay_row + i))

    for i in range(0, num_client):
        if num_relay_row * num_relay_col + i in left_client:
            result.append(Node(False, make_position(0, (int(i / 2) + 1) * (
                        ((num_relay_col - 1) * topology_term) / len(left_client))), left_relay,
                               num_relay_row * num_relay_col + i))
        else:
            result.append(Node(False, make_position(topology_term * (num_relay_row + 1), (int(i / 2) + 1) * (
                        ((num_relay_col - 1) * topology_term) / len(right_client))), right_relay,
                               num_relay_row * num_relay_col + i))

    return result

