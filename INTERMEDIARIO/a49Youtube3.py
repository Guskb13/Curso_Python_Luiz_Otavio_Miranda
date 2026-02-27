import time

# TODO create the mission_timer decorator and decorate both functions

def mission_timer(base_fn):
    def enhanced_fn(*args, **kwargs):
        start_time = time.time()
        for i in range(3, 0 , -1):
            print(f'{i}...')
        result = base_fn(*args, **kwargs) 
        end_time = time.time()
        print(f'Mission duration {end_time - start_time} seconds', end = '\n\n')
        
        return result
        
    return enhanced_fn    

@mission_timer
def launch_probe(target):
    print(f'Launching probe towards {target}...')
    time.sleep(1)
    return f"Probe successfully en route to {target}."

@mission_timer
def deploy_satellite(orbit_type, altitude_km):
    print(f'Deploying satellite into {orbit_type} orbit at {altitude_km} km...')
    time.sleep(2)

deploy_satellite("polar", 800)

result = launch_probe("Europa")
print("Stored mission result:", result)

# Call both functions

