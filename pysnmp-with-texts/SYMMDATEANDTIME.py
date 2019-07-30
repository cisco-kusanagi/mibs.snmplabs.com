#
# PySNMP MIB module SYMMDATEANDTIME (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMDATEANDTIME
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:57 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifNumber, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifNumber", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, Integer32, IpAddress, Gauge32, NotificationType, Counter64, iso, Counter32, ModuleIdentity, TimeTicks, MibIdentifier, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "IpAddress", "Gauge32", "NotificationType", "Counter64", "iso", "Counter32", "ModuleIdentity", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
symmClock, = mibBuilder.importSymbols("SYMM-COMMON-SMI", "symmClock")
symmDateAndTime = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1))
symmDateAndTime.setRevisions(('2011-07-18 13:17',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: symmDateAndTime.setRevisionsDescriptions(('Symmetricom common time and date MIB',))
if mibBuilder.loadTexts: symmDateAndTime.setLastUpdated('201107181316Z')
if mibBuilder.loadTexts: symmDateAndTime.setOrganization('Symmetricom')
if mibBuilder.loadTexts: symmDateAndTime.setContactInfo('Symmetricom Technical Support 1-888-367-7966 toll free USA 1-408-428-7907 worldwide Support@symmetricom.com')
if mibBuilder.loadTexts: symmDateAndTime.setDescription('This is the Symmetricom Common MIB for clock date and time. It has a status node and a configuration node.')
class DateAndTime(TextualConvention, OctetString):
    description = "A date-time specification. field octets contents range ----- ------ -------- ----- 1 1-2 year* 0..65536 2 3 month 1..12 3 4 day 1..31 4 5 hour 0..23 5 6 minutes 0..59 6 7 seconds 0..60 (use 60 for leap-second) 7 8 deci-seconds 0..9 8 9 direction from UTC '+' / '-' 9 10 hours from UTC* 0..13 10 11 minutes from UTC 0..59 * Notes: - the value of year is in network-byte order - daylight saving time in New Zealand is +13 For example, Tuesday May 26, 1992 at 1:30:15 PM EDT would be displayed as: 1992-5-26,13:30:15.0,-4:0 Note that if only local time is known, then timezone information (fields 8-10) is not present."
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d,1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
class TLatAndLon(TextualConvention, OctetString):
    description = "antenna latitude and longitude specification. field octets contents range ----- ------ -------- ----- 1 1 +/-180 deg '+' / '-' 2 2 degree 0..180 3 3 minute 0..59 4 4 second 0..59 5 5 second fraction 0..99 +/- dd:mm:ss.ss "
    status = 'current'
    displayHint = '1a1d:1d:1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

class TAntHeight(TextualConvention, OctetString):
    description = "antenna height specification. field octets contents range ----- ------ -------- ----- 1 1 +/- '+' / '-' 2 2-3 meter 0..10000 3 4 meter fraction 0..99 +/- hh.hh "
    status = 'current'
    displayHint = '1a2d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class TLocalTimeOffset(TextualConvention, OctetString):
    description = "A local time offset specification. field octets contents range ----- ------ -------- ----- 1 1 direction from UTC '+' / '-' 2 2 hours from UTC* 0..13 3 3 minutes from UTC 0..59 * Notes: - the value of year is in network-byte order - The hours range is 0..13 For example, the -6 local time offset would be displayed as: -6:0 "
    status = 'current'
    displayHint = '1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TSsm(TextualConvention, Integer32):
    description = 'The ssm hex code'
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

dateAndTimeStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 1))
symmDateAndTimeTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 1, 1), )
if mibBuilder.loadTexts: symmDateAndTimeTable.setStatus('current')
if mibBuilder.loadTexts: symmDateAndTimeTable.setDescription('Date and Time Status Table for the specified hardware module.')
symmDateAndTimeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: symmDateAndTimeEntry.setStatus('current')
if mibBuilder.loadTexts: symmDateAndTimeEntry.setDescription('An entry of the date and time status table. Table index is entPhysicalIndex (hardware module index). For TP5K modules with date and time information are: IMC.')
symmDateAndTimeInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: symmDateAndTimeInfo.setStatus('current')
if mibBuilder.loadTexts: symmDateAndTimeInfo.setDescription('The clock information for the specified module.')
symmCurrentDateTime = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: symmCurrentDateTime.setStatus('current')
if mibBuilder.loadTexts: symmCurrentDateTime.setDescription('Current UTC date and time.')
symmLeapPendingAndSecond = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: symmLeapPendingAndSecond.setStatus('current')
if mibBuilder.loadTexts: symmLeapPendingAndSecond.setDescription('Leap pending information and leap second.')
dateAndTimeConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 2))
symmLeapSecondConfig = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 2, 1), Unsigned32()).setUnits('Second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: symmLeapSecondConfig.setStatus('current')
if mibBuilder.loadTexts: symmLeapSecondConfig.setDescription('The accumulated leap seconds between TAI and UTC (in seconds). This is write-only.')
symmDateTimeConfig = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 2, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: symmDateTimeConfig.setStatus('current')
if mibBuilder.loadTexts: symmDateTimeConfig.setDescription('The date and time of IMC module. Format is YYYY-MM-DD,HH:MM:SS. Manually entered date and time will not be accepted when the system is GNSS mode.')
dateAndTimeConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 3))
if mibBuilder.loadTexts: dateAndTimeConformance.setStatus('current')
if mibBuilder.loadTexts: dateAndTimeConformance.setDescription('This subtree contains conformance statements for the SYMMETRICOM-LED-MIB module. ')
dateAndTimeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 3, 1))
dateTimeBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 3, 1, 1)).setObjects(("SYMMDATEANDTIME", "dateTimeStatusGroup"), ("SYMMDATEANDTIME", "dateTimeConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dateTimeBasicCompliance = dateTimeBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: dateTimeBasicCompliance.setDescription('Description.')
dateAndTimeUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 3, 2))
dateTimeStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 3, 2, 1)).setObjects(("SYMMDATEANDTIME", "symmDateAndTimeInfo"), ("SYMMDATEANDTIME", "symmCurrentDateTime"), ("SYMMDATEANDTIME", "symmLeapPendingAndSecond"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dateTimeStatusGroup = dateTimeStatusGroup.setStatus('current')
if mibBuilder.loadTexts: dateTimeStatusGroup.setDescription('Description.')
dateTimeConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 3, 2, 2)).setObjects(("SYMMDATEANDTIME", "symmLeapSecondConfig"), ("SYMMDATEANDTIME", "symmDateTimeConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dateTimeConfigGroup = dateTimeConfigGroup.setStatus('current')
if mibBuilder.loadTexts: dateTimeConfigGroup.setDescription('Description.')
mibBuilder.exportSymbols("SYMMDATEANDTIME", dateTimeBasicCompliance=dateTimeBasicCompliance, TLatAndLon=TLatAndLon, dateAndTimeCompliances=dateAndTimeCompliances, dateAndTimeUocGroups=dateAndTimeUocGroups, symmLeapPendingAndSecond=symmLeapPendingAndSecond, dateAndTimeConformance=dateAndTimeConformance, dateTimeConfigGroup=dateTimeConfigGroup, PYSNMP_MODULE_ID=symmDateAndTime, TSsm=TSsm, dateAndTimeStatus=dateAndTimeStatus, symmDateAndTimeInfo=symmDateAndTimeInfo, symmDateTimeConfig=symmDateTimeConfig, symmDateAndTimeTable=symmDateAndTimeTable, dateTimeStatusGroup=dateTimeStatusGroup, symmDateAndTime=symmDateAndTime, symmLeapSecondConfig=symmLeapSecondConfig, TAntHeight=TAntHeight, symmDateAndTimeEntry=symmDateAndTimeEntry, TLocalTimeOffset=TLocalTimeOffset, DateAndTime=DateAndTime, symmCurrentDateTime=symmCurrentDateTime, dateAndTimeConfig=dateAndTimeConfig)
