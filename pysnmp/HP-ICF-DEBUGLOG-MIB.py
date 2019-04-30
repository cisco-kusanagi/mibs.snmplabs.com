#
# PySNMP MIB module HP-ICF-DEBUGLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-DEBUGLOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:21:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
hpicfDebugLog, = mibBuilder.importSymbols("HP-ICF-OID", "hpicfDebugLog")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, iso, IpAddress, Unsigned32, Counter64, NotificationType, Integer32, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "IpAddress", "Unsigned32", "Counter64", "NotificationType", "Integer32", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Counter32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
hpicfDebugLogMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1))
hpicfDebugLogMib.setRevisions(('2017-07-04 00:00', '2016-03-18 00:00', '2016-02-17 00:00', '2009-09-22 00:00',))
if mibBuilder.loadTexts: hpicfDebugLogMib.setLastUpdated('201707040000Z')
if mibBuilder.loadTexts: hpicfDebugLogMib.setOrganization('HP Networking')
class HpicfDebugDestType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("syslog", 1), ("buffer", 2))

class HpicfDebugLogLevels(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("quiet", 0), ("fatal", 1), ("error", 2), ("info", 3), ("verbose", 4), ("debug", 5), ("debug2", 6), ("debug3", 7))

hpicfDebugLogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1))
hpicfDebugLogConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2))
hpicfDebugLogControlTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1), )
if mibBuilder.loadTexts: hpicfDebugLogControlTable.setStatus('current')
hpicfDebugLogControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1), ).setIndexNames((0, "HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogIndex"))
if mibBuilder.loadTexts: hpicfDebugLogControlEntry.setStatus('current')
hpicfDebugLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpicfDebugLogIndex.setStatus('current')
hpicfDebugLogDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDebugLogDescr.setStatus('current')
hpicfDebugLogContainedIn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDebugLogContainedIn.setStatus('current')
hpicfDebugLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDebugLogStatus.setStatus('current')
hpicfDebugLogPersistent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDebugLogPersistent.setStatus('current')
hpicfDebugLogLevel = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 2), HpicfDebugLogLevels().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDebugLogLevel.setStatus('current')
hpicfDebugDestControlTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3), )
if mibBuilder.loadTexts: hpicfDebugDestControlTable.setStatus('current')
hpicfDebugDestControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3, 1), ).setIndexNames((0, "HP-ICF-DEBUGLOG-MIB", "hpicfDebugDestIndex"))
if mibBuilder.loadTexts: hpicfDebugDestControlEntry.setStatus('current')
hpicfDebugDestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3, 1, 1), HpicfDebugDestType())
if mibBuilder.loadTexts: hpicfDebugDestIndex.setStatus('current')
hpicfDebugDestStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDebugDestStatus.setStatus('current')
hpicfDebugDestPersistent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDebugDestPersistent.setStatus('current')
hpicfDebugTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDebugTimeStamp.setStatus('current')
hpicfDebugLogCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 1))
hpicfDebugLogGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 2))
hpicfDebugDestGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 3))
hpicfDebugTimeStampGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 4))
hpicfDebugLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 2, 1)).setObjects(("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogDescr"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogContainedIn"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogStatus"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogLevel"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogPersistent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDebugLogGroup = hpicfDebugLogGroup.setStatus('current')
hpicfDebugDestGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 3, 1)).setObjects(("HP-ICF-DEBUGLOG-MIB", "hpicfDebugDestStatus"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugDestPersistent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDebugDestGroup = hpicfDebugDestGroup.setStatus('current')
hpicfDebugTimeStampGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 4, 1)).setObjects(("HP-ICF-DEBUGLOG-MIB", "hpicfDebugTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDebugTimeStampGroup = hpicfDebugTimeStampGroup.setStatus('current')
hpicfDebugLogCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 1, 1)).setObjects(("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogGroup"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugDestGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDebugLogCompliance = hpicfDebugLogCompliance.setStatus('deprecated')
hpicfDebugLogCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 1, 2)).setObjects(("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogGroup"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugDestGroup"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugTimeStampGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDebugLogCompliance1 = hpicfDebugLogCompliance1.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-DEBUGLOG-MIB", hpicfDebugTimeStamp=hpicfDebugTimeStamp, HpicfDebugLogLevels=HpicfDebugLogLevels, hpicfDebugLogGroups=hpicfDebugLogGroups, hpicfDebugLogControlEntry=hpicfDebugLogControlEntry, hpicfDebugLogControlTable=hpicfDebugLogControlTable, hpicfDebugLogObjects=hpicfDebugLogObjects, hpicfDebugLogStatus=hpicfDebugLogStatus, hpicfDebugDestGroups=hpicfDebugDestGroups, hpicfDebugTimeStampGroups=hpicfDebugTimeStampGroups, HpicfDebugDestType=HpicfDebugDestType, hpicfDebugDestControlTable=hpicfDebugDestControlTable, hpicfDebugDestStatus=hpicfDebugDestStatus, hpicfDebugDestControlEntry=hpicfDebugDestControlEntry, hpicfDebugLogIndex=hpicfDebugLogIndex, hpicfDebugDestIndex=hpicfDebugDestIndex, hpicfDebugLogContainedIn=hpicfDebugLogContainedIn, hpicfDebugLogLevel=hpicfDebugLogLevel, hpicfDebugLogGroup=hpicfDebugLogGroup, hpicfDebugLogPersistent=hpicfDebugLogPersistent, hpicfDebugDestGroup=hpicfDebugDestGroup, hpicfDebugLogDescr=hpicfDebugLogDescr, hpicfDebugLogCompliance=hpicfDebugLogCompliance, hpicfDebugLogCompliances=hpicfDebugLogCompliances, hpicfDebugDestPersistent=hpicfDebugDestPersistent, hpicfDebugTimeStampGroup=hpicfDebugTimeStampGroup, PYSNMP_MODULE_ID=hpicfDebugLogMib, hpicfDebugLogCompliance1=hpicfDebugLogCompliance1, hpicfDebugLogMib=hpicfDebugLogMib, hpicfDebugLogConformance=hpicfDebugLogConformance)
