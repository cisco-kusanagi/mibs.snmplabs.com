#
# PySNMP MIB module WWP-SYSLOG-COLLECTOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-SYSLOG-COLLECTOR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:38:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, IpAddress, Integer32, Gauge32, Bits, MibIdentifier, Unsigned32, Counter32, TimeTicks, Counter64, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Integer32", "Gauge32", "Bits", "MibIdentifier", "Unsigned32", "Counter32", "TimeTicks", "Counter64", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TextualConvention, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "TruthValue")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpSyslogCollectorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 46))
wwpSyslogCollectorMIB.setRevisions(('2003-01-21 10:12',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wwpSyslogCollectorMIB.setRevisionsDescriptions(('Initial Creation',))
if mibBuilder.loadTexts: wwpSyslogCollectorMIB.setLastUpdated('200301211012Z')
if mibBuilder.loadTexts: wwpSyslogCollectorMIB.setOrganization(' World Wide Packets Inc')
if mibBuilder.loadTexts: wwpSyslogCollectorMIB.setContactInfo(' Mib Meister Postal: World Wide Packets P.O. Box 950 Veradale, WA 99037 USA Phone: +1 509 242 9000 Email: mib.meister@worldwidepackets.com')
if mibBuilder.loadTexts: wwpSyslogCollectorMIB.setDescription('A MIB module to manage syslog collectors on the LEOS based WWP products.')
class SyslogFacility(TextualConvention, Integer32):
    description = 'This textual convention enumerates the facilities that originate syslog messages. The value noMap(24) indicates that the appropriate facility will be provided by the individual applications on the managed entity. If this option is not available on a particular entity attempt set the facillity to this value will fail with an error-status of wrongValue.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 99))
    namedValues = NamedValues(("kernel", 0), ("user", 1), ("mail", 2), ("daemon", 3), ("auth", 4), ("syslog", 5), ("lpr", 6), ("news", 7), ("uucp", 8), ("cron", 9), ("authPriv", 10), ("ftp", 11), ("ntp", 12), ("security", 13), ("console", 14), ("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23), ("noMap", 99))

class SyslogSeverity(TextualConvention, Integer32):
    description = 'This textual convention enumerates the severity levels of syslog messages. The syslog protocol uses the values 0 (emergency), to 7 (debug).'
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
if mibBuilder.loadTexts: wwpSyslogEnable.setDescription('Specifies whether or not the syslog client is enabled. This is the system wide parameter and will overwrite any collector specific managed object to enable or disable the syslog client.')
wwpSyslogCollectorTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1), )
if mibBuilder.loadTexts: wwpSyslogCollectorTable.setStatus('current')
if mibBuilder.loadTexts: wwpSyslogCollectorTable.setDescription('A table containing Syslog collector information.')
wwpSyslogCollectorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1), ).setIndexNames((0, "WWP-SYSLOG-COLLECTOR-MIB", "wwpSyslogCollectorAddr"))
if mibBuilder.loadTexts: wwpSyslogCollectorEntry.setStatus('current')
if mibBuilder.loadTexts: wwpSyslogCollectorEntry.setDescription('Defines the information pertaining to a syslog collector to which a syslog messages will be relayed. Entries within this table with an access level of read- create MUST be considered non-volatile and MUST be maintained across entity resets.')
wwpSyslogCollectorAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpSyslogCollectorAddr.setStatus('current')
if mibBuilder.loadTexts: wwpSyslogCollectorAddr.setDescription('The Ip address for the Syslog message collector.')
wwpSyslogCollectorUDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(514)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpSyslogCollectorUDPPort.setStatus('current')
if mibBuilder.loadTexts: wwpSyslogCollectorUDPPort.setDescription('The port number on the destination to which the syslog message will be forwarded over the udp transport.')
wwpSyslogCollectorFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1, 3), SyslogFacility().clone('daemon')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpSyslogCollectorFacility.setStatus('current')
if mibBuilder.loadTexts: wwpSyslogCollectorFacility.setDescription('The syslog facility code that will added to messages forwarded to this collector. ')
wwpSyslogCollectorMinSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1, 4), SyslogSeverity().clone('error')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpSyslogCollectorMinSeverity.setStatus('current')
if mibBuilder.loadTexts: wwpSyslogCollectorMinSeverity.setDescription('Any syslog message with a severity less than the severity specified by this object will be ignored by the collector. note: serverity level numeric values increase as their severity decreases, e.g. error(3) is more severe than debug(7).')
wwpSyslogCollectorMaxSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1, 5), SyslogSeverity().clone('emergency')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpSyslogCollectorMaxSeverity.setStatus('current')
if mibBuilder.loadTexts: wwpSyslogCollectorMaxSeverity.setDescription('Any syslog message with a severity greater than the severity specified by this object will be ignored by the collector. note: serverity level numeric values increase as their severity decreases, e.g. error(3) is more severe than debug(7).')
wwpSyslogCollectorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 46, 1, 2, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpSyslogCollectorStatus.setStatus('current')
if mibBuilder.loadTexts: wwpSyslogCollectorStatus.setDescription("This object is used to create and delete rows in the wwpSyslogCollectorTable. To create a new row the management station must set the object to 'CreateAndGo'. The collector can be disabled by setting this object to 'notInService'. ")
mibBuilder.exportSymbols("WWP-SYSLOG-COLLECTOR-MIB", wwpSyslogCollMIBNotifications=wwpSyslogCollMIBNotifications, wwpSyslogCollectorTable=wwpSyslogCollectorTable, wwpSyslogEnable=wwpSyslogEnable, PYSNMP_MODULE_ID=wwpSyslogCollectorMIB, wwpSyslogCollectorMIB=wwpSyslogCollectorMIB, wwpSyslogColl=wwpSyslogColl, wwpSyslogCollectorStatus=wwpSyslogCollectorStatus, wwpSyslogCollectorAddr=wwpSyslogCollectorAddr, wwpSyslogCollMIBObjects=wwpSyslogCollMIBObjects, wwpSyslogSystem=wwpSyslogSystem, wwpSyslogCollMIBNotificationPrefix=wwpSyslogCollMIBNotificationPrefix, SyslogFacility=SyslogFacility, wwpSyslogCollectorUDPPort=wwpSyslogCollectorUDPPort, wwpSyslogCollMIBConformance=wwpSyslogCollMIBConformance, wwpSyslogCollMIBCompliances=wwpSyslogCollMIBCompliances, wwpSyslogCollectorMaxSeverity=wwpSyslogCollectorMaxSeverity, wwpSyslogCollectorMinSeverity=wwpSyslogCollectorMinSeverity, wwpSyslogCollectorEntry=wwpSyslogCollectorEntry, wwpSyslogCollMIBGroups=wwpSyslogCollMIBGroups, wwpSyslogCollectorFacility=wwpSyslogCollectorFacility, SyslogSeverity=SyslogSeverity)
