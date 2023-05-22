import numpy as np



class EnvironmentalModel:

    def __init__(self):
        pass

    def _get_windspeed_func(self, time):
        '''
        @param time: the time in seconds
        @returns: a function f(x, y) that returns the current wind vector (in m/s) at the point (x, y)
        '''
        return lambda pos: np.array([
            1,
            1,
        ])

    def get_conditions(self, time):
        '''
        @param time: the time in seconds
        @returns: the environmental conditions at the given time as the following dictionary:
        {
            'wind': windspeed_func(pos): a function that returns the wind vector (in m/s) at the point pos=np.array([x, y])
        }
        '''
        return {
            'wind': self._get_windspeed_func(time),
        }