
from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from .forms import NewsForm





def create_news(request):
    if request.method == 'POST':

        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news:index')
    else:
        form = NewsForm()
    return render(request, 'news/create_news.html', {'form': form})

def update_news(request, news_id):
    news_instance = get_object_or_404(News, id=news_id)
    if request.method == 'POST':

        form = NewsForm(request.POST, instance=news_instance)
        if form.is_valid():
            form.save()
            return redirect('news:index')
    else:
        form = NewsForm(instance=news_instance)
    return render(request, 'news/update_news.html', {'form': form, 'news_id': news_id})




def delete_news(request, news_id):
    news_instance = get_object_or_404(News, id=news_id)
    if request.method == 'POST':
        news_instance.delete()
        return redirect('news:index')
    return render(request, 'news/delete_news.html', {'news_instance': news_instance, 'news_id1': news_id})
