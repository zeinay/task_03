from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        'my_list' : [
            { 'restaurant_name' : 'Zeinayus',
              'food_type' : 'Sea Food'
            },
            {'restaurant_name' : 'resto',
             'food_type' : 'vegi Food'
            }
        ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):
    context = { 'my_object' : {
    		'restaurant_name' : 'Zeinayus',
            'food_type' : 'Sea Food'
    		}
    }
    return render(request, 'detail.html', context)
