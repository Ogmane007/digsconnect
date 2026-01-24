from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .decorators import landlord_required
from .forms import StudentRegisterForm, PropertyForm, InquiryForm
from .models import Property, PropertyImage, Inquiry




from .forms import StudentRegisterForm, PropertyForm
from .models import Property


def home(request):
    properties = Property.objects.all()
    return render(request, 'properties/home.html', {'properties': properties})  

def search(request):
    q = request.GET.get('q', '').strip()
    min_price = request.GET.get('min_price', '').strip()
    max_price = request.GET.get('max_price', '').strip()
    sort = request.GET.get('sort', 'newest').strip()

    properties = Property.objects.all()

    if q:
        properties = properties.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q) |
            Q(address__icontains=q)
        )

    # Price filtering (safe parsing)
    try:
        if min_price:
            properties = properties.filter(price__gte=float(min_price))
    except ValueError:
        pass

    try:
        if max_price:
            properties = properties.filter(price__lte=float(max_price))
    except ValueError:
        pass

    # Sorting
    if sort == 'price_asc':
        properties = properties.order_by('price')
    elif sort == 'price_desc':
        properties = properties.order_by('-price')
    else:
        properties = properties.order_by('-created_at')  # newest

    context = {
        'properties': properties,
        'q': q,
        'min_price': min_price,
        'max_price': max_price,
        'sort': sort,
    }
    return render(request, 'properties/search.html', context)

def property_detail(request, property_id):
    prop = get_object_or_404(Property, id=property_id)
    return render(request, 'properties/property_detail.html', {'property': prop})





def register(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = StudentRegisterForm()

    return render(request, 'properties/register.html', {'form': form})

@login_required
@landlord_required
def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            prop = form.save(commit=False)
            prop.landlord = request.user
            prop.save()
            return redirect('home')
    else:
        form = PropertyForm()

    return render(request, 'properties/create_property.html', {'form': form})

@login_required
@landlord_required
def dashboard(request):
    my_properties = Property.objects.filter(landlord=request.user).order_by('-created_at')
    return render(request, 'properties/dashboard.html', {'properties': my_properties})


@login_required
@landlord_required
def edit_property(request, property_id):
    prop = get_object_or_404(Property, id=property_id, landlord=request.user)

    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=prop)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PropertyForm(instance=prop)

    return render(request, 'properties/edit_property.html', {'form': form, 'property': prop})


@login_required
@landlord_required
def delete_property(request, property_id):
    prop = get_object_or_404(Property, id=property_id, landlord=request.user)

    if request.method == 'POST':
        prop.delete()
        return redirect('dashboard')

    return render(request, 'properties/delete_property.html', {'property': prop})

@login_required
@landlord_required
def add_property_images(request, property_id):
    prop = get_object_or_404(Property, id=property_id, landlord=request.user)

    if request.method == 'POST':
        images = request.FILES.getlist('images')
        for image in images:
            PropertyImage.objects.create(property=prop, image=image)
        return redirect('dashboard')

    return render(
        request,
        'properties/add_property_images.html',
        {'property': prop}
    )

@login_required
def submit_inquiry(request, property_id):
    prop = get_object_or_404(Property, id=property_id)

    # Only students can inquire, and not on their own listing
    if request.user.userprofile.user_type != 'student' or prop.landlord == request.user:
        return redirect('property_detail', property_id=prop.id)

    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.property = prop
            inquiry.student = request.user
            inquiry.save()
            return redirect('property_detail', property_id=prop.id)
    else:
        form = InquiryForm()

    return render(request, 'properties/submit_inquiry.html', {'form': form, 'property': prop})


@login_required
@landlord_required
def manage_inquiries(request):
    inquiries = Inquiry.objects.filter(property__landlord=request.user).order_by('-created_at')
    return render(request, 'properties/manage_inquiries.html', {'inquiries': inquiries})

