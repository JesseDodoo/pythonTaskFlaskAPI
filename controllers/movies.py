import asyncio
from urllib import request
import requests
from flask import Flask, request, jsonify




async def get_all_movies():
    apikey = '99c279daee064cd2fda3ce485439cd81'
    search =  requests.get(f'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key={apikey}&page=1')
    data = search.json()
    print(data)

    return data['results']


async def get_by_name(movie_name):
    apikey = '99c279daee064cd2fda3ce485439cd81'
    search =  requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={apikey}&language=en-US&query={movie_name}&page=1&include_adult=false')
    data = search.json()
    print(data)

    return data['results']

