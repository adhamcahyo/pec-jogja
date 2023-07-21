from lms_app.models import Course

def analyze_learning_style(user):
    learning_style = user.learning_style

    
    if learning_style == 'visual':
        adaptive_courses = Course.objects.filter(learning_style='visual')
    elif learning_style == 'auditory':
        adaptive_courses = Course.objects.filter(learning_style='auditory')
    elif learning_style == 'kinesthetic':
        adaptive_courses = Course.objects.filter(learning_style='kinesthetic')
    else:
        adaptive_courses = Course.objects.all()

    return adaptive_courses
