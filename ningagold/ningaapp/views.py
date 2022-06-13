from django.shortcuts import redirect, render 
import random
from datetime import datetime
def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
        request.session['acti'] = 0
    return render(request,'index.html')

def check(request):
    g = 0
    if request.method == 'POST':
        if request.POST['tye'] == 'farm':
            #['tye'] is the name ,and 'farm' is the vaule in line 48 in index.HTML
            g = random.randint(1, 20)
            request.session['acti'] =f"You entered a farm and earned {g} Gold. ({datetime.now().strftime('%B %d, %Y %H:%M:%S %p')})" 
        elif request.POST['tye'] == 'cave':
            g = random.randint(1, 20)
            request.session['acti'] =f"You entered a cave and earned {g} Gold. ({datetime.now().strftime('%B %d, %Y %H:%M:%S %p')})"
        elif request.POST['tye'] == 'house':
            g = random.randint(1, 20)
            request.session['acti'] =f"You entered a house and earned {g} Gold. ({datetime.now().strftime('%B %d, %Y %H:%M:%S %p')})"
        elif request.POST['tye'] == 'quest':
            g = random.randint(-50, 50)
            if g < 0:
                request.session['acti'] =f"You completed a quest and lost {g} Golds. ({datetime.now().strftime('%B %d, %Y %H:%M:%S %p')})"
            elif g > 0:
                request.session['acti'] =f"You falied a quest and earned {g} Golds. ({datetime.now().strftime('%B %d, %Y %H:%M:%S %p')})"
    request.session['gold'] += g
    return redirect ('/')
