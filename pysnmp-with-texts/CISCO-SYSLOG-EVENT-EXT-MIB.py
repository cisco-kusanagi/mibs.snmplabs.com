#
# PySNMP MIB module CISCO-SYSLOG-EVENT-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SYSLOG-EVENT-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:13:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SyslogSeverity, = mibBuilder.importSymbols("CISCO-SYSLOG-MIB", "SyslogSeverity")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, iso, ModuleIdentity, Counter64, ObjectIdentity, MibIdentifier, Unsigned32, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "iso", "ModuleIdentity", "Counter64", "ObjectIdentity", "MibIdentifier", "Unsigned32", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSyslogEventExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 270))
ciscoSyslogEventExtMIB.setRevisions(('2002-02-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSyslogEventExtMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSyslogEventExtMIB.setLastUpdated('200202120000Z')
if mibBuilder.loadTexts: ciscoSyslogEventExtMIB.setOrganization('Cisco System Inc.')
if mibBuilder.loadTexts: ciscoSyslogEventExtMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive, San Jose CA 95134-1706. USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSyslogEventExtMIB.setDescription('This MIB module extends the Cisco Syslog MIB and provides network management support to handle and process Syslog messages as device events.')
ciscoSyslogEventExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 1))
cslogEventConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1))
class CslogEventDisposition(TextualConvention, Bits):
    description = 'This definition specifies the manner in which a Syslog message should be handled by the system as a device event. Events are first recorded by the Syslog subsystem, and then they can be counted, displayed on the console, or forward to external device. The four disposition mechanisms are: none(0) - Record only, no further handling. count(1) - All Syslog messages received after this bit is set will be counted according to their corresponding event types. display(2) - All Syslog messages received after this bit is set will be displayed on the device console, HTML console or WEB pages (pending on severity level configuration of each display types). notify(3) - All Syslog messages received after this bit is set will cause notification to be sent.'
    status = 'current'
    namedValues = NamedValues(("none", 0), ("count", 1), ("display", 2), ("notify", 3))

