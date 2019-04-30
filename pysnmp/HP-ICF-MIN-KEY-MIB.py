#
# PySNMP MIB module HP-ICF-MIN-KEY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-MIN-KEY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:22:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, ModuleIdentity, Counter32, NotificationType, ObjectIdentity, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, IpAddress, MibIdentifier, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Counter32", "NotificationType", "ObjectIdentity", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "IpAddress", "MibIdentifier", "Integer32", "Gauge32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
hpicfMinKeyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132))
hpicfMinKeyMIB.setRevisions(('2016-06-22 09:00',))
if mibBuilder.loadTexts: hpicfMinKeyMIB.setLastUpdated('201606220900Z')
if mibBuilder.loadTexts: hpicfMinKeyMIB.setOrganization('HP Networking')
hpicfMinKeyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0))
hpicfMinKeyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1))
hpicfMinKeyConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1))
hpicfMinKeyTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1), )
if mibBuilder.loadTexts: hpicfMinKeyTable.setStatus('current')
hpicfMinKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1, 1), ).setIndexNames((0, "HP-ICF-MIN-KEY-MIB", "hpicfMinKeyType"))
if mibBuilder.loadTexts: hpicfMinKeyEntry.setStatus('current')
hpicfMinKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("rsa", 1))))
if mibBuilder.loadTexts: hpicfMinKeyType.setStatus('current')
hpicfMinKeySize = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("minBit1024", 1), ("minBit2048", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfMinKeySize.setStatus('current')
hpicfMinKeyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfMinKeyRowStatus.setStatus('current')
hpicfMinKeyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1, 1))
hpicfMinKeyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1, 2))
hpicfMinKeyCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1, 1, 1)).setObjects(("HP-ICF-MIN-KEY-MIB", "hpicfMinKeyConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMinKeyCompliance1 = hpicfMinKeyCompliance1.setStatus('current')
hpicfMinKeyConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1, 2, 1)).setObjects(("HP-ICF-MIN-KEY-MIB", "hpicfMinKeySize"), ("HP-ICF-MIN-KEY-MIB", "hpicfMinKeyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMinKeyConfigGroup = hpicfMinKeyConfigGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-MIN-KEY-MIB", hpicfMinKeyRowStatus=hpicfMinKeyRowStatus, hpicfMinKeyCompliances=hpicfMinKeyCompliances, hpicfMinKeyConformance=hpicfMinKeyConformance, hpicfMinKeyMIB=hpicfMinKeyMIB, hpicfMinKeyCompliance1=hpicfMinKeyCompliance1, hpicfMinKeyEntry=hpicfMinKeyEntry, hpicfMinKeyType=hpicfMinKeyType, hpicfMinKeyGroups=hpicfMinKeyGroups, hpicfMinKeyTable=hpicfMinKeyTable, hpicfMinKeyConfigObjects=hpicfMinKeyConfigObjects, hpicfMinKeyObjects=hpicfMinKeyObjects, hpicfMinKeyConfigGroup=hpicfMinKeyConfigGroup, PYSNMP_MODULE_ID=hpicfMinKeyMIB, hpicfMinKeySize=hpicfMinKeySize)
