#
# PySNMP MIB module SYMMNTPCLIENT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMNTPCLIENT
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:26 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Counter64, MibIdentifier, Gauge32, NotificationType, Counter32, IpAddress, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Counter64", "MibIdentifier", "Gauge32", "NotificationType", "Counter32", "IpAddress", "TimeTicks", "Integer32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
EnableValue, symmPacketService = mibBuilder.importSymbols("SYMM-COMMON-SMI", "EnableValue", "symmPacketService")
symmNTPClient = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3))
symmNTPClient.setRevisions(('2018-03-21 11:07',))
if mibBuilder.loadTexts: symmNTPClient.setLastUpdated('201806280521Z')
if mibBuilder.loadTexts: symmNTPClient.setOrganization('Symmetricom')
class DateAndTime(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d,1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
class TLocalTimeOffset(TextualConvention, OctetString):
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
ntpcLastUpdate = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpcLastUpdate.setStatus('current')
ntpcStatus = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpcStatus.setStatus('current')
ntpcServerIP = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpcServerIP.setStatus('current')
ntpcServerLeapIndicator = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpcServerLeapIndicator.setStatus('current')
ntpcServerStratum = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpcServerStratum.setStatus('current')
ntpcServerRefID = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpcServerRefID.setStatus('current')
ntpClientConfigInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2))
ntpcServerIPAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 1), )
if mibBuilder.loadTexts: ntpcServerIPAddrTable.setStatus('current')
ntpcServerIPAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 1, 1), ).setIndexNames((0, "SYMMNTPCLIENT", "ntpcServerIPAddrIndex"))
if mibBuilder.loadTexts: ntpcServerIPAddrEntry.setStatus('current')
ntpcServerIPAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3)))
if mibBuilder.loadTexts: ntpcServerIPAddrIndex.setStatus('current')
ntpcServerIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpcServerIPAddress.setStatus('current')
ntpClientState = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 2), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpClientState.setStatus('current')
ntpClientSyncOnBoot = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 3), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpClientSyncOnBoot.setStatus('current')
ntpClientPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 17))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpClientPollInterval.setStatus('current')
ntpClientTime = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 5), NTPCLIENTTIME()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpClientTime.setStatus('current')
ntpClientConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 3))
if mibBuilder.loadTexts: ntpClientConformance.setStatus('current')
ntpClientCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 3, 1))
ntpClientBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 3, 1, 1)).setObjects(("SYMMNTPCLIENT", "ntpClientStatusInfoGroup"), ("SYMMNTPCLIENT", "ntpClientConfigInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntpClientBasicCompliance = ntpClientBasicCompliance.setStatus('current')
ntpClientUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 3, 2))
ntpClientStatusInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 3, 2, 1)).setObjects(("SYMMNTPCLIENT", "ntpcTimeOffset"), ("SYMMNTPCLIENT", "ntpcLastUpdate"), ("SYMMNTPCLIENT", "ntpcStatus"), ("SYMMNTPCLIENT", "ntpcServerIP"), ("SYMMNTPCLIENT", "ntpcServerLeapIndicator"), ("SYMMNTPCLIENT", "ntpcServerStratum"), ("SYMMNTPCLIENT", "ntpcServerRefID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntpClientStatusInfoGroup = ntpClientStatusInfoGroup.setStatus('current')
ntpClientConfigInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 3, 2, 2)).setObjects(("SYMMNTPCLIENT", "ntpcServerIPAddress"), ("SYMMNTPCLIENT", "ntpClientState"), ("SYMMNTPCLIENT", "ntpClientSyncOnBoot"), ("SYMMNTPCLIENT", "ntpClientPollInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntpClientConfigInfoGroup = ntpClientConfigInfoGroup.setStatus('current')
mibBuilder.exportSymbols("SYMMNTPCLIENT", ntpClientConformance=ntpClientConformance, ntpcServerLeapIndicator=ntpcServerLeapIndicator, ntpClientTime=ntpClientTime, symmNTPClient=symmNTPClient, ntpcServerIPAddress=ntpcServerIPAddress, DateAndTime=DateAndTime, ntpcServerIPAddrEntry=ntpcServerIPAddrEntry, TLocalTimeOffset=TLocalTimeOffset, ntpcServerIPAddrIndex=ntpcServerIPAddrIndex, ntpClientUocGroups=ntpClientUocGroups, ntpcTimeOffset=ntpcTimeOffset, ntpcServerRefID=ntpcServerRefID, PYSNMP_MODULE_ID=symmNTPClient, NTPCLIENTTIME=NTPCLIENTTIME, ntpClientStatusInfo=ntpClientStatusInfo, ntpClientBasicCompliance=ntpClientBasicCompliance, ntpcServerIPAddrTable=ntpcServerIPAddrTable, ntpcLastUpdate=ntpcLastUpdate, ntpClientSyncOnBoot=ntpClientSyncOnBoot, ntpcServerStratum=ntpcServerStratum, ntpcServerIP=ntpcServerIP, ntpClientConfigInfo=ntpClientConfigInfo, ntpClientPollInterval=ntpClientPollInterval, ntpClientConfigInfoGroup=ntpClientConfigInfoGroup, ntpClientStatusInfoGroup=ntpClientStatusInfoGroup, ntpClientState=ntpClientState, ntpClientCompliances=ntpClientCompliances, ntpcStatus=ntpcStatus)
