from django.db import models

# Create your models here.

class Header(models.Model):

    title = models.CharField('Title', max_length=30)
    email = models.EmailField('Email')
    phone = models.CharField('Phone Number', max_length=30)
    btn_name = models.CharField('Button Name', max_length=40)
    path1 = models.CharField('Path 1', max_length=40)
    path2 = models.CharField('Path 2', max_length=40)
    path3 = models.CharField('Path 3', max_length=40)
    path4 = models.CharField('Path 4', max_length=40)
    path5 = models.CharField('Path 5', max_length=40)
    path6 = models.CharField('Path 6', max_length=40)
    social1 = models.URLField('Social 1')
    social2 = models.URLField('Social 2')
    social3 = models.URLField('Social 3')
    social4 = models.URLField('Social4')
    subheader_background = models.ImageField('SubHeader Background')

    class Meta:

        verbose_name = 'Header'
        verbose_name_plural = 'Header'

class HomePage(models.Model):

    background = models.ImageField('Background')
    title = models.CharField('Title', max_length=50)
    text = models.TextField('Text')
    btn_name = models.CharField('Button Name', max_length=40)
    path = models.CharField('Path', max_length=30)

    def __str__(self) -> str:
        return self.title
    
class HomeAbout(models.Model):

    icon = models.CharField('Icon', max_length=10)
    title = models.CharField('Title', max_length=40)
    text = models.TextField('Text')

    class Meta:

        verbose_name = 'Home About'
        verbose_name_plural = 'Home About'

    def __str__(self) -> str:
        return self.title
    

class Offer(models.Model):

    title = models.CharField('Title', max_length=50)
    text = models.TextField('Text')
    img = models.ImageField('Image')

class OfferContent(models.Model):

    icon = models.CharField('Icon', max_length=10)
    title = models.CharField('Title', max_length=40)
    text = models.TextField('Text')

    def __str__(self) -> str:
        return self.title

class Story(models.Model):

    subheader_title = models.CharField('SubHeader Title', max_length=40)
    title = models.CharField('Title', max_length=50)
    text1 = models.TextField('Text1')
    text2 = models.TextField('Text2')
    text3 = models.TextField('Text3')
    img = models.ImageField('Image')

    class Meta:

        verbose_name = 'Story'
        verbose_name_plural = 'Story'

class About(models.Model):

    background = models.ImageField('Background')
    img = models.ImageField('Image')
    url = models.URLField('Video Url')
    title = models.CharField('Title', max_length=50)
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')

    class Meta:

        verbose_name = 'About'
        verbose_name_plural = 'About'

class AboutContent(models.Model):

    count = models.IntegerField('Count')
    title = models.CharField('Title', max_length=40)

    def __str__(self) -> str:
        return self.title
    
class TestimonialTitle(models.Model):

    title = models.CharField('Title', max_length=50)
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')

    class Meta:

        verbose_name = 'Testimonial Title'
        verbose_name_plural = 'Testimonial Title'

class Testimonial(models.Model):

    img = models.ImageField('Image')
    text = models.TextField('Text')
    name = models.CharField('Name', max_length=50)
    position = models.CharField('Position', max_length=50)

    def __str__(self) -> str:
        return self.name
    
class Gallery(models.Model):

    img = models.ImageField('Image')
    url = models.URLField('Image Url')

    class Meta:

        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'

class Teachers(models.Model):

    img = models.ImageField('Image')
    name = models.CharField('Name', max_length=50)
    position = models.CharField('Position', max_length=50)
    text1 = models.TextField('Text 1')
    social1 = models.URLField('Social 1')
    social2 = models.URLField('Social 2')
    social3 = models.URLField('Social 3')
    social4 = models.URLField('Social 4')
    text2 = models.TextField('Text 2')
    text3 = models.TextField('Text 3')
    email = models.EmailField('Email')
    phone = models.CharField('Phone Number', max_length=30)
    experience = models.IntegerField('Experience')

    class Meta:

        verbose_name = 'Teachers'
        verbose_name_plural = 'Teachers'

    def __str__(self) -> str:
        return f'{self.name} ----------------------- {self.position}'
    
class Courses(models.Model):

    category = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    img = models.ImageField('Image')
    seats = models.IntegerField('Seats')
    years = models.IntegerField('Years')
    title = models.CharField('Title', max_length=50)
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')
    text3 = models.TextField('Text 3')
    hours = models.IntegerField('Hours')
    slug = models.SlugField('Slug', unique=True)

    class Meta:

        verbose_name = 'Courses'
        verbose_name_plural = 'Courses'

    def __str__(self) -> str:
        return f'{self.title} ----------------------- {self.category.name}'
    
class ContactInfo(models.Model):

    icon = models.CharField('Icon', max_length=10)
    info = models.CharField('Info', max_length=50)

    def __str__(self) -> str:
        return self.info
    
class Contact(models.Model):

    name = models.CharField('UserName', max_length=50)
    email = models.EmailField('User Email')
    subject = models.CharField('Subject', max_length=50)
    message = models.TextField('Message')

    class Meta:

        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
    
    def __str__(self) -> str:
        return self.name
    
class AdmissionContent(models.Model):

    icon = models.CharField('Icon', max_length=10)
    title = models.CharField('Title', max_length=50)
    text = models.TextField('Text')

    def __str__(self) -> str:
        return self.title
    
class RegistrationInfo(models.Model):

    background = models.ImageField('Background')
    title = models.CharField('Title', max_length=50)
    text = models.TextField('Text')
    btn_name = models.CharField('Button Name', max_length=40)

class Registration(models.Model):

    name = models.CharField('Name Surname', max_length=80)
    course = models.CharField('Course', max_length=40)
    email = models.EmailField('Email')
    phone = models.CharField('Phone', max_length=30)
    message = models.TextField('Models', blank=True)

    class Meta:

        verbose_name = 'Registration'
        verbose_name_plural = 'Registration'

    def __str__(self) -> str:
        return self.name