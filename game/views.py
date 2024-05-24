from django.shortcuts import render,HttpResponse,redirect
from game.models import Room
from django.contrib import messages
def index(request):
    if request.method=='GET':
      return render(request,"index.html")
    elif request.method=='POST':
      print(request.POST)
      roomid = request.POST.get("room-id",None)
      playerName = request.POST.get("player-name","Unknown Player")
      if(roomid):
         try:
            room=Room.objects.get(id=roomid)
            return redirect(f"/game/{roomid}/{playerName}/")
         except Room.DoesNotExist:
            messages.error(request,"Room does not exist")
            return redirect("/")
            
      else:
         room =Room.objects.create()
         return redirect(f"/game/{room.id}/{playerName}/")
      
def game(request, id=None, name=None):
   try:
       room=Room.objects.get(id=id)
       return render (request,"game.html",{"room": room ,"name": name})
   except Room.DoesNotExist:
        messages.error(request,"Room does not exist.You idiot of Dev batalian(refrence of myself)")
        return redirect(f"/")
   