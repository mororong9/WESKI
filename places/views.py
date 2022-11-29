from .forms import PlaceForm
from .models import Place
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    places = Place.objects.order_by("-pk")
    context = {
        "places": places,
    }

    return render(request, "places/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        places_form = PlaceForm(request.POST, request.FILES)
        if places_form.is_valid():
            place = places_form.save(commit=False)
            place.user = request.user
            place.save()
            return redirect("places:index")
    else:
        place_form = PlaceForm()
    context = {
        "place_form": place_form,
    }
    return render(request, "places/create.html", context=context)


def detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    context = {
        "place": place,
    }
    return render(request, "places/detail.html", context)


@login_required
def update(request, pk):
    place = get_object_or_404(Place, pk=pk)
    # if request.user == place.user:
    if request.method == "POST":
        place_form = PlaceForm(request.POST, request.FILES, instance=place)
        if place_form.is_valid():
            place = place_form.save(commit=False)
            place.save()
            return redirect("places:detail", place.pk)
    else:
        place_form = PlaceForm(instance=place)
    context = {
        "place_form": place_form,
    }
    return render(request, "places/update.html", context)


@login_required
def delete(request, pk):
    place = Place.objects.get(pk=pk)
    place.delete()
    return redirect("places:index")


@login_required
def like(request, pk):
    print(request.POST)
    if request.user.is_authenticated:
        place = Place.objects.get(pk=pk)
        if place.like_users.filter(pk=request.user.pk).exists():
            place.like_users.remove(request.user)
            is_liked = False
        else:
            place.like_users.add(request.user)
            is_liked = True
    else:
        return redirect("places:detail", pk)
    return JsonResponse(
        {
            "is_liked": is_liked,
            "like_count": place.like_users.count(),
        }
    )
