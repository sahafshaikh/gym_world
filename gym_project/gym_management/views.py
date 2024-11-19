from django.shortcuts import render
from .models import Member, Trainer, GymClass

def home(request):
    class_count = GymClass.objects.count()  # Fixed: added 'objects'
    member_count = Member.objects.count()
    trainer_count = Trainer.objects.count()
    
    context = {
        'class_count': class_count,
        'member_count': member_count,
        'trainer_count': trainer_count,
    }
    return render(request, 'gym_management/home.html', context)