# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from django.db.models import Avg

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from ratings import models
from ratings.models import Ratings


@csrf_exempt
def index(request):

    if request.method == "POST":
        selected_movie = request.POST.get("Movies")
        rating = request.POST.get("star")
        r = Ratings(movie_name=selected_movie, ratings=rating)
        r.save()
        avg_rating = Ratings.objects.filter(movie_name=selected_movie).aggregate(Avg('ratings'))


    if request.method == "GET":
        avg_rating = ""

    text = "<body style=background-color:white;><h1>Hello, world. Welcome to the Movie Ratings Page</h1>" \
           "<!DOCTYPE html>" \
           "<html>" \
           "<body>" \
           "<p><b>List of Movies </b></p>" \
           "<form action='/ratings/' method='POST'>" \
           "<select name='Movies'>" \
           "<option value='baasha'>Baasha</option>" \
           "<option value='padayappa'>Padayappa</option>" \
           "<option value='enthiran'>Enthiran</option>" \
           "<option value='darbar'>Darbar</option>" \
           "</select>" \
           "<br><br>" \
           "<p><b>User Rating</b><p>" \
           "<div class='rating'>" \
           "<input id='star5' name='star' type='radio' value='5' class='radio-btn hide' />" \
           "<label for='star5'' >☆</label>" \
           "<input id='star4' name='star' type='radio' value='4' class='radio-btn hide' />" \
           "<label for='star4' >☆</label>" \
           "<input id='star3' name='star' type='radio' value='3' class='radio-btn hide' />" \
           "<label for='star3' >☆</label>" \
           "<input id='star2' name='star' type='radio' value='2' class='radio-btn hide' />" \
           "<label for='star2' >☆</label>" \
           "<input id='star1' name='star' type='radio' value='1' class='radio-btn hide' />" \
           "<label for='star1' >☆</label>" \
           "</div>" \
           "</div>" \
           "<style>" \
           ".txt-center {" \
           "text-align: center;" \
           "}" \
           ".hide {" \
           "display: none;" \
           "}" \
           ".clear {" \
           "float: none;" \
           "clear: both;" \
           "}" \
           ".rating {" \
           "width: 90px;" \
           "unicode-bidi: bidi-override;" \
           "direction: rtl;" \
           "text-align: center;" \
           "position: relative;" \
           "}" \
           ".rating > label {" \
           "float: right;" \
           "display: inline;" \
           "padding: 0;" \
           "margin: 0;" \
           "position: relative;" \
           "width: 1.1em;" \
           "cursor: pointer;" \
           "color: #000;" \
           "}" \
           ".rating > label:hover," \
           ".rating > label:hover ~ label," \
           ".rating > input.radio-btn:checked ~ label {" \
           "color: yellow;" \
           "}" \
           ".rating > label:hover:before," \
           ".rating > label:hover ~ label:before," \
           ".rating > input.radio-btn:checked ~ label:before," \
           ".rating > input.radio-btn:checked ~ label:before {" \
           "position: absolute;" \
           "left: 0;" \
           "color: yellow;" \
           "}" \
           "</style>" \
           "<br>" \
           "</br>" \
           "<p><b>Avg Rating </b></p>" \
           +str(avg_rating)+ \
           "<br></br>" \
           "<input type='submit'>" \
           "</form>" \
           "</body>" \
           "</html>"


    return HttpResponse(text)