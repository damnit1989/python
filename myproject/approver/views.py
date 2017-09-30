# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from datetime import datetime
from django import forms
from django.forms import ModelForm
from django.core.mail import send_mail
from django.db.models import Count
from django.http import HttpResponseRedirect
# from django.views.generic.simple import direct_to_template
from myproject import settings
from poster.views import *
from poster.models import Tweet, Comment

# Create your views here.

def list_tweets(request):
    twees_list = {}
    twees_list['pending_tweets'] = Tweet.objects.filter(state = 'pending').order_by('created_at')
    twees_list['published_tweets'] = Tweet.objects.filter(state = 'published').order_by('-published_at')
    return render(request,'list_tweets.html',twees_list)


class ReviewForm(forms.Form):
    new_comment = forms.CharField(max_length = 300,widget = forms.Textarea(attrs = {'cols':50,'rows':6}),required = False)
    APPROVAL_CHOICES = (
        ('approve','Approve this tweet and post it to Twitter'),
        ('reject','Reject this tweet and send it back to the author'),
    )
    approval =  models.ChoiceField(choices = APPROVAL_CHOICES, widget = forms.RadioSelect)
    
    
def review_tweet(request,tweet_id):
    review_list = {}
    reviewed_tweet = get_object_or_404(Tweet,id = tweet_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_comment = form.cleaned_data['new_comment']
            if form.cleaned_data['approval'] == 'approve':
                # publish_tweet(reviewed_tweet)
                # send_approval_email(reviewed_tweet,new_comment)
                reviewed_tweet.published_at = datetime.now()
                reviewed_tweet.state = 'published'
            else:
                link = request.build_absolute_uri(reverse(post_tweet,args = [reviewed_tweet.id]))
                send_rejection_email(reviewed_tweet,new_comment,link)
                reviewed_tweet.state = 'rejected'
            reviewed_tweet.save()
            if new_comment:
                c = Comment(tweet = reviewed_tweet,text = new_comment)
                c.save()
            return HttpResponseRedirect('/approve')
    else:
        form = ReviewForm()
    review_list['form'] = form
    review_list['tweet'] = reviewed_tweet
    review_list['comments'] = reviewed_tweet.comment_set.all()
    return render(request,'review_tweet.html',review_list)
    

def publish_tweet(tweet):
    pass
    # twitter = Twython(
        # twitter_token = settings.TWITTER_CONSUMER_KEY,
        # twitter_secret = settings.TEITTER_CONSUMER_SECRT,
        # oauth_token = settings.TWITTER_OAUTH_TOKEN,
        # oauth_token_secret = settings.TWITTER_OAUTH_TOKEN_SECRET,
    # )
    # twitter.updateStatus(status = tweet.text.encode('utf-8'))