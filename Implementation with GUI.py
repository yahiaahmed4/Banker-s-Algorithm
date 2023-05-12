import tkinter as tk

class BankersAlgorithm:
    def __init__(self, num_processes, num_resources):
        self.num_processes = num_processes
        self.num_resources = num_resources
        self.max_claim = [[0 for j in range(self.num_resources)] for i in range(self.num_processes)]
        self.current_alloc = [[0 for j in range(self.num_resources)] for i in range(self.num_processes)]
        self.available = [0 for j in range(self.num_resources)]
        self.safe_sequence = []

    def set_max_claim(self, process_id, resources):
        self.max_claim[process_id] = resources

    def set_current_alloc(self, process_id, resources):
        self.current_alloc[process_id] = resources

    def set_available(self, resources):
        self.available = resources

    def is_safe_state(self):
        # initialize work and finish arrays
        work = self.available[:]
        finish = [False for i in range(self.num_processes)]

        # find an unallocated process whose needs can be satisfied
        while True:
            found = False
            for i in range(self.num_processes):
                if not finish[i] and all([self.max_claim[i][j] - self.current_alloc[i][j] <= work[j] for j in range(self.num_resources)]):
                    # allocate resources to process i
                    work = [work[j] + self.current_alloc[i][j] for j in range(self.num_resources)]
                    finish[i] = True
                    self.safe_sequence.append(i)
                    found = True

            # no unallocated process could be found
            if not found:
                break

        # check if all processes were allocated resources
        return all(finish)

def handle_submit():
    global banker
    num_processes = int(processes_entry.get())
    num_resources = int(resources_entry.get())

    # create a new BankersAlgorithm object
    banker = BankersAlgorithm(num_processes, num_resources)

    # get the maximum resource claims for each process
    max_claim_frame.grid(row=2, column=0)
    for i in range(num_processes):
        tk.Label(max_claim_frame, text=f"Process {i} max claim: ").grid(row=i, column=0)
        max_claim_entries.append([])
        for j in range(num_resources):
            entry = tk.Entry(max_claim_frame, width=3)
            entry.grid(row=i, column=j+1)
            max_claim_entries[-1].append(entry)

    # get the current allocated resources for each process
    current_alloc_frame.grid(row=3, column=0)
    for i in range(num_processes):
        tk.Label(current_alloc_frame, text=f"Process {i} current alloc: ").grid(row=i, column=0)
        current_alloc_entries.append([])
        for j in range(num_resources):
            entry = tk.Entry(current_alloc_frame, width=3)
            entry.grid(row=i, column=j+1)
            current_alloc_entries[-1].append(entry)

    # get the available resources
    available_frame.grid(row=4, column=0)
    tk.Label(available_frame, text="Available: ").grid(row=0, column=0)
    for i in range(num_resources):
        entry = tk.Entry(available_frame, width=3)
        entry.grid(row=0, column=i+1)
        available_entries.append(entry)

def handle_check():
    global banker
    # set the maximum resource claims for each process
    for i in range(banker.num_processes):
        banker.set_max_claim(i, [int(entry.get()) for entry in max_claim_entries[i]])

    # set the current allocated resources for each process
    for i in range(banker.num_processes):
        banker.set_current_alloc(i, [int(entry.get()) for entry in current_alloc_entries[i]])

    # set the available resources
    banker.set_available([int(entry.get()) for entry in available_entries])

    # check if the state is safe
    if banker.is_safe_state():
        safe_label.config(text="SAFE. Safe sequence: " + str(banker.safe_sequence))
        unsafe_label.config(text="")
    else:
        safe_label.config(text="")
        unsafe_label.config(text="UNSAFE")

# create the GUI
root = tk.Tk()
root.title("Banker's Algorithm")
root.resizable(False, False)

processes_frame = tk.Frame(root)
processes_frame.grid(row=0, column=0)
tk.Label(processes_frame, text="Number of processes: ").grid(row=0, column=0)
processes_entry = tk.Entry(processes_frame, width=3)
processes_entry.grid(row=0, column=1)

resources_frame = tk.Frame(root)
resources_frame.grid(row=1, column=0)
tk.Label(resources_frame, text="Number of resources: ").grid(row=0, column=0)
resources_entry = tk.Entry(resources_frame, width=3)
resources_entry.grid(row=0, column=1)

submit_button = tk.Button(root, text="Submit", command=handle_submit)
submit_button.grid(row=2, column=1)

max_claim_frame = tk.Frame(root)
current_alloc_frame = tk.Frame(root)
available_frame = tk.Frame(root)
max_claim_entries = []
current_alloc_entries = []
available_entries = []

check_button = tk.Button(root, text="Check", command=handle_check)
check_button.grid(row=5, column=1)

safe_label = tk.Label(root)
safe_label.grid(row=6, column=0)

unsafe_label = tk.Label(root)
unsafe_label.grid(row=6, column=1)

root.mainloop()