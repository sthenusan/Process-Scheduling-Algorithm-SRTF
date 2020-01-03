
#object process define
class Process:
    def __init__(self, name, arrival, burst, origin, start, finish):
        self.name = name
        self.arrival = arrival
        self.burst = burst
        self.origin = origin
        self.start = start
        self.finish = finish

#this is the process schedular
class Scheduler:
    @staticmethod
    #function to count remaining process
    def count(processes, number_of_processes):
        process_remaining = 0
        for index in range(number_of_processes):
            if processes[index].burst > 0:
                process_remaining += 1
        return process_remaining

    @staticmethod
    # show the action of the schedular and show results of simulation
    def output(processes, number_of_processes):
        Scheduler.selection_sort(processes, 'arrival')
        total_waiting_time = 0
        print "process excecution finished....."
        print
        print('process  arrival  burst  waiting')
        print
        for index in range(number_of_processes):
            start = processes[index].start
            finish = processes[index].finish
            arrival = processes[index].arrival
            origin = processes[index].origin
            name = processes[index].name
            waiting_time = (start - arrival) + (finish - start - origin)
            print('\n%s \t %s \t %s \t %s' % (name, arrival, origin, waiting_time))
            total_waiting_time += waiting_time
            print
        print('total waiting time: %s' % total_waiting_time)
        print
        print('average waiting time: %s' % (total_waiting_time / number_of_processes))

    @staticmethod
    #method to traverse across ready queue and process the processes
    def start_processing(processes, number_of_processes):
        time = 0

        while scheduler.count(processes, number_of_processes) != 0:
            start_processing = -1

            for i in range(number_of_processes):
                arrival = processes[i].arrival
                burst = processes[i].burst
                if time >= arrival  and burst > 0:
                    if start_processing == -1:
                        start_processing = i
                    else:
                        if processes[i].burst < processes[start_processing].burst:
                            start_processing = i
                        elif processes[i].burst == processes[start_processing].burst:
                            if processes[i].finish == time:
                                start_processing = i

            if start_processing != -1:
                processes[start_processing].burst -= 1
                processes[start_processing].finish = time + 1

                if processes[start_processing].start == -1:
                    processes[start_processing].start = time
                    
            if time >= processes[start_processing].arrival:
                print "process "+ str(processes[start_processing].name)+" is processing" +" at time "+ str(time)
            else:
                print "There are No process in the ready queue"
            time += 1

    @staticmethod
    def run(processes, number_of_processes):
        Scheduler.start_processing(processes, number_of_processes)
        Scheduler.output(processes, number_of_processes)

    @staticmethod
    # Sorting method to order the process by its arrival time
    def selection_sort(k, key):
        n = len(k)
        for index in range(n):
            minimum = index
            for j in range(index + 1, n):
                if getattr(k[j], key) < getattr(k[minimum], key):
                    minimum = j
            tmp = k[minimum]
            k[minimum] = k[index]
            k[index] = tmp

            
#demo
if __name__ == '__main__':
    scheduler = Scheduler()

    processes = []
    number_of_processes = int(input('Enter the total no of processes: '))

    for i in range(1, number_of_processes + 1):
        arrival = int(input('Enter p%s arrival time: ' % i))
        burst = int(input('Enter p%s burst time: ' % i))
        name = 'p%s' % i
        process = Process(name=name, arrival=arrival, burst=burst, origin=burst, start=-1, finish=-1)
        processes.append(process)

    scheduler.run(processes, number_of_processes)
