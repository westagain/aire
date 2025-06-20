import requests
from django.shortcuts import render
from collections import OrderedDict

OPENLIB_URL = 'https://openlibrary.org/api/books'

def fetch_book_data(olid):
    params = {
        'bibkeys': f'OLID:{olid}',
        'format': 'json',
        'jscmd': 'data',
    }
    resp = requests.get(OPENLIB_URL, params=params)
    data = resp.json().get(f'OLID:{olid}', {})
    return {
        'title': data.get('title', 'Unknown Title'),
        'cover': data.get('cover', {}).get('medium', ''),
        'pages': data.get('number_of_pages'),
    }

def home(request):
    # 15 “Reading AIRE’s Choice” OLIDs
    aire_choice_ids = [
        'OL24382006M','OL37027463M','OL3700132M','OL26491060M','OL49340160M',
        'OL3301586M','OL6089177M','OL32062395M','OL9228706M','OL7881774M',
        'OL7261842M','OL14448179M','OL8978383M','OL6178260M','OL13993207M',
    ]
    # split into 3 pages of 5
    aire_choice_pages = [
        [fetch_book_data(olid) for olid in aire_choice_ids[i*5:(i+1)*5]]
        for i in range(3)
    ]

    # Recommendations by genre (contemporary choices)
    recs = OrderedDict([
        ('Biographies', [
            'OL27242580M',  # Becoming
            'OL3111516M',   # Steve Jobs
            'OL103902M',    # Long Walk to Freedom
            'OL4397425M',   # Educated
            'OL21206126M',  # Born a Crime
        ]),
        ('Military History', [
            'OL26331938M',  # The Rise and Fall of the Third Reich
            'OL3230257M',   # The Guns of August
            'OL23371494M',  # Band of Brothers
            'OL7549969M',   # The Second World War
            'OL13948158M',  # The Vietnam War
        ]),
        ('Business', [
            'OL35498M',      # Good to Great
            'OL14025995M',   # Zero to One
            'OL14174756M',   # The Lean Startup
            'OL16305M',      # Outliers
            'OL24537887M',   # Start with Why
        ]),
    ])
    recs_pages = [
        {'genre': genre, 'books': [fetch_book_data(olid) for olid in ids]}
        for genre, ids in recs.items()
    ]

    return render(request, 'books/index.html', {
        'aire_choice_pages': aire_choice_pages,
        'recs_pages': recs_pages,
    })
