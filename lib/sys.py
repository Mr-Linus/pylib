import psutil
import datetime
import socket


class SYSTEM(object):
# Systen Information
    hostname = socket.gethostname()
    nowtime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    disk = psutil.disk_partitions()

    def system_uptime(self):
        return round((datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())).seconds / 3600, 2)

    class CPU(object):
        num = psutil.cpu_count(logical=False)
        Lnum = psutil.cpu_count(logical=True)
        # per = psutil.cpu_percent()
        
        def get_percent(self):
            sum = 0
            for persent in psutil.cpu_percent(interval=1, percpu=True):
                sum += persent
            return int(sum / self.Lnum)

    class MEM(object):
        persent = psutil.virtual_memory().percent
        used_MB = psutil.virtual_memory().used / 1024 / 1024
        used_GB = round(used_MB / 1024, 2)
        free_MB = psutil.virtual_memory().free / 1024 / 1024
        free_GB = round(free_MB / 1024, 2)
        total_MB = psutil.virtual_memory().total / 1024 / 1024
        total_GB = round(total_MB / 1024, 2)

    class SWAP(object):
        used = psutil.swap_memory().used / 1024 / 1024
        total = psutil.swap_memory().total / 1024 / 1024
        free = psutil.swap_memory().free / 1024 / 1024

    class NET(object):
        send_byte = psutil.net_io_counters().bytes_sent
        send_KB = send_byte / 1024
        send_MB = round(send_KB / 1024, 2)
        send_GB = round(send_MB / 1024, 2)
        recv_byte = psutil.net_io_counters().bytes_recv
        recv_KB = recv_byte / 1024
        recv_MB = round(recv_KB / 1024, 2)
        recv_GB = round(recv_MB / 1024, 2)

        def get_netcard(self):
            netcard_info = []
            info = psutil.net_if_addrs()
            for device, ip in info.items():
                for item in ip:
                    if item[0] == 2 and not item[1] == '127.0.0.1':
                        netcard_info.append((device, item[1]))
            return netcard_info

    class DISK(object):
        disk = psutil.disk_partitions()

        def print_list(self):
            result = ""

            def optback(opt):
                if (opt == 'ro'):
                    return ("Read-Only")
                elif (opt == 'rw'):
                    return ("Read-Write")
                else:
                    return ("Unknown")

            disk = psutil.disk_partitions()
            print("-----Device Information-----")
            for i in range(0, len(disk)):
                result += \
                    str(" Device:" + str(disk[i].device) + " Mount:" +
                        str(disk[i].mountpoint) + " Fstype:" +
                        str(disk[i].fstype) + " Opt: " +
                        str(optback(disk[i].opts)) + "\n")

            print(result)





if __name__ == '__main__':
    print(SYSTEM().CPU().per)





