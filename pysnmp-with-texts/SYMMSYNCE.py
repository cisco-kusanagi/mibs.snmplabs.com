#
# PySNMP MIB module SYMMSYNCE (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMSYNCE
# Produced by pysmi-0.3.4 at Tue Jul 30 11:35:09 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifNumber, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifNumber", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Unsigned32, Counter32, ModuleIdentity, Integer32, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, NotificationType, iso, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "Counter32", "ModuleIdentity", "Integer32", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "NotificationType", "iso", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
EnableValue, symmPhysicalSignal = mibBuilder.importSymbols("SYMM-COMMON-SMI", "EnableValue", "symmPhysicalSignal")
symmSyncE = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8))
symmSyncE.setRevisions(('2011-02-24 17:47',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: symmSyncE.setRevisionsDescriptions(('Symmetricom common SyncE',))
if mibBuilder.loadTexts: symmSyncE.setLastUpdated('201102241746Z')
if mibBuilder.loadTexts: symmSyncE.setOrganization('Symmetricom')
if mibBuilder.loadTexts: symmSyncE.setContactInfo('Symmetricom Technical Support 1-888-367-7966 toll free USA 1-408-428-7907 worldwide Support@symmetricom.com')
if mibBuilder.loadTexts: symmSyncE.setDescription('This is the Symmetricom Common MIB for SyncE. It has two main nodes: SyncE status and SyncE configuration.')
class SYNCEPQLMODE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("bidirectional", 1), ("unidirectional", 2))

class DateAndTime(TextualConvention, OctetString):
    description = "A date-time specification. field octets contents range ----- ------ -------- ----- 1 1-2 year* 0..65536 2 3 month 1..12 3 4 day 1..31 4 5 hour 0..23 5 6 minutes 0..59 6 7 seconds 0..60 (use 60 for leap-second) 7 8 deci-seconds 0..9 8 9 direction from UTC '+' / '-' 9 10 hours from UTC* 0..13 10 11 minutes from UTC 0..59 * Notes: - the value of year is in network-byte order - daylight saving time in New Zealand is +13 For example, Tuesday May 26, 1992 at 1:30:15 PM EDT would be displayed as: 1992-5-26,13:30:15.0,-4:0 Note that if only local time is known, then timezone information (fields 8-10) is not present."
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d,1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
class TLatAndLon(TextualConvention, OctetString):
    description = "antenna latitude and longitude specification. field octets contents range ----- ------ -------- ----- 1 1 +/-180 deg '+' / '-' 2 2 degree 0..180 3 3 minute 0..59 4 4 second 0..59 5 5 second fraction 0..99 +/- dd:mm:ss.ss "
    status = 'current'
    displayHint = '1a1d:1d:1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

class TAntHeight(TextualConvention, OctetString):
    description = "antenna height specification. field octets contents range ----- ------ -------- ----- 1 1 +/- '+' / '-' 2 2-3 meter 0..10000 3 4 meter fraction 0..99 +/- hh.hh "
    status = 'current'
    displayHint = '1a2d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class TLocalTimeOffset(TextualConvention, OctetString):
    description = "A local time offset specification. field octets contents range ----- ------ -------- ----- 1 1 direction from UTC '+' / '-' 2 2 hours from UTC* 0..13 3 3 minutes from UTC 0..59 * Notes: - the value of year is in network-byte order - The hours range is 0..13 For example, the -6 local time offset would be displayed as: -6:0 "
    status = 'current'
    displayHint = '1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TSsm(TextualConvention, Integer32):
    description = 'The ssm hex code'
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

syncEStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1))
syncEOutputStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1, 1), )
if mibBuilder.loadTexts: syncEOutputStatusTable.setStatus('current')
if mibBuilder.loadTexts: syncEOutputStatusTable.setDescription("SyncE output status table. It monitors whether ESMC and QL are enabled or disabled. SyncE 'output' indicates that the port is intended as a SyncE clock master port.")
syncEOutputStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMSYNCE", "syncEOutputStatusIndex"))
if mibBuilder.loadTexts: syncEOutputStatusEntry.setStatus('current')
if mibBuilder.loadTexts: syncEOutputStatusEntry.setDescription('An entry of the SyncE output status table. Table index is ifIndex (port and interface index).')
syncEOutputStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: syncEOutputStatusIndex.setStatus('current')
if mibBuilder.loadTexts: syncEOutputStatusIndex.setDescription('Local index of the SyncE output status table.')
syncEOutputEsmcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEOutputEsmcStatus.setStatus('current')
if mibBuilder.loadTexts: syncEOutputEsmcStatus.setDescription('SyncE output port ESMC state. It can be Enable (1) or Disable (2). If ESMC state is disabled, ESMC is not used.')
syncEOutputStatusRxQL = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEOutputStatusRxQL.setStatus('current')
if mibBuilder.loadTexts: syncEOutputStatusRxQL.setDescription("Received QL value. This is the SSM value in the incoming ESMC. Its value can be actual or 'n/a.' In the asynchronous mode the SSM value is 'n/a.'")
syncEOutputStatusTxQL = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEOutputStatusTxQL.setStatus('current')
if mibBuilder.loadTexts: syncEOutputStatusTxQL.setDescription("Transmitted QL value. This is the SSM value in the outgoing ESMC. Its value can be actual or 'n/a.' In the asynchronous mode the SSM value is 'n/a.'")
syncEConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2))
syncEOutputConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2, 1), )
if mibBuilder.loadTexts: syncEOutputConfigTable.setStatus('current')
if mibBuilder.loadTexts: syncEOutputConfigTable.setDescription('SyncE output port configuration table.')
syncEOutputConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMSYNCE", "syncEOutputConfigIndex"))
if mibBuilder.loadTexts: syncEOutputConfigEntry.setStatus('current')
if mibBuilder.loadTexts: syncEOutputConfigEntry.setDescription('An entry of the SyncE output configuration table. Table index is IfIndex (port and interface index).')
syncEOutputConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: syncEOutputConfigIndex.setStatus('current')
if mibBuilder.loadTexts: syncEOutputConfigIndex.setDescription('Local index of the SyncE output configuration table.')
syncEOutputEsmcState = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2, 1, 1, 2), EnableValue().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syncEOutputEsmcState.setStatus('current')
if mibBuilder.loadTexts: syncEOutputEsmcState.setDescription('SyncE output port ESMC state. It can be either Enable (1) or Disable (2). If ESMC is disabled, ESMC messages are not sent.')
syncEOutputQLState = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2, 1, 1, 3), EnableValue().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syncEOutputQLState.setStatus('current')
if mibBuilder.loadTexts: syncEOutputQLState.setDescription('SyncE output port QL state. It can either Enable (1) or Disable (2). ')
syncEOutputQLMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2, 1, 1, 4), SYNCEPQLMODE().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syncEOutputQLMode.setStatus('current')
if mibBuilder.loadTexts: syncEOutputQLMode.setDescription('SyncE output port output QL mode. It can be unidirectional or bidirectional. In the unidirectional mode, the outgoing QL value is independent of the incoming QL value. In the bidirectional mode, the outgoing QL value is changed to DNU if it is the same as the incoming QL value. ')
syncEConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 3))
if mibBuilder.loadTexts: syncEConformance.setStatus('current')
if mibBuilder.loadTexts: syncEConformance.setDescription('This subtree contains conformance statements for the SYMMETRICOM-LED-MIB module. ')
syncECompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 3, 1))
syncEBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 3, 1, 1)).setObjects(("SYMMSYNCE", "syncEOutputStatusGroup"), ("SYMMSYNCE", "syncEConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syncEBasicCompliance = syncEBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: syncEBasicCompliance.setDescription('The compliance statement for SNMP entities which have SyncE packet service.')
syncEUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 3, 2))
syncEOutputStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 3, 2, 1)).setObjects(("SYMMSYNCE", "syncEOutputEsmcStatus"), ("SYMMSYNCE", "syncEOutputStatusRxQL"), ("SYMMSYNCE", "syncEOutputStatusTxQL"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syncEOutputStatusGroup = syncEOutputStatusGroup.setStatus('current')
if mibBuilder.loadTexts: syncEOutputStatusGroup.setDescription('Description.')
syncEConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 3, 2, 2)).setObjects(("SYMMSYNCE", "syncEOutputEsmcState"), ("SYMMSYNCE", "syncEOutputQLState"), ("SYMMSYNCE", "syncEOutputQLMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syncEConfigGroup = syncEConfigGroup.setStatus('current')
if mibBuilder.loadTexts: syncEConfigGroup.setDescription('A collection of objects providing information applicable to SyncE configuration group.')
mibBuilder.exportSymbols("SYMMSYNCE", syncEOutputQLState=syncEOutputQLState, TLocalTimeOffset=TLocalTimeOffset, syncEOutputStatusEntry=syncEOutputStatusEntry, TLatAndLon=TLatAndLon, syncEOutputStatusTable=syncEOutputStatusTable, syncEOutputEsmcStatus=syncEOutputEsmcStatus, syncEBasicCompliance=syncEBasicCompliance, syncEConfigGroup=syncEConfigGroup, TAntHeight=TAntHeight, syncEOutputConfigIndex=syncEOutputConfigIndex, SYNCEPQLMODE=SYNCEPQLMODE, syncEStatus=syncEStatus, syncEOutputStatusIndex=syncEOutputStatusIndex, TSsm=TSsm, syncEOutputConfigEntry=syncEOutputConfigEntry, syncEOutputStatusRxQL=syncEOutputStatusRxQL, DateAndTime=DateAndTime, PYSNMP_MODULE_ID=symmSyncE, syncEOutputQLMode=syncEOutputQLMode, syncEOutputEsmcState=syncEOutputEsmcState, syncECompliances=syncECompliances, syncEOutputStatusGroup=syncEOutputStatusGroup, syncEConfig=syncEConfig, syncEUocGroups=syncEUocGroups, syncEOutputStatusTxQL=syncEOutputStatusTxQL, syncEConformance=syncEConformance, symmSyncE=symmSyncE, syncEOutputConfigTable=syncEOutputConfigTable)
