from SQL import SQL
from lib.sys import SYSTEM
from lib.nvidia import NVIDIA

map_table = {
    # Data Type int
    'CPUNUM': 'SYSTEMINT',
    'CPULNUM': 'SYSTEMINT',
    'CPUPER': 'SYSTEMINT',
    'MEMPER': 'SYSTEMINT',
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
    'IP': 'SYSTEMCHAR',
    'GCARDNAME': 'SYSTEMCHAR',
    'GCARDVERSION': 'SYSTEMCHAR',
    # Data Type Time
    'UPTIME': 'SYSTEMTIME',
}

map_context = {
    'CPUNUM': SYSTEM.CPU.num,
    'CPULNUM': SYSTEM.CPU.Lnum,
    'CPUPER': SYSTEM.CPU().get_percent(),
    'MEMPER': SYSTEM.MEM.persent,
    # Data Type float
    'MEMUSED': SYSTEM.MEM.used_GB,
    'MEMFREE': SYSTEM.MEM.free_GB,
    'MEMTOTAL': SYSTEM.MEM.total_GB,
    'SWAPUSED': SYSTEM.SWAP.used,
    'SWAPFREE': SYSTEM.SWAP.free,
    'SWAPTOTAL': SYSTEM.SWAP.total,
    'GCARDFREE': NVIDIA.MEM().get_mem('GB', 'free'),
    'GCARDUSED': NVIDIA.MEM().get_mem('GB', 'used'),
    'GCARDTOTAL': NVIDIA.MEM().get_mem('GB', 'total'),
    'NETSEND': SYSTEM.NET.send_MB,
    'NETRECV': SYSTEM.NET.recv_MB,
    # Data Type String
    'HOSTNAME': SYSTEM.hostname,
    'IP': SYSTEM.NET().get_netcard(),
    'GCARDNAME': NVIDIA().get_card_info(),
    'GCARDVERSION': NVIDIA().get_driver_version(),
    # Data Type Time
    'UPTIME': SYSTEM().system_uptime(),
}


def update_all():
    sql = SQL()
    for data_type, table in map_table:
        sql.update(table=table, data_type=data_type, context=map_context[data_type])
