from rest_framework import serializers
from .models import Header, HomePage, HomeAbout, Offer, OfferContent, Story, About, AboutContent, TestimonialTitle, Testimonial, Gallery
from .models import Teachers, Courses, ContactInfo, Contact, AdmissionContent, RegistrationInfo, Registration

class HeaderSerializer(serializers.ModelSerializer):

    class Meta:

        model = Header
        fields = '__all__'
        
class HomePageSerializer(serializers.ModelSerializer):

    class Meta:

        model = HomePage
        fields = '__all__'
        
class HomeAboutSerializer(serializers.ModelSerializer):

    class Meta:

        model = HomeAbout
        fields = '__all__'
         
class OfferSerializer(serializers.ModelSerializer):

    class Meta:

        model = Offer
        fields = '__all__'      
         
class OfferContentSerializer(serializers.ModelSerializer):

    class Meta:

        model = OfferContent
        fields = '__all__'
         
class StorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Story
        fields = '__all__'
         
class AboutSerializer(serializers.ModelSerializer):

    class Meta:

        model = About
        fields = '__all__'
         
class AboutContentSerializer(serializers.ModelSerializer):

    class Meta:

        model = AboutContent
        fields = '__all__'
         
class TestimonialTitleSerializer(serializers.ModelSerializer):

    class Meta:

        model = TestimonialTitle
        fields = '__all__'
         
class TestimonialSerializer(serializers.ModelSerializer):

    class Meta:

        model = Testimonial
        fields = '__all__'
         
class GallerySerializer(serializers.ModelSerializer):

    class Meta:

        model = Gallery
        fields = '__all__'  
         
class TeachersSerializer(serializers.ModelSerializer):

    class Meta:

        model = Teachers
        fields = '__all__'
         
class CoursesSerializer(serializers.ModelSerializer):
    category = TeachersSerializer(read_only=True)

    class Meta:

        model = Courses
        fields = '__all__'       
         
class ContactInfoSerializer(serializers.ModelSerializer):

    class Meta:

        model = ContactInfo
        fields = '__all__'   
         
class ContactSerializer(serializers.ModelSerializer):

    class Meta:

        model = Contact
        fields = '__all__'
         
class AdmissionContentSerializer(serializers.ModelSerializer):

    class Meta:

        model = AdmissionContent
        fields = '__all__'
          
class RegistrationInfoSerializer(serializers.ModelSerializer):

    class Meta:

        model = RegistrationInfo
        fields = '__all__'
          
class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Registration
        fields = '__all__'