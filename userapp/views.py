import requests
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.permissions import AllowAny

from userapp.forms import DestinationForm
from userapp.models import Destination
from userapp.serializers import TourismSerializers


# Create your views here.

class DestinationCreateview(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = TourismSerializers
    permission_classes = [AllowAny]


class DestinationDetail(generics.RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = TourismSerializers


class DestinationUpdateview(generics.RetrieveUpdateAPIView):
    queryset = Destination.objects.all()
    serializer_class = TourismSerializers


class DestinationDelete(generics.DestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = TourismSerializers


def home(request):
    api_url = 'http://127.0.0.1:8000/create/'
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            original_data = data

            paginator = Paginator(original_data, 3)
            try:
                page = int(request.GET.get('page', 1))
            except:
                page = 1
            try:
                destinations = paginator.page(page)
            except(EmptyPage, InvalidPage):
                destinations = Paginator.page(paginator.num_pages)
            context = {
                'original_data': original_data,
                'destinations': destinations,
                'page': page,
            }
            return render(request, 'tourist_dest/home.html', context)

        else:
            return render(request, 'tourist_dest/home.html', {'error_message': f'error:{response.status_code}'})

    except requests.RequestException as e:
        return render(request, 'tourist_dest/home.html', {'error_message': f'error:{str(e)}'})


def create_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                api_url = 'http://127.0.0.1:8000/create/'
                data = form.cleaned_data
                print(data)

                response = requests.post(api_url, data=data, files={'dest_image': request.FILES['dest_image']})
                if response.status_code == 400:
                    messages.success(request, f'Destination added successfully')
                    return redirect('/')
                else:
                    messages.error(request, f'Error{response.status_code}')
            except requests.RequestException as e:
                messages.error(request, f'Error during API request {str(e)}')
        else:
            messages.error(request, 'form is invalid')
    else:
        form = DestinationForm()
    return render(request, 'tourist_dest/create_destination.html', {'form': form})


def destination(request):
    api_url = 'http://127.0.0.1:8000/create/'
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            original_data = data

            paginator = Paginator(original_data, 3)
            try:
                page = int(request.GET.get('page', 1))
            except:
                page = 1
            try:
                destinations = paginator.page(page)
            except(EmptyPage, InvalidPage):
                destinations = Paginator.page(paginator.num_pages)
            context = {
                'original_data': original_data,
                'destinations': destinations,
                'page': page,
            }
            return render(request, 'tourist_dest/destination.html', context)

        else:
            return render(request, 'tourist_dest/destination.html', {'error_message': f'error:{response.status_code}'})

    except requests.RequestException as e:
        return render(request, 'tourist_dest/destination.html', {'error_message': f'error:{str(e)}'})


def destdetail(request, destination_id):
    api_url = f'http://127.0.0.1:8000/detail/{destination_id}/'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        original_data = data
    return render(request, 'tourist_dest/destdetail.html', {'destination': original_data})


def update_detail(request, destination_id):
    api_url = f'http://127.0.0.1:8000/detail/{destination_id}/'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        original_data = data
    return render(request, 'tourist_dest/update.html', {'data': original_data})


def update_destination(request, destination_id):
    if request.method == 'POST':
        api_url = f'http://127.0.0.1:8000/update/{destination_id}/'



        data = {
            'placename': request.POST.get('placename'),
            'weather': request.POST.get('weather'),
            'district': request.POST.get('district'),
            'state': request.POST.get('state'),
            'google_map_link': request.POST.get('google_map_link'),
            'description': request.POST.get('description')
        }

        files = {'dest_image': request.FILES.get('dest_image')}
        response = requests.put(api_url, data=data, files=files)

        if response.status_code == 200:
            messages.success(request, 'Destination updated successfully')
            return redirect('/')
        else:
            messages.error(request, f'error submitting data to the REST API:{response.status_code}')
    return render(request, 'tourist_dest/update.html')

def destination_delete(request, destination_id):
    api_url = f'http://127.0.0.1:8000/delete/{destination_id}'
    response = requests.delete(api_url)

    if response.status_code == 200:
        print(f'Item with id {destination_id} has been deleted')

    else:
        print(f'Failed to delete item status code {response.status_code}')
    return redirect('/')
