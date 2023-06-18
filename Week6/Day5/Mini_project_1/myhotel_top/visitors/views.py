from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

from django.views import generic
from .models import Booking, Room, Message
from .forms import BookingForm, FilterForm, ContactForm
from django.core.exceptions import ValidationError

# Create your views here.



class HomePageView(generic.ListView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['title'] = "Hotel Torquay | Homepage"
        return context

    def get_queryset(self):
        return None


class InfoPageView(generic.ListView):
    template_name = 'info.html'

    def get_context_data(self, **kwargs):
        context = super(InfoPageView, self).get_context_data(**kwargs)
        context['title'] = "Hotel Booking Website"
        return context

    def get_queryset(self):
        return None


class RoomsView(generic.ListView):
    template_name = 'booking.html'
    context_object_name = 'rooms'
    paginate_by = 10
    model = Room
    queryset = model.objects.all()
    paginator = Paginator(queryset, paginate_by)
    form_class = FilterForm

    def get_context_data(self, **kwargs):
        context = super(RoomsView, self).get_context_data(**kwargs)
        context['title'] = "Booking"
        context['form'] = FilterForm
        context['total_rooms'] = len(self.paginator.object_list)
        return context

    def post(self, request):
        form = FilterForm(data=request.POST)
        self.object_list = self.get_queryset()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        for field, items in form.errors.items():
            for item in items:
                messages.error(self.request, item)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

    def get_queryset(self, *args, **kwargs):
        if 'room' in kwargs:
            room = kwargs['room']
            return self.model.objects.filter(id=room.id)
        return self.model.objects.all()

    # booking adding form
    def form_valid(self, form):
        data = form.cleaned_data

        check_in = data['check_in']
        check_out = data['check_out']
        guests_num = data['guests_num']

        booking = Booking(
            guest='Check',
            check_in=check_in,
            check_out=check_out,
            guests_num=guests_num
        )

        context = self.get_context_data()

        try:
            booking.full_clean()
        except ValidationError as e:
            print(e.message_dict)
        else:
            context['rooms'] = (booking.room,)

        return render(request=self.request, template_name=self.template_name, context=context)


class OrderView(generic.DetailView):
    template_name = 'order.html'
    context_object_name = 'room'
    model = Room
    form_class = BookingForm

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context['title'] = "Order"
        context['form'] = BookingForm
        return context

    def post(self, request, pk):
        form = BookingForm(data=request.POST)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        for field, items in form.errors.items():
            for item in items:
                messages.error(self.request, item)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.filter(id=self.kwargs['pk'])

    def form_valid(self, form):
        data = form.cleaned_data

        guests_name = data['guest']
        check_in = data['check_in']
        check_out = data['check_out']
        guests_num = data['guests_num']

        booking = Booking(
            guest=guests_name,
            check_in=check_in,
            check_out=check_out,
            guests_num=guests_num
        )
        try:
            booking.full_clean()
        except ValidationError as e:
            print(e.message_dict)
        else:
            booking.save()
            messages.success(self.request, "Your booking was processed successfully")

        return redirect('home')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            message = Message(
                name=name,
                email=email,
                message=message
            )
            message.save()

            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})