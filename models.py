# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bindll(models.Model):
    bindingdbreactant_set_id = models.IntegerField(db_column='BindingDBReactant_set_id',primary_key=True)  # Field name made lowercase.
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
    def __str__(self):
        return self.targetnameassignedbycuratorordatasource
        
    class Meta:
        managed = True
        db_table = 'BINDLL'
