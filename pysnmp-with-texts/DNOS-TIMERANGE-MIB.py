#
# PySNMP MIB module DNOS-TIMERANGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-TIMERANGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:52:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, Gauge32, ModuleIdentity, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, IpAddress, MibIdentifier, Counter64, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Gauge32", "ModuleIdentity", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "IpAddress", "MibIdentifier", "Counter64", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
fastPathTimeRange = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53))
fastPathTimeRange.setRevisions(('2011-01-26 00:00', '2009-09-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastPathTimeRange.setRevisionsDescriptions(('Postal address updated.', 'Initial version.',))
if mibBuilder.loadTexts: fastPathTimeRange.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathTimeRange.setOrganization('Dell, Inc.')
if mibBuilder.loadTexts: fastPathTimeRange.setContactInfo('')
if mibBuilder.loadTexts: fastPathTimeRange.setDescription('The Broadcom Private MIB for DNOS Time Ranges')
fastPathTimeRangeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1))
class TimeRangeAbsoluteDateAndTime(TextualConvention, OctetString):
    description = 'A date-time specification for absolute time entry in a time range. field octets contents range ----- ------ -------- ----- 1 1-2 year 0..65536 2 3 month 1..12 3 4 day 1..31 4 5 hour 0..23 5 6 minutes 0..59 For example, Oct 9, 2009 at 1:30 PM would be displayed as: 2009-10-9,13:30.'
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class TimeRangePeriodicTime(TextualConvention, OctetString):
    description = 'A time specification for periodic time entry in a time range. field octets contents range ----- ------ -------- ----- 1 1 hour 0..23 1 1 minutes 0..59 For example,1:30 PM would be displayed as: 13:30.'
    status = 'current'
    displayHint = '1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class TimeRangePeriodicDate(TextualConvention, OctetString):
    description = 'A date specification for periodic time entry in a time range. field octets contents range ----- ------ -------- ----- 1 1-2 year 1993..2035 2 3 month 1..12 3 4 day 1..31 For example, Oct 9, 2009 would be displayed as: 2009-10-9'
    status = 'current'
    displayHint = '2d-1d-1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

timeRangeAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeRangeAdminMode.setStatus('current')
if mibBuilder.loadTexts: timeRangeAdminMode.setDescription('TimeRange admin mode: enable - enable TimeRange disable - disable TimeRange.')
timeRangeIndexNextFree = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeRangeIndexNextFree.setStatus('current')
if mibBuilder.loadTexts: timeRangeIndexNextFree.setDescription('This object contains an unused value for the timeRangeIndex to be used when creating a new TimeRange. A value of zero indicates the TimeRange table is full.')
timeRangeTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 3), )
if mibBuilder.loadTexts: timeRangeTable.setStatus('current')
if mibBuilder.loadTexts: timeRangeTable.setDescription('A table of TimeRange instances.')
timeRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 3, 1), ).setIndexNames((0, "DNOS-TIMERANGE-MIB", "timeRangeIndex"))
if mibBuilder.loadTexts: timeRangeEntry.setStatus('current')
if mibBuilder.loadTexts: timeRangeEntry.setDescription('timeRangeIndex and timeRangeName must be set to complete a new timeRangeEntry instance')
timeRangeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: timeRangeIndex.setStatus('current')
if mibBuilder.loadTexts: timeRangeIndex.setDescription('The TimeRange table index this instance is associated with.')
timeRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangeName.setStatus('current')
if mibBuilder.loadTexts: timeRangeName.setDescription('The name of this TimeRange entry, which must consist of 1 to 31 alphanumeric characters and uniquely identify this TimeRange. This object must be set to complete a new TimeRange row instance.')
timeRangeOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("active", 0), ("inactive", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeRangeOperState.setStatus('current')
if mibBuilder.loadTexts: timeRangeOperState.setDescription('Operating status of the time-range. It depends on the current time and the periodic and absolute time entries defined in the time-range')
timeRangeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangeStatus.setStatus('current')
if mibBuilder.loadTexts: timeRangeStatus.setDescription('Status of this instance. active(1) - this TimeRange instance is active createAndGo(4) - set to this value to create an instance destroy(6) - set to this value to delete an instance')
timeRangeAbsoluteEntryTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 4), )
if mibBuilder.loadTexts: timeRangeAbsoluteEntryTable.setStatus('current')
if mibBuilder.loadTexts: timeRangeAbsoluteEntryTable.setDescription('A table of absolute entries for time ranges')
timeRangeAbsoluteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 4, 1), ).setIndexNames((0, "DNOS-TIMERANGE-MIB", "timeRangeIndex"), (0, "DNOS-TIMERANGE-MIB", "timeRangeAbsoluteEntryIndex"))
if mibBuilder.loadTexts: timeRangeAbsoluteEntry.setStatus('current')
if mibBuilder.loadTexts: timeRangeAbsoluteEntry.setDescription('A table of absolute entries for time ranges. Atleast one of timeRangeAbsoluteStartDateAndTime and timeRangeAbsoluteEndDateAndTime must be set to complete a new Absolute entry instance.')
timeRangeAbsoluteEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)))
if mibBuilder.loadTexts: timeRangeAbsoluteEntryIndex.setStatus('current')
if mibBuilder.loadTexts: timeRangeAbsoluteEntryIndex.setDescription('The index of this absolute time entry within time range.')
timeRangeAbsoluteStartDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 4, 1, 2), TimeRangeAbsoluteDateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangeAbsoluteStartDateAndTime.setStatus('current')
if mibBuilder.loadTexts: timeRangeAbsoluteStartDateAndTime.setDescription('The start time for an absolute entry in the time range')
timeRangeAbsoluteEndDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 4, 1, 3), TimeRangeAbsoluteDateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangeAbsoluteEndDateAndTime.setStatus('current')
if mibBuilder.loadTexts: timeRangeAbsoluteEndDateAndTime.setDescription(' The end time for an absolute entry in the time range.')
timeRangeAbsoluteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangeAbsoluteStatus.setStatus('current')
if mibBuilder.loadTexts: timeRangeAbsoluteStatus.setDescription('Status of this instance. active(1) - this timeRangeAbsoluteEntry is active createAndGo(4) - set to this value to create an instance destroy(6) - set to this value to delete an instance')
timeRangePeriodicEntryTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5), )
if mibBuilder.loadTexts: timeRangePeriodicEntryTable.setStatus('current')
if mibBuilder.loadTexts: timeRangePeriodicEntryTable.setDescription('A table periodic entries for time ranges')
timeRangePeriodicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1), ).setIndexNames((0, "DNOS-TIMERANGE-MIB", "timeRangeIndex"), (0, "DNOS-TIMERANGE-MIB", "timeRangePeriodicEntryIndex"))
if mibBuilder.loadTexts: timeRangePeriodicEntry.setStatus('current')
if mibBuilder.loadTexts: timeRangePeriodicEntry.setDescription('A table periodic entries for time ranges. All the objects in the periodic entry must be set to complete a new periodic entry instance. Objects timeRangePeriodicStartDay and timeRangePeriodicStartTime together forms the start dayandtime and objects timeRangePeriodicEndDay and timeRangePeriodicEndTime toghetehr forms end dayandtime. The time range to which the periodic entry belongs is active between start dayandtime and end dayandtime. If more than one day is specified in the timeRangePeriodicStartDay, then the same days should be specified in the timeRangePeriodicEndDay ')
timeRangePeriodicEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)))
if mibBuilder.loadTexts: timeRangePeriodicEntryIndex.setStatus('current')
if mibBuilder.loadTexts: timeRangePeriodicEntryIndex.setDescription('The index of this periodic entry within time range.')
timeRangePeriodicFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicFrequency.setStatus('current')
if mibBuilder.loadTexts: timeRangePeriodicFrequency.setDescription('The frequency of this periodic entry within the time range.')
timeRangePeriodicPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicPattern.setStatus('current')
if mibBuilder.loadTexts: timeRangePeriodicPattern.setDescription('The pattern for a periodic entry in the time range. Can be one of the following: 0 - weekly, 1 - daily, 2 - monthly.')
timeRangePeriodicDayMask = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicDayMask.setStatus('current')
if mibBuilder.loadTexts: timeRangePeriodicDayMask.setDescription("Depending on the value of the timeRangeEntryPattern this field can have different meanings. In case timeRangeEntryPattern is set to 'daily' or 'weekly' the field contains a bitmap where each bit presents a day of week. Structure of the bitmap is the following : bit 0 - sunday, bit 1 - monday, bit 2 - tuesday, bit 3 - wednesday, bit 4 - thursday, bit 5 - friday, bit 6 - saturday. In case timeRangeEntryPattern is set to 'monthly' the field contains a day of month (1..31).")
timeRangePeriodicStartDate = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 5), TimeRangePeriodicDate()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicStartDate.setStatus('current')
if mibBuilder.loadTexts: timeRangePeriodicStartDate.setDescription('The start date for a periodic entry in the time range')
timeRangePeriodicStartDay = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 6), Bits().clone(namedValues=NamedValues(("sunday", 1), ("monday", 2), ("tuesday", 3), ("wednesday", 4), ("thursday", 5), ("friday", 6), ("saturday", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicStartDay.setStatus('current')
if mibBuilder.loadTexts: timeRangePeriodicStartDay.setDescription('The starting day or days on which the configuration that referenced the time range starts going into effect. Same day can be set for both timeRangePeriodicStartDay and timeRangePeriodicEndDay objects ')
timeRangePeriodicStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 7), TimeRangePeriodicTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicStartTime.setStatus('current')
if mibBuilder.loadTexts: timeRangePeriodicStartTime.setDescription('The starting time for an periodic entry in the time range.')
timeRangePeriodicEndDate = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 8), TimeRangePeriodicDate()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicEndDate.setStatus('current')
if mibBuilder.loadTexts: timeRangePeriodicEndDate.setDescription('The end date for a periodic entry in the time range')
timeRangePeriodicEndDay = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 9), Bits().clone(namedValues=NamedValues(("sunday", 1), ("monday", 2), ("tuesday", 3), ("wednesday", 4), ("thursday", 5), ("friday", 6), ("saturday", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicEndDay.setStatus('current')
if mibBuilder.loadTexts: timeRangePeriodicEndDay.setDescription('The ending day or days on which the configuration that referenced the time range is no longer in efect. Same day can be set for both timeRangePeriodicStartDay and timeRangePeriodicEndDay objects')
timeRangePeriodicEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 10), TimeRangePeriodicTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicEndTime.setStatus('current')
if mibBuilder.loadTexts: timeRangePeriodicEndTime.setDescription('The end time for an periodic entry in the time range. Use end time 00:00 to specify last minute of the day.')
timeRangePeriodicStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicStatus.setStatus('current')
if mibBuilder.loadTexts: timeRangePeriodicStatus.setDescription('Status of this instance. active(1) - this timeRangePeriodicEntry is active createAndGo(4) - set to this value to create an instance destroy(6) - set to this value to delete an instance')
mibBuilder.exportSymbols("DNOS-TIMERANGE-MIB", timeRangeTable=timeRangeTable, timeRangeOperState=timeRangeOperState, timeRangeAbsoluteStatus=timeRangeAbsoluteStatus, timeRangeAdminMode=timeRangeAdminMode, timeRangePeriodicEndDate=timeRangePeriodicEndDate, timeRangePeriodicDayMask=timeRangePeriodicDayMask, TimeRangePeriodicDate=TimeRangePeriodicDate, timeRangeAbsoluteEndDateAndTime=timeRangeAbsoluteEndDateAndTime, TimeRangePeriodicTime=TimeRangePeriodicTime, timeRangeAbsoluteEntryIndex=timeRangeAbsoluteEntryIndex, timeRangeIndex=timeRangeIndex, TimeRangeAbsoluteDateAndTime=TimeRangeAbsoluteDateAndTime, timeRangeAbsoluteEntryTable=timeRangeAbsoluteEntryTable, timeRangeName=timeRangeName, timeRangePeriodicStartDate=timeRangePeriodicStartDate, timeRangePeriodicFrequency=timeRangePeriodicFrequency, timeRangePeriodicEndDay=timeRangePeriodicEndDay, timeRangePeriodicEndTime=timeRangePeriodicEndTime, timeRangeAbsoluteEntry=timeRangeAbsoluteEntry, timeRangeEntry=timeRangeEntry, timeRangePeriodicEntryIndex=timeRangePeriodicEntryIndex, PYSNMP_MODULE_ID=fastPathTimeRange, timeRangeStatus=timeRangeStatus, timeRangePeriodicStartTime=timeRangePeriodicStartTime, timeRangeAbsoluteStartDateAndTime=timeRangeAbsoluteStartDateAndTime, timeRangePeriodicEntry=timeRangePeriodicEntry, timeRangeIndexNextFree=timeRangeIndexNextFree, fastPathTimeRange=fastPathTimeRange, timeRangePeriodicStatus=timeRangePeriodicStatus, fastPathTimeRangeGroup=fastPathTimeRangeGroup, timeRangePeriodicEntryTable=timeRangePeriodicEntryTable, timeRangePeriodicPattern=timeRangePeriodicPattern, timeRangePeriodicStartDay=timeRangePeriodicStartDay)
