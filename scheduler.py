from process import Process

class Scheduler:


    #Constructor
    def __init__(self,process_list):
        self.process_list = process_list
        self.q1 = []
        self.q2 = []

        process_list[0].print_info()