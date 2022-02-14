import util


def main():
    num_row_relay = 4
    num_col_relay = 5
    num_client = 20
    print("<-- 1. Make Topology -->")
    node_list = util.make_topology(num_row_relay, num_col_relay, num_client)
    print("Number of Client Node : " + str(node_list[0].num_client))
    print("Number of Relay Node : " + str(node_list[0].num_relay))


if __name__ == "__main__":
    main()
