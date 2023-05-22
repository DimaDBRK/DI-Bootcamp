from pyowm.owm import OWM
owm = OWM('your-api-key')
reg = owm.city_id_registry()
list_of_geopoints = reg.geopoints_for('Rome', matching='exact')