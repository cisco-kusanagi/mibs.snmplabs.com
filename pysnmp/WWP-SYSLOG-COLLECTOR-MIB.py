#
# PySNMP MIB module WWP-SYSLOG-COLLECTOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-SYSLOG-COLLECTOR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:32:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, MibIdentifier, Counter32, iso, Integer32, TimeTicks, Counter64, Unsigned32, ModuleIdentity, IpAddress, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "MibIdentifier", "Counter32", "iso", "Integer32", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32")
RowStatus, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TruthValue")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpSyslogCollectorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 46))
wwpSyslogCollectorMIB.setRevisions(('2003-01-21 10:12',))
if mibBuilder.loadTexts: wwpSyslogCollectorMIB.setLastUpdated('200301211012Z')
if mibBuilder.loadTexts: wwpSyslogCollectorMIB.setOrganization(' World Wide Packets Inc')
class SyslogFacility(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 99))
    namedValues = NamedValues(("kernel", 0), ("user", 1), ("mail", 2), ("daemon", 3), ("auth", 4), ("syslog", 5), ("lpr", 6), ("news", 7), ("uucp", 8), ("cron", 9), ("authPriv", 10), ("ftp", 11), ("ntp", 12), ("security", 13), ("console", 14), ("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23), ("noMap", 99))

class SyslogSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 99))
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7), ("other", 99))

wwpSyslogCollMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1))
wwpSyslogSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 1))
wwpSyslogColl = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2))
wwpSyslogCollMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 46, 2))
wwpSyslogCollMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 46, 2, 0))
wwpSyslogCollMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 46, 3))
wwpSyslogCollMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 46, 3, 1))
wwpSyslogCollMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 46, 3, 2))
wwpSyslogEnable = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpSyslogEnable.setStatus('current')
wwpSyslogCollectorTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1), )
if mibBuilder.loadTexts: wwpSyslogCollectorTable.setStatus('current')
wwpSyslogCollectorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1), ).setIndexNames((0, "WWP-SYSLOG-COLLECTOR-MIB", "wwpSyslogCollectorAddr"))
if mibBuilder.loadTexts: wwpSyslogCollectorEntry.setStatus('current')
wwpSyslogCollectorAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpSyslogCollectorAddr.setStatus('current')
wwpSyslogCollectorUDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(514)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpSyslogCollectorUDPPort.setStatus('current')
wwpSyslogCollectorFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1, 3), SyslogFacility().clone('daemon')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpSyslogCollectorFacility.setStatus('current')
wwpSyslogCollectorMinSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1, 4), SyslogSeverity().clone('error')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpSyslogCollectorMinSeverity.setStatus('current')
wwpSyslogCollectorMaxSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1, 5), SyslogSeverity().clone('emergency')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpSyslogCollectorMaxSeverity.setStatus('current')
wwpSyslogCollectorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpSyslogCollectorStatus.setStatus('current')
mibBuilder.exportSymbols("WWP-SYSLOG-COLLECTOR-MIB", wwpSyslogCollMIBCompliances=wwpSyslogCollMIBCompliances, wwpSyslogCollMIBConformance=wwpSyslogCollMIBConformance, wwpSyslogCollectorEntry=wwpSyslogCollectorEntry, wwpSyslogCollMIBGroups=wwpSyslogCollMIBGroups, PYSNMP_MODULE_ID=wwpSyslogCollectorMIB, wwpSyslogColl=wwpSyslogColl, wwpSyslogCollectorMinSeverity=wwpSyslogCollectorMinSeverity, wwpSyslogCollectorMaxSeverity=wwpSyslogCollectorMaxSeverity, wwpSyslogCollectorUDPPort=wwpSyslogCollectorUDPPort, wwpSyslogCollectorMIB=wwpSyslogCollectorMIB, wwpSyslogCollMIBObjects=wwpSyslogCollMIBObjects, wwpSyslogSystem=wwpSyslogSystem, SyslogSeverity=SyslogSeverity, wwpSyslogEnable=wwpSyslogEnable, wwpSyslogCollectorStatus=wwpSyslogCollectorStatus, wwpSyslogCollectorFacility=wwpSyslogCollectorFacility, wwpSyslogCollMIBNotifications=wwpSyslogCollMIBNotifications, SyslogFacility=SyslogFacility, wwpSyslogCollMIBNotificationPrefix=wwpSyslogCollMIBNotificationPrefix, wwpSyslogCollectorAddr=wwpSyslogCollectorAddr, wwpSyslogCollectorTable=wwpSyslogCollectorTable)
