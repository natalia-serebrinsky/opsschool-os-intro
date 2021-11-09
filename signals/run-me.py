#!/usr/bin/env python

import os, sys
import signal
import time
import atexit
import uuid


def before_exit():
    print('Program exiting normally')

def signal_handler(signum, frame):
    handler_id = str(uuid.uuid4()) # a unique id for this handler instance
    print('[{}] Caught signal : {}, at line: {}'.format(handler_id, signum, frame.f_lineno))
    time.sleep(1) # this is so you have time to send another signal before the handler finishes
    print('[{}] Signal handler ({}) done'.format(handler_id, signum))

def signal_handler_quit(signum, frame):
    print('Caught signal quit : {}, at line: {}'.format(signum, frame.f_lineno))
    time.sleep(1) # this is so you have time to send another signal before the handler finishes
    print('Signal handler quit({}) done'.format(signum))

def signal_handler_hup(signum, frame):
    print('Caught signal hup : {}, at line: {}'.format(signum, frame.f_lineno))
    time.sleep(1) # this is so you have time to send another signal before the handler finishes
    print('Signal handler hup({}) done'.format(signum))

def sig_handler_usr1(signum, frame):
    print("lala")

def sig_handler_usr2(signum, frame):
    print("lele")

def main():
    atexit.register(before_exit)

    # In python's signal package, signal numbers are given as named constants:
    # E.g. TERM signal is signal.SIGTERM

    # To install a signal handler, uncomment and modify the following line
    signal.signal(signal.SIGINT, signal_handler)

    # To ignore a signal, uncomment and modify the following line
    #signal.signal(signal.SIGIsNT, signal.SIG_IGN)
    
    signal.signal(signal.SIGQUIT, signal_handler_quit)
    signal.signal(signal.SIGHUP, signal_handler_hup)

    #signal.signal(signal.SIGKILL, signal_handler_kill) 
    #SIGKILL crashes the process 

    signal.signal(signal.SIGUSR1, sig_handler_usr1)
    signal.signal(signal.SIGUSR2, sig_handler_usr2)


    print('PID: {}'.format(os.getpid()))
    while True:
        print('[{}] Running, sleeping for 10 seconds'.format(time.time()))
        time.sleep(10)


if __name__ == "__main__":
    main()