from table.models import Name, Group


def top_name(request):
    return {'top_name': Name.objects.first()}


def group_name(request):
    return {'group_name': Group.objects.all()}



