from rx import Observer, Observable


class TemperatureObserver(Observer):

    def on_next(self, x):
        print('Temperature is: %s degrees centigrade' % x)
        if x > 6:
            print('Warning: Temperature is exceeding recomended limit')
        if x == 9:
            print('Datacenter is shutting down. Temperature is too high')

    def on_error(self, error):
        print('Error: %s' % error)

    def on_completed(self):
        print('All temps read')


observ = Observable.from_iterable(range(10))

subscr = observ.subscribe(TemperatureObserver())
