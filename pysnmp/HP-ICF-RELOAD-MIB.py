#
# PySNMP MIB module HP-ICF-RELOAD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-RELOAD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:22:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpicfBasic, = mibBuilder.importSymbols("HP-ICF-BASIC", "hpicfBasic")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, Integer32, Unsigned32, MibIdentifier, ModuleIdentity, Counter32, TimeTicks, Counter64, Bits, IpAddress, Gauge32, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Counter32", "TimeTicks", "Counter64", "Bits", "IpAddress", "Gauge32", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime")
hpicfReloadMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20))
hpicfReloadMIB.setRevisions(('2009-12-03 00:00', '2009-10-01 00:00',))
if mibBuilder.loadTexts: hpicfReloadMIB.setLastUpdated('200912030000Z')
if mibBuilder.loadTexts: hpicfReloadMIB.setOrganization('HP Networking')
hpicfReloadObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 1))
hpicfEntityReload = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2))
hpicfReloadConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3))
class ReloadControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("reloadSlotNone", 1), ("fullPowerCycleReload", 2))

hpicfReloadState = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notScheduled", 1), ("reloadAfter", 2), ("reloadAt", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfReloadState.setStatus('current')
hpicfReloadAfter = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfReloadAfter.setStatus('current')
hpicfReloadAt = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 1, 3), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfReloadAt.setStatus('current')
hpicfReloadTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2, 2), )
if mibBuilder.loadTexts: hpicfReloadTable.setStatus('current')
hpicfReloadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpicfReloadEntry.setStatus('current')
hpicfReloadControl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2, 2, 1, 1), ReloadControl()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfReloadControl.setStatus('current')
hpicfReloadDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfReloadDateTime.setStatus('current')
hpicfReloadGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 1))
hpicfReloadCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 2))
hpicfReloadGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 1, 1)).setObjects(("HP-ICF-RELOAD-MIB", "hpicfReloadState"), ("HP-ICF-RELOAD-MIB", "hpicfReloadAfter"), ("HP-ICF-RELOAD-MIB", "hpicfReloadAt"), ("HP-ICF-RELOAD-MIB", "hpicfReloadControl"), ("HP-ICF-RELOAD-MIB", "hpicfReloadDateTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfReloadGroup = hpicfReloadGroup.setStatus('current')
hpicfReloadFullCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 2, 1)).setObjects(("HP-ICF-RELOAD-MIB", "hpicfReloadGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfReloadFullCompliance1 = hpicfReloadFullCompliance1.setStatus('current')
hpicfReloadFullCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 2, 2)).setObjects(("HP-ICF-RELOAD-MIB", "hpicfReloadGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfReloadFullCompliance2 = hpicfReloadFullCompliance2.setStatus('current')
hpicfReloadReadOnlyCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 2, 3)).setObjects(("HP-ICF-RELOAD-MIB", "hpicfReloadGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfReloadReadOnlyCompliance1 = hpicfReloadReadOnlyCompliance1.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-RELOAD-MIB", hpicfReloadState=hpicfReloadState, hpicfReloadControl=hpicfReloadControl, hpicfEntityReload=hpicfEntityReload, hpicfReloadDateTime=hpicfReloadDateTime, hpicfReloadCompliances=hpicfReloadCompliances, hpicfReloadConformance=hpicfReloadConformance, hpicfReloadGroups=hpicfReloadGroups, hpicfReloadTable=hpicfReloadTable, hpicfReloadGroup=hpicfReloadGroup, hpicfReloadReadOnlyCompliance1=hpicfReloadReadOnlyCompliance1, hpicfReloadObjects=hpicfReloadObjects, ReloadControl=ReloadControl, hpicfReloadFullCompliance1=hpicfReloadFullCompliance1, hpicfReloadFullCompliance2=hpicfReloadFullCompliance2, hpicfReloadEntry=hpicfReloadEntry, PYSNMP_MODULE_ID=hpicfReloadMIB, hpicfReloadAfter=hpicfReloadAfter, hpicfReloadAt=hpicfReloadAt, hpicfReloadMIB=hpicfReloadMIB)
