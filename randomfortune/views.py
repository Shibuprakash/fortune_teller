import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
fortuneList = [ "A beautiful, smart, and loving person will be coming into your life.",
  "Your hard work will soon pay off in unexpected ways.",
  "Happiness is around the corner—keep moving forward.",
  "An exciting opportunity lies ahead; seize it with confidence.",
  "Success is a journey, not a destination. Keep going!",
  "You will soon receive good news that will bring joy.",
  "Trust yourself; your intuition is guiding you well.",
  "A great adventure awaits—be ready for new experiences.",
  "Unexpected kindness will come your way today.",
  "You are capable of achieving great things. Believe in yourself!" ]



def fortune(request):
    fortune = random.choice(fortuneList)
    context = {"TodaysFortune" : fortune, "Firstname" : "Shibu"}
    return render(request, "randomfortune/fortune.html",context)