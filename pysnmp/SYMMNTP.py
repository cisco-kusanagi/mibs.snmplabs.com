#
# PySNMP MIB module SYMMNTP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMNTP
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:25 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, ifNumber = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifNumber")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, iso, NotificationType, Counter32, ObjectIdentity, MibIdentifier, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, ModuleIdentity, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "NotificationType", "Counter32", "ObjectIdentity", "MibIdentifier", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "ModuleIdentity", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
symmPacketService, EnableValue = mibBuilder.importSymbols("SYMM-COMMON-SMI", "symmPacketService", "EnableValue")
symmNTP = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2))
if mibBuilder.loadTexts: symmNTP.setLastUpdated('201512111510Z')
if mibBuilder.loadTexts: symmNTP.setOrganization('Symmetricom')
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

ntpStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1))
ntpCommonStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1), )
if mibBuilder.loadTexts: ntpCommonStatusTable.setStatus('current')
ntpCommonStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMNTP", "ntpStatusIndex"))
if mibBuilder.loadTexts: ntpCommonStatusEntry.setStatus('current')
ntpStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: ntpStatusIndex.setStatus('current')
ntpStatusEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 2), EnableValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpStatusEnable.setStatus('current')
ntpStatusMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpStatusMode.setStatus('current')
ntpStatusLeapStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpStatusLeapStatus.setStatus('current')
ntpStatusStratumLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpStatusStratumLevel.setStatus('current')
ntpStatusRootDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpStatusRootDispersion.setStatus('current')
ntpStatusPacketLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpStatusPacketLoad.setStatus('current')
ntpStatusVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpStatusVersion.setStatus('current')
ntpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2))
ntpCommonConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1), )
if mibBuilder.loadTexts: ntpCommonConfigTable.setStatus('current')
ntpCommonConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMNTP", "ntpCommonIndex"))
if mibBuilder.loadTexts: ntpCommonConfigEntry.setStatus('current')
ntpCommonIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: ntpCommonIndex.setStatus('current')
ntpCommonState = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 2), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpCommonState.setStatus('current')
ntpCommonTTL = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpCommonTTL.setStatus('current')
ntpCommonDSCP = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 4), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpCommonDSCP.setStatus('current')
ntpCommonDSCPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpCommonDSCPValue.setStatus('current')
ntpCommonVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpCommonVlanId.setStatus('current')
ntpCommonServiceLoadAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpCommonServiceLoadAlarmThreshold.setStatus('current')
ntpConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 3))
if mibBuilder.loadTexts: ntpConformance.setStatus('current')
ntpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 3, 1))
ntpBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 3, 1, 1)).setObjects(("SYMMNTP", "ntpStatusGroup"), ("SYMMNTP", "ntpConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntpBasicCompliance = ntpBasicCompliance.setStatus('current')
ntpUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 3, 2))
ntpStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 3, 2, 1)).setObjects(("SYMMNTP", "ntpStatusEnable"), ("SYMMNTP", "ntpStatusMode"), ("SYMMNTP", "ntpStatusLeapStatus"), ("SYMMNTP", "ntpStatusStratumLevel"), ("SYMMNTP", "ntpStatusRootDispersion"), ("SYMMNTP", "ntpStatusPacketLoad"), ("SYMMNTP", "ntpStatusVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntpStatusGroup = ntpStatusGroup.setStatus('current')
ntpConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 2, 3, 2, 2)).setObjects(("SYMMNTP", "ntpCommonState"), ("SYMMNTP", "ntpCommonTTL"), ("SYMMNTP", "ntpCommonDSCP"), ("SYMMNTP", "ntpCommonDSCPValue"), ("SYMMNTP", "ntpCommonVlanId"), ("SYMMNTP", "ntpCommonServiceLoadAlarmThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntpConfigGroup = ntpConfigGroup.setStatus('current')
mibBuilder.exportSymbols("SYMMNTP", ntpCompliances=ntpCompliances, ntpCommonStatusTable=ntpCommonStatusTable, ntpCommonConfigTable=ntpCommonConfigTable, ntpStatusPacketLoad=ntpStatusPacketLoad, ntpConfigGroup=ntpConfigGroup, PYSNMP_MODULE_ID=symmNTP, ntpBasicCompliance=ntpBasicCompliance, ntpStatusEnable=ntpStatusEnable, ntpConfig=ntpConfig, ntpStatusMode=ntpStatusMode, ntpCommonDSCPValue=ntpCommonDSCPValue, ntpStatus=ntpStatus, TSsm=TSsm, TAntHeight=TAntHeight, TLocalTimeOffset=TLocalTimeOffset, ntpStatusRootDispersion=ntpStatusRootDispersion, ntpCommonStatusEntry=ntpCommonStatusEntry, ntpStatusVersion=ntpStatusVersion, ntpCommonIndex=ntpCommonIndex, symmNTP=symmNTP, ntpCommonVlanId=ntpCommonVlanId, ntpUocGroups=ntpUocGroups, ntpCommonConfigEntry=ntpCommonConfigEntry, ntpStatusStratumLevel=ntpStatusStratumLevel, ntpCommonServiceLoadAlarmThreshold=ntpCommonServiceLoadAlarmThreshold, ntpConformance=ntpConformance, ntpStatusIndex=ntpStatusIndex, ntpCommonState=ntpCommonState, DateAndTime=DateAndTime, ntpCommonDSCP=ntpCommonDSCP, ntpStatusLeapStatus=ntpStatusLeapStatus, TLatAndLon=TLatAndLon, ntpCommonTTL=ntpCommonTTL, ntpStatusGroup=ntpStatusGroup)
