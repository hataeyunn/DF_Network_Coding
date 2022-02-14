from enum import Enum


class Flag(Enum):
    DF_RREQ = 0
    DF_RREP = 1
    DF_DATA = 2
    DSR_RREQ = 3
    DSR_RREP = 4
    DSR_DATA = 5
    DF_CODING = 6


class Packet:
    def __init__(self, flag, source, destination, now):
        self.flag = Flag(flag)
        self.source = [source]
        self.destination = [destination]
        self.start_time = now
        self.size = 100
        self.route = source.route
        self.next_node = source
        self.current_node = source

    def Set_flag(self, flag):
        self.flag = Flag(flag)

    def Get_route(self):
        return self.route

    def Set_route(self, current):
        if self.flag == 'DSR_RREQ':
            self.current_node = current
        else:
            self.current_node = current
            if self.current_node != self.destination:
                self.next_node = self.route(self.route.index(self.current_node) + 1)
