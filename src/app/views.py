import asyncio
from django.shortcuts import render


async def index_view(request):
    return render(
        request,
        "app/index.html",
        {}
    )