#
# PySNMP MIB module CISCO-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FIREWALL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:41:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, NotificationType, TimeTicks, IpAddress, Counter64, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, Bits, iso, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "TimeTicks", "IpAddress", "Counter64", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "Bits", "iso", "Gauge32", "Unsigned32")
TextualConvention, DisplayString, RowPointer, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowPointer", "DateAndTime")
ciscoFirewallMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 147))
ciscoFirewallMIB.setRevisions(('2005-12-06 00:00', '1999-04-29 12:00',))
if mibBuilder.loadTexts: ciscoFirewallMIB.setLastUpdated('200512060000Z')
if mibBuilder.loadTexts: ciscoFirewallMIB.setOrganization('Cisco Systems, Inc.')
ciscoFirewallMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 1))
cfwEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1))
cfwBasicEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1))
cfwNetEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2))
cfwSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2))
cfwStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1))
cfwStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2))
class ResourceStatistics(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("highUse", 1), ("highLoad", 2), ("maximum", 3), ("minimum", 4), ("low", 5), ("high", 6), ("average", 7), ("free", 8), ("inUse", 9))

class Hardware(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("memory", 1), ("disk", 2), ("power", 3), ("netInterface", 4), ("cpu", 5), ("primaryUnit", 6), ("secondaryUnit", 7), ("other", 8))

class Services(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41))
    namedValues = NamedValues(("otherFWService", 1), ("fileXferFtp", 2), ("fileXferTftp", 3), ("fileXferFtps", 4), ("loginTelnet", 5), ("loginRlogin", 6), ("loginTelnets", 7), ("remoteExecSunRPC", 8), ("remoteExecMSRPC", 9), ("remoteExecRsh", 10), ("remoteExecXserver", 11), ("webHttp", 12), ("webHttps", 13), ("mailSmtp", 14), ("multimediaStreamworks", 15), ("multimediaH323", 16), ("multimediaNetShow", 17), ("multimediaVDOLive", 18), ("multimediaRealAV", 19), ("multimediaRTSP", 20), ("dbOracle", 21), ("dbMSsql", 22), ("contInspProgLang", 23), ("contInspUrl", 24), ("directoryNis", 25), ("directoryDns", 26), ("directoryNetbiosns", 27), ("directoryNetbiosdgm", 28), ("directoryNetbiosssn", 29), ("directoryWins", 30), ("qryWhois", 31), ("qryFinger", 32), ("qryIdent", 33), ("fsNfsStatus", 34), ("fsNfs", 35), ("fsCifs", 36), ("protoIcmp", 37), ("protoTcp", 38), ("protoUdp", 39), ("protoIp", 40), ("protoSnmp", 41))

class HardwareStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("other", 1), ("up", 2), ("down", 3), ("error", 4), ("overTemp", 5), ("busy", 6), ("noMedia", 7), ("backup", 8), ("active", 9), ("standby", 10))

class SecurityEvent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("none", 2), ("dos", 3), ("recon", 4), ("pakFwd", 5), ("addrSpoof", 6), ("svcSpoof", 7), ("thirdParty", 8), ("complete", 9), ("invalPak", 10), ("illegCom", 11), ("policy", 12))

class ContentInspectionEvent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("okay", 2), ("error", 3), ("found", 4), ("clean", 5), ("reject", 6), ("saved", 7))

class ConnectionEvent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("other", 1), ("accept", 2), ("error", 3), ("drop", 4), ("close", 5), ("timeout", 6), ("refused", 7), ("reset", 8), ("noResp", 9))

class ConnectionStat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("totalOpen", 2), ("currentOpen", 3), ("currentClosing", 4), ("currentHalfOpen", 5), ("currentInUse", 6), ("high", 7))

class AccessEvent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("grant", 2), ("deny", 3), ("denyMult", 4), ("error", 5))

class AuthenticationEvent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("succ", 2), ("error", 3), ("fail", 4), ("succPriv", 5), ("failPriv", 6), ("failMult", 7))

class GenericEvent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("abnormal", 1), ("okay", 2), ("error", 3))

