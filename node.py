from queue import Queue
import packet

class Node:
    num_relay = 0
    num_client = 0
    static_route = []
    def __init__(self, relay, position, connection,number):
        self.is_relay = relay
        self.number = number
        self.connection = connection
        self.buffer = Queue()
        self.position = position  # x,y dict
        self.bidir = 0
        self.bidir_table = []
        self.route = []
        if self.is_relay:
            Node.num_relay += 1
        else:
            Node.num_client += 1

    def Get_bidir(self):
        return self.bidir

    def Get_position(self):
        return self.position

    def Get_bidir_table(self):
        return self.bidir_table
    def Make_packet(self,flag):
        if self.number%2 == 0:
            pkt = packet(flag,self.number+1)#진행중, source는 오브젝, destination은 넘버 int값으로..

    def Add_bidir(self,in_node,out_node):
        self.bidir+=1
        if in_node.number > out_node.number:
            self.bidir_table.append(out_node,in_node)
        else :
            self.bidir_table.append(in_node,out_node)
    def Ready_to_Send(self):
