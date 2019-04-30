#
# PySNMP MIB module HP-ICF-DEVICEIDENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-DEVICEIDENTITY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:21:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Bits, ObjectIdentity, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, Unsigned32, IpAddress, Counter32, iso, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "ObjectIdentity", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "Unsigned32", "IpAddress", "Counter32", "iso", "Integer32", "TimeTicks")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
hpicfDeviceIdentityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135))
hpicfDeviceIdentityMIB.setRevisions(('2017-01-03 00:00',))
if mibBuilder.loadTexts: hpicfDeviceIdentityMIB.setLastUpdated('201701030000Z')
if mibBuilder.loadTexts: hpicfDeviceIdentityMIB.setOrganization('HP Networking')
hpicfDeviceIdentityConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1))
hpicfDeviceIdentityConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2))
hpicfDeviceIdentityTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1), )
if mibBuilder.loadTexts: hpicfDeviceIdentityTable.setStatus('current')
hpicfDeviceIdentityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1), ).setIndexNames((0, "HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityIndex"))
if mibBuilder.loadTexts: hpicfDeviceIdentityEntry.setStatus('current')
hpicfDeviceIdentityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: hpicfDeviceIdentityIndex.setStatus('current')
hpicfDeviceIdentityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfDeviceIdentityRowStatus.setStatus('current')
hpicfDeviceIdentityName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfDeviceIdentityName.setStatus('current')
hpicfDeviceIdentityLldpOui = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfDeviceIdentityLldpOui.setStatus('current')
hpicfDeviceIdentityLldpSubType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfDeviceIdentityLldpSubType.setStatus('current')
hpicfDeviceIdentityGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 1))
hpicfDeviceIdentityCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 2))
hpicfiDeviceIdentityCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 2, 1)).setObjects(("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfiDeviceIdentityCompliance = hpicfiDeviceIdentityCompliance.setStatus('current')
hpicfDeviceIdentityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 1, 1)).setObjects(("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityRowStatus"), ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityName"), ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpOui"), ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpSubType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDeviceIdentityGroup = hpicfDeviceIdentityGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-DEVICEIDENTITY-MIB", hpicfDeviceIdentityTable=hpicfDeviceIdentityTable, hpicfDeviceIdentityLldpSubType=hpicfDeviceIdentityLldpSubType, hpicfDeviceIdentityGroup=hpicfDeviceIdentityGroup, hpicfDeviceIdentityLldpOui=hpicfDeviceIdentityLldpOui, hpicfDeviceIdentityEntry=hpicfDeviceIdentityEntry, hpicfDeviceIdentityConfig=hpicfDeviceIdentityConfig, hpicfDeviceIdentityConformance=hpicfDeviceIdentityConformance, hpicfDeviceIdentityCompliances=hpicfDeviceIdentityCompliances, hpicfDeviceIdentityName=hpicfDeviceIdentityName, hpicfDeviceIdentityGroups=hpicfDeviceIdentityGroups, hpicfiDeviceIdentityCompliance=hpicfiDeviceIdentityCompliance, hpicfDeviceIdentityRowStatus=hpicfDeviceIdentityRowStatus, PYSNMP_MODULE_ID=hpicfDeviceIdentityMIB, hpicfDeviceIdentityMIB=hpicfDeviceIdentityMIB, hpicfDeviceIdentityIndex=hpicfDeviceIdentityIndex)
