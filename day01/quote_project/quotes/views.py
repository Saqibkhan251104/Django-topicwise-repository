from django.shortcuts import render
import random 

quotes_list = [
      "The only way to do great work is to love what you do. – Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "The best way to predict the future is to create it. – Abraham Lincoln",
    "You are never too old to set another goal or to dream a new dream. – C.S. Lewis"
]

def home(request):
    random_quote = random.choice(quotes_list)
    return render(request, 'quotes/home.html', {'quote' :random_quote})

def about(request):
    return render(request, 'quotes/about.html')