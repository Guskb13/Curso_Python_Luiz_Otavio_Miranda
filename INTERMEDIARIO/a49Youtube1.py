import time

# TODO create the mission_timer decorator and decorate both functions

def mission_timer(base_fn):
    def enhanced_fn():
        start_time = time.time()
        print('3...')
        print('2...')
        print('1...')
        base_fn()
        end_time = time.time()
        print(f"Mission duration: {end_time - start_time} seconds\n")
        
    return enhanced_fn    


@mission_timer
def launch_probe():
    print("Launching probe...")
    time.sleep(1)

@mission_timer
def deploy_satellite():
    print("Deploying satellite...")
    time.sleep(2)


launch_probe()

deploy_satellite()





# Call both functions

