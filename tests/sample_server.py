# -*- coding: utf-8 -*-

#import gevent
#from gevent import monkey
#monkey.patch_all()
#import zmq.green as zmq

import zmq
from zwsgi.baseserver import ZMQBaseServer


def main():

    context = zmq.Context()
    poller = zmq.Poller()
    ppoller = zmq.Poller()
    server=(zmq.REP, 'tcp', '127.0.0.1', '7000')
    server = ZMQBaseServer(server, context=context, poller=poller, ppoller=ppoller)
    server.serve()

if __name__ == "__main__":
    main()
