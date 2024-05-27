from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from .models import Tweet
from pprint import pprint
from datetime import datetime
from .forms import TweetForm
import cloudinary

def tweetListView(request):
  # Get all tweets, limit = 20
  tweets = Tweet.objects.order_by('created_at').reverse().all()[:20]

  # Show output with tweets
  return render(request, 'tweet_list.html',
    {'tweets': tweets})

def tweetEditView(request, tweet_id):
  # Get requested tweet
  tweet = Tweet.objects.get(id = tweet_id)

  # If the method is POST
  if request.method == 'POST':
    form = TweetForm(request.POST, request.FILES, instance=tweet)
    if form.is_valid():
      # Save and redirect to home
      form.save()
      return HttpResponseRedirect('/')
    else:
      print(form.errors)

  else:
    # Show editting screen
    form = TweetForm
    return render(request, 'tweet_edit.html',
    {'tweet': tweet, 'form': form})

def tweetAdd(request):
  # If the method is POST
  if request.method == 'POST':
    form = TweetForm(request.POST, request.FILES)
    if form.is_valid():
      # Save and redirect to home
      form.save()
    else:
      print(form.errors)

  return HttpResponseRedirect('/')

def tweetDelete(request, tweet_id):
  # Get tweet
  tweet_to_delete = Tweet.objects.get(id=tweet_id)
  
  # Delete
  tweet_to_delete.delete()

  return HttpResponseRedirect('/')

def tweetLikeAdd(request, tweet_id):
  # Get requested tweet
  tweet = Tweet.objects.get(id = tweet_id)

  # Add count
  new_like_count = tweet.like_count + 1
  tweet.like_count = new_like_count

  # Save
  tweet.save()

  return JsonResponse({'result': 'successful'})

def tweetLikeSubtract(request, tweet_id):
  # Get requested tweet
  tweet = Tweet.objects.get(id = tweet_id)

  # Subtract count
  new_like_count = tweet.like_count - 1
  tweet.like_count = new_like_count

  # Save
  tweet.save()

  return JsonResponse({'result': 'successful'})
