from django.shortcuts import render
from . import models
from random import randint
from django.http import JsonResponse
from django.db.models import Count
import requests
import json

# Create your views here.
def index(request):
    context = {}
    # Get all known tags
    # Select 5 for questions
    all_tags = list(models.Tag.objects.all())
    # Select 5 for questions
    rand_selection = []
    for i in range(0,5):
        rand_selection.append(randint(0,len(all_tags)-1))
    context['question_tags'] = []
    context['image_url'] = {}
    for i in range(0,5):
        context['question_tags'].append(all_tags[rand_selection[i]])
        tags = [str(all_tags[rand_selection[i]]), 'greyscale']
        tag_string = ','.join(tags)
        payload = {'api_key': '63c1470d6730c8c27c06176060489644','tags':tag_string,'tag_mode':'any','media':'photos','format':'json','method':'flickr.photos.search'}
        res = requests.get('https://api.flickr.com/services/rest/?',params=payload)
        photo = res.text
        photo = photo[photo.index('{'):len(photo)-1]
        photo = json.loads(photo)
        photo = photo['photos']['photo'][0]
        farm_id = str(photo['farm'])
        server_id = str(photo['server'])
        id = str(photo['id'])
        secret = str(photo['secret'])
        image_url = 'https://farm' + farm_id + '.staticflickr.com/' + server_id + '/' + id + '_' + secret + '.jpg'
        print(image_url)
        context['image_url'][str(all_tags[rand_selection[i]].id)] = image_url 
    return render(request, 'app/index.html', context)

def get_activities(request):
    context = {}
    #get no list from request
    no_list = request.GET.get("no_list","")
    yes_list = request.GET.get("yes_list","")

    no_list = no_list.split(',')
    yes_list = yes_list.split(',')
    if no_list[0] == '':
        no_list = [1,2]
    if yes_list[0] == '':
        yes_list = [3,4]
    print(no_list)

    all_act_tags = models.ActivityTag.objects.all()
    acts_to_exclude = all_act_tags.filter(tag_id__in=no_list)
    act_ids_to_exclude = []
    for act in acts_to_exclude:
        act_ids_to_exclude.append(act.activity_id.id)

    acts_to_prefer = models.ActivityTag.objects.filter(tag_id__in=yes_list)
    act_ids_to_prefer = []
    for act in acts_to_prefer:
        act_ids_to_prefer.append(act.activity_id.id)

    act_ids_to_remove = set(act_ids_to_prefer).intersection(act_ids_to_exclude)
    print(str(act_ids_to_remove))
    act_ids_to_select = [i for i in act_ids_to_prefer if i not in act_ids_to_remove]
    print(str(act_ids_to_select))
    chosen_activity = None
    if (len(act_ids_to_select) == 0):
        chosen_activity = models.Activity.objects.exclude(id__in=act_ids_to_exclude)[0]
        print("0" + str(chosen_activity))
    elif (len(act_ids_to_select) == 1):
        chosen_activity = models.Activity.objects.filter(id__in=act_ids_to_select)[0]
        print("1" + str(chosen_activity))
    else:
        a = models.ActivityTag.objects.filter(activity_id__in=act_ids_to_select)
        a2 = a.filter(tag_id__in=yes_list)
        print(a)
        print(a2)
        b = a2.values('activity_id').annotate(total=Count('activity_id')).order_by('-total')
        print(b)
        chosen_activity = models.Activity.objects.get(id=b[0]['activity_id'])
    if (chosen_activity == None):
        chosen_activity.activity_desc = "Hmmm, iDunno doesn't know..."

    context['activity_id'] = chosen_activity.id
    context['activity_name'] = chosen_activity.activity_name
    context['search_term'] = chosen_activity.search_term
    context['activity_desc'] = chosen_activity.activity_desc
    context['places_term'] = chosen_activity.places_term
    return JsonResponse(context)


# Record selection
def record_selection(request):
    req = request.GET.get
    yes_string_list = req('yes_list').split(',')
    yes_string_list = models.Tag.objects.filter(id__in=yes_string_list)
    yes_string_list = [str(i) for i in yes_string_list]
    yes_string = ','.join(yes_string_list) 
    no_string_list = req('no_list').split(',')
    no_string_list = models.Tag.objects.filter(id__in=no_string_list)
    no_string_list = [str(i) for i in no_string_list]
    no_string = ','.join(no_string_list)
    decision = True if req('outcome') == '1' else False
    selection = models.UserSelection.objects.create(outcome=decision,suggested_activity_id=req('activity'),lat=req('lat'),lng=req('lng'),yes_list=yes_string,no_list=no_string)
    return JsonResponse({'status':'OK'})
