from django.shortcuts import render

def business_card(request):
    user = {
        'name': 'Rajagokila',
        'title': 'Python Fullstack Developer',
        'email': 'rajagokila@example.com',
        'phone': '+91-9876543210',
        'location': 'Chennai, India',
    }
    return render(request, 'profiles/business_card.html', {'user': user})
