# Simple consumer-producer architecture
from multiprocessing import Lock
from multiprocessing import Process
from multiprocessing import Queue
import random
import time

# Names of combat machines from Horizon: Zero Dawn video-game
MACHINES = {
    'Terra-formers Machines': [
        'Broadhead', 'Grazer', 'Trampler', 'Charger'
    ],
    'Purifiers Machines': [
        'Lancehorn', 'Snapmaw', 'Strider'
    ],
    'Combat Class Machines': [
        'Ravager', 'Sawtooth', 'Stalker', 'Thunderjaw'
    ],
    'FARO War Machines': [
        'Corruptor', 'Deathbringer'
    ],
    'Communication Machines': [
        'Tallneck'
    ]
}


# Emulating work of a "focus" gadget from the game
# Will print the message before every queue sending
def focus(m_type):
    print('Unknown machine {} type is discovered.'.format(m_type))


# Producer function. Produces new machines of different danger level
def machine_cauldron(queue, lock, machines):
    with lock:
        print('Scanning area...')

    for machine_type, machines_list in machines.items():
        time.sleep(5)
        focus(machine_type)
        machine_name = machines_list[
            random.randint(0, len(machines_list) - 1)
        ]
        queue.put((machine_type, machine_name))
    with lock:
        print('No more machines will come.')


# Consumer function. Huntress will fight a dangerous machine or run away
def huntress(queue, lock):
    with lock:
        print('Careful! Unknown machine!')
    while True:
        machine_type, machine_name = queue.get()
        time.sleep(3)
        with lock:
            if machine_type == 'Communication Machines':
                print("It's just a Tallneck! It's safe.")
            elif machine_type == 'FARO War Machines':
                print("It is a {}. Too dangerous, you'd better run!".
                      format(machine_name))
            else:
                print("{} type: {} successfully destroyed".
                      format(machine_type, machine_name))


if __name__ == '__main__':

    queue = Queue()
    lock = Lock()

    machines_process = Process(target=machine_cauldron,
                               args=(queue, lock, MACHINES))
    aloy = Process(target=huntress, args=(queue, lock))
    aloy.daemon = True

    aloy.start()
    machines_process.start()

    machines_process.join()
    time.sleep(3)
    print('Area is safe now.')
