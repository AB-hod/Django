# Generated by Django 3.2.9 on 2021-11-24 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bindll',
            fields=[
                ('bindingdbreactant_set_id', models.IntegerField(db_column='BindingDBReactant_set_id', primary_key=True, serialize=False)),
                ('ligandsmiles', models.TextField(blank=True, db_column='LigandSMILES', null=True)),
                ('ligandinchi', models.TextField(blank=True, db_column='LigandInChI', null=True)),
                ('ligandinchikey', models.TextField(blank=True, db_column='LigandInChIKey', null=True)),
                ('bindingdbmonomerid', models.IntegerField(blank=True, db_column='BindingDBMonomerID', null=True)),
                ('bindingdbligandname', models.TextField(blank=True, db_column='BindingDBLigandName', null=True)),
                ('targetnameassignedbycuratorordatasource', models.TextField(blank=True, db_column='TargetNameAssignedbyCuratororDataSource', null=True)),
                ('targetsourceorganismaccordingtocuratorordatasource', models.TextField(blank=True, db_column='TargetSourceOrganismAccordingtoCuratororDataSource', null=True)),
                ('ki_nm', models.TextField(blank=True, db_column='Ki_nM', null=True)),
                ('ic50_nm', models.TextField(blank=True, db_column='IC50_nM', null=True)),
                ('kd_nm', models.TextField(blank=True, db_column='Kd_nM', null=True)),
                ('ec50_nm', models.TextField(blank=True, db_column='EC50_nM', null=True)),
                ('pmid', models.TextField(blank=True, db_column='PMID', null=True)),
                ('pubchemaid', models.TextField(blank=True, db_column='PubChemAID', null=True)),
                ('patentnumber', models.TextField(blank=True, db_column='PatentNumber', null=True)),
                ('linktoligandinbindingdb', models.TextField(blank=True, db_column='LinktoLigandinBindingDB', null=True)),
                ('pdbids_forligand_targetcomplex', models.TextField(blank=True, db_column='PDBIDs_forLigand_TargetComplex', null=True)),
                ('pubchemcid', models.IntegerField(blank=True, db_column='PubChemCID', null=True)),
                ('pubchemsid', models.IntegerField(blank=True, db_column='PubChemSID', null=True)),
                ('chebiidofligand', models.TextField(blank=True, db_column='ChEBIIDofLigand', null=True)),
                ('chemblidofligand', models.TextField(blank=True, db_column='ChEMBLIDofLigand', null=True)),
                ('drugbankidofligand', models.TextField(blank=True, db_column='DrugBankIDofLigand', null=True)),
                ('iuphar_gracidofligand', models.TextField(blank=True, db_column='IUPHAR_GRACIDofLigand', null=True)),
                ('keggidofligand', models.TextField(blank=True, db_column='KEGGIDofLigand', null=True)),
                ('zincidofligand', models.TextField(blank=True, db_column='ZINCIDofLigand', null=True)),
                ('bindingdbtargetchainsequence', models.TextField(blank=True, db_column='BindingDBTargetChainSequence', null=True)),
                ('pdbids_oftargetchain', models.TextField(blank=True, db_column='PDBIDs_ofTargetChain', null=True)),
                ('uniprot_swissprot_recommendednameoftargetchain', models.TextField(blank=True, db_column='UniProt_SwissProt_RecommendedNameofTargetChain', null=True)),
                ('uniprot_swissprot_entrynameoftargetchain', models.TextField(blank=True, db_column='UniProt_SwissProt_EntryNameofTargetChain', null=True)),
                ('uniprot_swissprot_primaryidoftargetchain', models.TextField(blank=True, db_column='UniProt_SwissProt_PrimaryIDofTargetChain', null=True)),
                ('uniprot_swissprot_secondaryids_oftargetchain', models.TextField(blank=True, db_column='UniProt_SwissProt_SecondaryIDs_ofTargetChain', null=True)),
                ('uniprot_swissprot_alternativeids_oftargetchain', models.TextField(blank=True, db_column='UniProt_SwissProt_AlternativeIDs_ofTargetChain', null=True)),
                ('uniprot_trembl_submittednameoftargetchain', models.TextField(blank=True, db_column='UniProt_TrEMBL_SubmittedNameofTargetChain', null=True)),
                ('uniprot_trembl_entrynameoftargetchain', models.TextField(blank=True, db_column='UniProt_TrEMBL_EntryNameofTargetChain', null=True)),
                ('uniprot_trembl_primaryidoftargetchain', models.TextField(blank=True, db_column='UniProt_TrEMBL_PrimaryIDofTargetChain', null=True)),
                ('uniprot_trembl_secondaryids_oftargetchain', models.TextField(blank=True, db_column='UniProt_TrEMBL_SecondaryIDs_ofTargetChain', null=True)),
                ('uniprot_trembl_alternativeids_oftargetchain', models.TextField(blank=True, db_column='UniProt_TrEMBL_AlternativeIDs_ofTargetChain', null=True)),
            ],
            options={
                'db_table': 'BINDLL',
                'managed': True,
            },
        ),
    ]
