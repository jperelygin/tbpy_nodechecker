import sched, time
import node_check

s = sched.scheduler(time.time, time.sleep)

delay = # <int> number of seconds of delay

def repeatable(sc):
    info = node_check.check()
    node_check.send(info)
    s.enter(delay, 1, repeatable, (sc,))

if __name__ == '__main__':
    print("sender is running NOW")
    s.enter(delay, 1, repeatable, (s,))
    s.run()
