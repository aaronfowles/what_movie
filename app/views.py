from django.shortcuts import render
from . import models
from random import randint
from django.http import JsonResponse
from django.db.models import Count

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
    for i in range(0,5):
        context['question_tags'].append(all_tags[rand_selection[i]])
    return render(request, 'app/index.html', context)

def get_activities(request):
    context = {}
    #get no list from request
    no_list = request.GET.get("no_list","")
    yes_list = request.GET.get("yes_list","")

    no_list = no_list.split(',')
    yes_list = yes_list.split(',')

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
    
    act_ids_to_select = [i for i in act_ids_to_prefer if i not in act_ids_to_remove]
    chosen_activity = None
    if (len(act_ids_to_select) == 0):
        chosen_activity = models.Activity.objects.exclude(id__in=act_ids_to_exclude)[0]
    elif (len(act_ids_to_select) == 1):
        chosen_activity = models.Activity.objects.filter(id__in=act_ids_to_select)[0]
    else:
        a = models.ActivityTag.objects.exclude(tag_id__in=no_list)
        b = a.filter(tag_id__in=yes_list)
        c = b.values('activity_id').annotate(total=Count('activity_id')).order_by('activity_id')
        chosen_activity = models.Activity.objects.get(id=c[0]['activity_id'])
    if (chosen_activity == None):
        chosen_activity.activity_desc = "Hmmm, iDunno doesn't know..."

    context['activity_id'] = chosen_activity.id
    context['activity_name'] = chosen_activity.activity_name
    context['search_term'] = chosen_activity.search_term
    context['activity_desc'] = chosen_activity.activity_desc
    return JsonResponse(context)
