#
# PySNMP MIB module CTRON-SFPS-FLOOD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-SFPS-FLOOD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:30:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
sfpsResolveCounter, sfpsMobileUserTable, sfpsMobileUserReset, sfpsISPFlood = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsResolveCounter", "sfpsMobileUserTable", "sfpsMobileUserReset", "sfpsISPFlood")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, IpAddress, MibIdentifier, TimeTicks, Counter32, ModuleIdentity, Bits, Gauge32, NotificationType, ObjectIdentity, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "IpAddress", "MibIdentifier", "TimeTicks", "Counter32", "ModuleIdentity", "Bits", "Gauge32", "NotificationType", "ObjectIdentity", "Counter64", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class HexInteger(Integer32):
    pass

class SfpsAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

sfpsServiceCenterFloodTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1), )
if mibBuilder.loadTexts: sfpsServiceCenterFloodTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterFloodTable.setDescription('This table gives flood semantics to call processing.')
sfpsServiceCenterFloodEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1, 1), ).setIndexNames((0, "CTRON-SFPS-FLOOD-MIB", "sfpsServiceCenterFloodAddress"))
if mibBuilder.loadTexts: sfpsServiceCenterFloodEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterFloodEntry.setDescription('Each entry contains the configuration of the Flood Entry.')
sfpsServiceCenterFloodAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1, 1, 1), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterFloodAddress.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterFloodAddress.setDescription('Server hash, part of instance key.')
sfpsServiceCenterFloodMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterFloodMetric.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterFloodMetric.setDescription('Defines order servers are called low to high.')
sfpsServiceCenterFloodName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterFloodName.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterFloodName.setDescription('Server name.')
sfpsServiceCenterFloodOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("kStatusRunning", 1), ("kStatusHalted", 2), ("kStatusPending", 3), ("kStatusFaulted", 4), ("kStatusNotStarted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterFloodOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterFloodOperStatus.setDescription('Operational state of entry.')
sfpsServiceCenterFloodAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsServiceCenterFloodAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterFloodAdminStatus.setDescription('Administrative State of Entry.')
sfpsServiceCenterFloodStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterFloodStatusTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterFloodStatusTime.setDescription('Time Tick of last operStatus change.')
sfpsServiceCenterFloodRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterFloodRequests.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterFloodRequests.setDescription('Requests made to server.')
sfpsServiceCenterFloodResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterFloodResponses.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsServiceCenterFloodResponses.setDescription('GOOD replies by server.')
sfpsMobileUserTableAOType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMobileUserTableAOType.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMobileUserTableAOType.setDescription('')
sfpsMobileUserTableAOValue = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMobileUserTableAOValue.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMobileUserTableAOValue.setDescription('')
sfpsMobileUserTableCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMobileUserTableCount.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMobileUserTableCount.setDescription('')
sfpsMobileUserTableNewSwitch = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 1, 4), SfpsAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMobileUserTableNewSwitch.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMobileUserTableNewSwitch.setDescription('')
sfpsMobileUserTableLastSeen = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 1, 5), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsMobileUserTableLastSeen.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMobileUserTableLastSeen.setDescription('')
sfpsMobileUserTableFirstSceen = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 1, 6), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsMobileUserTableFirstSceen.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMobileUserTableFirstSceen.setDescription('')
sfpsMobileUserTablePort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsMobileUserTablePort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMobileUserTablePort.setDescription('')
sfpsMobileUserResetReset = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 2, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsMobileUserResetReset.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMobileUserResetReset.setDescription('')
sfpsMobileUserResetCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsMobileUserResetCount.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsMobileUserResetCount.setDescription('')
sfpsResolveCounterTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8, 1), )
if mibBuilder.loadTexts: sfpsResolveCounterTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsResolveCounterTable.setDescription('')
sfpsResolveCounterTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8, 1, 1), ).setIndexNames((0, "CTRON-SFPS-FLOOD-MIB", "sfpsResolveCounterTableSource"))
if mibBuilder.loadTexts: sfpsResolveCounterTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsResolveCounterTableEntry.setDescription('')
sfpsResolveCounterTableSource = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8, 1, 1, 1), SfpsAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsResolveCounterTableSource.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsResolveCounterTableSource.setDescription('')
sfpsResolveCounterTableNumReq = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsResolveCounterTableNumReq.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsResolveCounterTableNumReq.setDescription('')
sfpsResolveCounterTableNumRep = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsResolveCounterTableNumRep.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsResolveCounterTableNumRep.setDescription('')
sfpsResolveCounterTableNumUnkRep = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsResolveCounterTableNumUnkRep.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsResolveCounterTableNumUnkRep.setDescription('')
sfpsResolveCounterTableTicReq = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsResolveCounterTableTicReq.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsResolveCounterTableTicReq.setDescription('')
sfpsResolveCounterTableTicRep = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsResolveCounterTableTicRep.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsResolveCounterTableTicRep.setDescription('')
sfpsResolveCounterTableTicUnkRep = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8, 1, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsResolveCounterTableTicUnkRep.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsResolveCounterTableTicUnkRep.setDescription('')
mibBuilder.exportSymbols("CTRON-SFPS-FLOOD-MIB", sfpsMobileUserResetReset=sfpsMobileUserResetReset, sfpsMobileUserTableAOType=sfpsMobileUserTableAOType, sfpsServiceCenterFloodResponses=sfpsServiceCenterFloodResponses, sfpsResolveCounterTableSource=sfpsResolveCounterTableSource, sfpsMobileUserTableCount=sfpsMobileUserTableCount, sfpsResolveCounterTableTicUnkRep=sfpsResolveCounterTableTicUnkRep, sfpsMobileUserTablePort=sfpsMobileUserTablePort, sfpsServiceCenterFloodTable=sfpsServiceCenterFloodTable, sfpsServiceCenterFloodName=sfpsServiceCenterFloodName, HexInteger=HexInteger, sfpsResolveCounterTableNumUnkRep=sfpsResolveCounterTableNumUnkRep, sfpsMobileUserTableAOValue=sfpsMobileUserTableAOValue, sfpsServiceCenterFloodEntry=sfpsServiceCenterFloodEntry, sfpsServiceCenterFloodMetric=sfpsServiceCenterFloodMetric, sfpsServiceCenterFloodOperStatus=sfpsServiceCenterFloodOperStatus, sfpsResolveCounterTableEntry=sfpsResolveCounterTableEntry, sfpsServiceCenterFloodAddress=sfpsServiceCenterFloodAddress, SfpsAddress=SfpsAddress, sfpsServiceCenterFloodStatusTime=sfpsServiceCenterFloodStatusTime, sfpsResolveCounterTableNumReq=sfpsResolveCounterTableNumReq, sfpsResolveCounterTableNumRep=sfpsResolveCounterTableNumRep, sfpsServiceCenterFloodAdminStatus=sfpsServiceCenterFloodAdminStatus, sfpsResolveCounterTable=sfpsResolveCounterTable, sfpsServiceCenterFloodRequests=sfpsServiceCenterFloodRequests, sfpsMobileUserTableLastSeen=sfpsMobileUserTableLastSeen, sfpsMobileUserTableNewSwitch=sfpsMobileUserTableNewSwitch, sfpsResolveCounterTableTicRep=sfpsResolveCounterTableTicRep, sfpsMobileUserTableFirstSceen=sfpsMobileUserTableFirstSceen, sfpsResolveCounterTableTicReq=sfpsResolveCounterTableTicReq, sfpsMobileUserResetCount=sfpsMobileUserResetCount)
