from django.urls import path
from .views import HeaderView, HomePageView, HomeAboutView, OfferView, OfferContentView, StoryView, AboutView, AboutContentView
from .views import TestimonialTitleView, TestimonialView, GalleryView, TeachersView, CoursesView, ContactInfoView, ContactView
from .views import AdmissionContentView, RegistrationInfoView, RegistrationView

urlpatterns = [
    path('header/', HeaderView.as_view()),
    path('homepage/', HomePageView.as_view()),
    path('home_about/', HomeAboutView.as_view()),
    path('offer/', OfferView.as_view()),
    path('offer_content/', OfferContentView.as_view()),
    path('story/', StoryView.as_view()),
    path('story/', StoryView.as_view()),
    path('about/', AboutView.as_view()),
    path('about_content/', AboutContentView.as_view()),
    path('testimonial_title/', TestimonialTitleView.as_view()),
    path('testimonial/', TestimonialView.as_view()),
    path('gallery/', GalleryView.as_view()),
    path('teachers/', TeachersView.as_view()),
    path('courses/', CoursesView.as_view()),
    path('contact_info/', ContactInfoView.as_view()),
    path('contact/', ContactView.as_view()),
    path('admission_content/', AdmissionContentView.as_view()),
    path('registration_info/', RegistrationInfoView.as_view()),
    path('registration/', RegistrationView.as_view()),
]