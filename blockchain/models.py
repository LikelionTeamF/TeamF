from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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


class Etf(models.Model):
    tickers = models.CharField(primary_key=True, max_length=20)
    etf_name = models.CharField(max_length=100)
    theme = models.CharField(max_length=20)
    return_3m = models.FloatField()

    class Meta:
        managed = False
        db_table = 'etf'


class KrPrice(models.Model):
    date = models.DateField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volumne = models.FloatField(blank=True, null=True)
    tickers = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'kr_price'
        unique_together = (('date', 'tickers'),)


class KrSector(models.Model):
    tickers = models.CharField(primary_key=True, max_length=20)
    cmp_name = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'kr_sector'


class KrTicker(models.Model):
    tickers = models.CharField(primary_key=True, max_length=20)
    cmp_name = models.CharField(max_length=100)
    mkt = models.CharField(max_length=100)
    mkt_cap = models.IntegerField()
    eps = models.FloatField(blank=True, null=True)
    before_eps = models.FloatField(blank=True, null=True)
    bps = models.FloatField(blank=True, null=True)
    dividend = models.FloatField(blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=20)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'kr_ticker'


class Pdf(models.Model):
    parent_etf_ticker = models.CharField(primary_key=True, max_length=20)
    tickers = models.CharField(max_length=20)
    cmp_name = models.CharField(max_length=100)
    mkt_cap = models.IntegerField()
    mkt = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'pdf'
        unique_together = (('parent_etf_ticker', 'tickers'),)


class Shares(models.Model):
    tickers = models.CharField(primary_key=True, max_length=20)
    shares = models.BigIntegerField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shares'


class ThemeInfo(models.Model):
    theme_code = models.CharField(primary_key=True, max_length=100)
    theme_title = models.CharField(max_length=100, blank=True, null=True)
    theme_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'theme_info'


class ThemePdfs(models.Model):
    stk_name = models.CharField(primary_key=True, max_length=100)
    theme_title = models.CharField(max_length=100)
    stk_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'theme_pdfs'
        unique_together = (('stk_name', 'theme_title'),)