from django.db import models

# Create your models here.

escolhas = [
    ("Nutricionista", "Nutricionista"),
    ("Ortopedista", "Ortopedista"),
    ("Dentista", "Dentista"),
    ("Pediatra", "Pediatra"),
    ("Cardiologista", "Cardiologista"),
    ("Oftalmologista", "Oftalmologista"),
]

class Medico(models.Model):
    nome = models.CharField(max_length=255)
    especialidade = models.CharField(max_length=50, choices=escolhas)
    crm = models.CharField(max_length=100, unique=True)
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return self.nome
    
statusConsulta = [
    ("Agendado", "Agendado"),
    ("Realizado", "Realizado"),
    ("Cancelado", "Cancelado")
]

class Consulta(models.Model):
    paciente = models.CharField(max_length=255)
    data = models.DateField(auto_created=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=statusConsulta)

    def __str__(self):
        return self.paciente