import psutil
import datetime
import socket
import time


class SYSTEM(object):
    """
    Description: This class is used to obtain information
    about each hardware parameter of the system.
    """
    hostname = socket.gethostname()
    nowtime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    disk = psutil.disk_partitions()

    def system_uptime(self):
        """
        Description: Get system running time.
        :return: system running time.
        """
        return round((datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())).seconds / 3600, 2)

    class CPU(object):
        """
        Description: This class is used to obtain information about CPU.
        """
        # Get the number of CPU cores.
        num = psutil.cpu_count(logical=False)
        # Get the number of CPU logical cores.
        Lnum = psutil.cpu_count(logical=True)
        # If your have single core you could use
        # the following para to get the CPU using rate:
        # per = psutil.cpu_percent()

        def get_percent(self):
            """
            Description: Get the average using rate of multi-core.
            :return: the average using rate of multi-core.
            """
            sum = 0
            for persent in psutil.cpu_percent(interval=1, percpu=True):
                sum += persent
            return int(sum / self.Lnum)

    class MEM(object):
        """
        Description: This class is used to obtain information about system memory.
        """
        def get_mem(self, unit, mtype):
            """
            Description: Get the memory usage status.
            :param unit: Memory unit. e.g: MB, GB.
            :param mtype: Memory type. e.g: total, free, used.
            :return: The size of the request type memory.
            """
            def return_type(mtype):
                return {
                    'total': psutil.virtual_memory().total,
                    'free': psutil.virtual_memory().free,
                    'used': psutil.virtual_memory().used,
                }.get(mtype, 'error')

            return {
                'MB': round(return_type(mtype) / (1024 ** 2), 2),
                'GB': round(return_type(mtype) / (1024 ** 3), 2),
            }.get(unit, 'error')

        def get_per(self):
            """
            Description: Get the percentage of using memory.
            :return: the percentage of using memory.
            """
            return psutil.virtual_memory().percent

    class SWAP(object):
        """
        Description: Get the SWAP usage status.
        """
        used = psutil.swap_memory().used / (1024 ** 2)
        total = psutil.swap_memory().total / (1024 ** 2)
        free = psutil.swap_memory().free / (1024 ** 2)

    class NET(object):
        """
        Description: Get network I/O status.
        """
        send_byte = psutil.net_io_counters().bytes_sent
        send_KB = send_byte / 1024
        send_MB = round(send_KB / 1024, 2)
        send_GB = round(send_MB / 1024, 2)
        recv_byte = psutil.net_io_counters().bytes_recv
        recv_KB = recv_byte / 1024
        recv_MB = round(recv_KB / 1024, 2)
        recv_GB = round(recv_MB / 1024, 2)

        def get_netcard(self):
            """
            Get information about network adapter.
            :return: information about network adapter.
            """
            netcard_info = []
            info = psutil.net_if_addrs()
            for device, ip in info.items():
                for item in ip:
                    if item[0] == 2 and not item[1] == '127.0.0.1':
                        netcard_info.append((device, item[1]))
            return netcard_info

    class DISK(object):
        """
        Description: Get information about the block devices.
        """
        disk = psutil.disk_partitions()
        def print_list(self):
            """
            Description: Print the information about
            the block devices.
            :return: None
            """
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
                    str(" Device: " + str(disk[i].device) +
                        " Mount: " + str(disk[i].mountpoint) +
                        " Usage: " + str(psutil.disk_usage(disk[i].mountpoint)) +
                        " Fstype: " + str(disk[i].fstype) +
                        " Opt: " + str(optback(disk[i].opts)) + "\n")

            print(result)

        def get_list(self):
            disk_list = []
            disk_part = psutil.disk_partitions()
            for block in disk_part:
                disk_list.append({"Device": block.device,
                                  "MountPoint": block.mountpoint,
                                  "Per": psutil.disk_usage(block.mountpoint).percent,
                                  "total": psutil.disk_usage(block.mountpoint).total / (1024 ** 3),
                                  "used": psutil.disk_usage(block.mountpoint).used / (1024 ** 3),
                                  "free": psutil.disk_usage(block.mountpoint).free / (1024 ** 3),
                                  "Fstype": block.fstype
                                  })
            return disk_list


if __name__ == '__main__':
        print(SYSTEM().DISK().get_list())
        time.sleep(1)





