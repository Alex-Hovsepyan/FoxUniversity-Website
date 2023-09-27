from django.shortcuts import render
from rest_framework import generics
from .models import Header, HomePage, HomeAbout, Offer, OfferContent, Story, About, AboutContent, TestimonialTitle, Testimonial, Gallery
from .models import Teachers, Courses, ContactInfo, Contact, AdmissionContent, RegistrationInfo, Registration
from .serializers import HeaderSerializer, HomePageSerializer, HomeAboutSerializer, OfferSerializer, OfferContentSerializer, StorySerializer
from .serializers import AboutSerializer, AboutContentSerializer, TestimonialTitleSerializer, TestimonialSerializer, GallerySerializer
from .serializers import TeachersSerializer, CoursesSerializer, ContactInfoSerializer, ContactSerializer, AdmissionContentSerializer
from .serializers import RegistrationInfoSerializer, RegistrationSerializer
# Create your views here.

class HeaderView(generics.ListCreateAPIView):

    queryset = Header.objects.all()
    serializer_class = HeaderSerializer

class HomePageView(generics.ListCreateAPIView):

    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer

class HomeAboutView(generics.ListCreateAPIView):

    queryset = HomeAbout.objects.all()
    serializer_class = HomeAboutSerializer

class OfferView(generics.ListCreateAPIView):

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class OfferContentView(generics.ListCreateAPIView):

    queryset = OfferContent.objects.all()
    serializer_class = OfferContentSerializer

class StoryView(generics.ListCreateAPIView):

    queryset = Story.objects.all()
    serializer_class = StorySerializer

class AboutView(generics.ListCreateAPIView):

    queryset = About.objects.all()
    serializer_class = AboutSerializer

class AboutContentView(generics.ListCreateAPIView):

    queryset = AboutContent.objects.all()
    serializer_class = AboutContentSerializer

class TestimonialTitleView(generics.ListCreateAPIView):

    queryset = TestimonialTitle.objects.all()
    serializer_class = TestimonialTitleSerializer

class TestimonialView(generics.ListCreateAPIView):

    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class GalleryView(generics.ListCreateAPIView):

    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class TeachersView(generics.ListCreateAPIView):

    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer

class CoursesView(generics.ListCreateAPIView):

    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

class ContactInfoView(generics.ListCreateAPIView):

    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

class ContactView(generics.ListCreateAPIView):

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class AdmissionContentView(generics.ListCreateAPIView):

    queryset = AdmissionContent.objects.all()
    serializer_class = AdmissionContentSerializer

class RegistrationInfoView(generics.ListCreateAPIView):

    queryset = RegistrationInfo.objects.all()
    serializer_class = RegistrationInfoSerializer

class RegistrationView(generics.ListCreateAPIView):

    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer