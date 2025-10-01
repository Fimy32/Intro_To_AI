from Backwards_Chaining.backwards_classes import *

while True:
    Weather = Database([Query(False,"Is it rainy?","Y"),Query(True,"Is it bright","Y"),Query(True,"Is it yellow?","Y"),Query(False,"Is it tornadoey?","Y")],"Sunny")
    #for i in range(4):
        #Weather.add_query()
    Weather.calculate_likelihood()
    #Weather.expert_system()
    Weather.statistic_system()
    print("\n"*3)