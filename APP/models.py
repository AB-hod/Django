# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bindingdb10120(models.Model):
    bindingdbreactant_set_id = models.IntegerField(db_column='BindingDBReactant_set_id', primary_key=True)  # Field name made lowercase.
    ligandsmiles = models.TextField(db_column='LigandSMILES', blank=True, null=True)  # Field name made lowercase.
    ligandinchi = models.TextField(db_column='LigandInChI', blank=True, null=True)  # Field name made lowercase.
    ligandinchikey = models.TextField(db_column='LigandInChIKey', blank=True, null=True)  # Field name made lowercase.
    bindingdbmonomerid = models.IntegerField(db_column='BindingDBMonomerID', blank=True, null=True)  # Field name made lowercase.
    bindingdbligandname = models.TextField(db_column='BindingDBLigandName', blank=True, null=True)  # Field name made lowercase.
    targetnameassignedbycuratorordatasource = models.TextField(db_column='TargetNameAssignedbyCuratororDataSource', blank=True, null=True)  # Field name made lowercase.
    targetsourceorganismaccordingtocuratorordatasource = models.TextField(db_column='TargetSourceOrganismAccordingtoCuratororDataSource', blank=True, null=True)  # Field name made lowercase.
    ki_nm = models.TextField(db_column='Ki_nM', blank=True, null=True)  # Field name made lowercase.
    ic50_nm = models.TextField(db_column='IC50_nM', blank=True, null=True)  # Field name made lowercase.
    kd_nm = models.TextField(db_column='Kd_nM', blank=True, null=True)  # Field name made lowercase.
    ec50_nm = models.TextField(db_column='EC50_nM', blank=True, null=True)  # Field name made lowercase.
    pmid = models.TextField(db_column='PMID', blank=True, null=True)  # Field name made lowercase.
    pubchemaid = models.TextField(db_column='PubChemAID', blank=True, null=True)  # Field name made lowercase.
    patentnumber = models.TextField(db_column='PatentNumber', blank=True, null=True)  # Field name made lowercase.
    linktoligandinbindingdb = models.TextField(db_column='LinktoLigandinBindingDB', blank=True, null=True)  # Field name made lowercase.
    pdbids_forligand_targetcomplex = models.TextField(db_column='PDBIDs_forLigand_TargetComplex', blank=True, null=True)  # Field name made lowercase.
    pubchemcid = models.IntegerField(db_column='PubChemCID', blank=True, null=True)  # Field name made lowercase.
    pubchemsid = models.IntegerField(db_column='PubChemSID', blank=True, null=True)  # Field name made lowercase.
    chebiidofligand = models.TextField(db_column='ChEBIIDofLigand', blank=True, null=True)  # Field name made lowercase.
    chemblidofligand = models.TextField(db_column='ChEMBLIDofLigand', blank=True, null=True)  # Field name made lowercase.
    drugbankidofligand = models.TextField(db_column='DrugBankIDofLigand', blank=True, null=True)  # Field name made lowercase.
    iuphar_gracidofligand = models.TextField(db_column='IUPHAR_GRACIDofLigand', blank=True, null=True)  # Field name made lowercase.
    keggidofligand = models.TextField(db_column='KEGGIDofLigand', blank=True, null=True)  # Field name made lowercase.
    zincidofligand = models.TextField(db_column='ZINCIDofLigand', blank=True, null=True)  # Field name made lowercase.
    bindingdbtargetchainsequence = models.TextField(db_column='BindingDBTargetChainSequence', blank=True, null=True)  # Field name made lowercase.
    pdbids_oftargetchain = models.TextField(db_column='PDBIDs_ofTargetChain', blank=True, null=True)  # Field name made lowercase.
    uniprot_swissprot_recommendednameoftargetchain = models.TextField(db_column='UniProt_SwissProt_RecommendedNameofTargetChain', blank=True, null=True)  # Field name made lowercase.
    uniprot_swissprot_entrynameoftargetchain = models.TextField(db_column='UniProt_SwissProt_EntryNameofTargetChain', blank=True, null=True)  # Field name made lowercase.
    uniprot_swissprot_primaryidoftargetchain = models.TextField(db_column='UniProt_SwissProt_PrimaryIDofTargetChain', blank=True, null=True)  # Field name made lowercase.
    uniprot_swissprot_secondaryids_oftargetchain = models.TextField(db_column='UniProt_SwissProt_SecondaryIDs_ofTargetChain', blank=True, null=True)  # Field name made lowercase.
    uniprot_swissprot_alternativeids_oftargetchain = models.TextField(db_column='UniProt_SwissProt_AlternativeIDs_ofTargetChain', blank=True, null=True)  # Field name made lowercase.
    uniprot_trembl_submittednameoftargetchain = models.TextField(db_column='UniProt_TrEMBL_SubmittedNameofTargetChain', blank=True, null=True)  # Field name made lowercase.
    uniprot_trembl_entrynameoftargetchain = models.TextField(db_column='UniProt_TrEMBL_EntryNameofTargetChain', blank=True, null=True)  # Field name made lowercase.
    uniprot_trembl_primaryidoftargetchain = models.TextField(db_column='UniProt_TrEMBL_PrimaryIDofTargetChain', blank=True, null=True)  # Field name made lowercase.
    uniprot_trembl_secondaryids_oftargetchain = models.TextField(db_column='UniProt_TrEMBL_SecondaryIDs_ofTargetChain', blank=True, null=True)  # Field name made lowercase.
    uniprot_trembl_alternativeids_oftargetchain = models.TextField(db_column='UniProt_TrEMBL_AlternativeIDs_ofTargetChain', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bindingdb10120'


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class Qwe(models.Model):
    qwe = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qwe'
