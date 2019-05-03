from django.db import models


# Create your models here


class UporabniDio(models.Model):
    ID_Uporabni_Dio = models.AutoField(primary_key=True)
    naziv = models.CharField(max_length=100)
    biljna_vrsta = models.ManyToManyField('BiljnaVrsta')

    def __str__(self):
        return self.naziv


class Slika(models.Model):
    ID_Slike = models.AutoField(primary_key=True)
    naziv_slike = models.CharField(max_length=50)
    opis_slike = models.CharField(max_length=255)
    ID_uporabni_dio = models.ForeignKey(UporabniDio, on_delete=models.CASCADE)

    def __str__(self):
        return self.naziv_slike


class Rod(models.Model):
    ID_roda = models.AutoField(primary_key=True)
    naziv_roda = models.CharField(max_length=30)

    def __str__(self):
        return self.naziv_roda


class Sistematicar(models.Model):
    ID_sistematicara = models.AutoField(primary_key=True)
    naziv_sistematicara = models.CharField(max_length=100)

    def __str__(self):
        return self.naziv_sistematicara


class BiljnaVrsta(models.Model):
    ID_biljne_vrste = models.AutoField(primary_key=True)
    hrvatski_naziv_vrste = models.CharField(max_length=100)
    latinski_naziv = models.CharField(max_length=100)
    sinonim_vrste = models.CharField(max_length=100)
    opis_vrste = models.CharField(max_length=255)
    ID_roda = models.ForeignKey(Rod, on_delete=models.CASCADE)
    ID_sistematicara = models.ForeignKey(
        Sistematicar, on_delete=models.CASCADE)

    def __str__(self):
        return self.hrvatski_naziv_vrste


class Porodica(models.Model):
    ID_porodice = models.AutoField(primary_key=True)
    hrvatski_naziv_porodice = models.CharField(max_length=100)
    latisnki_naziv_porodice = models.CharField(max_length=100)
    ID_roda = models.ForeignKey(Rod, on_delete=models.CASCADE)

    def __str__(self):
        return self.hrvatski_naziv_porodice


class Podvrsta(models.Model):
    ID_podvrste = models.AutoField(primary_key=True)
    naziv_podvrste = models.CharField(max_length=100)
    ID_bilje_vrste = models.ForeignKey(BiljnaVrsta, on_delete=models.CASCADE)

    def __str__(self):
        return self.naziv_podvrste


class Varijet(models.Model):
    ID_varijeta = models.AutoField(primary_key=True)
    naziv_varijeta = models.CharField(max_length=100)
    ID_podvrste = models.ForeignKey(Podvrsta, on_delete=models.CASCADE)

    def __str__(self):
        return self.naziv_varijeta