cfwBasicEventsTableLastRow = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicEventsTableLastRow.setStatus('current')
cfwBasicEventsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2), )
if mibBuilder.loadTexts: cfwBasicEventsTable.setStatus('current')
cfwBasicEventsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-FIREWALL-MIB", "cfwBasicEventIndex"))
if mibBuilder.loadTexts: cfwBasicEventsEntry.setStatus('current')
cfwBasicEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cfwBasicEventIndex.setStatus('current')
cfwBasicEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicEventTime.setStatus('current')
cfwBasicSecurityEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 3), SecurityEvent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicSecurityEventType.setStatus('current')
cfwBasicContentInspEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 4), ContentInspectionEvent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicContentInspEventType.setStatus('current')
cfwBasicConnectionEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 5), ConnectionEvent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicConnectionEventType.setStatus('current')
cfwBasicAccessEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 6), AccessEvent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicAccessEventType.setStatus('current')
cfwBasicAuthenticationEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 7), AuthenticationEvent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicAuthenticationEventType.setStatus('current')
cfwBasicGenericEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 8), GenericEvent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicGenericEventType.setStatus('current')
cfwBasicEventDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicEventDescription.setStatus('current')
cfwBasicEventDetailsTableRow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 10), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBasicEventDetailsTableRow.setStatus('current')
cfwNetEventsTableLastRow = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventsTableLastRow.setStatus('current')
cfwNetEventsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2), )
if mibBuilder.loadTexts: cfwNetEventsTable.setStatus('current')
cfwNetEventsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-FIREWALL-MIB", "cfwNetEventIndex"))
if mibBuilder.loadTexts: cfwNetEventsEntry.setStatus('current')
cfwNetEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cfwNetEventIndex.setStatus('current')
cfwNetEventInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventInterface.setStatus('current')
cfwNetEventSrcIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventSrcIpAddress.setStatus('current')
cfwNetEventInsideSrcIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventInsideSrcIpAddress.setStatus('current')
cfwNetEventDstIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventDstIpAddress.setStatus('current')
cfwNetEventInsideDstIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventInsideDstIpAddress.setStatus('current')
cfwNetEventSrcIpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventSrcIpPort.setStatus('current')
cfwNetEventInsideSrcIpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventInsideSrcIpPort.setStatus('current')
cfwNetEventDstIpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventDstIpPort.setStatus('current')
cfwNetEventInsideDstIpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventInsideDstIpPort.setStatus('current')
cfwNetEventService = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 11), Services()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventService.setStatus('current')
cfwNetEventServiceInformation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventServiceInformation.setStatus('current')
cfwNetEventIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 13), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventIdentity.setStatus('current')
cfwNetEventDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 14), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwNetEventDescription.setStatus('current')
cfwHardwareStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1, 1), )
if mibBuilder.loadTexts: cfwHardwareStatusTable.setStatus('current')
cfwHardwareStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1, 1, 1), ).setIndexNames((0, "CISCO-FIREWALL-MIB", "cfwHardwareType"))
if mibBuilder.loadTexts: cfwHardwareStatusEntry.setStatus('current')
cfwHardwareType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1, 1, 1, 1), Hardware())
if mibBuilder.loadTexts: cfwHardwareType.setStatus('current')
cfwHardwareInformation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwHardwareInformation.setStatus('current')
cfwHardwareStatusValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1, 1, 1, 3), HardwareStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwHardwareStatusValue.setStatus('current')
cfwHardwareStatusDetail = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwHardwareStatusDetail.setStatus('current')
cfwBufferStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 1), )
if mibBuilder.loadTexts: cfwBufferStatsTable.setStatus('current')
cfwBufferStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 1, 1), ).setIndexNames((0, "CISCO-FIREWALL-MIB", "cfwBufferStatSize"), (0, "CISCO-FIREWALL-MIB", "cfwBufferStatType"))
if mibBuilder.loadTexts: cfwBufferStatsEntry.setStatus('current')
cfwBufferStatSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cfwBufferStatSize.setStatus('current')
cfwBufferStatType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 1, 1, 2), ResourceStatistics())
if mibBuilder.loadTexts: cfwBufferStatType.setStatus('current')
cfwBufferStatInformation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBufferStatInformation.setStatus('current')
cfwBufferStatValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwBufferStatValue.setStatus('current')
cfwConnectionStatTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2), )
if mibBuilder.loadTexts: cfwConnectionStatTable.setStatus('current')
cfwConnectionStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2, 1), ).setIndexNames((0, "CISCO-FIREWALL-MIB", "cfwConnectionStatService"), (0, "CISCO-FIREWALL-MIB", "cfwConnectionStatType"))
if mibBuilder.loadTexts: cfwConnectionStatEntry.setStatus('current')
cfwConnectionStatService = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2, 1, 1), Services())
if mibBuilder.loadTexts: cfwConnectionStatService.setStatus('current')
cfwConnectionStatType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2, 1, 2), ConnectionStat())
if mibBuilder.loadTexts: cfwConnectionStatType.setStatus('current')
cfwConnectionStatDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwConnectionStatDescription.setStatus('current')
cfwConnectionStatCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwConnectionStatCount.setStatus('current')
cfwConnectionStatValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfwConnectionStatValue.setStatus('current')
ciscoFirewallMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 2))
ciscoFirewallMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0))
cfwSecurityNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0, 2)).setObjects(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"), ("CISCO-FIREWALL-MIB", "cfwBasicSecurityEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
if mibBuilder.loadTexts: cfwSecurityNotification.setStatus('current')
cfwContentInspectNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0, 3)).setObjects(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"), ("CISCO-FIREWALL-MIB", "cfwBasicContentInspEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
if mibBuilder.loadTexts: cfwContentInspectNotification.setStatus('current')
cfwConnNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0, 4)).setObjects(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"), ("CISCO-FIREWALL-MIB", "cfwBasicConnectionEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
if mibBuilder.loadTexts: cfwConnNotification.setStatus('current')
cfwAccessNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0, 5)).setObjects(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"), ("CISCO-FIREWALL-MIB", "cfwBasicAccessEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
if mibBuilder.loadTexts: cfwAccessNotification.setStatus('current')
cfwAuthNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0, 6)).setObjects(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"), ("CISCO-FIREWALL-MIB", "cfwBasicAuthenticationEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
if mibBuilder.loadTexts: cfwAuthNotification.setStatus('current')
cfwGenericNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0, 7)).setObjects(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"), ("CISCO-FIREWALL-MIB", "cfwBasicGenericEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
if mibBuilder.loadTexts: cfwGenericNotification.setStatus('current')
ciscoFirewallMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 3))
ciscoFirewallMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 1))
ciscoFirewallMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 2))
ciscoFirewallMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 1, 1)).setObjects(("CISCO-FIREWALL-MIB", "ciscoFirewallMIBStatisticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFirewallMIBCompliance = ciscoFirewallMIBCompliance.setStatus('deprecated')
ciscoFirewallMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 1, 2)).setObjects(("CISCO-FIREWALL-MIB", "ciscoFirewallMIBStatisticsGroup"), ("CISCO-FIREWALL-MIB", "ciscoFirewallMIBEventsGroup"), ("CISCO-FIREWALL-MIB", "ciscoFirewallMIBNotificationGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFirewallMIBComplianceRev1 = ciscoFirewallMIBComplianceRev1.setStatus('current')
ciscoFirewallMIBEventsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 2, 1)).setObjects(("CISCO-FIREWALL-MIB", "cfwBasicEventsTableLastRow"), ("CISCO-FIREWALL-MIB", "cfwBasicEventTime"), ("CISCO-FIREWALL-MIB", "cfwBasicSecurityEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicContentInspEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicConnectionEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicAccessEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicAuthenticationEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicGenericEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"), ("CISCO-FIREWALL-MIB", "cfwNetEventsTableLastRow"), ("CISCO-FIREWALL-MIB", "cfwNetEventInterface"), ("CISCO-FIREWALL-MIB", "cfwNetEventSrcIpAddress"), ("CISCO-FIREWALL-MIB", "cfwNetEventInsideSrcIpAddress"), ("CISCO-FIREWALL-MIB", "cfwNetEventDstIpAddress"), ("CISCO-FIREWALL-MIB", "cfwNetEventInsideDstIpAddress"), ("CISCO-FIREWALL-MIB", "cfwNetEventSrcIpPort"), ("CISCO-FIREWALL-MIB", "cfwNetEventInsideSrcIpPort"), ("CISCO-FIREWALL-MIB", "cfwNetEventDstIpPort"), ("CISCO-FIREWALL-MIB", "cfwNetEventInsideDstIpPort"), ("CISCO-FIREWALL-MIB", "cfwNetEventService"), ("CISCO-FIREWALL-MIB", "cfwNetEventServiceInformation"), ("CISCO-FIREWALL-MIB", "cfwNetEventIdentity"), ("CISCO-FIREWALL-MIB", "cfwNetEventDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFirewallMIBEventsGroup = ciscoFirewallMIBEventsGroup.setStatus('current')
ciscoFirewallMIBStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 2, 2)).setObjects(("CISCO-FIREWALL-MIB", "cfwHardwareInformation"), ("CISCO-FIREWALL-MIB", "cfwHardwareStatusValue"), ("CISCO-FIREWALL-MIB", "cfwHardwareStatusDetail"), ("CISCO-FIREWALL-MIB", "cfwBufferStatInformation"), ("CISCO-FIREWALL-MIB", "cfwBufferStatValue"), ("CISCO-FIREWALL-MIB", "cfwConnectionStatDescription"), ("CISCO-FIREWALL-MIB", "cfwConnectionStatCount"), ("CISCO-FIREWALL-MIB", "cfwConnectionStatValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFirewallMIBStatisticsGroup = ciscoFirewallMIBStatisticsGroup.setStatus('current')
ciscoFirewallMIBNotificationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 2, 3)).setObjects(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"), ("CISCO-FIREWALL-MIB", "cfwBasicSecurityEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicContentInspEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicConnectionEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicAccessEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicAuthenticationEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicGenericEventType"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"), ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFirewallMIBNotificationGroup = ciscoFirewallMIBNotificationGroup.setStatus('obsolete')
ciscoFirewallMIBNotificationGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 2, 4)).setObjects(("CISCO-FIREWALL-MIB", "cfwSecurityNotification"), ("CISCO-FIREWALL-MIB", "cfwContentInspectNotification"), ("CISCO-FIREWALL-MIB", "cfwConnNotification"), ("CISCO-FIREWALL-MIB", "cfwAccessNotification"), ("CISCO-FIREWALL-MIB", "cfwAuthNotification"), ("CISCO-FIREWALL-MIB", "cfwGenericNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFirewallMIBNotificationGroupRev1 = ciscoFirewallMIBNotificationGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-FIREWALL-MIB", cfwBasicEvents=cfwBasicEvents, ciscoFirewallMIBGroups=ciscoFirewallMIBGroups, cfwNetEventService=cfwNetEventService, cfwBasicEventIndex=cfwBasicEventIndex, cfwNetEvents=cfwNetEvents, cfwStatus=cfwStatus, cfwNetEventsTable=cfwNetEventsTable, cfwNetEventInsideSrcIpAddress=cfwNetEventInsideSrcIpAddress, cfwNetEventIndex=cfwNetEventIndex, cfwAuthNotification=cfwAuthNotification, cfwNetEventsTableLastRow=cfwNetEventsTableLastRow, cfwConnectionStatTable=cfwConnectionStatTable, cfwBufferStatsTable=cfwBufferStatsTable, cfwStatistics=cfwStatistics, cfwNetEventInsideDstIpPort=cfwNetEventInsideDstIpPort, cfwConnectionStatService=cfwConnectionStatService, cfwNetEventInterface=cfwNetEventInterface, AccessEvent=AccessEvent, cfwNetEventInsideSrcIpPort=cfwNetEventInsideSrcIpPort, ciscoFirewallMIBEventsGroup=ciscoFirewallMIBEventsGroup, cfwHardwareStatusValue=cfwHardwareStatusValue, cfwBasicEventTime=cfwBasicEventTime, cfwBufferStatsEntry=cfwBufferStatsEntry, ciscoFirewallMIBNotificationGroup=ciscoFirewallMIBNotificationGroup, ciscoFirewallMIBCompliance=ciscoFirewallMIBCompliance, ConnectionEvent=ConnectionEvent, cfwBasicEventDetailsTableRow=cfwBasicEventDetailsTableRow, ciscoFirewallMIBComplianceRev1=ciscoFirewallMIBComplianceRev1, cfwHardwareStatusEntry=cfwHardwareStatusEntry, ciscoFirewallMIB=ciscoFirewallMIB, cfwHardwareType=cfwHardwareType, SecurityEvent=SecurityEvent, cfwConnectionStatType=cfwConnectionStatType, cfwBufferStatSize=cfwBufferStatSize, cfwConnectionStatDescription=cfwConnectionStatDescription, cfwBufferStatInformation=cfwBufferStatInformation, cfwNetEventsEntry=cfwNetEventsEntry, cfwBufferStatType=cfwBufferStatType, HardwareStatus=HardwareStatus, cfwConnectionStatCount=cfwConnectionStatCount, cfwNetEventInsideDstIpAddress=cfwNetEventInsideDstIpAddress, cfwAccessNotification=cfwAccessNotification, ciscoFirewallMIBStatisticsGroup=ciscoFirewallMIBStatisticsGroup, cfwBasicSecurityEventType=cfwBasicSecurityEventType, cfwEvents=cfwEvents, cfwBasicEventsTableLastRow=cfwBasicEventsTableLastRow, GenericEvent=GenericEvent, ResourceStatistics=ResourceStatistics, cfwConnNotification=cfwConnNotification, ciscoFirewallMIBNotifications=ciscoFirewallMIBNotifications, cfwHardwareInformation=cfwHardwareInformation, AuthenticationEvent=AuthenticationEvent, cfwNetEventDstIpPort=cfwNetEventDstIpPort, Services=Services, cfwSecurityNotification=cfwSecurityNotification, cfwBasicGenericEventType=cfwBasicGenericEventType, ciscoFirewallMIBObjects=ciscoFirewallMIBObjects, ciscoFirewallMIBCompliances=ciscoFirewallMIBCompliances, cfwNetEventIdentity=cfwNetEventIdentity, cfwBasicAccessEventType=cfwBasicAccessEventType, ciscoFirewallMIBConformance=ciscoFirewallMIBConformance, PYSNMP_MODULE_ID=ciscoFirewallMIB, cfwConnectionStatValue=cfwConnectionStatValue, ConnectionStat=ConnectionStat, cfwNetEventDstIpAddress=cfwNetEventDstIpAddress, cfwNetEventSrcIpPort=cfwNetEventSrcIpPort, cfwSystem=cfwSystem, cfwHardwareStatusTable=cfwHardwareStatusTable, ciscoFirewallMIBNotificationGroupRev1=ciscoFirewallMIBNotificationGroupRev1, cfwBufferStatValue=cfwBufferStatValue, cfwGenericNotification=cfwGenericNotification, cfwContentInspectNotification=cfwContentInspectNotification, cfwBasicAuthenticationEventType=cfwBasicAuthenticationEventType, cfwNetEventServiceInformation=cfwNetEventServiceInformation, Hardware=Hardware, cfwNetEventSrcIpAddress=cfwNetEventSrcIpAddress, cfwBasicEventsTable=cfwBasicEventsTable, cfwHardwareStatusDetail=cfwHardwareStatusDetail, cfwBasicEventDescription=cfwBasicEventDescription, ciscoFirewallMIBNotificationPrefix=ciscoFirewallMIBNotificationPrefix, cfwNetEventDescription=cfwNetEventDescription, cfwBasicConnectionEventType=cfwBasicConnectionEventType, cfwBasicEventsEntry=cfwBasicEventsEntry, cfwBasicContentInspEventType=cfwBasicContentInspEventType, ContentInspectionEvent=ContentInspectionEvent, cfwConnectionStatEntry=cfwConnectionStatEntry)
