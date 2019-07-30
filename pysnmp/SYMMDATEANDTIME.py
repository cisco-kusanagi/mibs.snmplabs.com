#
# PySNMP MIB module SYMMDATEANDTIME (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMDATEANDTIME
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:18 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifNumber, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifNumber", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, Integer32, Unsigned32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, ModuleIdentity, IpAddress, TimeTicks, ObjectIdentity, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "Unsigned32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "ModuleIdentity", "IpAddress", "TimeTicks", "ObjectIdentity", "Gauge32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
symmClock, = mibBuilder.importSymbols("SYMM-COMMON-SMI", "symmClock")
symmDateAndTime = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1))
symmDateAndTime.setRevisions(('2011-07-18 13:17',))
if mibBuilder.loadTexts: symmDateAndTime.setLastUpdated('201107181316Z')
if mibBuilder.loadTexts: symmDateAndTime.setOrganization('Symmetricom')
class DateAndTime(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d,1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
class TLatAndLon(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a1d:1d:1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

class TAntHeight(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a2d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class TLocalTimeOffset(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TSsm(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

dateAndTimeStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 1))
symmDateAndTimeTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 1, 1), )
if mibBuilder.loadTexts: symmDateAndTimeTable.setStatus('current')
symmDateAndTimeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: symmDateAndTimeEntry.setStatus('current')
symmDateAndTimeInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: symmDateAndTimeInfo.setStatus('current')
symmCurrentDateTime = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: symmCurrentDateTime.setStatus('current')
symmLeapPendingAndSecond = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: symmLeapPendingAndSecond.setStatus('current')
dateAndTimeConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 2))
symmLeapSecondConfig = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 2, 1), Unsigned32()).setUnits('Second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: symmLeapSecondConfig.setStatus('current')
symmDateTimeConfig = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 2, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: symmDateTimeConfig.setStatus('current')
dateAndTimeConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 3))
if mibBuilder.loadTexts: dateAndTimeConformance.setStatus('current')
dateAndTimeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 3, 1))
dateTimeBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 3, 1, 1)).setObjects(("SYMMDATEANDTIME", "dateTimeStatusGroup"), ("SYMMDATEANDTIME", "dateTimeConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dateTimeBasicCompliance = dateTimeBasicCompliance.setStatus('current')
dateAndTimeUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 3, 2))
dateTimeStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 3, 2, 1)).setObjects(("SYMMDATEANDTIME", "symmDateAndTimeInfo"), ("SYMMDATEANDTIME", "symmCurrentDateTime"), ("SYMMDATEANDTIME", "symmLeapPendingAndSecond"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dateTimeStatusGroup = dateTimeStatusGroup.setStatus('current')
dateTimeConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 3, 2, 2)).setObjects(("SYMMDATEANDTIME", "symmLeapSecondConfig"), ("SYMMDATEANDTIME", "symmDateTimeConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dateTimeConfigGroup = dateTimeConfigGroup.setStatus('current')
mibBuilder.exportSymbols("SYMMDATEANDTIME", symmDateAndTime=symmDateAndTime, dateAndTimeStatus=dateAndTimeStatus, dateTimeConfigGroup=dateTimeConfigGroup, symmLeapPendingAndSecond=symmLeapPendingAndSecond, TAntHeight=TAntHeight, symmCurrentDateTime=symmCurrentDateTime, dateAndTimeCompliances=dateAndTimeCompliances, TSsm=TSsm, symmDateAndTimeTable=symmDateAndTimeTable, dateAndTimeUocGroups=dateAndTimeUocGroups, symmDateTimeConfig=symmDateTimeConfig, symmDateAndTimeEntry=symmDateAndTimeEntry, TLatAndLon=TLatAndLon, PYSNMP_MODULE_ID=symmDateAndTime, symmLeapSecondConfig=symmLeapSecondConfig, dateTimeBasicCompliance=dateTimeBasicCompliance, dateAndTimeConfig=dateAndTimeConfig, dateTimeStatusGroup=dateTimeStatusGroup, DateAndTime=DateAndTime, symmDateAndTimeInfo=symmDateAndTimeInfo, TLocalTimeOffset=TLocalTimeOffset, dateAndTimeConformance=dateAndTimeConformance)
