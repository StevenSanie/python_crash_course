def car_info(manufacturer, model, **args):
	args['manufacturer'] = manufacturer
	args['model'] = model
	return args
car = car_info('Mercedes', 'MIG34', color = 'black', quantity = 1 )
print(car)