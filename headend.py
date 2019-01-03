from SQL import SQL
from lib.sys import SYSTEM
from lib.nvidia import NVIDIA

map_table = {
    # Data Type int
    'CPUNUM': 'SYSTEMINT',
    'CPULNUM': 'SYSTEMINT',
    'CPUPER': 'SYSTEMINT',
    'MEMPER': 'SYSTEMINT',
    'NET_SENDPER': 'SYSTEMFLOAT',
    'NET_RECVPER': 'SYSTEMFLOAT',
    # Data Type float
    'MEMUSED': 'SYSTEMFLOAT',
    'MEMFREE': 'SYSTEMFLOAT',
    'MEMTOTAL': 'SYSTEMFLOAT',
    'SWAPUSED': 'SYSTEMFLOAT',
    'SWAPFREE': 'SYSTEMFLOAT',
    'SWAPTOTAL': 'SYSTEMFLOAT',
    'GCARDFREE': 'SYSTEMFLOAT',
    'GCARDUSED': 'SYSTEMFLOAT',
    'GCARDTOTAL': 'SYSTEMFLOAT',
    'NETSEND': 'SYSTEMFLOAT',
    'NETRECV': 'SYSTEMFLOAT',
    # Data Type String
    'HOSTNAME': 'SYSTEMCHAR',
    #'IP': 'SYSTEMCHAR',
    #'GCARDNAME': 'SYSTEMCHAR',
    'GCARDVER': 'SYSTEMCHAR',
    # Data Type Time
    #'UPTIME': 'SYSTEMTIME',
}


def update_all():
    sql = SQL()
    map_context = {
        'CPUNUM': SYSTEM.CPU.num,
        'CPULNUM': SYSTEM.CPU.Lnum,
        'CPUPER': SYSTEM.CPU().get_percent(),
        'MEMPER': SYSTEM.MEM().get_per(),
        # Data Type float
        'MEMUSED': SYSTEM.MEM().get_mem('GB', 'used'),
        'MEMFREE': SYSTEM.MEM().get_mem('GB', 'free'),
        'MEMTOTAL': SYSTEM.MEM().get_mem('GB', 'total'),
        'SWAPUSED': SYSTEM.SWAP().used / 1024,
        'SWAPFREE': SYSTEM.SWAP().free / 1024,
        'SWAPTOTAL': SYSTEM.SWAP().total / 1024,
        'GCARDFREE': NVIDIA.MEM().get_mem('GB', 'free'),
        'GCARDUSED': NVIDIA.MEM().get_mem('GB', 'used'),
        'GCARDTOTAL': NVIDIA.MEM().get_mem('GB', 'total'),
        'NETSEND': SYSTEM.NET.send_MB,
        'NETRECV': SYSTEM.NET.recv_MB,
        'NET_SENDPER': SYSTEM.NET().send_MB / (SYSTEM.NET.recv_MB + SYSTEM.NET.send_MB),
        'NET_RECVPER': SYSTEM.NET().recv_MB / (SYSTEM.NET.recv_MB + SYSTEM.NET.send_MB),
        # Data Type String
        'HOSTNAME': SYSTEM.hostname,
        # 'IP': SYSTEM.NET().get_netcard(),
        # 'GCARDNAME': NVIDIA().get_card_info(),
        'GCARDVER': NVIDIA().get_driver_version(),
        # Data Type Time
        # 'UPTIME': SYSTEM().system_uptime(),
    }
    for data_type, table in map_table.items():
        if table == 'SYSTEMCHAR':
            sql.update_char(table=table, data_type=data_type, context=map_context[data_type])
        else:
            sql.update_num(table=table, data_type=data_type, context=map_context[data_type])

