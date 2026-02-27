import time

# TODO create the mission_timer decorator and decorate both functions

def mission_timer(base_fn):
    def enhanced_fn(*args, **kwargs):
        start_time = time.time()
        print('3...')
        print('2...')
        print('1...')
        base_fn(*args, **kwargs)
        end_time = time.time()
        print(f'Mission duration {end_time - start_time} seconds', end= '\n\n')    
    return enhanced_fn    

@mission_timer
def launch_probe(target):
    print(f'Launching probe towards {target}...')
    time.sleep(1)

@mission_timer
def deploy_satellite(orbit_type, altitude_km):
    print(f'Deploying satellite into {orbit_type} orbit at {altitude_km} km...')
    time.sleep(2)

target = 'Mars'

orbit_type = 'geostationary'
altitude_km = '35786'

launch_probe(target)

deploy_satellite('polar', '800')

deploy_satellite(orbit_type, altitude_km)





# Call both functions

