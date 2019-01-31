from lib.SQL.core import SQL
from lib.system.core import SYSTEM
from lib.system.nvidia import NVIDIA
import grpc
import grpc_lib.connect_pb2 as connect_pb2
import grpc_lib.connect_pb2_grpc as connect_pb2_grpc

# Association table name and table structure
map_tables = {
    "SYSTEMCHAR": "TYPE CHAR(20) CONTEXT CHAR(30)",
    "SYSTEMINT": "TYPE CHAR(20) CONTEXT TINYINT(4)",
    "SYSTEFLOAT": "TYPE CHAR(20) CONTEXT FLOAT(8,2)",
}

# Association table name and table fields
map_table_field = {
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
    #'HOSTNAME': 'SYSTEMCHAR',
    #'IP': 'SYSTEMCHAR',
    #'GCARDNAME': 'SYSTEMCHAR',
    #'GCARDVER': 'SYSTEMCHAR',
    # Data Type Time
    #'UPTIME': 'SYSTEMTIME',
}


def update_all():
    """
    Description: Get infomation from pylib and update it to
    the database with grpc server.
    :return: None
    """
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
        #'GCARDVER': NVIDIA().get_driver_version(),
        # Data Type Time
        # 'UPTIME': SYSTEM().system_uptime(),
    }
    for data_type, table in map_table_field.items():
        if table == 'SYSTEMCHAR':
            sql.update_char(table=table, data_type=data_type, context=map_context[data_type])
        else:
            sql.update_num(table=table, data_type=data_type, context=map_context[data_type])


def update_all_grpc():
    """
    Description: Get infomation from pylib with grpc-server and update it to
    the database.
    :return: None
    """
    channel = grpc.insecure_channel('10.128.35.163:50051')
    stub = connect_pb2_grpc.SystemStub(channel)
    stubNV = connect_pb2_grpc.NVIDIAStub(channel)
    sql = SQL()
    map_context = {
        'CPUNUM': stub.cpu(connect_pb2.Request(name="num")).result,
        'CPULNUM': stub.cpu(connect_pb2.Request(name="Lnum")).result,
        'CPUPER': stub.cpu(connect_pb2.Request(name="per")).result,
        'MEMPER': stub.mem_per(connect_pb2.Request()).result,
        # Data Type float
        'MEMUSED': stub.mem(connect_pb2.Request(unit="GB", type="used")).result,
        'MEMFREE': stub.mem(connect_pb2.Request(unit="GB", type="free")).result,
        'MEMTOTAL': stub.mem(connect_pb2.Request(unit="GB", type="total")).result,
        'SWAPUSED': stub.swap(connect_pb2.Request(type="used")).result / 1024,
        'SWAPFREE': stub.swap(connect_pb2.Request(type="free")).result / 1024,
        'SWAPTOTAL': stub.swap(connect_pb2.Request(type="total")).result / 1024,
        'GCARDFREE': stubNV.mem(connect_pb2.Request(unit="GB", type="free")).result,
        'GCARDUSED': stubNV.mem(connect_pb2.Request(unit="GB", type="used")).result,
        'GCARDTOTAL': stubNV.mem(connect_pb2.Request(unit="GB", type="total")).result,
        'NETSEND': stub.net(connect_pb2.Request(type="send")).result,
        'NETRECV': stub.net(connect_pb2.Request(type="recv")).result,
        'NET_SENDPER': stub.net(connect_pb2.Request(type="send")).result / (
                               stub.net(connect_pb2.Request(type="send")).result
                               + stub.net(connect_pb2.Request(type="recv")).result),
        'NET_RECVPER': stub.net(connect_pb2.Request(type="recv")).result / (
                               stub.net(connect_pb2.Request(type="send")).result
                               + stub.net(connect_pb2.Request(type="recv")).result),
        # Data Type String
        #'HOSTNAME': SYSTEM.hostname,
        # 'IP': SYSTEM.NET().get_netcard(),
        # 'GCARDNAME': NVIDIA().get_card_info(),
        #'GCARDVER': NVIDIA().get_driver_version(),
        # Data Type Time
        # 'UPTIME': SYSTEM().system_uptime(),
    }
    for data_type, table in map_table_field.items():
        if table == 'SYSTEMCHAR':
            sql.update_char(table=table, data_type=data_type, context=map_context[data_type])
        else:
            sql.update_num(table=table, data_type=data_type, context=map_context[data_type])


def restore_db(db_name):
    """
    Description: restore the database
    :param db_name: database's name
    :return: None
    """
    db = SQL()
    # Step 1: Delete old db
    db.delete_db(db_name=db_name)
    # Step 2: Create new db
    db.create_db(db_name=db_name)
    # Step 3: Set the operation db to the new db
    db.change_db(db_name=db_name)
    # Step 4: Create tables
    for table, list_name in map_tables.items():
        db.create_table(table_name=table, list_name=list_name)
    # Step 5: Insert initial value into the tables
    for field, table in map_table_field.items():
        if table == "SYSTEMCHAR":
            db.insert(table=table, context="\"" + str(field) + "\" ," + "\'0\'")
        else:
            db.insert(table=table, context="\"" + str(field) + "\" ," + "0")
