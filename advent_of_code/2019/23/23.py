#!/usr/bin/env python3

import operator
import threading
from collections import defaultdict, deque
from time import sleep


def abs_addr(base, addr, flag):
    return addr + (0 if flag == 0 else base)


def run(mem, inp_cb, out_cb, halt_event):
    mem = defaultdict(int, enumerate(mem))
    pos, base = 0, 0
    while True:
        if halt_event.is_set():
            break
        pm, opc = mem[pos] // 100, mem[pos] % 100
        if opc == 1:  # add
            op = operator.add
            il, ol = 2, 1
        elif opc == 2:  # mul
            op = operator.mul
            il, ol = 2, 1
        elif opc == 3:  # read
            op = inp_cb
            il, ol = 0, 1
        elif opc == 4:  # print
            op = lambda x: x
            il, ol = 1, 3
        elif opc == 5:  # jump-if-true
            op = lambda c, v: v if c else None
            il, ol = 2, 2
        elif opc == 6:  # jump-if-false
            op = lambda c, v: v if not c else None
            il, ol = 2, 2
        elif opc == 7:  # less than
            op = lambda x, y: int(x < y)
            il, ol = 2, 1
        elif opc == 8:  # equals
            op = lambda x, y: int(x == y)
            il, ol = 2, 1
        elif opc == 9:  # base adjust
            op = lambda x: x
            il, ol = 1, 4
        elif opc == 99:  # halt
            break
        else:
            print('Wrong opc %d at %d' % (opc, pos))
            print(mem)
            exit()

        inp = []
        for _ in range(il):
            v = mem[(pos := pos + 1)]
            f, pm = pm % 10, pm // 10
            inp.append(v if f == 1 else mem[abs_addr(base, v, f)])

        ret = op(*inp)

        if ol == 1:
            f, pm = pm % 10, pm // 10
            mem[abs_addr(base, mem[(pos := pos + 1)], f)] = ret
        pos += 1

        if ol == 2 and ret != None:
            pos = ret

        if ol == 4:
            base += ret

        if ol == 3:
            out_cb(ret)


class Machine:
    def __init__(self, id, send_cb, halt_event):
        self._que = deque([id])
        self._lock = threading.Lock()
        self._out_packet = []
        self._send_cb = send_cb
        self._idle = False
        self._halt_event = halt_event
        self.id = id

        self._thread = threading.Thread(
            target=run, args=(mem, self._get_que_item, self._out_cb, halt_event)
        )

    def _out_cb(self, x):
        self._out_packet.append(x)
        self._idle = False
        if len(self._out_packet) == 3:
            to_id, *packet = self._out_packet
            self._send_cb(to_id, packet)
            self._out_packet = []

    def send(self, packet):
        with self._lock:
            self._idle = False
            self._que.extend(packet)

    def _get_que_item(self):
        with self._lock:
            if self._que:
                return self._que.popleft()
            else:
                self._idle = True
                return -1

    def start(self):
        self._thread.start()

    def join(self):
        self._thread.join()


class Network:
    def __init__(self, n_machines):
        self._halt_event = threading.Event()
        self._registry = {
            i: Machine(i, self.send, self._halt_event) for i in range(n_machines)
        }
        self._nat_packet = None
        self._lock = threading.RLock()
        self._governor_thread = threading.Thread(target=self._governor)

        self._first_y_to_nat = None
        self._last_y_from_nat = None
        self._first_d_y_from_nat = None

    def send(self, id, packet):
        with self._lock:
            if id == 255:
                self._nat_packet = packet
                if self._first_y_to_nat == None:
                    self._first_y_to_nat = packet[1]
            else:
                self._registry[id].send(packet)

    def _nat(self):
        with self._lock:
            time_to_nat = all(machine._idle for machine in self._registry.values())
            if time_to_nat and self._nat_packet != None:
                self.send(0, self._nat_packet)

                if (
                    self._first_d_y_from_nat == None
                    and self._nat_packet[1] == self._last_y_from_nat
                ):
                    self._first_d_y_from_nat = self._nat_packet[1]
                self._last_y_from_nat = self._nat_packet[1]

                self._nat_packet = None

    def _governor(self):
        while not self._halt_event.is_set():
            sleep(0.1)
            self._nat()
            if self._first_y_to_nat and self._first_d_y_from_nat:
                self._halt_event.set()

    def start(self):
        for machine in self._registry.values():
            machine.start()
        self._governor_thread.start()

    def join(self):
        self._halt_event.wait()
        for machine in self._registry.values():
            machine.join()
        self._governor_thread.join()

    def get_results(self):
        self._halt_event.wait()
        return self._first_y_to_nat, self._first_d_y_from_nat


def main():
    global mem
    n_machines = 50
    mem = [int(x) for x in open('input').read().strip().split(',')]

    net = Network(n_machines)
    net.start()
    net.join()
    s1, s2 = net.get_results()

    print('First Y to NAT:', s1)
    print('First double Y from NAT:', s2)


main()
