from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from djstripe.models import Customer
import stripe
from issues.models import Vote,Ticket
from common.models import User

def createFeatureVote(_issue,_voter):
        vote = Vote.objects.create(
                issue = _issue,
                voter = _voter
                )
        vote.save()

@api_view(['POST'])
def charge(request):
        if request.method=="POST":
                try:
                        stripe.api_key = "sk_test_jBCAlpQ4UIbmhUlL81YEbvhi"
                        charge = stripe.Charge.create(
                                amount = 500,
                                currency = 'usd',
                                description = "Upvote feature",
                                source = request.data.get('tok')
                        )
                        issue = Ticket.objects.get(ticket_id = request.data.get('issue'))
                        user = User.objects.get(username = request.data.get('user'))
                        createFeatureVote(issue,user)
                except:
                        return Response({"error":"Payment unsuccessful"})
        return Response({"success":"Payment was successful!"})