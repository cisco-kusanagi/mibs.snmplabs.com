#
# PySNMP MIB module SYMMNTP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMNTP
# Produced by pysmi-0.3.4 at Tue Jul 30 11:35:05 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifNumber, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifNumber", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter64, Gauge32, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, TimeTicks, iso, Counter32, MibIdentifier, IpAddress, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "TimeTicks", "iso", "Counter32", "MibIdentifier", "IpAddress", "NotificationType", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
symmPacketService, EnableValue = mibBuilder.importSymbols("SYMM-COMMON-SMI", "symmPacketService", "EnableValue")
symmNTP = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2))
if mibBuilder.loadTexts: symmNTP.setLastUpdated('201512111510Z')
if mibBuilder.loadTexts: symmNTP.setOrganization('Symmetricom')
if mibBuilder.loadTexts: symmNTP.setContactInfo('Symmetricom Technical Support 1-888-367-7966 toll free USA 1-408-428-7907 worldwide Support@symmetricom.com ')
if mibBuilder.loadTexts: symmNTP.setDescription('This is the Symmetricom NTP MIB. It has two main nodes: NTP status and NTP configuration.')
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

ntpStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1))
ntpCommonStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1), )
if mibBuilder.loadTexts: ntpCommonStatusTable.setStatus('current')
if mibBuilder.loadTexts: ntpCommonStatusTable.setDescription('The NTP status table. It provides status for the NTP server operation. There are 7 status parameters.')
ntpCommonStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMNTP", "ntpStatusIndex"))
if mibBuilder.loadTexts: ntpCommonStatusEntry.setStatus('current')
if mibBuilder.loadTexts: ntpCommonStatusEntry.setDescription('An entry of the NTP status table. Table index is ifIndex (port and interface index).')
ntpStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: ntpStatusIndex.setStatus('current')
if mibBuilder.loadTexts: ntpStatusIndex.setDescription('Local index of the NTP common status table.')
ntpStatusEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 2), EnableValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpStatusEnable.setStatus('current')
if mibBuilder.loadTexts: ntpStatusEnable.setDescription('The NTP enable status for the specified NTP port. It can be Enable (1) or Disable (2). When NTP is disabled at a port, it does not transmit or respond to NTP packets, and all alarms associated with NTP for this port are cleared.')
ntpStatusMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpStatusMode.setStatus('current')
if mibBuilder.loadTexts: ntpStatusMode.setDescription('The NTP operational mode. It can act as server or client. Currently only the server mode is supported.')
ntpStatusLeapStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpStatusLeapStatus.setStatus('current')
if mibBuilder.loadTexts: ntpStatusLeapStatus.setDescription('The NTP leap second status. Possible values are : No warning, Leap insertion, Leap deletion, Not in sync.')
ntpStatusStratumLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpStatusStratumLevel.setStatus('current')
if mibBuilder.loadTexts: ntpStatusStratumLevel.setDescription('The stratum level of the reference for the NTP clock at the specified port. Its range is 1-4. Only stratum level 1(PRC/PRS) is supported.')
ntpStatusRootDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpStatusRootDispersion.setStatus('current')
if mibBuilder.loadTexts: ntpStatusRootDispersion.setDescription('Root dispersion. Hardcoded to be 0.')
ntpStatusPacketLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpStatusPacketLoad.setStatus('current')
if mibBuilder.loadTexts: ntpStatusPacketLoad.setDescription('NTP packet response load. Its range is 1-100 in unit of %.')
ntpStatusVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpStatusVersion.setStatus('current')
if mibBuilder.loadTexts: ntpStatusVersion.setDescription('NTP protocol version. Only version 4 is supported.')
ntpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2))
ntpCommonConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1), )
if mibBuilder.loadTexts: ntpCommonConfigTable.setStatus('current')
if mibBuilder.loadTexts: ntpCommonConfigTable.setDescription('The NTP server configuration table.')
ntpCommonConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMNTP", "ntpCommonIndex"))
if mibBuilder.loadTexts: ntpCommonConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ntpCommonConfigEntry.setDescription('An entry of the NTP server configuration table. Table index is ifIndex (port and interface index).')
ntpCommonIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: ntpCommonIndex.setStatus('current')
if mibBuilder.loadTexts: ntpCommonIndex.setDescription('Local index of the NTP common parameter configuration table.')
ntpCommonState = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 2), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpCommonState.setStatus('current')
if mibBuilder.loadTexts: ntpCommonState.setDescription('The NTP service enable state for the specified port. It can be Enable (1) or Disable (2). Default value is Enable. When NTP is disabled at a port, it does not transmit or respond to NTP packets, and all alarms associated with NTP for this port are cleared.')
ntpCommonTTL = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpCommonTTL.setStatus('current')
if mibBuilder.loadTexts: ntpCommonTTL.setDescription('IP header time-to-live (TTL) field for the NTP packets. Range is 1-255. Default value is 64.')
ntpCommonDSCP = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 4), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpCommonDSCP.setStatus('current')
if mibBuilder.loadTexts: ntpCommonDSCP.setDescription('Differentiated service code point (DSCP) state for the specified NTP port. It can be either Enable (1) or Disable (2). Default value is Disable. If DSCP state is Enable, the QoS field will have a configured DSCP value.')
ntpCommonDSCPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpCommonDSCPValue.setStatus('current')
if mibBuilder.loadTexts: ntpCommonDSCPValue.setDescription('DSCP value for PTP packets leaving this port. Range is 0-63, and default value is 0.')
ntpCommonVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpCommonVlanId.setStatus('current')
if mibBuilder.loadTexts: ntpCommonVlanId.setDescription('The VLAN ID associated with the NTP service at this port. Each port only supports one NTP VLAN.')
ntpCommonServiceLoadAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpCommonServiceLoadAlarmThreshold.setStatus('current')
if mibBuilder.loadTexts: ntpCommonServiceLoadAlarmThreshold.setDescription('It shows percentage (%) of NTP service load alarm threshold')
ntpConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 3))
if mibBuilder.loadTexts: ntpConformance.setStatus('current')
if mibBuilder.loadTexts: ntpConformance.setDescription('This subtree contains conformance statements for the SYMMETRICOM-LED-MIB module. ')
ntpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 3, 1))
ntpBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 3, 1, 1)).setObjects(("SYMMNTP", "ntpStatusGroup"), ("SYMMNTP", "ntpConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntpBasicCompliance = ntpBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: ntpBasicCompliance.setDescription('The compliance statement for SNMP entities which have NTP packet service.')
ntpUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 3, 2))
ntpStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 3, 2, 1)).setObjects(("SYMMNTP", "ntpStatusEnable"), ("SYMMNTP", "ntpStatusMode"), ("SYMMNTP", "ntpStatusLeapStatus"), ("SYMMNTP", "ntpStatusStratumLevel"), ("SYMMNTP", "ntpStatusRootDispersion"), ("SYMMNTP", "ntpStatusPacketLoad"), ("SYMMNTP", "ntpStatusVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntpStatusGroup = ntpStatusGroup.setStatus('current')
if mibBuilder.loadTexts: ntpStatusGroup.setDescription('A collection of objects providing information applicable to NTP status group.')
ntpConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 3, 2, 2)).setObjects(("SYMMNTP", "ntpCommonState"), ("SYMMNTP", "ntpCommonTTL"), ("SYMMNTP", "ntpCommonDSCP"), ("SYMMNTP", "ntpCommonDSCPValue"), ("SYMMNTP", "ntpCommonVlanId"), ("SYMMNTP", "ntpCommonServiceLoadAlarmThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntpConfigGroup = ntpConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ntpConfigGroup.setDescription('A collection of objects providing information applicable to NTP configuration group.')
mibBuilder.exportSymbols("SYMMNTP", ntpStatusLeapStatus=ntpStatusLeapStatus, ntpCompliances=ntpCompliances, symmNTP=symmNTP, ntpStatusRootDispersion=ntpStatusRootDispersion, ntpCommonStatusTable=ntpCommonStatusTable, ntpCommonConfigEntry=ntpCommonConfigEntry, ntpStatusGroup=ntpStatusGroup, ntpConfig=ntpConfig, TLocalTimeOffset=TLocalTimeOffset, TLatAndLon=TLatAndLon, ntpCommonDSCP=ntpCommonDSCP, ntpCommonConfigTable=ntpCommonConfigTable, TAntHeight=TAntHeight, ntpCommonTTL=ntpCommonTTL, ntpCommonDSCPValue=ntpCommonDSCPValue, ntpStatusStratumLevel=ntpStatusStratumLevel, ntpCommonIndex=ntpCommonIndex, ntpBasicCompliance=ntpBasicCompliance, ntpStatusPacketLoad=ntpStatusPacketLoad, ntpStatusMode=ntpStatusMode, ntpStatusVersion=ntpStatusVersion, ntpStatusIndex=ntpStatusIndex, ntpUocGroups=ntpUocGroups, DateAndTime=DateAndTime, ntpCommonVlanId=ntpCommonVlanId, ntpCommonStatusEntry=ntpCommonStatusEntry, ntpCommonState=ntpCommonState, ntpConformance=ntpConformance, TSsm=TSsm, ntpStatusEnable=ntpStatusEnable, PYSNMP_MODULE_ID=symmNTP, ntpCommonServiceLoadAlarmThreshold=ntpCommonServiceLoadAlarmThreshold, ntpConfigGroup=ntpConfigGroup, ntpStatus=ntpStatus)
