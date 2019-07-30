#
# PySNMP MIB module SYMMCOMMONPTP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMCOMMONPTP
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:16 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, ifNumber = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifNumber")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Unsigned32, ObjectIdentity, ModuleIdentity, iso, Bits, MibIdentifier, Counter32, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "iso", "Bits", "MibIdentifier", "Counter32", "Gauge32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
EnableValue, symmPacketService = mibBuilder.importSymbols("SYMM-COMMON-SMI", "EnableValue", "symmPacketService")
symmPTPv2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1))
symmPTPv2.setRevisions(('2018-07-31 06:20',))
if mibBuilder.loadTexts: symmPTPv2.setLastUpdated('201807310620Z')
if mibBuilder.loadTexts: symmPTPv2.setOrganization('Symmetricom')
class PTPPROFILEVALUE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("profileTelecom2008", 1), ("profileDefault", 2), ("profileHybrid", 3), ("profileITU8265one", 4), ("profileEthernetDefault", 5), ("profileITU8275one", 6), ("profileITU8275two", 7))

class PTPTIMESCALETYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("auto", 1), ("arb", 2), ("ptp", 3))

class PTPMGMTADDRTYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("unicast", 0), ("multicast", 1))

class PTPTRANSPORTTYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ethernet", 1), ("ipv4", 2))

class PTPADDRMODETYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unicast", 0), ("multicast", 1), ("multicasthybrid", 2))

class PORTSTATEVALUE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class G82751McAddrValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("mac011b19000000", 1), ("mac0180c200000e", 2))

class VLANID(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("none", 1))

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

