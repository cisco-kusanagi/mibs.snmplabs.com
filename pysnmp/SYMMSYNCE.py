#
# PySNMP MIB module SYMMSYNCE (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMSYNCE
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:29 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifNumber, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifNumber", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, Integer32, Bits, Unsigned32, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks, ObjectIdentity, Counter64, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Bits", "Unsigned32", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Counter64", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
EnableValue, symmPhysicalSignal = mibBuilder.importSymbols("SYMM-COMMON-SMI", "EnableValue", "symmPhysicalSignal")
symmSyncE = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8))
symmSyncE.setRevisions(('2011-02-24 17:47',))
if mibBuilder.loadTexts: symmSyncE.setLastUpdated('201102241746Z')
if mibBuilder.loadTexts: symmSyncE.setOrganization('Symmetricom')
class SYNCEPQLMODE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("bidirectional", 1), ("unidirectional", 2))

class DateAndTime(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d,1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
class TLatAndLon(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a1d:1d:1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

class TAntHeight(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a2d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class TLocalTimeOffset(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TSsm(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

syncEStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1))
syncEOutputStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1, 1), )
if mibBuilder.loadTexts: syncEOutputStatusTable.setStatus('current')
syncEOutputStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMSYNCE", "syncEOutputStatusIndex"))
if mibBuilder.loadTexts: syncEOutputStatusEntry.setStatus('current')
syncEOutputStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: syncEOutputStatusIndex.setStatus('current')
syncEOutputEsmcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEOutputEsmcStatus.setStatus('current')
syncEOutputStatusRxQL = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEOutputStatusRxQL.setStatus('current')
syncEOutputStatusTxQL = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEOutputStatusTxQL.setStatus('current')
syncEConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2))
syncEOutputConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2, 1), )
if mibBuilder.loadTexts: syncEOutputConfigTable.setStatus('current')
syncEOutputConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMSYNCE", "syncEOutputConfigIndex"))
if mibBuilder.loadTexts: syncEOutputConfigEntry.setStatus('current')
syncEOutputConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: syncEOutputConfigIndex.setStatus('current')
syncEOutputEsmcState = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2, 1, 1, 2), EnableValue().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syncEOutputEsmcState.setStatus('current')
syncEOutputQLState = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2, 1, 1, 3), EnableValue().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syncEOutputQLState.setStatus('current')
syncEOutputQLMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2, 1, 1, 4), SYNCEPQLMODE().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syncEOutputQLMode.setStatus('current')
syncEConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 3))
if mibBuilder.loadTexts: syncEConformance.setStatus('current')
syncECompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 3, 1))
syncEBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 3, 1, 1)).setObjects(("SYMMSYNCE", "syncEOutputStatusGroup"), ("SYMMSYNCE", "syncEConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syncEBasicCompliance = syncEBasicCompliance.setStatus('current')
syncEUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 3, 2))
syncEOutputStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 3, 2, 1)).setObjects(("SYMMSYNCE", "syncEOutputEsmcStatus"), ("SYMMSYNCE", "syncEOutputStatusRxQL"), ("SYMMSYNCE", "syncEOutputStatusTxQL"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syncEOutputStatusGroup = syncEOutputStatusGroup.setStatus('current')
syncEConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 3, 2, 2)).setObjects(("SYMMSYNCE", "syncEOutputEsmcState"), ("SYMMSYNCE", "syncEOutputQLState"), ("SYMMSYNCE", "syncEOutputQLMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syncEConfigGroup = syncEConfigGroup.setStatus('current')
mibBuilder.exportSymbols("SYMMSYNCE", syncEOutputStatusTable=syncEOutputStatusTable, syncEOutputStatusTxQL=syncEOutputStatusTxQL, syncEConformance=syncEConformance, SYNCEPQLMODE=SYNCEPQLMODE, syncECompliances=syncECompliances, syncEOutputConfigEntry=syncEOutputConfigEntry, syncEOutputQLState=syncEOutputQLState, syncEConfigGroup=syncEConfigGroup, syncEOutputStatusRxQL=syncEOutputStatusRxQL, TSsm=TSsm, TAntHeight=TAntHeight, syncEOutputQLMode=syncEOutputQLMode, TLocalTimeOffset=TLocalTimeOffset, syncEConfig=syncEConfig, syncEOutputConfigTable=syncEOutputConfigTable, syncEOutputEsmcState=syncEOutputEsmcState, syncEBasicCompliance=syncEBasicCompliance, DateAndTime=DateAndTime, syncEOutputEsmcStatus=syncEOutputEsmcStatus, PYSNMP_MODULE_ID=symmSyncE, syncEUocGroups=syncEUocGroups, TLatAndLon=TLatAndLon, syncEStatus=syncEStatus, syncEOutputConfigIndex=syncEOutputConfigIndex, syncEOutputStatusIndex=syncEOutputStatusIndex, symmSyncE=symmSyncE, syncEOutputStatusEntry=syncEOutputStatusEntry, syncEOutputStatusGroup=syncEOutputStatusGroup)
