import asyncio
from django.shortcuts import render


async def index_view(request):
    return render(
        request,
        "chat/index.html",
        {}
    )
    
async def room_view(request, room_name):
    return render(
        request,
        "chat/room.html",
        {
            "room_name": room_name
        }
    )