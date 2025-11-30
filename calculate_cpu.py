import time
'''
Docstring for calculate_cpu

proc_matrix generated in process_proc method is already free of strings and
has the numerical values for the following:

0     1     2     3     4     5     6     7      8       9
user nice system idle iowait irq softirq steal guest guest_nice

total of 10 columns that correspond to the above
'''


def process_proc():
    '''
    generates a matrix of /proc/stat; generated only when process_proc is called
    '''
    proc_matrix=[]
    
    with open("/proc/stat") as kernel_file:
        for line in kernel_file:
            if line.startswith("cpu"):
                line = line.replace("\n"," ").strip()
                as_l= line.split(" ")
                as_l[:] = as_l[1:]
                
                if as_l[0]=="":
                    as_l.pop(0)
                if as_l[-1]=="":
                    as_l.pop(-1)

                #convert strings to numbers
                nums=[]
                for char in as_l:
                    nums.append(int(char))
                proc_matrix.append(nums)
    return proc_matrix



def get_total():
    proc_matrix = process_proc()
    total =0
    for line in proc_matrix:
        total += sum(line)
    return total

def get_idle():
    proc_matrix = process_proc()

    idles=0
    for line in proc_matrix:
        idles+=line[3]
    
    return idles

def get_cpu_usage():
    past_total = get_total()
    past_idle = get_idle()

    time.sleep(1)

    current_total= get_total()
    current_idle = get_idle()

    delta_idle = current_idle - past_idle
    delta_total = current_total - past_total

    cpu_percent = round(100 * (1 - delta_idle / delta_total),2)
    return cpu_percent

if __name__=="__main__":
    print(get_cpu_usage())