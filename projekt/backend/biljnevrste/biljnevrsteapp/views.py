from rest_framework import viewsets

from .serializers import *

'''
API endpoint za unos, uredjivanje uporabnih dijelova
'''


class UporabniDioViewSet(viewsets.ModelViewSet):
    queryset = UporabniDio.objects.all()
    serializer_class = UporabniDioSerializer


'''
API endpint za unos, uredjivanje slika
'''


class SlikaViewSet(viewsets.ModelViewSet):
    queryset = Slika.objects.all()
    serializer_class = SlikaSerializer


'''
API endpint za unos, uredjivanje rodova
'''


class RodViewSet(viewsets.ModelViewSet):
    queryset = Rod.objects.all()
    serializer_class = RodSerializer


'''
API endpoint za unos, uredjivanje sistematicara
'''


class SistematicarViewSet(viewsets.ModelViewSet):
    queryset = Sistematicar.objects.all()
    serializer_class = SistematicarSerializer


'''
API endpoint za unos, uredjivanje biljnih vrsta
'''


class BiljnaVrstaViewSet(viewsets.ModelViewSet):
    queryset = BiljnaVrsta.objects.all()
    serializer_class = BiljnaVrstaSerializer


'''
API endpoint za unos, uredjivanje porodica
'''


class PorodicaViewSet(viewsets.ModelViewSet):
    queryset = Porodica.objects.all()
    serializer_class = PorodicaSerializer


'''
API endpoint za unos, uredjivanje podvrsta
'''


class PodvrstaViewSet(viewsets.ModelViewSet):
    queryset = Podvrsta.objects.all()
    serializer_class = PodvrstaSerializer


'''
API endpoint za unos, uredjivanje varijeta
'''


class VarijetViewSet(viewsets.ModelViewSet):
    queryset = Varijet.objects.all()
    serializer_class = VarijetSerializer
