#
# PySNMP MIB module SYMMOUTGEN (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMOUTGEN
# Produced by pysmi-0.3.4 at Tue Jul 30 11:35:08 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifNumber, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifNumber", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, Integer32, Bits, Counter32, TimeTicks, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, MibIdentifier, iso, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "Bits", "Counter32", "TimeTicks", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "MibIdentifier", "iso", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
symmPhysicalSignal, = mibBuilder.importSymbols("SYMM-COMMON-SMI", "symmPhysicalSignal")
symmOutGen = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6))
symmOutGen.setRevisions(('2011-07-18 11:21',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: symmOutGen.setRevisionsDescriptions(('New',))
if mibBuilder.loadTexts: symmOutGen.setLastUpdated('201107181121Z')
if mibBuilder.loadTexts: symmOutGen.setOrganization('Symmetricom')
if mibBuilder.loadTexts: symmOutGen.setContactInfo('Symmetricom Technical Support 1-888-367-7966 toll free USA 1-408-428-7907 worldwide Support@symmetricom.com ')
if mibBuilder.loadTexts: symmOutGen.setDescription('This is the Symmetricom Common MIB for output generation. It specifies output port behavior (on | squelch | AIS) when the system clock state is not Normal Tracking. TP5K defines five clock states: warm-up, free-run, fast track, normal track, and holdover. ')
class GENERALOUTGENTYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("squelch", 1), ("on", 2), ("ais", 3))

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

outGenStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 1))
outGenConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2))
outGenConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1), )
if mibBuilder.loadTexts: outGenConfigTable.setStatus('current')
if mibBuilder.loadTexts: outGenConfigTable.setDescription('Output generation configuration table. Each table entry specifies port behavior for each of the four clock states. Only ports with the following physical signals are affected by this output generation table: E1/T1, 1PPS+TOD, 1PPS, and 10 MHz. Ethernet port signals (PTP, NTP, SyncE) use quality level parameters to indicate usability.')
outGenConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMOUTGEN", "outGenConfigIndex"))
if mibBuilder.loadTexts: outGenConfigEntry.setStatus('current')
if mibBuilder.loadTexts: outGenConfigEntry.setDescription('An entry of the output generation configuration table. Table index is ifIndex.')
outGenConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: outGenConfigIndex.setStatus('current')
if mibBuilder.loadTexts: outGenConfigIndex.setDescription('Local index of the output generation configuration table.')
outGenConfigWarmup = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1, 1, 2), GENERALOUTGENTYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outGenConfigWarmup.setStatus('current')
if mibBuilder.loadTexts: outGenConfigWarmup.setDescription('Output behavior during clock warm-up state for the specified port. Values can be on (1), squelch (2), or AIS (3).')
outGenConfigFreerun = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1, 1, 3), GENERALOUTGENTYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outGenConfigFreerun.setStatus('current')
if mibBuilder.loadTexts: outGenConfigFreerun.setDescription('Output behavior during clock free-run state for the specified port. Values can be on (1), squelch (2), or AIS (3).')
outGenConfigHoldover = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1, 1, 4), GENERALOUTGENTYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outGenConfigHoldover.setStatus('current')
if mibBuilder.loadTexts: outGenConfigHoldover.setDescription('Output behavior during clock holdover state for the specified port. Values can be on (1), squelch (2), or AIS (3).')
outGenConfigFasttrack = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1, 1, 5), GENERALOUTGENTYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outGenConfigFasttrack.setStatus('current')
if mibBuilder.loadTexts: outGenConfigFasttrack.setDescription('Output behavior during clock fast-track state for the specified port. Values can be on (1), squelch (2), or AIS (3).')
outGenConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 3))
if mibBuilder.loadTexts: outGenConformance.setStatus('current')
if mibBuilder.loadTexts: outGenConformance.setDescription('This subtree contains conformance statements for the SYMMETRICOM-LED-MIB module. ')
outGenCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 3, 1))
outGenBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 3, 1, 1)).setObjects(("SYMMOUTGEN", "outGenGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    outGenBasicCompliance = outGenBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: outGenBasicCompliance.setDescription('The compliance statement for SNMP entities which have output generation.')
outGenUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 3, 2))
outGenGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 3, 2, 1)).setObjects(("SYMMOUTGEN", "outGenConfigWarmup"), ("SYMMOUTGEN", "outGenConfigFreerun"), ("SYMMOUTGEN", "outGenConfigHoldover"), ("SYMMOUTGEN", "outGenConfigFasttrack"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    outGenGroup = outGenGroup.setStatus('current')
if mibBuilder.loadTexts: outGenGroup.setDescription('A collection of objects providing information applicable to common output generation group.')
mibBuilder.exportSymbols("SYMMOUTGEN", DateAndTime=DateAndTime, TLocalTimeOffset=TLocalTimeOffset, outGenStatus=outGenStatus, outGenConfig=outGenConfig, outGenConfigWarmup=outGenConfigWarmup, outGenConfigIndex=outGenConfigIndex, outGenGroup=outGenGroup, TAntHeight=TAntHeight, outGenUocGroups=outGenUocGroups, outGenConformance=outGenConformance, outGenConfigHoldover=outGenConfigHoldover, outGenConfigFreerun=outGenConfigFreerun, outGenConfigFasttrack=outGenConfigFasttrack, TLatAndLon=TLatAndLon, symmOutGen=symmOutGen, outGenCompliances=outGenCompliances, outGenConfigTable=outGenConfigTable, outGenConfigEntry=outGenConfigEntry, TSsm=TSsm, GENERALOUTGENTYPE=GENERALOUTGENTYPE, PYSNMP_MODULE_ID=symmOutGen, outGenBasicCompliance=outGenBasicCompliance)
