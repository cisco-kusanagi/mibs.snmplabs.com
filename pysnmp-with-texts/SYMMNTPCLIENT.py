#
# PySNMP MIB module SYMMNTPCLIENT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMNTPCLIENT
# Produced by pysmi-0.3.4 at Tue Jul 30 11:35:06 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, ObjectIdentity, Unsigned32, iso, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, IpAddress, Integer32, Bits, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Unsigned32", "iso", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "IpAddress", "Integer32", "Bits", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
EnableValue, symmPacketService = mibBuilder.importSymbols("SYMM-COMMON-SMI", "EnableValue", "symmPacketService")
symmNTPClient = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3))
symmNTPClient.setRevisions(('2018-03-21 11:07',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: symmNTPClient.setRevisionsDescriptions((' Symmetricom NTP Client ',))
if mibBuilder.loadTexts: symmNTPClient.setLastUpdated('201806280521Z')
if mibBuilder.loadTexts: symmNTPClient.setOrganization('Symmetricom')
if mibBuilder.loadTexts: symmNTPClient.setContactInfo('Symmetricom Technical Support 1-888-367-7966 toll free USA 1-408-428-7907 worldwide Support@symmetricom.com ')
if mibBuilder.loadTexts: symmNTPClient.setDescription('This is the Symmetricom NTP Client MIB. It has two main nodes: NTPClient status and NTPClient configuration.')
class DateAndTime(TextualConvention, OctetString):
    description = "A date-time specification. field octets contents range ----- ------ -------- ----- 1 1-2 year* 0..65536 2 3 month 1..12 3 4 day 1..31 4 5 hour 0..23 5 6 minutes 0..59 6 7 seconds 0..60 (use 60 for leap-second) 7 8 deci-seconds 0..9 8 9 direction from UTC '+' / '-' 9 10 hours from UTC* 0..13 10 11 minutes from UTC 0..59 * Notes: - the value of year is in network-byte order - daylight saving time in New Zealand is +13 For example, Tuesday May 26, 1992 at 1:30:15 PM EDT would be displayed as: 1992-5-26,13:30:15.0,-4:0 Note that if only local time is known, then timezone information (fields 8-10) is not present."
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d,1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
class TLocalTimeOffset(TextualConvention, OctetString):
    description = "A local time offset specification. field octets contents range ----- ------ -------- ----- 1 1 direction from UTC '+' / '-' 2 2 hours from UTC* 0..13 3 3 minutes from UTC 0..59 * Notes: - the value of year is in network-byte order - The hours range is 0..13 For example, the -6 local time offset would be displayed as: -6:0 "
    status = 'current'
    displayHint = '1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class NTPCLIENTTIME(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("syncNow", 1), ("writeOnlyObject", 2))

ntpClientStatusInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1))
ntpcTimeOffset = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 1), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpcTimeOffset.setStatus('current')
if mibBuilder.loadTexts: ntpcTimeOffset.setDescription('NTP client Time Offset')
ntpcLastUpdate = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpcLastUpdate.setStatus('current')
if mibBuilder.loadTexts: ntpcLastUpdate.setDescription('NTP client Last Update')
ntpcStatus = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpcStatus.setStatus('current')
if mibBuilder.loadTexts: ntpcStatus.setDescription('NTP client Status')
ntpcServerIP = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpcServerIP.setStatus('current')
if mibBuilder.loadTexts: ntpcServerIP.setDescription('NTP client ServerIP')
ntpcServerLeapIndicator = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpcServerLeapIndicator.setStatus('current')
if mibBuilder.loadTexts: ntpcServerLeapIndicator.setDescription('NTP client Server Leap Indicator')
ntpcServerStratum = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpcServerStratum.setStatus('current')
if mibBuilder.loadTexts: ntpcServerStratum.setDescription('NTP client Server Leap Indicator')
ntpcServerRefID = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpcServerRefID.setStatus('current')
if mibBuilder.loadTexts: ntpcServerRefID.setDescription('NTP client Server Reference ID')
ntpClientConfigInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2))
ntpcServerIPAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 1), )
if mibBuilder.loadTexts: ntpcServerIPAddrTable.setStatus('current')
if mibBuilder.loadTexts: ntpcServerIPAddrTable.setDescription("The NTP-Client Server IP Table. This table's row be added or deleted")
ntpcServerIPAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 1, 1), ).setIndexNames((0, "SYMMNTPCLIENT", "ntpcServerIPAddrIndex"))
if mibBuilder.loadTexts: ntpcServerIPAddrEntry.setStatus('current')
if mibBuilder.loadTexts: ntpcServerIPAddrEntry.setDescription('NTP-Client Server entry')
ntpcServerIPAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3)))
if mibBuilder.loadTexts: ntpcServerIPAddrIndex.setStatus('current')
if mibBuilder.loadTexts: ntpcServerIPAddrIndex.setDescription('Local index of the NTP Client Server IP table.')
ntpcServerIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpcServerIPAddress.setStatus('current')
if mibBuilder.loadTexts: ntpcServerIPAddress.setDescription('NTP-Client Server IP Address. IPv4 or IPv6 Address')
ntpClientState = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 2), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpClientState.setStatus('current')
if mibBuilder.loadTexts: ntpClientState.setDescription('The NTP-Client State ')
ntpClientSyncOnBoot = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 3), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpClientSyncOnBoot.setStatus('current')
if mibBuilder.loadTexts: ntpClientSyncOnBoot.setDescription('The NTP-Client Sync-On-Boot ')
ntpClientPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 17))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpClientPollInterval.setStatus('current')
if mibBuilder.loadTexts: ntpClientPollInterval.setDescription('The NTP-Client Poll Interval ')
ntpClientTime = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 5), NTPCLIENTTIME()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpClientTime.setStatus('current')
if mibBuilder.loadTexts: ntpClientTime.setDescription('The NTP-Client Time. This is write-only object. Valid ')
ntpClientConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 3))
if mibBuilder.loadTexts: ntpClientConformance.setStatus('current')
if mibBuilder.loadTexts: ntpClientConformance.setDescription('This subtree contains conformance statements for the SYMMNTPCLIENT.mib . ')
ntpClientCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 3, 1))
ntpClientBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 3, 1, 1)).setObjects(("SYMMNTPCLIENT", "ntpClientStatusInfoGroup"), ("SYMMNTPCLIENT", "ntpClientConfigInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntpClientBasicCompliance = ntpClientBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: ntpClientBasicCompliance.setDescription('The compliance statement for SNMP entities which have NTP packet service.')
ntpClientUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 3, 2))
ntpClientStatusInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 3, 2, 1)).setObjects(("SYMMNTPCLIENT", "ntpcTimeOffset"), ("SYMMNTPCLIENT", "ntpcLastUpdate"), ("SYMMNTPCLIENT", "ntpcStatus"), ("SYMMNTPCLIENT", "ntpcServerIP"), ("SYMMNTPCLIENT", "ntpcServerLeapIndicator"), ("SYMMNTPCLIENT", "ntpcServerStratum"), ("SYMMNTPCLIENT", "ntpcServerRefID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntpClientStatusInfoGroup = ntpClientStatusInfoGroup.setStatus('current')
if mibBuilder.loadTexts: ntpClientStatusInfoGroup.setDescription('A collection of objects providing information applicable to NTP-Client status group.')
ntpClientConfigInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 3, 2, 2)).setObjects(("SYMMNTPCLIENT", "ntpcServerIPAddress"), ("SYMMNTPCLIENT", "ntpClientState"), ("SYMMNTPCLIENT", "ntpClientSyncOnBoot"), ("SYMMNTPCLIENT", "ntpClientPollInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntpClientConfigInfoGroup = ntpClientConfigInfoGroup.setStatus('current')
if mibBuilder.loadTexts: ntpClientConfigInfoGroup.setDescription('A collection of objects providing information applicable to NTP-Client configuration group.')
mibBuilder.exportSymbols("SYMMNTPCLIENT", ntpcServerLeapIndicator=ntpcServerLeapIndicator, ntpcServerStratum=ntpcServerStratum, ntpcServerIPAddress=ntpcServerIPAddress, symmNTPClient=symmNTPClient, ntpcServerIPAddrIndex=ntpcServerIPAddrIndex, ntpcTimeOffset=ntpcTimeOffset, ntpClientConfigInfo=ntpClientConfigInfo, TLocalTimeOffset=TLocalTimeOffset, ntpClientConfigInfoGroup=ntpClientConfigInfoGroup, ntpClientSyncOnBoot=ntpClientSyncOnBoot, ntpClientConformance=ntpClientConformance, ntpcLastUpdate=ntpcLastUpdate, PYSNMP_MODULE_ID=symmNTPClient, ntpClientPollInterval=ntpClientPollInterval, ntpcStatus=ntpcStatus, NTPCLIENTTIME=NTPCLIENTTIME, DateAndTime=DateAndTime, ntpClientState=ntpClientState, ntpClientBasicCompliance=ntpClientBasicCompliance, ntpcServerIPAddrTable=ntpcServerIPAddrTable, ntpcServerIPAddrEntry=ntpcServerIPAddrEntry, ntpClientTime=ntpClientTime, ntpClientStatusInfo=ntpClientStatusInfo, ntpcServerIP=ntpcServerIP, ntpClientStatusInfoGroup=ntpClientStatusInfoGroup, ntpClientCompliances=ntpClientCompliances, ntpcServerRefID=ntpcServerRefID, ntpClientUocGroups=ntpClientUocGroups)
