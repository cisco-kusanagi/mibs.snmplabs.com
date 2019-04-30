#
# PySNMP MIB module HP-ICF-LAYER3VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-LAYER3VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:21:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, TimeTicks, Bits, Unsigned32, Counter32, ObjectIdentity, Integer32, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "Bits", "Unsigned32", "Counter32", "ObjectIdentity", "Integer32", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "NotificationType", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpicfLayer3VlanConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70))
hpicfLayer3VlanConfigMIB.setRevisions(('2010-03-23 00:00',))
if mibBuilder.loadTexts: hpicfLayer3VlanConfigMIB.setLastUpdated('201003230000Z')
if mibBuilder.loadTexts: hpicfLayer3VlanConfigMIB.setOrganization('HP Networking')
hpicfLayer3VlanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 1))
hpicfLayer3VlanConfigConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2))
hpicfLayer3VlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 1, 1), )
if mibBuilder.loadTexts: hpicfLayer3VlanConfigTable.setStatus('current')
hpicfLayer3VlanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfLayer3VlanConfigEntry.setStatus('current')
hpicfLayer3VlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfLayer3VlanStatus.setStatus('current')
hpicfL3VlanConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2, 1))
hpicfLayer3VlanConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2, 2))
hpicfL3VlanConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2, 1, 1)).setObjects(("HP-ICF-LAYER3VLAN-MIB", "hpicfLayer3VlanConfigGroup"), ("HP-ICF-LAYER3VLAN-MIB", "hpicfLayer3VlanConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfL3VlanConfigMIBCompliance = hpicfL3VlanConfigMIBCompliance.setStatus('current')
hpicfLayer3VlanConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2, 2, 1)).setObjects(("HP-ICF-LAYER3VLAN-MIB", "hpicfLayer3VlanStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLayer3VlanConfigGroup = hpicfLayer3VlanConfigGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-LAYER3VLAN-MIB", hpicfLayer3VlanConfig=hpicfLayer3VlanConfig, PYSNMP_MODULE_ID=hpicfLayer3VlanConfigMIB, hpicfLayer3VlanConfigTable=hpicfLayer3VlanConfigTable, hpicfLayer3VlanConfigConformance=hpicfLayer3VlanConfigConformance, hpicfLayer3VlanConfigGroup=hpicfLayer3VlanConfigGroup, hpicfLayer3VlanStatus=hpicfLayer3VlanStatus, hpicfL3VlanConfigMIBCompliance=hpicfL3VlanConfigMIBCompliance, hpicfLayer3VlanConfigMIB=hpicfLayer3VlanConfigMIB, hpicfLayer3VlanConfigEntry=hpicfLayer3VlanConfigEntry, hpicfLayer3VlanConfigMIBGroups=hpicfLayer3VlanConfigMIBGroups, hpicfL3VlanConfigMIBCompliances=hpicfL3VlanConfigMIBCompliances)
