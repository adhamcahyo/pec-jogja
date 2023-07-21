from django.shortcuts import render
from .models import Transcript

def transcript_verification(request, transcript_id):
    transcript = Transcript.objects.get(pk=transcript_id)
    return render(request, 'blockchain_integration/templates/transcript_verification.html', {'transcript': transcript})