cslogEventDetailDefault = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noDisplay", 1), ("sparseDetail", 2), ("normalDetail", 3), ("verboseDetail", 4), ("exhaustiveDetail", 5))).clone('normalDetail')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventDetailDefault.setStatus('current')
if mibBuilder.loadTexts: cslogEventDetailDefault.setDescription('This object defines the detail level at which Syslog messages are displayed on the console or HTML user interface. Detail level classifications are: noDisplay(1) - No display at all. sparseDetail(2) - Minimum detail. normalDetail(3) - General detail. verboseDetail(4) - Verbose detail. exhaustiveDetail(5) - Full detail.')
cslogEventSeverityDispConsole = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 2), SyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventSeverityDispConsole.setStatus('current')
if mibBuilder.loadTexts: cslogEventSeverityDispConsole.setDescription('This object indicates which syslog severity level messages can be displayed on the console. A high severity value implies a low severity. If the display bit on the object cslogEventDisposition is set for this severity, all messages have severity values less than or equal to clogMaxSeverity and this object will be displayed on the console.')
cslogEventSeverityDispHtmlGUI = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 3), SyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventSeverityDispHtmlGUI.setStatus('current')
if mibBuilder.loadTexts: cslogEventSeverityDispHtmlGUI.setDescription('This object indicates which syslog severity level messages can be displayed on the event log GUI. A high severity value implies a low severity. If the display bit on the object cslogEventDisposition is set for this severity, all messages have severity values less than or equal to clogMaxSeverity and this object will be displayed on the event log GUI web pages.')
cslogEventSeverityDispHtmlConsol = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 4), SyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventSeverityDispHtmlConsol.setStatus('current')
if mibBuilder.loadTexts: cslogEventSeverityDispHtmlConsol.setDescription('This object indicates which syslog severity level messages can be displayed on the HTML event log console. A high severity value implies a low severity. If the display bit on the object cslogEventDisposition is set for this severity, all messages have severity values less than or equal to clogMaxSeverity and this object will be displayed on the GUI browser console page.')
cslogEventDispositionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5), )
if mibBuilder.loadTexts: cslogEventDispositionTable.setStatus('current')
if mibBuilder.loadTexts: cslogEventDispositionTable.setDescription('This table contains parameters to configure Syslog message disposition mechanisms and keep message counts.')
cslogEventDispositionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1), ).setIndexNames((0, "CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDispositionSeverity"))
if mibBuilder.loadTexts: cslogEventDispositionEntry.setStatus('current')
if mibBuilder.loadTexts: cslogEventDispositionEntry.setDescription('There is one entry per Syslog severity in the cslogEventDispositionTable. Each entry contains parameters for message disposition and count.')
cslogEventDispositionSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1, 1), SyslogSeverity())
if mibBuilder.loadTexts: cslogEventDispositionSeverity.setStatus('current')
if mibBuilder.loadTexts: cslogEventDispositionSeverity.setDescription('This object defines the Syslog serverity.')
cslogEventDisposition = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1, 2), CslogEventDisposition().clone(namedValues=NamedValues(("none", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventDisposition.setStatus('current')
if mibBuilder.loadTexts: cslogEventDisposition.setDescription('This object defines the disposition method for Syslog messages of a specific severity.')
cslogEventDispositionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cslogEventDispositionCount.setStatus('current')
if mibBuilder.loadTexts: cslogEventDispositionCount.setDescription('This is the number of Syslog messages of a specific severity.')
ciscoSlogEventExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 2))
ciscoSlogEventExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 1))
ciscoSlogEventExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 2))
ciscoSlogEventExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 1, 1)).setObjects(("CISCO-SYSLOG-EVENT-EXT-MIB", "ciscoSlogEventExtConfigGroup"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "ciscoSlogEventExtStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlogEventExtCompliance = ciscoSlogEventExtCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoSlogEventExtCompliance.setDescription('The compliance statement for the cslogEventExt groups.')
ciscoSlogEventExtConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 2, 1)).setObjects(("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDetailDefault"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventSeverityDispConsole"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventSeverityDispHtmlGUI"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventSeverityDispHtmlConsol"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDisposition"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlogEventExtConfigGroup = ciscoSlogEventExtConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoSlogEventExtConfigGroup.setDescription('These are objects supporting Syslog event configuration.')
ciscoSlogEventExtStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 2, 2)).setObjects(("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDispositionCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlogEventExtStatsGroup = ciscoSlogEventExtStatsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoSlogEventExtStatsGroup.setDescription('These are objects to provide Syslog event statistics.')
mibBuilder.exportSymbols("CISCO-SYSLOG-EVENT-EXT-MIB", cslogEventDispositionSeverity=cslogEventDispositionSeverity, cslogEventDisposition=cslogEventDisposition, ciscoSyslogEventExtMIB=ciscoSyslogEventExtMIB, ciscoSlogEventExtStatsGroup=ciscoSlogEventExtStatsGroup, cslogEventDetailDefault=cslogEventDetailDefault, cslogEventDispositionTable=cslogEventDispositionTable, cslogEventSeverityDispHtmlGUI=cslogEventSeverityDispHtmlGUI, cslogEventDispositionEntry=cslogEventDispositionEntry, ciscoSlogEventExtMIBConformance=ciscoSlogEventExtMIBConformance, cslogEventSeverityDispHtmlConsol=cslogEventSeverityDispHtmlConsol, cslogEventConfig=cslogEventConfig, CslogEventDisposition=CslogEventDisposition, ciscoSlogEventExtCompliance=ciscoSlogEventExtCompliance, ciscoSlogEventExtMIBCompliances=ciscoSlogEventExtMIBCompliances, cslogEventSeverityDispConsole=cslogEventSeverityDispConsole, cslogEventDispositionCount=cslogEventDispositionCount, ciscoSyslogEventExtMIBObjects=ciscoSyslogEventExtMIBObjects, PYSNMP_MODULE_ID=ciscoSyslogEventExtMIB, ciscoSlogEventExtConfigGroup=ciscoSlogEventExtConfigGroup, ciscoSlogEventExtMIBGroups=ciscoSlogEventExtMIBGroups)
