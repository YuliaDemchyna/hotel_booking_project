from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel, Room, Booking
from django.urls import reverse
from datetime import datetime
from django.utils import timezone
from django.http import HttpRequest, HttpResponse


def home_page_view(request: HttpRequest) -> HttpResponse:
    hotels = Hotel.objects.all()
    return render(request, 'booking/home.html', {'hotels': hotels})


def hotel_detail_view(request: HttpRequest, hotel_id: int) -> HttpResponse:
    hotel = get_object_or_404(Hotel, id=hotel_id)
    rooms = hotel.rooms.filter(is_active=True)
    return render(request, 'booking/hotel.html', {'hotel': hotel, 'rooms': rooms})


def booking_page_view(request: HttpRequest, hotel_id: int, room_id: int) -> HttpResponse:
    hotel = get_object_or_404(Hotel, id=hotel_id)
    room = get_object_or_404(Room, id=room_id, hotel=hotel)

    if request.method == 'POST':
        check_in = request.POST.get('check_in_date')
        check_out = request.POST.get('check_out_date')
        guest_name = request.POST.get('guest_name')
        guest_email = request.POST.get('guest_email')
        guest_phone = request.POST.get('guest_phone')

        try:
            check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()
            check_out_date = datetime.strptime(check_out, '%Y-%m-%d').date()
            if check_in_date >= check_out_date:
                raise ValueError("Check-out date must be after check-in date.")
            if check_in_date < timezone.now().date():
                raise ValueError("Check-in date cannot be in the past.")
        except ValueError as e:
            error = str(e)
            return render(request, 'booking/booking.html', {
                'hotel': hotel,
                'room': room,
                'error': error
            })

        overlapping_bookings = Booking.objects.filter(
            room=room,
            check_in_date__lt=check_out_date,
            check_out_date__gt=check_in_date,
            status='CONFIRMED'
        )

        if overlapping_bookings.exists():
            error = "The room is not available for the selected dates."
            return render(request, 'booking/booking.html', {
                'hotel': hotel,
                'room': room,
                'error': error
            })

        booking = Booking.objects.create(
            room=room,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            guest_name=guest_name,
            guest_email=guest_email,
            guest_phone=guest_phone,
            status='CONFIRMED'
        )

        return redirect(reverse('booking:confirmation', args=[booking.id]))

    return render(request, 'booking/booking.html', {'hotel': hotel, 'room': room})


def confirmation_page_view(request: HttpRequest, booking_id: int) -> HttpResponse:
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking/confirmation.html', {'booking': booking})
