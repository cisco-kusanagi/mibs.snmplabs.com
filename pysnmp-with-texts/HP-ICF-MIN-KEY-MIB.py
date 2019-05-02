#
# PySNMP MIB module HP-ICF-MIN-KEY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-MIN-KEY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:34:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, ObjectIdentity, ModuleIdentity, Integer32, Bits, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, MibIdentifier, Counter64, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Integer32", "Bits", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "MibIdentifier", "Counter64", "IpAddress", "Unsigned32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
hpicfMinKeyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132))
hpicfMinKeyMIB.setRevisions(('2016-06-22 09:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfMinKeyMIB.setRevisionsDescriptions(('Initial version of minimum key MIB module.',))
if mibBuilder.loadTexts: hpicfMinKeyMIB.setLastUpdated('201606220900Z')
if mibBuilder.loadTexts: hpicfMinKeyMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfMinKeyMIB.setContactInfo('Hewlett-Packard Enterprise Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfMinKeyMIB.setDescription('This MIB module describes objects for enforcing minimum secure key size in the HPE Integrated Communication Facility product line.')
hpicfMinKeyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0))
hpicfMinKeyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1))
hpicfMinKeyConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1))
hpicfMinKeyTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1), )
if mibBuilder.loadTexts: hpicfMinKeyTable.setStatus('current')
if mibBuilder.loadTexts: hpicfMinKeyTable.setDescription('A table of minimum secure key size objects')
hpicfMinKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1, 1), ).setIndexNames((0, "HP-ICF-MIN-KEY-MIB", "hpicfMinKeyType"))
if mibBuilder.loadTexts: hpicfMinKeyEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfMinKeyEntry.setDescription('An entry in the hpicfMinKeyTable.')
hpicfMinKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("rsa", 1))))
if mibBuilder.loadTexts: hpicfMinKeyType.setStatus('current')
if mibBuilder.loadTexts: hpicfMinKeyType.setDescription('This object specifies the key type for which the minimum secure key size enforced.')
hpicfMinKeySize = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("minBit1024", 1), ("minBit2048", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfMinKeySize.setStatus('current')
if mibBuilder.loadTexts: hpicfMinKeySize.setDescription('This object specifies the minimum secure key size enforced. The default value for this attribute will be 1024')
hpicfMinKeyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfMinKeyRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfMinKeyRowStatus.setDescription('Status of this row, by which new entries may be created or existing entries deleted from this table.')
hpicfMinKeyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1, 1))
hpicfMinKeyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1, 2))
hpicfMinKeyCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1, 1, 1)).setObjects(("HP-ICF-MIN-KEY-MIB", "hpicfMinKeyConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMinKeyCompliance1 = hpicfMinKeyCompliance1.setStatus('current')
if mibBuilder.loadTexts: hpicfMinKeyCompliance1.setDescription('The compliance statement')
hpicfMinKeyConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1, 2, 1)).setObjects(("HP-ICF-MIN-KEY-MIB", "hpicfMinKeySize"), ("HP-ICF-MIN-KEY-MIB", "hpicfMinKeyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMinKeyConfigGroup = hpicfMinKeyConfigGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfMinKeyConfigGroup.setDescription('A collection of objects providing configuration for minimum secure key size.')
mibBuilder.exportSymbols("HP-ICF-MIN-KEY-MIB", hpicfMinKeyCompliance1=hpicfMinKeyCompliance1, hpicfMinKeyConformance=hpicfMinKeyConformance, hpicfMinKeyEntry=hpicfMinKeyEntry, hpicfMinKeyTable=hpicfMinKeyTable, hpicfMinKeySize=hpicfMinKeySize, PYSNMP_MODULE_ID=hpicfMinKeyMIB, hpicfMinKeyMIB=hpicfMinKeyMIB, hpicfMinKeyType=hpicfMinKeyType, hpicfMinKeyCompliances=hpicfMinKeyCompliances, hpicfMinKeyObjects=hpicfMinKeyObjects, hpicfMinKeyGroups=hpicfMinKeyGroups, hpicfMinKeyConfigGroup=hpicfMinKeyConfigGroup, hpicfMinKeyConfigObjects=hpicfMinKeyConfigObjects, hpicfMinKeyRowStatus=hpicfMinKeyRowStatus)
