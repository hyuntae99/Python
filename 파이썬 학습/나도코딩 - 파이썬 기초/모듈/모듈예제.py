# import theater_module
# theater_module.price(3)
# theater_module.price_soldier(2)
# theater_module.price_morning(3)

# import theater_module as mv
# mv.price(3)
# mv.price_soldier(2)
# mv.price_morning(3)

# from theater_module import *
# price(3)
# price_soldier(2)
# price_morning(3)

# from theater_module import price, price_soldier
# price(3)
# price_soldier(2)
# price_morning(3) # 사용 불가

from theater_module import price_soldier as s
s(2)