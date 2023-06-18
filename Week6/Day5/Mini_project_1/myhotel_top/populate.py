import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myhotel.settings")
import django
django.setup()
from visitors.models import Booking, Room
from datetime import datetime, timedelta
from faker import Faker
import random
from django.core.exceptions import ValidationError

def bookings(qty):
    BOOKINGS_TOTAL = qty
    MAX_PERIOD = 14
    
    while BOOKINGS_TOTAL > 0:
       
        fake = Faker()
        tomorrow = datetime.now() + timedelta(1)
        check_in = fake.date_between(start_date=tomorrow, end_date=tomorrow + timedelta(365))
        check_out = check_in + timedelta(random.randint(1, MAX_PERIOD))
        room = random.choice(Room.objects.all())
        # booking_list = Booking.objects.select_related('room').filter(room=room.id)

        booking = Booking(
            guest=fake.name(),
            check_in=check_in,
            check_out=check_out,
            guests_num=random.randint(1, 4),
            room=room,
        )

        try:
            booking.save()
        except ValidationError:
            continue
        else:
            BOOKINGS_TOTAL -= 1
            

def rooms(qty):
    ROOMS_TOTAL = qty

    for i in range(1, ROOMS_TOTAL+1):   
        # Room.objects.all().delete()
        # quit()
        room_type_name = random.choice(Room.RoomType.names)
        room_type = Room.RoomType[room_type_name]

        room = Room(
            room_type=room_type,
            price=int(room_type * 200),
            room_number=i,
        )
        room.save()


# driver

# bookings(100)
# rooms(200)