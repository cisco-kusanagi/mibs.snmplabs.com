#
# PySNMP MIB module H3C-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-SYSLOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:10:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ModuleIdentity, TimeTicks, ObjectIdentity, Integer32, Unsigned32, Bits, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Integer32", "Unsigned32", "Bits", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "NotificationType", "Counter64")
TextualConvention, TruthValue, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "RowStatus")
h3cSyslog = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63))
if mibBuilder.loadTexts: h3cSyslog.setLastUpdated('200905050000Z')
if mibBuilder.loadTexts: h3cSyslog.setOrganization('Huawei-3com Technologies Co., Ltd.')
class MessageLevelType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("informational", 7), ("debug", 8))

class TimeStampType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("date", 2), ("boot", 3), ("dateWithoutYear", 4))

class FacilityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("kernel", 0), ("userLevel", 1), ("mailSystem", 2), ("systemDaemons", 3), ("securityAuthorization", 4), ("internallyMessages", 5), ("linePrinter", 6), ("networkNews", 7), ("uucp", 8), ("clockDaemon", 9), ("securityAuthorization2", 10), ("ftpDaemon", 11), ("ntp", 12), ("logAudit", 13), ("logAlert", 14), ("clockDaemon2", 15), ("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23))

h3cSyslogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1))
h3cSyslogObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 1))
h3cSyslogState = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSyslogState.setStatus('current')
h3cSyslogMaxLoghost = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSyslogMaxLoghost.setStatus('current')
h3cSyslogMaxChannel = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSyslogMaxChannel.setStatus('current')
h3cSyslogMaxLogbufferSize = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSyslogMaxLogbufferSize.setStatus('current')
h3cSyslogMaxTrapbufferSize = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSyslogMaxTrapbufferSize.setStatus('current')
h3cSyslogConsole = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 2))
h3cSyslogConsoleChannel = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 2, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSyslogConsoleChannel.setStatus('current')
h3cSyslogMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 3))
h3cSyslogMonitorChannel = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 3, 1), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSyslogMonitorChannel.setStatus('current')
h3cSyslogSnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 4))
h3cSyslogSnmpChannel = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 4, 1), Integer32().clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSyslogSnmpChannel.setStatus('current')
h3cSyslogLogbuffer = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 5))
h3cSyslogLogbufferChannel = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 5, 1), Integer32().clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSyslogLogbufferChannel.setStatus('current')
h3cSyslogLogbufferSize = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 5, 2), Integer32().clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSyslogLogbufferSize.setStatus('current')
h3cSyslogLogbufferTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 5, 3), )
if mibBuilder.loadTexts: h3cSyslogLogbufferTable.setStatus('current')
h3cSyslogLogbufferEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 5, 3, 1), ).setIndexNames((0, "H3C-SYSLOG-MIB", "h3cLogbufferIndex"))
if mibBuilder.loadTexts: h3cSyslogLogbufferEntry.setStatus('current')
h3cLogbufferIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 5, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cLogbufferIndex.setStatus('current')
h3cLogbufferCurrentMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 5, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLogbufferCurrentMessages.setStatus('current')
h3cLogbufferOverwrittenMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 5, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLogbufferOverwrittenMessages.setStatus('current')
h3cLogbufferDroppedMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 5, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLogbufferDroppedMessages.setStatus('current')
h3cSyslogTrapbuffer = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 6))
h3cSyslogTrapbufferChannel = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 6, 1), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSyslogTrapbufferChannel.setStatus('current')
h3cSyslogTrapbufferSize = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 6, 2), Integer32().clone(256)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSyslogTrapbufferSize.setStatus('current')
h3cSyslogTrapbufferTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 6, 3), )
if mibBuilder.loadTexts: h3cSyslogTrapbufferTable.setStatus('current')
h3cSyslogTrapbufferEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 6, 3, 1), ).setIndexNames((0, "H3C-SYSLOG-MIB", "h3cTrapbufferIndex"))
if mibBuilder.loadTexts: h3cSyslogTrapbufferEntry.setStatus('current')
h3cTrapbufferIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 6, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cTrapbufferIndex.setStatus('current')
h3cTrapbufferCurrentMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 6, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTrapbufferCurrentMessages.setStatus('current')
h3cTrapbufferOverwrittenMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 6, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTrapbufferOverwrittenMessages.setStatus('current')
h3cTrapbufferDroppedMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 6, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTrapbufferDroppedMessages.setStatus('current')
h3cSyslogLoghost = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7))
h3cSyslogLoghostSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSyslogLoghostSourceInterface.setStatus('current')
h3cSyslogLoghostTimestampType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 2), TimeStampType().clone('date')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSyslogLoghostTimestampType.setStatus('current')
h3cSyslogLoghostTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3), )
if mibBuilder.loadTexts: h3cSyslogLoghostTable.setStatus('current')
h3cSyslogLoghostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3, 1), ).setIndexNames((0, "H3C-SYSLOG-MIB", "h3cSyslogLoghostIndex"))
if mibBuilder.loadTexts: h3cSyslogLoghostEntry.setStatus('current')
h3cSyslogLoghostIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: h3cSyslogLoghostIndex.setStatus('current')
h3cSyslogLoghostChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3, 1, 2), Integer32().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSyslogLoghostChannel.setStatus('current')
h3cSyslogLoghostIpaddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3, 1, 3), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSyslogLoghostIpaddressType.setStatus('current')
h3cSyslogLoghostIpaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSyslogLoghostIpaddress.setStatus('current')
h3cSyslogLoghostFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3, 1, 5), FacilityType().clone('local7')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSyslogLoghostFacility.setStatus('current')
h3cSyslogLoghostLanguage = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("chinese", 1), ("english", 2))).clone('english')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSyslogLoghostLanguage.setStatus('current')
h3cSyslogLoghostOperateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSyslogLoghostOperateRowStatus.setStatus('current')
h3cSyslogLoghostIpaddressPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 7, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(514)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSyslogLoghostIpaddressPort.setStatus('current')
h3cSyslogChannel = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 8))
h3cSyslogChannelTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 8, 1), )
if mibBuilder.loadTexts: h3cSyslogChannelTable.setStatus('current')
h3cSyslogChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 8, 1, 1), ).setIndexNames((0, "H3C-SYSLOG-MIB", "h3cSyslogChannelIndex"))
if mibBuilder.loadTexts: h3cSyslogChannelEntry.setStatus('current')
h3cSyslogChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 8, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cSyslogChannelIndex.setStatus('current')
h3cSyslogChannelName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 8, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSyslogChannelName.setStatus('current')
h3cSyslogModule = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 9))
h3cSyslogModuleTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 9, 1), )
if mibBuilder.loadTexts: h3cSyslogModuleTable.setStatus('current')
h3cSyslogModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 9, 1, 1), ).setIndexNames((0, "H3C-SYSLOG-MIB", "h3cSyslogModuleIndex"))
if mibBuilder.loadTexts: h3cSyslogModuleEntry.setStatus('current')
h3cSyslogModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 9, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cSyslogModuleIndex.setStatus('current')
h3cSyslogModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 9, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSyslogModuleName.setStatus('current')
h3cSyslogLog = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 10))
h3cSyslogLogTimestampType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 10, 1), TimeStampType().clone('date')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSyslogLogTimestampType.setStatus('current')
h3cSyslogLogTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 10, 2), )
if mibBuilder.loadTexts: h3cSyslogLogTable.setStatus('current')
h3cSyslogLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 10, 2, 1), ).setIndexNames((0, "H3C-SYSLOG-MIB", "h3cSyslogChannelIndex"), (0, "H3C-SYSLOG-MIB", "h3cSyslogModuleIndex"))
if mibBuilder.loadTexts: h3cSyslogLogEntry.setStatus('current')
h3cSyslogLogState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 10, 2, 1, 1), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSyslogLogState.setStatus('current')
h3cSyslogLogLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 10, 2, 1, 2), MessageLevelType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSyslogLogLevel.setStatus('current')
h3cSyslogLogRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 10, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSyslogLogRowStatus.setStatus('current')
h3cSyslogTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 11))
h3cSyslogTrapTimestampType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 11, 1), TimeStampType().clone('date')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSyslogTrapTimestampType.setStatus('current')
h3cSyslogTrapTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 11, 2), )
if mibBuilder.loadTexts: h3cSyslogTrapTable.setStatus('current')
h3cSyslogTrapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 11, 2, 1), ).setIndexNames((0, "H3C-SYSLOG-MIB", "h3cSyslogChannelIndex"), (0, "H3C-SYSLOG-MIB", "h3cSyslogModuleIndex"))
if mibBuilder.loadTexts: h3cSyslogTrapEntry.setStatus('current')
h3cSyslogTrapState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 11, 2, 1, 1), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSyslogTrapState.setStatus('current')
h3cSyslogTrapLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 11, 2, 1, 2), MessageLevelType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSyslogTrapLevel.setStatus('current')
h3cSyslogTrapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 11, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSyslogTrapRowStatus.setStatus('current')
h3cSyslogDebug = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 12))
h3cSyslogDebugTimestampType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 12, 1), TimeStampType().clone('boot')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSyslogDebugTimestampType.setStatus('current')
h3cSyslogDebugTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 12, 2), )
if mibBuilder.loadTexts: h3cSyslogDebugTable.setStatus('current')
h3cSyslogDebugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 12, 2, 1), ).setIndexNames((0, "H3C-SYSLOG-MIB", "h3cSyslogChannelIndex"), (0, "H3C-SYSLOG-MIB", "h3cSyslogModuleIndex"))
if mibBuilder.loadTexts: h3cSyslogDebugEntry.setStatus('current')
h3cSyslogDebugState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 12, 2, 1, 1), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSyslogDebugState.setStatus('current')
h3cSyslogDebugLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 12, 2, 1, 2), MessageLevelType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSyslogDebugLevel.setStatus('current')
h3cSyslogDebugRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 63, 1, 12, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSyslogDebugRowStatus.setStatus('current')
mibBuilder.exportSymbols("H3C-SYSLOG-MIB", h3cSyslogTrapTable=h3cSyslogTrapTable, FacilityType=FacilityType, h3cSyslogTrapRowStatus=h3cSyslogTrapRowStatus, h3cSyslogChannelTable=h3cSyslogChannelTable, h3cLogbufferDroppedMessages=h3cLogbufferDroppedMessages, h3cSyslogMaxLoghost=h3cSyslogMaxLoghost, h3cTrapbufferOverwrittenMessages=h3cTrapbufferOverwrittenMessages, h3cSyslogMaxTrapbufferSize=h3cSyslogMaxTrapbufferSize, h3cSyslogTrapbufferTable=h3cSyslogTrapbufferTable, h3cSyslogLogbufferSize=h3cSyslogLogbufferSize, h3cSyslogTrapTimestampType=h3cSyslogTrapTimestampType, h3cLogbufferIndex=h3cLogbufferIndex, h3cSyslogLoghostIpaddressPort=h3cSyslogLoghostIpaddressPort, h3cSyslogTrapbuffer=h3cSyslogTrapbuffer, h3cSyslogLogTable=h3cSyslogLogTable, h3cSyslogTrapbufferEntry=h3cSyslogTrapbufferEntry, h3cSyslogConsoleChannel=h3cSyslogConsoleChannel, h3cSyslogDebugEntry=h3cSyslogDebugEntry, h3cSyslogDebugTimestampType=h3cSyslogDebugTimestampType, h3cSyslogModuleEntry=h3cSyslogModuleEntry, h3cSyslogTrap=h3cSyslogTrap, MessageLevelType=MessageLevelType, h3cSyslogLoghostChannel=h3cSyslogLoghostChannel, h3cSyslogLoghostFacility=h3cSyslogLoghostFacility, h3cSyslogChannelEntry=h3cSyslogChannelEntry, h3cSyslogLogTimestampType=h3cSyslogLogTimestampType, h3cSyslogLoghostIpaddressType=h3cSyslogLoghostIpaddressType, h3cSyslogModuleIndex=h3cSyslogModuleIndex, h3cSyslogObject=h3cSyslogObject, h3cSyslogChannelName=h3cSyslogChannelName, h3cSyslogLogRowStatus=h3cSyslogLogRowStatus, h3cSyslogMaxLogbufferSize=h3cSyslogMaxLogbufferSize, h3cSyslogDebugState=h3cSyslogDebugState, h3cTrapbufferDroppedMessages=h3cTrapbufferDroppedMessages, h3cSyslogLogLevel=h3cSyslogLogLevel, h3cSyslogDebug=h3cSyslogDebug, h3cSyslogTrapLevel=h3cSyslogTrapLevel, h3cSyslogModule=h3cSyslogModule, h3cSyslogLogbufferEntry=h3cSyslogLogbufferEntry, h3cSyslogLogbufferChannel=h3cSyslogLogbufferChannel, h3cSyslogLoghostSourceInterface=h3cSyslogLoghostSourceInterface, h3cSyslogLogEntry=h3cSyslogLogEntry, h3cSyslogDebugLevel=h3cSyslogDebugLevel, h3cSyslogState=h3cSyslogState, h3cSyslogSnmpChannel=h3cSyslogSnmpChannel, PYSNMP_MODULE_ID=h3cSyslog, h3cSyslogTrapbufferChannel=h3cSyslogTrapbufferChannel, h3cSyslogChannelIndex=h3cSyslogChannelIndex, h3cSyslogTrapState=h3cSyslogTrapState, h3cSyslogLoghostTable=h3cSyslogLoghostTable, h3cSyslogLoghostIpaddress=h3cSyslogLoghostIpaddress, h3cLogbufferCurrentMessages=h3cLogbufferCurrentMessages, h3cTrapbufferCurrentMessages=h3cTrapbufferCurrentMessages, h3cSyslogLogState=h3cSyslogLogState, h3cSyslogLoghostLanguage=h3cSyslogLoghostLanguage, h3cSyslogMonitorChannel=h3cSyslogMonitorChannel, h3cSyslogChannel=h3cSyslogChannel, h3cSyslogSnmp=h3cSyslogSnmp, h3cSyslogLoghostTimestampType=h3cSyslogLoghostTimestampType, h3cSyslogObjects=h3cSyslogObjects, TimeStampType=TimeStampType, h3cSyslogMonitor=h3cSyslogMonitor, h3cSyslogDebugRowStatus=h3cSyslogDebugRowStatus, h3cSyslogLoghost=h3cSyslogLoghost, h3cSyslogLog=h3cSyslogLog, h3cSyslogLoghostIndex=h3cSyslogLoghostIndex, h3cTrapbufferIndex=h3cTrapbufferIndex, h3cSyslogTrapbufferSize=h3cSyslogTrapbufferSize, h3cLogbufferOverwrittenMessages=h3cLogbufferOverwrittenMessages, h3cSyslog=h3cSyslog, h3cSyslogTrapEntry=h3cSyslogTrapEntry, h3cSyslogLoghostEntry=h3cSyslogLoghostEntry, h3cSyslogModuleName=h3cSyslogModuleName, h3cSyslogModuleTable=h3cSyslogModuleTable, h3cSyslogLogbufferTable=h3cSyslogLogbufferTable, h3cSyslogLoghostOperateRowStatus=h3cSyslogLoghostOperateRowStatus, h3cSyslogDebugTable=h3cSyslogDebugTable, h3cSyslogMaxChannel=h3cSyslogMaxChannel, h3cSyslogConsole=h3cSyslogConsole, h3cSyslogLogbuffer=h3cSyslogLogbuffer)
