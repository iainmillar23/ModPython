units = [
'NUBIAN_AFRICAN_FOREST_ELEPHANT',
'INDONESIAN_KRIS_SWORDSMAN',
'KHMER_WAR_CANOE',
'KOREAN_TURTLE_SHIP',
'DUTCH_SCHUTTERIJ',
'GEORGIAN_TADZREULI',
'CREE_OTEHTAPIW',
'MAPUCHE_GUERILLA',
'SCOTTISH_GALLOWGLASS',
'MONGOLIAN_HUI_HUI_PAO',
'ZULU_ASSEGAI']


for unit in units:

    print ("INSERT INTO TypeTags (Type, Tag) VALUES ('ABILITY_%s', 'CLASS_%s');" % (unit,unit))
    #print ("INSERT INTO UnitAbilities (UnitAbilityType, Name, Description) VALUES ('ABILITY_%s','LOC_ABILITY_%s_NAME','LOC_ABILITY_%s_DESCRIPTION');" % (unit,unit,unit))