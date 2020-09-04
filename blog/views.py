from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Course
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# def home(request):
#     context = {
#         'courses': Course.objects.filter(admin_approver=True)
#     }
#     return render(request, 'blog/home.html' ,context)

class CourseListView(ListView):
    model = Course
         
    context_object_name = 'courses'
    template_name = 'blog/home.html'
    paginate_by = 5
    def get_queryset(self):
        return self.model.objects.filter(admin_approver=True)

 



class CourseDetailView(DetailView):
    model = Course



class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    fields =['instructor_name', 'course_image', 'Course_Title', 
     'Course_Subtitle', 'Language', 'Requirement_1', 'Requirement_2', 'Requirement_3', 
     'Description', 'What_you_ll_learn_1', 'What_you_ll_learn_2', 'What_you_ll_learn_3', 'link_to_course']
    def form_valid(self ,form):
        form.instance.instructor_name = self.request.user
        return super().form_valid(form)  