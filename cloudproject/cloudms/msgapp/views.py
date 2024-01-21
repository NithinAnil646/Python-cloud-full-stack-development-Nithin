# msgapp/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import Message

def message_board(request):
    return render(request, 'msgapp/message_board.html')

def submit_message(request):
    # Logic to save the submitted message to the database (you need to create the Message model)
    sender = request.POST.get('sender')
    receiver = request.POST.get('receiver')
    message_content = request.POST.get('message')

    # Save the message to the database
    message = Message.objects.create(sender=sender, receiver=receiver, content=message_content)
    
    return JsonResponse({'status': 'success'})

def get_messages(request):
    # Logic to retrieve the latest 20 messages for a specific receiver from the database
    receiver_name = request.POST.get('get_receiver')
    messages = Message.objects.filter(receiver=receiver_name).order_by('-timestamp')[:20]

    # Return the messages as JSON
    messages_data = [{'source': msg.sender, 'time': msg.timestamp, 'content': msg.content} for msg in messages]
    return JsonResponse({'messages': messages_data})
