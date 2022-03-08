# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()


# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()
 
 
# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()



# from travel import * #travel은 파일로 여러개의 모듈이 존재해서 범위를 설정해야함
# trip_to1 = vietnam.VietnamPackage()
# trip_to1.detail()
# trip_to2 = thailand.ThailandPackage()
# trip_to2.detail()

import inspect
import random
from travel import *

print(inspect.getfile(random)) #위치파악
print(inspect.getfile(thailand))