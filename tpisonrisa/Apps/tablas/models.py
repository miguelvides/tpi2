# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Area(models.Model):
    idarea = models.AutoField(primary_key=True)
    nombrearea = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Clanes(models.Model):
    idclan = models.AutoField(primary_key=True)
    nombreclan = models.CharField(max_length=500, blank=True, null=True)
    idhorario = models.ForeignKey('Horario', models.DO_NOTHING, db_column='idhorario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clanes'


class Constelacion(models.Model):
    idconstelacion = models.AutoField(primary_key=True)
    descripcionconstelacion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'constelacion'


class Credenciales(models.Model):
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuario', primary_key=True)
    nombreusuario = models.CharField(max_length=150, blank=True, null=True)
    contrasena = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credenciales'


class Detalletaller(models.Model):
    iddetalletaller = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuario', blank=True, null=True)
    idtaller = models.ForeignKey('Taller', models.DO_NOTHING, db_column='idtaller', blank=True, null=True)
    pago = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalletaller'


class Detallevisita(models.Model):
    iddetalle = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuario', blank=True, null=True)
    idpeticionvisita = models.ForeignKey('Peticionvisita', models.DO_NOTHING, db_column='idpeticionvisita', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detallevisita'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estado(models.Model):
    idestado = models.AutoField(primary_key=True)
    descripcionestado = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado'


class Horario(models.Model):
    idhorario = models.AutoField(primary_key=True)
    jornada = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horario'


class Peticionvisita(models.Model):
    idpeticionvisita = models.AutoField(primary_key=True)
    nombrecontacto = models.CharField(max_length=150, blank=True, null=True)
    correocontacto = models.CharField(max_length=150)
    fechavisita = models.DateField()
    horavisita = models.TimeField()
    entidad = models.CharField(max_length=150)
    lugardevisita = models.CharField(max_length=150)
    capacidadmax = models.SmallIntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    encargadovisita = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='encargadovisita', blank=True, null=True)
    idestado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='idestado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peticionvisita'


class Recursosonriseros(models.Model):
    idrecurso = models.AutoField(primary_key=True)
    nombrerecurso = models.CharField(max_length=50)
    talla = models.CharField(max_length=50, blank=True, null=True)
    preciorecurso = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recursosonriseros'


class Solicitudrecurso(models.Model):
    idsolicitudrecurso = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuario', blank=True, null=True)
    recursosonrisero = models.ForeignKey(Recursosonriseros, models.DO_NOTHING, db_column='recursosonrisero', blank=True, null=True)
    pago = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitudrecurso'


class Taller(models.Model):
    idtaller = models.AutoField(primary_key=True)
    nombretaller = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    precio = models.TextField(blank=True, null=True)
    encargado = models.TextField(blank=True, null=True)
    max = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taller'


class Tipousuario(models.Model):
    idtipousuario = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=75)

    class Meta:
        managed = False
        db_table = 'tipousuario'


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombresonrisero = models.CharField(max_length=75, blank=True, null=True)
    nombremortal = models.CharField(max_length=150)
    dui = models.CharField(max_length=10, blank=True, null=True)
    correo = models.CharField(max_length=150, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    generacion = models.SmallIntegerField(blank=True, null=True)
    idtipousuario = models.ForeignKey(Tipousuario, models.DO_NOTHING, db_column='idtipousuario', blank=True, null=True)
    idclan = models.ForeignKey(Clanes, models.DO_NOTHING, db_column='idclan', blank=True, null=True)
    idarea = models.ForeignKey(Area, models.DO_NOTHING, db_column='idarea', blank=True, null=True)
    idconstelacion = models.ForeignKey(Constelacion, models.DO_NOTHING, db_column='idconstelacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class VoluntarioPrueba(models.Model):
    nombre = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'voluntario_prueba'


class VoluntarioSong(models.Model):
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'voluntario_song'