ptpv2Status = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1))
ptpv2StatusTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1), )
if mibBuilder.loadTexts: ptpv2StatusTable.setStatus('current')
ptpv2StatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMCOMMONPTP", "ptpv2StatusIndex"))
if mibBuilder.loadTexts: ptpv2StatusEntry.setStatus('current')
ptpv2StatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: ptpv2StatusIndex.setStatus('current')
ptpv2StatusPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1, 2), EnableValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpv2StatusPortEnable.setStatus('current')
ptpv2StatusClockID = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpv2StatusClockID.setStatus('current')
ptpv2StatusProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1, 4), PTPPROFILEVALUE()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpv2StatusProfile.setStatus('current')
ptpv2StatusClockClass = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpv2StatusClockClass.setStatus('current')
ptpv2StatusClockAccuracy = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpv2StatusClockAccuracy.setStatus('current')
ptpv2StatusTimescale = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1, 7), PTPTIMESCALETYPE()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpv2StatusTimescale.setStatus('current')
ptpv2StatusNumClient = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpv2StatusNumClient.setStatus('current')
ptpv2StatusClientLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpv2StatusClientLoad.setStatus('current')
ptpv2ClientDataTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 2), )
if mibBuilder.loadTexts: ptpv2ClientDataTable.setStatus('current')
ptpv2ClientDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 2, 1), ).setIndexNames((0, "SYMMCOMMONPTP", "ptpv2ClientDataIndex"))
if mibBuilder.loadTexts: ptpv2ClientDataEntry.setStatus('current')
ptpv2ClientDataIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpv2ClientDataIndex.setStatus('current')
ptpv2ClientData = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpv2ClientData.setStatus('current')
ptpv2Config = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2))
ptpv2CommonTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1), )
if mibBuilder.loadTexts: ptpv2CommonTable.setStatus('current')
ptpv2CommonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMCOMMONPTP", "ptpv2CommonIndex"))
if mibBuilder.loadTexts: ptpv2CommonEntry.setStatus('current')
ptpv2CommonIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: ptpv2CommonIndex.setStatus('current')
ptpv2Profile = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 2), PTPPROFILEVALUE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2Profile.setStatus('current')
ptpv2ClockID = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2ClockID.setStatus('current')
ptpv2Priority1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2Priority1.setStatus('current')
ptpv2Priority2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2Priority2.setStatus('current')
ptpv2Domain = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2Domain.setStatus('current')
ptpv2DSCPState = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 7), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2DSCPState.setStatus('current')
ptpv2DSCPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2DSCPValue.setStatus('current')
ptpv2State = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 9), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2State.setStatus('current')
ptpv2MaxClient = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1500)).clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2MaxClient.setStatus('current')
ptpv2AnnounceLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-4, 4)).clone(-3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2AnnounceLimit.setStatus('current')
ptpv2SyncLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-7, 7)).clone(-7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2SyncLimit.setStatus('current')
ptpv2DelayLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-7, 7)).clone(-7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2DelayLimit.setStatus('current')
ptpv2TwoStep = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 14), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2TwoStep.setStatus('current')
ptpv2MgmtAddrMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 15), PTPMGMTADDRTYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2MgmtAddrMode.setStatus('current')
ptpv2TTL = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2TTL.setStatus('current')
ptpv2AlternateGM = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 17), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2AlternateGM.setStatus('current')
ptpv2TimeScale = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 18), PTPTIMESCALETYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2TimeScale.setStatus('current')
ptpv2Dither = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 19), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2Dither.setStatus('current')
ptpv2ServiceLoadAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2ServiceLoadAlarmThreshold.setStatus('current')
ptpv2UnicastTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 2), )
if mibBuilder.loadTexts: ptpv2UnicastTable.setStatus('current')
ptpv2UnicastEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMCOMMONPTP", "ptpv2UnicastIndex"))
if mibBuilder.loadTexts: ptpv2UnicastEntry.setStatus('current')
ptpv2UnicastIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: ptpv2UnicastIndex.setStatus('current')
ptpv2UnicastNeg = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 2, 1, 2), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2UnicastNeg.setStatus('current')
ptpv2UnicastLeaseDurLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2UnicastLeaseDurLimit.setStatus('current')
ptpv2UnicastInterfaceRateTLV = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 2, 1, 4), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2UnicastInterfaceRateTLV.setStatus('current')
ptpv2UnicastLeaseExtension = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2UnicastLeaseExtension.setStatus('current')
ptpv2MulticastTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 3), )
if mibBuilder.loadTexts: ptpv2MulticastTable.setStatus('current')
ptpv2MulticastEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMCOMMONPTP", "ptpv2MulticastIndex"))
if mibBuilder.loadTexts: ptpv2MulticastEntry.setStatus('current')
ptpv2MulticastIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: ptpv2MulticastIndex.setStatus('current')
ptpv2MulticastAnnounceInt = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-4, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2MulticastAnnounceInt.setStatus('current')
ptpv2MulticastSyncInt = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-7, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2MulticastSyncInt.setStatus('current')
ptpv2MulticastDelayInt = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-7, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2MulticastDelayInt.setStatus('current')
ptpv2MulticastAnnoTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2MulticastAnnoTimeout.setStatus('current')
ptpv2MulticastVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2MulticastVlanId.setStatus('current')
ptpv2MulticastClientTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 3600)).clone(360)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2MulticastClientTimeout.setStatus('current')
ptpv2G82751Table = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 4), )
if mibBuilder.loadTexts: ptpv2G82751Table.setStatus('current')
ptpv2G82751Entry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMCOMMONPTP", "ptpv2G82751Index"))
if mibBuilder.loadTexts: ptpv2G82751Entry.setStatus('current')
ptpv2G82751Index = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: ptpv2G82751Index.setStatus('current')
ptpv2G82751MulticastAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 4, 1, 2), G82751McAddrValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2G82751MulticastAddr.setStatus('current')
ptpv2G82751LocalPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2G82751LocalPriority.setStatus('current')
ptpv2ReflectorTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 5), )
if mibBuilder.loadTexts: ptpv2ReflectorTable.setStatus('current')
ptpv2ReflectorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMCOMMONPTP", "ptpv2ReflectorIndex"))
if mibBuilder.loadTexts: ptpv2ReflectorEntry.setStatus('current')
ptpv2ReflectorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: ptpv2ReflectorIndex.setStatus('current')
ptpv2ReflectorAnnounceIntv = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-3, 0))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2ReflectorAnnounceIntv.setStatus('current')
ptpv2ReflectorSyncDelayIntv = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-7, -4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2ReflectorSyncDelayIntv.setStatus('current')
ptpv2ReflectorClientTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2ReflectorClientTimeout.setStatus('current')
ptpv2ReflectorVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 5, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptpv2ReflectorVlanID.setStatus('current')
ptpv2Conformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3))
if mibBuilder.loadTexts: ptpv2Conformance.setStatus('current')
ptpv2Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3, 1))
ptpv2BasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3, 1, 1)).setObjects(("SYMMCOMMONPTP", "ptpv2StatusGroup"), ("SYMMCOMMONPTP", "ptpv2ClientDataGroup"), ("SYMMCOMMONPTP", "ptpv2CommonGroup"), ("SYMMCOMMONPTP", "ptpv2UnicastGroup"), ("SYMMCOMMONPTP", "ptpv2MulticastGroup"), ("SYMMCOMMONPTP", "ptpv2G82751Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpv2BasicCompliance = ptpv2BasicCompliance.setStatus('current')
ptpv2UocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3, 2))
ptpv2StatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3, 2, 1)).setObjects(("SYMMCOMMONPTP", "ptpv2StatusPortEnable"), ("SYMMCOMMONPTP", "ptpv2StatusClockID"), ("SYMMCOMMONPTP", "ptpv2StatusProfile"), ("SYMMCOMMONPTP", "ptpv2StatusClockClass"), ("SYMMCOMMONPTP", "ptpv2StatusClockAccuracy"), ("SYMMCOMMONPTP", "ptpv2StatusTimescale"), ("SYMMCOMMONPTP", "ptpv2StatusNumClient"), ("SYMMCOMMONPTP", "ptpv2StatusClientLoad"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpv2StatusGroup = ptpv2StatusGroup.setStatus('current')
ptpv2ClientDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3, 2, 2)).setObjects(("SYMMCOMMONPTP", "ptpv2ClientDataIndex"), ("SYMMCOMMONPTP", "ptpv2ClientData"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpv2ClientDataGroup = ptpv2ClientDataGroup.setStatus('current')
ptpv2CommonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3, 2, 3)).setObjects(("SYMMCOMMONPTP", "ptpv2Profile"), ("SYMMCOMMONPTP", "ptpv2ClockID"), ("SYMMCOMMONPTP", "ptpv2Priority1"), ("SYMMCOMMONPTP", "ptpv2Priority2"), ("SYMMCOMMONPTP", "ptpv2Domain"), ("SYMMCOMMONPTP", "ptpv2DSCPState"), ("SYMMCOMMONPTP", "ptpv2DSCPValue"), ("SYMMCOMMONPTP", "ptpv2State"), ("SYMMCOMMONPTP", "ptpv2MaxClient"), ("SYMMCOMMONPTP", "ptpv2AnnounceLimit"), ("SYMMCOMMONPTP", "ptpv2SyncLimit"), ("SYMMCOMMONPTP", "ptpv2DelayLimit"), ("SYMMCOMMONPTP", "ptpv2TwoStep"), ("SYMMCOMMONPTP", "ptpv2MgmtAddrMode"), ("SYMMCOMMONPTP", "ptpv2TTL"), ("SYMMCOMMONPTP", "ptpv2AlternateGM"), ("SYMMCOMMONPTP", "ptpv2TimeScale"), ("SYMMCOMMONPTP", "ptpv2Dither"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpv2CommonGroup = ptpv2CommonGroup.setStatus('current')
ptpv2UnicastGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3, 2, 4)).setObjects(("SYMMCOMMONPTP", "ptpv2UnicastNeg"), ("SYMMCOMMONPTP", "ptpv2UnicastLeaseDurLimit"), ("SYMMCOMMONPTP", "ptpv2UnicastInterfaceRateTLV"), ("SYMMCOMMONPTP", "ptpv2UnicastLeaseExtension"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpv2UnicastGroup = ptpv2UnicastGroup.setStatus('current')
ptpv2MulticastGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3, 2, 5)).setObjects(("SYMMCOMMONPTP", "ptpv2MulticastAnnounceInt"), ("SYMMCOMMONPTP", "ptpv2MulticastSyncInt"), ("SYMMCOMMONPTP", "ptpv2MulticastDelayInt"), ("SYMMCOMMONPTP", "ptpv2MulticastAnnoTimeout"), ("SYMMCOMMONPTP", "ptpv2MulticastVlanId"), ("SYMMCOMMONPTP", "ptpv2MulticastClientTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpv2MulticastGroup = ptpv2MulticastGroup.setStatus('current')
ptpv2G82751Group = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3, 2, 6)).setObjects(("SYMMCOMMONPTP", "ptpv2G82751MulticastAddr"), ("SYMMCOMMONPTP", "ptpv2G82751LocalPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpv2G82751Group = ptpv2G82751Group.setStatus('current')
mibBuilder.exportSymbols("SYMMCOMMONPTP", ptpv2ReflectorAnnounceIntv=ptpv2ReflectorAnnounceIntv, PYSNMP_MODULE_ID=symmPTPv2, ptpv2Domain=ptpv2Domain, ptpv2StatusClockClass=ptpv2StatusClockClass, ptpv2StatusNumClient=ptpv2StatusNumClient, ptpv2ClientDataTable=ptpv2ClientDataTable, PTPADDRMODETYPE=PTPADDRMODETYPE, ptpv2ClientData=ptpv2ClientData, ptpv2UnicastTable=ptpv2UnicastTable, ptpv2ReflectorSyncDelayIntv=ptpv2ReflectorSyncDelayIntv, ptpv2TTL=ptpv2TTL, ptpv2Compliances=ptpv2Compliances, ptpv2G82751Index=ptpv2G82751Index, ptpv2MulticastClientTimeout=ptpv2MulticastClientTimeout, PTPMGMTADDRTYPE=PTPMGMTADDRTYPE, DateAndTime=DateAndTime, ptpv2StatusTimescale=ptpv2StatusTimescale, ptpv2Profile=ptpv2Profile, ptpv2G82751Entry=ptpv2G82751Entry, ptpv2StatusProfile=ptpv2StatusProfile, ptpv2MulticastSyncInt=ptpv2MulticastSyncInt, ptpv2State=ptpv2State, ptpv2CommonIndex=ptpv2CommonIndex, ptpv2MulticastGroup=ptpv2MulticastGroup, ptpv2StatusClockAccuracy=ptpv2StatusClockAccuracy, ptpv2TimeScale=ptpv2TimeScale, ptpv2UocGroups=ptpv2UocGroups, ptpv2ClockID=ptpv2ClockID, ptpv2UnicastInterfaceRateTLV=ptpv2UnicastInterfaceRateTLV, ptpv2G82751Group=ptpv2G82751Group, ptpv2StatusGroup=ptpv2StatusGroup, VLANID=VLANID, ptpv2MulticastIndex=ptpv2MulticastIndex, ptpv2MulticastTable=ptpv2MulticastTable, PTPTIMESCALETYPE=PTPTIMESCALETYPE, PTPTRANSPORTTYPE=PTPTRANSPORTTYPE, ptpv2StatusEntry=ptpv2StatusEntry, ptpv2ReflectorEntry=ptpv2ReflectorEntry, ptpv2MulticastVlanId=ptpv2MulticastVlanId, ptpv2UnicastEntry=ptpv2UnicastEntry, ptpv2Config=ptpv2Config, ptpv2TwoStep=ptpv2TwoStep, ptpv2CommonTable=ptpv2CommonTable, PTPPROFILEVALUE=PTPPROFILEVALUE, ptpv2DSCPState=ptpv2DSCPState, TLatAndLon=TLatAndLon, ptpv2CommonGroup=ptpv2CommonGroup, ptpv2UnicastIndex=ptpv2UnicastIndex, ptpv2G82751LocalPriority=ptpv2G82751LocalPriority, ptpv2MaxClient=ptpv2MaxClient, ptpv2G82751Table=ptpv2G82751Table, ptpv2ClientDataGroup=ptpv2ClientDataGroup, ptpv2MulticastAnnounceInt=ptpv2MulticastAnnounceInt, G82751McAddrValue=G82751McAddrValue, ptpv2AlternateGM=ptpv2AlternateGM, ptpv2Status=ptpv2Status, TSsm=TSsm, ptpv2UnicastNeg=ptpv2UnicastNeg, ptpv2StatusIndex=ptpv2StatusIndex, ptpv2ClientDataEntry=ptpv2ClientDataEntry, ptpv2BasicCompliance=ptpv2BasicCompliance, TLocalTimeOffset=TLocalTimeOffset, ptpv2ServiceLoadAlarmThreshold=ptpv2ServiceLoadAlarmThreshold, ptpv2StatusTable=ptpv2StatusTable, ptpv2MgmtAddrMode=ptpv2MgmtAddrMode, ptpv2AnnounceLimit=ptpv2AnnounceLimit, ptpv2DSCPValue=ptpv2DSCPValue, PORTSTATEVALUE=PORTSTATEVALUE, ptpv2ReflectorTable=ptpv2ReflectorTable, symmPTPv2=symmPTPv2, ptpv2ClientDataIndex=ptpv2ClientDataIndex, ptpv2UnicastGroup=ptpv2UnicastGroup, ptpv2StatusClockID=ptpv2StatusClockID, ptpv2MulticastEntry=ptpv2MulticastEntry, ptpv2ReflectorClientTimeout=ptpv2ReflectorClientTimeout, ptpv2StatusClientLoad=ptpv2StatusClientLoad, ptpv2SyncLimit=ptpv2SyncLimit, ptpv2Priority1=ptpv2Priority1, ptpv2ReflectorIndex=ptpv2ReflectorIndex, ptpv2G82751MulticastAddr=ptpv2G82751MulticastAddr, TAntHeight=TAntHeight, ptpv2DelayLimit=ptpv2DelayLimit, ptpv2ReflectorVlanID=ptpv2ReflectorVlanID, ptpv2StatusPortEnable=ptpv2StatusPortEnable, ptpv2UnicastLeaseDurLimit=ptpv2UnicastLeaseDurLimit, ptpv2MulticastDelayInt=ptpv2MulticastDelayInt, ptpv2Conformance=ptpv2Conformance, ptpv2Dither=ptpv2Dither, ptpv2Priority2=ptpv2Priority2, ptpv2UnicastLeaseExtension=ptpv2UnicastLeaseExtension, ptpv2MulticastAnnoTimeout=ptpv2MulticastAnnoTimeout, ptpv2CommonEntry=ptpv2CommonEntry)
