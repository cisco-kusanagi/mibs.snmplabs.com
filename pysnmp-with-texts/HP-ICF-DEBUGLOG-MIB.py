#
# PySNMP MIB module HP-ICF-DEBUGLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-DEBUGLOG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:33:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
hpicfDebugLog, = mibBuilder.importSymbols("HP-ICF-OID", "hpicfDebugLog")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Gauge32, iso, IpAddress, MibIdentifier, ObjectIdentity, Counter32, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, Integer32, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "IpAddress", "MibIdentifier", "ObjectIdentity", "Counter32", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "Integer32", "Bits", "TimeTicks")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
hpicfDebugLogMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1))
hpicfDebugLogMib.setRevisions(('2017-07-04 00:00', '2016-03-18 00:00', '2016-02-17 00:00', '2009-09-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfDebugLogMib.setRevisionsDescriptions(('Added hpicfDebugTimeStamp', 'Changed description of hpicfDebugLogStatus and hpicfDebugDestStatus', 'Added hpicfDebugLogPersistent and hpicfDebugDestPersistent', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: hpicfDebugLogMib.setLastUpdated('201707040000Z')
if mibBuilder.loadTexts: hpicfDebugLogMib.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfDebugLogMib.setContactInfo('Hewlett Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfDebugLogMib.setDescription('The Debug MIB allows to enable / disable debug logging for all debug message types. This HP application enables / disables debug log messages.')
class HpicfDebugDestType(TextualConvention, Integer32):
    description = "This value specifies the destination for the debug log messages as described below. syslog - Send debug messages to syslog server. buffer - Print debug messages to a buffer in memory. The destination type will be 'none' by default. The destination for debug logging can be set to Syslog- Server/Debug Buffer or a combination of these."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("syslog", 1), ("buffer", 2))

class HpicfDebugLogLevels(TextualConvention, Integer32):
    description = 'This textual convention enumerates the Log levels for a debug message type such as SSH for debug logging.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("quiet", 0), ("fatal", 1), ("error", 2), ("info", 3), ("verbose", 4), ("debug", 5), ("debug2", 6), ("debug3", 7))

hpicfDebugLogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1))
hpicfDebugLogConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2))
hpicfDebugLogControlTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1), )
if mibBuilder.loadTexts: hpicfDebugLogControlTable.setStatus('current')
if mibBuilder.loadTexts: hpicfDebugLogControlTable.setDescription('This table contains one entry per debug message type for debug logging configuration.')
hpicfDebugLogControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1), ).setIndexNames((0, "HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogIndex"))
if mibBuilder.loadTexts: hpicfDebugLogControlEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfDebugLogControlEntry.setDescription('Debug logging configuration information for a particular debug message type.')
hpicfDebugLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpicfDebugLogIndex.setStatus('current')
if mibBuilder.loadTexts: hpicfDebugLogIndex.setDescription('An unique number that identifies the debug message type for debug logging.')
hpicfDebugLogDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDebugLogDescr.setStatus('current')
if mibBuilder.loadTexts: hpicfDebugLogDescr.setDescription('This object provides description for the debug message type that can be enabled for debug logging.')
hpicfDebugLogContainedIn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDebugLogContainedIn.setStatus('current')
if mibBuilder.loadTexts: hpicfDebugLogContainedIn.setDescription("The value of hpicfDebugLogIndex for the debug message type which 'contains' this debug message type. Note that the set of 'containment' relationships define a strict hierarchy.")
hpicfDebugLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDebugLogStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfDebugLogStatus.setDescription("This object enables or disables a specific debug option. The object 'hpicfDebugLogDescr' can be queried to see which instance corresponds to which debug option. Note that disabling an instance of this object also disables the corresponding instance of the object 'hpicfDebugLogPersistent'.")
hpicfDebugLogPersistent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDebugLogPersistent.setStatus('current')
if mibBuilder.loadTexts: hpicfDebugLogPersistent.setDescription('This object determines the status of a debug message type for persistent debug logging.')
hpicfDebugLogLevel = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 2), HpicfDebugLogLevels().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDebugLogLevel.setStatus('current')
if mibBuilder.loadTexts: hpicfDebugLogLevel.setDescription("The log level value for debug message type such as SSH.This scalar takes syslog severity values 'fatal|error|info|verbose|debug|debug2|debug3'. ")
hpicfDebugDestControlTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3), )
if mibBuilder.loadTexts: hpicfDebugDestControlTable.setStatus('current')
if mibBuilder.loadTexts: hpicfDebugDestControlTable.setDescription('This table contains one entry per debug destination type i.e. Syslog/Buffer.')
hpicfDebugDestControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3, 1), ).setIndexNames((0, "HP-ICF-DEBUGLOG-MIB", "hpicfDebugDestIndex"))
if mibBuilder.loadTexts: hpicfDebugDestControlEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfDebugDestControlEntry.setDescription('Debug logging configuration information for a particular debug destination type.')
hpicfDebugDestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3, 1, 1), HpicfDebugDestType())
if mibBuilder.loadTexts: hpicfDebugDestIndex.setStatus('current')
if mibBuilder.loadTexts: hpicfDebugDestIndex.setDescription('The index that uniquely identifies each debug destination type for debug logging.')
hpicfDebugDestStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDebugDestStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfDebugDestStatus.setDescription("This object determines the enable or disable status of a particular debug destination type such as Syslog Server or Buffer. Note that disabling an instance of this object also disables the corrsponding instance of the object 'hpicfDebugDestPersistent'.")
hpicfDebugDestPersistent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDebugDestPersistent.setStatus('current')
if mibBuilder.loadTexts: hpicfDebugDestPersistent.setDescription('This object determines the status of a particular debug destination type for persistent configuration.')
hpicfDebugTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDebugTimeStamp.setStatus('current')
if mibBuilder.loadTexts: hpicfDebugTimeStamp.setDescription('This object is used to enable or disable system time to be associated with the debug log message. true - enable system time to be associated with the debug logs. false - enable system Uptime to be associated with the debug logs. By default, system Uptime will be associated with the debug logs.')
hpicfDebugLogCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 1))
hpicfDebugLogGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 2))
hpicfDebugDestGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 3))
hpicfDebugTimeStampGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 4))
hpicfDebugLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 2, 1)).setObjects(("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogDescr"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogContainedIn"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogStatus"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogLevel"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogPersistent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDebugLogGroup = hpicfDebugLogGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfDebugLogGroup.setDescription('A collection of objects representing the configuration parameters for debug logging.')
hpicfDebugDestGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 3, 1)).setObjects(("HP-ICF-DEBUGLOG-MIB", "hpicfDebugDestStatus"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugDestPersistent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDebugDestGroup = hpicfDebugDestGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfDebugDestGroup.setDescription('A collection of objects representing the configuration parameters for debug destination. ')
hpicfDebugTimeStampGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 4, 1)).setObjects(("HP-ICF-DEBUGLOG-MIB", "hpicfDebugTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDebugTimeStampGroup = hpicfDebugTimeStampGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfDebugTimeStampGroup.setDescription('An object representing the configuration parameters for debug log time stamp. ')
hpicfDebugLogCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 1, 1)).setObjects(("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogGroup"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugDestGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDebugLogCompliance = hpicfDebugLogCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfDebugLogCompliance.setDescription('The compliance statement for debug logging entities which implement the DEBUGLOG-MIB with support for writable objects. Such an implementation can be both monitored and configured via SNMP.')
hpicfDebugLogCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 1, 2)).setObjects(("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogGroup"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugDestGroup"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugTimeStampGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDebugLogCompliance1 = hpicfDebugLogCompliance1.setStatus('current')
if mibBuilder.loadTexts: hpicfDebugLogCompliance1.setDescription('The compliance statement for debug logging entities which implement the DEBUGLOG-MIB with support for writable objects. Such an implementation can be both monitored and configured via SNMP.')
mibBuilder.exportSymbols("HP-ICF-DEBUGLOG-MIB", PYSNMP_MODULE_ID=hpicfDebugLogMib, hpicfDebugLogConformance=hpicfDebugLogConformance, hpicfDebugDestGroups=hpicfDebugDestGroups, hpicfDebugLogCompliances=hpicfDebugLogCompliances, hpicfDebugDestGroup=hpicfDebugDestGroup, hpicfDebugLogGroups=hpicfDebugLogGroups, hpicfDebugLogGroup=hpicfDebugLogGroup, hpicfDebugLogDescr=hpicfDebugLogDescr, hpicfDebugLogStatus=hpicfDebugLogStatus, hpicfDebugLogCompliance=hpicfDebugLogCompliance, hpicfDebugLogContainedIn=hpicfDebugLogContainedIn, hpicfDebugLogPersistent=hpicfDebugLogPersistent, hpicfDebugTimeStamp=hpicfDebugTimeStamp, hpicfDebugLogControlTable=hpicfDebugLogControlTable, hpicfDebugTimeStampGroup=hpicfDebugTimeStampGroup, hpicfDebugLogCompliance1=hpicfDebugLogCompliance1, hpicfDebugLogLevel=hpicfDebugLogLevel, hpicfDebugDestPersistent=hpicfDebugDestPersistent, hpicfDebugLogIndex=hpicfDebugLogIndex, hpicfDebugDestControlEntry=hpicfDebugDestControlEntry, hpicfDebugLogObjects=hpicfDebugLogObjects, hpicfDebugDestControlTable=hpicfDebugDestControlTable, HpicfDebugLogLevels=HpicfDebugLogLevels, hpicfDebugLogMib=hpicfDebugLogMib, hpicfDebugDestIndex=hpicfDebugDestIndex, HpicfDebugDestType=HpicfDebugDestType, hpicfDebugDestStatus=hpicfDebugDestStatus, hpicfDebugTimeStampGroups=hpicfDebugTimeStampGroups, hpicfDebugLogControlEntry=hpicfDebugLogControlEntry)
