from Sensors import *
from Utility import *

sendDatas = False


############################################################

def get_prepared_value(sensor, value_type):
    return value_type + ":" + sensor.get_value(value_type) + ";"


############################################################

def start():
    sendDatas = True
    ssh_thread = threading.Thread(target=__sending_datas(), args=())
    Utility.threads.append(ssh_thread)
    ssh_thread.start()


############################################################

def __sending_datas():
    while sendDatas:
        output = "datas:"
        output += get_prepared_value(gyro_sensor, ValueTypes.gyro_angle.value)
        output += get_prepared_value(gyro_sensor, ValueTypes.gyro_angle_smooth.value)
        #################################
        output += get_prepared_value(ir_seeker, ValueTypes.ir_direction.value)
        output += get_prepared_value(ir_seeker, ValueTypes.ir_direction_smooth.value)
        output += get_prepared_value(ir_seeker, ValueTypes.ir_angle.value)
        output += get_prepared_value(ir_seeker, ValueTypes.ir_angle_smooth.value)
        output += get_prepared_value(ir_seeker, ValueTypes.ir_distance.value)
        output += get_prepared_value(ir_seeker, ValueTypes.ir_distance_smooth.value)
        #################################
        output += get_prepared_value(color_sensor, ValueTypes.color.value)
        output += get_prepared_value(color_sensor, ValueTypes.reflect.value)
        output += get_prepared_value(color_sensor, ValueTypes.ambiente.value)
        print(output)
        sleep(0.5)
