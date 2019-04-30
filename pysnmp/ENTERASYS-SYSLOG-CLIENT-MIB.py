#
# PySNMP MIB module ENTERASYS-SYSLOG-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-SYSLOG-CLIENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:50:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, ModuleIdentity, Counter32, iso, Counter64, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, IpAddress, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Counter32", "iso", "Counter64", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "IpAddress", "NotificationType", "Bits")
TimeStamp, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "RowStatus", "TextualConvention")
etsysSyslogClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14))
etsysSyslogClientMIB.setRevisions(('2011-03-08 20:15', '2009-07-17 14:38', '2009-02-17 20:53', '2009-01-16 18:59', '2003-11-06 15:15', '2003-07-31 14:19', '2001-12-03 19:55', '2001-08-08 00:00',))
if mibBuilder.loadTexts: etsysSyslogClientMIB.setLastUpdated('201103082015Z')
if mibBuilder.loadTexts: etsysSyslogClientMIB.setOrganization('Enterasys Networks')
class SyslogUdpPort(TextualConvention, Unsigned32):
    status = 'current'

class SyslogFacility(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23))

class SyslogSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("info", 7), ("debug", 8))

etsysSyslogClient = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 1))
etsysSyslogServer = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2))
etsysSyslogApplication = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 3))
etsysSyslogNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 5))
etsysSyslogClientMessages = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSyslogClientMessages.setStatus('current')
etsysSyslogClientMessagesDropped = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSyslogClientMessagesDropped.setStatus('current')
etsysSyslogClientLastMessageTime = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSyslogClientLastMessageTime.setStatus('current')
etsysSyslogClientControl = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 1, 4), Bits().clone(namedValues=NamedValues(("etsysSyslogClientControlConsoleLogging", 0), ("etsysSyslogClientControlPersistentLogging", 1), ("etsysSyslogClientControlSecurePersistentLogging", 2))).clone(namedValues=NamedValues(("etsysSyslogClientControlConsoleLogging", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSyslogClientControl.setStatus('current')
etsysSyslogClientSecureMessagesDropped = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSyslogClientSecureMessagesDropped.setStatus('current')
etsysSyslogServerMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSyslogServerMaxEntries.setStatus('current')
etsysSyslogServerNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSyslogServerNumEntries.setStatus('current')
etsysSyslogServerTableNextAvailableIndex = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSyslogServerTableNextAvailableIndex.setStatus('current')
etsysSyslogServerTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4), )
if mibBuilder.loadTexts: etsysSyslogServerTable.setStatus('current')
etsysSyslogServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1), ).setIndexNames((0, "ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerIndex"))
if mibBuilder.loadTexts: etsysSyslogServerEntry.setStatus('current')
etsysSyslogServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: etsysSyslogServerIndex.setStatus('current')
etsysSyslogServerDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysSyslogServerDescription.setStatus('current')
etsysSyslogServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysSyslogServerAddressType.setStatus('current')
etsysSyslogServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysSyslogServerAddress.setStatus('current')
etsysSyslogServerUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1, 5), SyslogUdpPort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysSyslogServerUdpPort.setStatus('current')
etsysSyslogServerFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1, 6), SyslogFacility()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysSyslogServerFacility.setStatus('current')
etsysSyslogServerSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1, 7), SyslogSeverity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysSyslogServerSeverity.setStatus('current')
etsysSyslogServerMessagesIgnored = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSyslogServerMessagesIgnored.setStatus('current')
etsysSyslogServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 4, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysSyslogServerRowStatus.setStatus('current')
etsysSyslogServerDefaultUdpPort = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 5), SyslogUdpPort().clone(514)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSyslogServerDefaultUdpPort.setStatus('current')
etsysSyslogServerDefaultFacility = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 6), SyslogFacility().clone('local7')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSyslogServerDefaultFacility.setStatus('current')
etsysSyslogServerDefaultSeverity = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 2, 7), SyslogSeverity().clone('error')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSyslogServerDefaultSeverity.setStatus('current')
etsysSyslogApplicationTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 3, 1), )
if mibBuilder.loadTexts: etsysSyslogApplicationTable.setStatus('current')
etsysSyslogApplicationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 3, 1, 1), ).setIndexNames((0, "ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogApplicationIndex"))
if mibBuilder.loadTexts: etsysSyslogApplicationEntry.setStatus('current')
etsysSyslogApplicationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 3, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: etsysSyslogApplicationIndex.setStatus('current')
etsysSyslogApplicationDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 3, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSyslogApplicationDescription.setStatus('current')
etsysSyslogApplicationMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 3, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSyslogApplicationMnemonic.setStatus('current')
etsysSyslogApplicationSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 3, 1, 1, 4), SyslogSeverity().clone('error')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSyslogApplicationSeverity.setStatus('current')
etsysSyslogApplicationAllowedServers = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 3, 1, 1, 5), Bits().clone(namedValues=NamedValues(("etsysSyslogServerIndex1", 0), ("etsysSyslogServerIndex2", 1), ("etsysSyslogServerIndex3", 2), ("etsysSyslogServerIndex4", 3), ("etsysSyslogServerIndex5", 4), ("etsysSyslogServerIndex6", 5), ("etsysSyslogServerIndex7", 6), ("etsysSyslogServerIndex8", 7), ("etsysSyslogServerConsole", 8), ("etsysSyslogServerFile", 9), ("etsysSyslogServerSecureFile", 10))).clone(namedValues=NamedValues(("etsysSyslogServerIndex1", 0), ("etsysSyslogServerIndex2", 1), ("etsysSyslogServerIndex3", 2), ("etsysSyslogServerIndex4", 3), ("etsysSyslogServerIndex5", 4), ("etsysSyslogServerIndex6", 5), ("etsysSyslogServerIndex7", 6), ("etsysSyslogServerIndex8", 7), ("etsysSyslogServerConsole", 8), ("etsysSyslogServerFile", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSyslogApplicationAllowedServers.setStatus('current')
etsysSyslogSecureLogArchiveNotification = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 5, 1))
if mibBuilder.loadTexts: etsysSyslogSecureLogArchiveNotification.setStatus('current')
etsysSyslogSecureLogDroppedMsgNotification = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 5, 2)).setObjects(("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogClientSecureMessagesDropped"))
if mibBuilder.loadTexts: etsysSyslogSecureLogDroppedMsgNotification.setStatus('current')
etsysSyslogClientConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4))
etsysSyslogClientGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 1))
etsysSyslogClientCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 2))
etsysSyslogClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 1, 1)).setObjects(("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogClientMessages"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogClientMessagesDropped"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogClientLastMessageTime"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogClientControl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSyslogClientGroup = etsysSyslogClientGroup.setStatus('current')
etsysSyslogServerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 1, 2)).setObjects(("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerMaxEntries"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerNumEntries"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerTableNextAvailableIndex"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerDescription"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerAddressType"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerAddress"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerUdpPort"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerFacility"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerSeverity"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerMessagesIgnored"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSyslogServerGroup = etsysSyslogServerGroup.setStatus('current')
etsysSyslogApplicationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 1, 3)).setObjects(("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogApplicationDescription"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogApplicationMnemonic"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogApplicationSeverity"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogApplicationAllowedServers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSyslogApplicationGroup = etsysSyslogApplicationGroup.setStatus('current')
etsysSyslogServerDefaultsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 1, 4)).setObjects(("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerDefaultUdpPort"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerDefaultFacility"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerDefaultSeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSyslogServerDefaultsGroup = etsysSyslogServerDefaultsGroup.setStatus('current')
etsysSyslogNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 1, 5)).setObjects(("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogSecureLogArchiveNotification"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogSecureLogDroppedMsgNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSyslogNotificationGroup = etsysSyslogNotificationGroup.setStatus('current')
etsysSyslogSecureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 1, 6)).setObjects(("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogClientSecureMessagesDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSyslogSecureGroup = etsysSyslogSecureGroup.setStatus('current')
etsysSyslogClientCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 2, 1)).setObjects(("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogClientGroup"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerGroup"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogServerDefaultsGroup"), ("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogApplicationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSyslogClientCompliance = etsysSyslogClientCompliance.setStatus('current')
etsysSyslogNotificationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 2, 2)).setObjects(("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSyslogNotificationCompliance = etsysSyslogNotificationCompliance.setStatus('current')
etsysSyslogSecureCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 14, 4, 2, 3)).setObjects(("ENTERASYS-SYSLOG-CLIENT-MIB", "etsysSyslogSecureGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSyslogSecureCompliance = etsysSyslogSecureCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-SYSLOG-CLIENT-MIB", etsysSyslogClientCompliance=etsysSyslogClientCompliance, etsysSyslogServerTableNextAvailableIndex=etsysSyslogServerTableNextAvailableIndex, etsysSyslogApplicationDescription=etsysSyslogApplicationDescription, etsysSyslogServerGroup=etsysSyslogServerGroup, etsysSyslogNotification=etsysSyslogNotification, etsysSyslogServerTable=etsysSyslogServerTable, etsysSyslogServerDefaultUdpPort=etsysSyslogServerDefaultUdpPort, etsysSyslogServerUdpPort=etsysSyslogServerUdpPort, etsysSyslogClientCompliances=etsysSyslogClientCompliances, etsysSyslogClientLastMessageTime=etsysSyslogClientLastMessageTime, etsysSyslogSecureLogArchiveNotification=etsysSyslogSecureLogArchiveNotification, etsysSyslogServerDefaultFacility=etsysSyslogServerDefaultFacility, etsysSyslogApplicationMnemonic=etsysSyslogApplicationMnemonic, etsysSyslogServerNumEntries=etsysSyslogServerNumEntries, etsysSyslogClientGroup=etsysSyslogClientGroup, SyslogFacility=SyslogFacility, SyslogUdpPort=SyslogUdpPort, etsysSyslogClientMessagesDropped=etsysSyslogClientMessagesDropped, etsysSyslogApplicationTable=etsysSyslogApplicationTable, etsysSyslogServerEntry=etsysSyslogServerEntry, etsysSyslogClientMIB=etsysSyslogClientMIB, etsysSyslogClientConformance=etsysSyslogClientConformance, etsysSyslogApplicationGroup=etsysSyslogApplicationGroup, etsysSyslogServerDefaultsGroup=etsysSyslogServerDefaultsGroup, etsysSyslogServerRowStatus=etsysSyslogServerRowStatus, SyslogSeverity=SyslogSeverity, etsysSyslogApplicationAllowedServers=etsysSyslogApplicationAllowedServers, etsysSyslogClientControl=etsysSyslogClientControl, etsysSyslogApplicationIndex=etsysSyslogApplicationIndex, etsysSyslogClientSecureMessagesDropped=etsysSyslogClientSecureMessagesDropped, etsysSyslogClient=etsysSyslogClient, etsysSyslogServerFacility=etsysSyslogServerFacility, etsysSyslogClientGroups=etsysSyslogClientGroups, etsysSyslogNotificationGroup=etsysSyslogNotificationGroup, etsysSyslogServerDescription=etsysSyslogServerDescription, etsysSyslogServerIndex=etsysSyslogServerIndex, etsysSyslogServerMaxEntries=etsysSyslogServerMaxEntries, etsysSyslogApplication=etsysSyslogApplication, etsysSyslogServer=etsysSyslogServer, etsysSyslogServerSeverity=etsysSyslogServerSeverity, etsysSyslogNotificationCompliance=etsysSyslogNotificationCompliance, etsysSyslogServerMessagesIgnored=etsysSyslogServerMessagesIgnored, etsysSyslogSecureCompliance=etsysSyslogSecureCompliance, etsysSyslogServerAddress=etsysSyslogServerAddress, etsysSyslogApplicationEntry=etsysSyslogApplicationEntry, etsysSyslogServerAddressType=etsysSyslogServerAddressType, etsysSyslogClientMessages=etsysSyslogClientMessages, etsysSyslogServerDefaultSeverity=etsysSyslogServerDefaultSeverity, PYSNMP_MODULE_ID=etsysSyslogClientMIB, etsysSyslogApplicationSeverity=etsysSyslogApplicationSeverity, etsysSyslogSecureLogDroppedMsgNotification=etsysSyslogSecureLogDroppedMsgNotification, etsysSyslogSecureGroup=etsysSyslogSecureGroup)
