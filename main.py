from headend import update_all_grpc
import time
if __name__ == '__main__':
    while(1):
        update_all_grpc()
        time.sleep(1)
