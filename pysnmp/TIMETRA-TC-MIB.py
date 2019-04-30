#
# PySNMP MIB module TIMETRA-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMETRA-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:01:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, Gauge32, iso, ModuleIdentity, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, Integer32, Unsigned32, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "Gauge32", "iso", "ModuleIdentity", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "Integer32", "Unsigned32", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
timetraModules, = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "timetraModules")
timetraTCMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 2))
timetraTCMIBModule.setRevisions(('1911-02-01 00:00', '1909-02-28 00:00', '1908-07-01 00:00', '1908-01-01 00:00', '1907-01-01 00:00', '1906-03-23 00:00', '1905-08-31 00:00', '1905-01-24 00:00', '1904-01-15 00:00', '1903-08-15 00:00', '1903-01-20 00:00', '1901-05-29 00:00',))
if mibBuilder.loadTexts: timetraTCMIBModule.setLastUpdated('201102010000Z')
if mibBuilder.loadTexts: timetraTCMIBModule.setOrganization('Alcatel-Lucent')
class InterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class TmnxPortID(TextualConvention, Unsigned32):
    status = 'current'

class TmnxEncapVal(TextualConvention, Unsigned32):
    status = 'current'

class QTag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class QTagOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4094)

class QTagFullRange(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4095)

class QTagFullRangeOrNone(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 4095), )
class TmnxStrSapId(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class IpAddressPrefixLength(TextualConvention, Integer32):
    reference = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 32)

class TmnxActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("doAction", 1), ("notApplicable", 2))

class TmnxAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noop", 1), ("inService", 2), ("outOfService", 3))

class TmnxOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("inService", 2), ("outOfService", 3), ("transition", 4))

class TmnxStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("create", 1), ("delete", 2))

class TmnxEnabledDisabled(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class TmnxEnabledDisabledOrInherit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("inherit", 3))

class TNamedItem(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

class TNamedItemOrEmpty(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 32), )
class TLNamedItem(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 64)

class TLNamedItemOrEmpty(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 64), )
class TItemDescription(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 80)

class TItemLongDescription(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 160)

class TmnxVRtrID(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 10240)

class TmnxVRtrIDOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 10240)

class TmnxBgpAutonomousSystem(TextualConvention, Integer32):
    reference = 'BGP4-MIB.bgpPeerRemoteAs'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TmnxBgpLocalPreference(TextualConvention, Unsigned32):
    reference = 'RFC 1771 section 4.3 Path Attributes e)'
    status = 'current'

class TmnxBgpPreference(TextualConvention, Unsigned32):
    reference = 'RFC 1771 section 4.3 Path Attributes e)'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TmnxCustId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), )
class BgpPeeringStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("notApplicable", 0), ("installed", 1), ("notInstalled", 2), ("noEnhancedSubmgt", 3), ("wrongAntiSpoof", 4), ("parentItfDown", 5), ("hostInactive", 6), ("noDualHomingSupport", 7), ("invalidRadiusAttr", 8), ("noDynamicPeerGroup", 9), ("duplicatePeer", 10), ("maxPeersReached", 11), ("genError", 12))

class TmnxServId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ValueRangeConstraint(2147483648, 2147483648), ValueRangeConstraint(2147483649, 2147483649), ValueRangeConstraint(2147483650, 2147483650), )
class ServiceAdminStatus(TextualConvention, Integer32):
    reference = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class ServiceOperStatus(TextualConvention, Integer32):
    reference = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class TPolicyID(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 65535), ValueRangeConstraint(65536, 65536), ValueRangeConstraint(65537, 65537), )
class TTmplPolicyID(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class TSapIngressPolicyID(TPolicyID):
    status = 'current'

class TSapEgressPolicyID(TPolicyID):
    status = 'current'
    subtypeSpec = TPolicyID.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 65535), ValueRangeConstraint(65536, 65536), ValueRangeConstraint(65537, 65537), )
class TSdpIngressPolicyID(TPolicyID):
    status = 'current'

class TSdpEgressPolicyID(TPolicyID):
    status = 'current'

class TQosQGrpInstanceIDorZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TmnxBsxTransitIpPolicyId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class TmnxBsxTransitIpPolicyIdOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TmnxBsxTransPrefPolicyId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class TmnxBsxTransPrefPolicyIdOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TmnxBsxAarpId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class TmnxBsxAarpIdOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TmnxBsxAarpServiceRefType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("dualHomed", 1), ("shuntSubscriberSide", 2), ("shuntNetworkSide", 3))

class TSapEgrEncapGrpQosPolicyIdOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TSapEgrEncapGroupType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("isid", 1))

class TSapEgrEncapGroupActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("create", 1), ("destroy", 2))

class TPerPacketOffset(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32, 31)

class TPerPacketOffsetOvr(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-128, -128), ValueRangeConstraint(-32, 31), )
class TIngressHsmdaPerPacketOffset(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32, 31)

class TEgressQPerPacketOffset(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-64, 32)

class TIngHsmdaPerPacketOffsetOvr(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-128, -128), ValueRangeConstraint(-32, 31), )
class TEgressHsmdaPerPacketOffset(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32, 31)

class THsmdaCounterIdOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class THsmdaCounterIdOrZeroOrAll(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TEgrHsmdaPerPacketOffsetOvr(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-128, -128), ValueRangeConstraint(-32, 31), )
class TIngressHsmdaCounterId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class TIngressHsmdaCounterIdOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TEgressHsmdaCounterId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class TEgressHsmdaCounterIdOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TEgrRateModType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("aggRateLimit", 2), ("namedScheduler", 3))

class TPolicyStatementNameOrEmpty(TNamedItemOrEmpty):
    status = 'current'

class TmnxVcType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 9, 10, 11, 17, 18, 19, 20, 21, 23, 25, 4096))
    namedValues = NamedValues(("frDlciMartini", 1), ("atmSdu", 2), ("atmCell", 3), ("ethernetVlan", 4), ("ethernet", 5), ("atmVccCell", 9), ("atmVpcCell", 10), ("ipipe", 11), ("satopE1", 17), ("satopT1", 18), ("satopE3", 19), ("satopT3", 20), ("cesopsn", 21), ("cesopsnCas", 23), ("frDlci", 25), ("mirrorDest", 4096))

class TmnxVcId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TmnxVcIdOrNone(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class Dot1PPriority(TextualConvention, Integer32):
    reference = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 7), )
class Dot1PPriorityMask(TextualConvention, Integer32):
    reference = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class ServiceAccessPoint(TextualConvention, Integer32):
    reference = 'assigned numbers: http://www.iana.org/assignments/ieee-802-numbers'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TLspExpValue(TextualConvention, Integer32):
    reference = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 7), )
class TIpProtocol(TextualConvention, Integer32):
    reference = 'http://www.iana.org/assignments/protocol-numbers'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TIpOption(TextualConvention, Integer32):
    reference = 'http://www.iana.org/assignments/ip-parameters'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class TTcpUdpPort(TextualConvention, Integer32):
    reference = 'http://www.iana.org/assignments/port-numbers'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TOperator(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("none", 0), ("eq", 1), ("range", 2), ("lt", 3), ("gt", 4))

class TTcpUdpPortOperator(TOperator):
    status = 'current'

class TFrameType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5))
    namedValues = NamedValues(("e802dot3", 0), ("e802dot2LLC", 1), ("e802dot2SNAP", 2), ("ethernetII", 3), ("atm", 5))

class TQueueId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TQueueIdOrAll(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TIngressQueueId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TIngressMeterId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TSapIngressMeterId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TNetworkIngressMeterId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 16), )
class TEgressQueueId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TIngressHsmdaQueueId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TEgressHsmdaQueueId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class THsmdaSchedulerPolicyGroupId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2), )
class THsmdaPolicyIncludeQueues(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("q1to2", 1), ("q1to3", 2))

class THsmdaPolicyScheduleClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 3)

class TDSCPName(TNamedItem):
    status = 'current'

class TDSCPNameOrEmpty(TNamedItemOrEmpty):
    status = 'current'

class TDSCPValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 63)

class TDSCPValueOrNone(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 63), )
class TDSCPFilterActionValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TFCName(TNamedItem):
    status = 'current'

class TFCNameOrEmpty(TNamedItemOrEmpty):
    status = 'current'

class TFCSet(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("be", 0), ("l2", 1), ("af", 2), ("l1", 3), ("h2", 4), ("ef", 5), ("h1", 6), ("nc", 7))

class TFCType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("be", 0), ("l2", 1), ("af", 2), ("l1", 3), ("h2", 4), ("ef", 5), ("h1", 6), ("nc", 7))

class TmnxTunnelType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("sdp", 1), ("ldp", 2), ("rsvp", 3), ("gre", 4), ("bypass", 5), ("invalid", 6), ("bgp", 7))

class TmnxTunnelID(TextualConvention, Unsigned32):
    status = 'current'

class TmnxBgpRouteTarget(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxVPNRouteDistinguisher(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class SdpBindId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class TmnxVRtrMplsLspID(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TPortSchedulerPIR(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class TPortSchedulerPIRRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 400000000), )
class TPortSchedulerCIR(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 400000000), )
class TWeight(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class TNonZeroWeight(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 100)

class TPolicerWeight(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 100)

class THsmdaWeight(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 100)

class THsmdaWrrWeight(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 32)

class THsmdaWeightClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8))
    namedValues = NamedValues(("class1", 1), ("class2", 2), ("class4", 4), ("class8", 8))

class THsmdaWeightOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(1, 100), )
class THsmdaWrrWeightOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(1, 32), )
class TCIRRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class THPolCIRRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 20000000), )
class TRateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("kbps", 1), ("percent", 2))

class TBWRateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("kbps", 1), ("percentPortLimit", 2), ("percentLocalLimit", 3))

class TPolicerRateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("kbps", 1), ("percentLocalLimit", 2))

class TCIRRateOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class THPolCIRRateOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 20000000), )
class TCIRPercentOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(0, 10000), )
class THsmdaCIRKRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class THsmdaCIRKRateOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class THsmdaCIRMRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000), )
class THsmdaCIRMRateOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000), )
class TPIRRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class THPolVirtualSchePIRRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 800000000), )
class THPolVirtualScheCIRRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 800000000), )
class TAdvCfgRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100000000)

class TMaxDecRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 100000000), )
class THPolPIRRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 20000000), )
class TSecondaryShaper10GPIRRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 10000), )
class TExpSecondaryShaperPIRRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 10000000), )
class TExpSecondaryShaperClassRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 10000000), )
class TPIRRateOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class THPolPIRRateOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 20000000), )
class TPIRPercentOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(1, 10000), )
class TPIRRateOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class THsmdaPIRKRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class THsmdaPIRKRateOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class THsmdaPIRMRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000), )
class THsmdaPIRMRateOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000), )
class TmnxDHCP6MsgType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("dhcp6MsgTypeSolicit", 1), ("dhcp6MsgTypeAdvertise", 2), ("dhcp6MsgTypeRequest", 3), ("dhcp6MsgTypeConfirm", 4), ("dhcp6MsgTypeRenew", 5), ("dhcp6MsgTypeRebind", 6), ("dhcp6MsgTypeReply", 7), ("dhcp6MsgTypeRelease", 8), ("dhcp6MsgTypeDecline", 9), ("dhcp6MsgTypeReconfigure", 10), ("dhcp6MsgTypeInfoRequest", 11), ("dhcp6MsgTypeRelayForw", 12), ("dhcp6MsgTypeRelayReply", 13), ("dhcp6MsgTypeMaxValue", 14))

class TmnxOspfInstance(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 31)

class TmnxBGPFamilyType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ipv4Unicast", 0), ("ipv4Multicast", 1), ("ipv4UastMcast", 2), ("ipv4MplsLabel", 3), ("ipv4Vpn", 4), ("ipv6Unicast", 5), ("ipv6Multicast", 6), ("ipv6UcastMcast", 7), ("ipv6MplsLabel", 8), ("ipv6Vpn", 9), ("l2Vpn", 10), ("ipv4Mvpn", 11), ("msPw", 12), ("ipv4Flow", 13), ("mdtSafi", 14), ("routeTarget", 15), ("mcastVpnIpv4", 16))

class TmnxIgmpGroupFilterMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("include", 1), ("exclude", 2))

class TmnxIgmpGroupType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("dynamic", 2))

class TmnxIgmpVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("version1", 1), ("version2", 2), ("version3", 3))

class TmnxMldGroupFilterMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("include", 1), ("exclude", 2))

class TmnxMldGroupType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("dynamic", 2))

class TmnxMldVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("version1", 1), ("version2", 2))

class TmnxManagedRouteStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("installed", 0), ("notYetInstalled", 1), ("wrongAntiSpoofType", 2), ("outOfMemory", 3), ("shadowed", 4), ("routeTableFull", 5), ("parentInterfaceDown", 6), ("hostInactive", 7), ("enhancedSubMgmtRequired", 8), ("deprecated1", 9), ("l2AwNotSupported", 10))

class TmnxAncpString(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 63)

class TmnxAncpStringOrZero(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 63)

class TmnxMulticastAddrFamily(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ipv4Multicast", 0), ("ipv6Multicast", 1))

class TmnxAsciiSpecification(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 255)

class TmnxMacSpecification(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 17)

class TmnxBinarySpecification(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 255)

class TmnxDefSubIdSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("useSapId", 1), ("useString", 2), ("useAutoId", 3))

class TmnxSubIdentString(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxSubIdentStringOrEmpty(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class TmnxSubRadServAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("direct", 1), ("roundRobin", 2), ("hashBased", 3))

class TmnxSubRadiusAttrType(TextualConvention, Unsigned32):
    reference = 'RFC 2865 Remote Authentication Dial In User Service (RADIUS) section 5. Attributes'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TmnxSubRadiusVendorId(TextualConvention, Unsigned32):
    reference = 'RFC 2865 Remote Authentication Dial In User Service (RADIUS) section 5.26. Vendor-Specific.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16777215)

class TmnxRadiusPendingReqLimit(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4096)

class TmnxRadiusServerOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("inService", 2), ("outOfService", 3), ("transition", 4), ("overloaded", 5))

class TmnxSubProfileString(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 16)

class TmnxSubProfileStringOrEmpty(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

class TmnxSlaProfileString(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 16)

class TmnxSlaProfileStringOrEmpty(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

class TmnxAppProfileString(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 16)

class TmnxAppProfileStringOrEmpty(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

class TmnxSubMgtIntDestIdOrEmpty(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class TmnxSubMgtIntDestId(TmnxSubMgtIntDestIdOrEmpty):
    status = 'current'
    subtypeSpec = TmnxSubMgtIntDestIdOrEmpty.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxDefInterDestIdSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("useString", 1), ("useTopQTag", 2), ("useVpi", 3))

class TmnxSubNasPortSuffixType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("circuitId", 1), ("remoteId", 2))

class TmnxSubNasPortPrefixType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("userString", 1))

class TmnxSubNasPortTypeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("standard", 1), ("config", 2))

class TmnxSubMgtOrgStrOrZero(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class TmnxSubMgtOrgString(TmnxSubMgtOrgStrOrZero):
    status = 'current'
    subtypeSpec = TmnxSubMgtOrgStrOrZero.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxFilterProfileStringOrEmpty(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

class TmnxAccessLoopEncapDataLink(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("aal5", 0), ("ethernet", 1))

class TmnxAccessLoopEncaps1(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notAvailable", 0), ("untaggedEthernet", 1), ("singleTaggedEthernet", 2))

class TmnxAccessLoopEncaps2(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("notAvailable", 0), ("pppoaLlc", 1), ("pppoaNull", 2), ("ipoaLlc", 3), ("ipoaNull", 4), ("ethernetOverAal5LlcFcs", 5), ("ethernetOverAal5LlcNoFcs", 6), ("ethernetOverAal5NullFcs", 7), ("ethernetOverAal5NullNoFcs", 8))

class TmnxSubAleOffsetMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("auto", 1))

class TmnxSubAleOffset(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("none", 0), ("pppoaLlc", 1), ("pppoaNull", 2), ("pppoeoaLlc", 3), ("pppoeoaLlcFcs", 4), ("pppoeoaLlcTagged", 5), ("pppoeoaLlcTaggedFcs", 6), ("pppoeoaNull", 7), ("pppoeoaNullFcs", 8), ("pppoeoaNullTagged", 9), ("pppoeoaNullTaggedFcs", 10), ("ipoaLlc", 11), ("ipoaNull", 12), ("ipoeoaLlc", 13), ("ipoeoaLlcFcs", 14), ("ipoeoaLlcTagged", 15), ("ipoeoaLlcTaggedFcs", 16), ("ipoeoaNull", 17), ("ipoeoaNullFcs", 18), ("ipoeoaNullTagged", 19), ("ipoeoaNullTaggedFcs", 20), ("pppoe", 21), ("pppoeTagged", 22), ("ipoe", 23), ("ipoeTagged", 24))

class TmnxDhcpOptionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("ipv4", 1), ("ascii", 2), ("hex", 3), ("ipv6", 4), ("domain", 5))

class TmnxPppoeUserName(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 128)

class TmnxPppoeUserNameOrEmpty(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 128)

class TCpmProtPolicyID(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TCpmProtPolicyIDOrDefault(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 255), )
class TMlpppQoSProfileId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TMcFrQoSProfileId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TmnxPppoeSessionId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TmnxPppoePadoDelay(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 30), )
class TmnxPppoeSessionInfoOrigin(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 0), ("default", 1), ("radius", 2), ("localUserDb", 3), ("dhcp", 4), ("midSessionChange", 5), ("tags", 6), ("l2tp", 7))

class TmnxPppoeSessionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("local", 1), ("localWholesale", 2), ("localRetail", 3), ("l2tp", 4))

class TmnxPppNcpProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipcp", 1), ("ipv6cp", 2))

class TmnxMlpppEpClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("null", 0), ("local", 1), ("ipv4Address", 2), ("macAddress", 3), ("magicNumber", 4), ("directoryNumber", 5))

class TNetworkPolicyID(TPolicyID):
    status = 'current'
    subtypeSpec = TPolicyID.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 65535), ValueRangeConstraint(65536, 65536), ValueRangeConstraint(65537, 65537), )
class TItemScope(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("exclusive", 1), ("template", 2))

class TItemMatch(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("off", 1), ("false", 2), ("true", 3))

class TPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("low", 1), ("high", 2))

class TPriorityOrDefault(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("low", 1), ("high", 2), ("default", 3))

class TProfileUseDEOrNone(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("in", 1), ("out", 2), ("de", 3))

class TPriorityOrUndefined(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("low", 1), ("high", 2))

class TProfile(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("in", 1), ("out", 2))

class TProfileOrDei(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 13))
    namedValues = NamedValues(("in", 1), ("out", 2), ("use-dei", 13))

class TDEProfile(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("in", 1), ("out", 2), ("de", 3))

class TDEProfileOrDei(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 13))
    namedValues = NamedValues(("in", 1), ("out", 2), ("de", 3), ("use-dei", 13))

class TProfileOrNone(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("in", 1), ("out", 2))

class TAdaptationRule(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("max", 1), ("min", 2), ("closest", 3))

class TAdaptationRuleOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("noOverride", 0), ("max", 1), ("min", 2), ("closest", 3))

class TRemarkType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("dscp", 2), ("precedence", 3))

class TPrecValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class TPrecValueOrNone(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 7), )
class TBurstSize(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 131072), )
class TBurstSizeOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 131072), )
class TBurstPercent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class TBurstHundredthsOfPercent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 10000)

class TBurstPercentOrDefault(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100), )
class TBurstPercentOrDefaultOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100), )
class TRatePercent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class TPIRRatePercent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 100)

class TLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 8)

class TLevelOrDefault(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TQWeight(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 100), )
class TMeterMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("priority", 1), ("profile", 2))

class TPlcyMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("roundRobin", 1), ("weightedRoundRobin", 2), ("weightedDeficitRoundRobin", 3))

class TPlcyQuanta(TextualConvention, Integer32):
    status = 'current'

class TQueueMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("priority", 1), ("profile", 2))

class TEntryIndicator(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TEntryId(TEntryIndicator):
    status = 'current'
    subtypeSpec = TEntryIndicator.subtypeSpec + ValueRangeConstraint(1, 65535)

class TMatchCriteria(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("ip", 1), ("mac", 2), ("none", 3), ("dscp", 4), ("dot1p", 5), ("prec", 6))

class TmnxMdaQos(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("mda", 1), ("hsmda1", 2), ("hsmda2", 3))

class TAtmTdpDescrType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("clp0And1pcr", 0), ("clp0And1pcrPlusClp0And1scr", 1), ("clp0And1pcrPlusClp0scr", 2), ("clp0And1pcrPlusClp0scrTag", 3))

class TDEValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1), )
class TQGroupType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("port", 0), ("vpls", 1))

class TQosOverrideType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("queue", 1), ("policer", 2), ("aggRateLimit", 3), ("arbiter", 4), ("scheduler", 5))

class TmnxIPsecTunnelTemplateId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 2048)

class TmnxIPsecTunnelTemplateIdOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 2048)

class TmnxIpSecIsaOperFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("adminDown", 0), ("noActive", 1), ("noResources", 2))

class TmnxIkePolicyAuthMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("psk", 1), ("hybridX509XAuth", 2), ("plainX509XAuth", 3), ("plainPskXAuth", 4), ("cert", 5))

class TmnxIkePolicyOwnAuthMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 5))
    namedValues = NamedValues(("symmetric", 0), ("psk", 1), ("cert", 5))

class TmnxRsvpDSTEClassType(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class TmnxAccPlcyQICounters(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("hpo", 0), ("lpo", 1), ("ucp", 2), ("hoo", 3), ("loo", 4), ("uco", 5), ("apo", 6), ("aoo", 7), ("hpd", 8), ("lpd", 9), ("hod", 10), ("lod", 11), ("ipf", 12), ("opf", 13), ("iof", 14), ("oof", 15))

class TmnxAccPlcyQECounters(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ipf", 0), ("ipd", 1), ("opf", 2), ("opd", 3), ("iof", 4), ("iod", 5), ("oof", 6), ("ood", 7))

class TmnxAccPlcyOICounters(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("apo", 0), ("aoo", 1), ("hpd", 2), ("lpd", 3), ("hod", 4), ("lod", 5), ("ipf", 6), ("opf", 7), ("iof", 8), ("oof", 9))

class TmnxAccPlcyOECounters(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ipf", 0), ("ipd", 1), ("opf", 2), ("opd", 3), ("iof", 4), ("iod", 5), ("oof", 6), ("ood", 7))

class TmnxAccPlcyAACounters(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("any", 0), ("sfa", 1), ("nfa", 2), ("sfd", 3), ("nfd", 4), ("saf", 5), ("naf", 6), ("spa", 7), ("npa", 8), ("sba", 9), ("nba", 10), ("spd", 11), ("npd", 12), ("sbd", 13), ("nbd", 14), ("sdf", 15), ("mdf", 16), ("ldf", 17), ("tfd", 18), ("tfc", 19), ("sbm", 20), ("spm", 21), ("smt", 22), ("nbm", 23), ("npm", 24), ("nmt", 25))

class TmnxVdoGrpIdIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4)

class TmnxVdoGrpId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4)

class TmnxVdoGrpIdOrInherit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 4), )
class TmnxVdoFccServerMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("burst", 1), ("dent", 2), ("hybrid", 3))

class TmnxVdoPortNumber(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1024, 5999), ValueRangeConstraint(6251, 65535), )
class TmnxVdoIfName(TNamedItem):
    status = 'current'

class TmnxTimeInSec(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 86400)

class TmnxMobProfName(TNamedItem):
    status = 'current'

class TmnxMobProfNameOrEmpty(TNamedItemOrEmpty):
    status = 'current'

class TmnxMobProfIpTtl(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class TmnxMobDiaTransTimer(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 180)

class TmnxMobDiaRetryCount(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 8)

class TmnxMobDiaPeerHost(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 80)

class TmnxMobGwId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class TmnxMobNode(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 30)

class TmnxMobBufferLimit(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1000, 12000)

class TmnxMobQueueLimit(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1000, 12000)

class TmnxMobRtrAdvtInterval(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 60)

class TmnxMobRtrAdvtLifeTime(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 24)

class TmnxMobAddrScheme(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("stateful", 1), ("stateless", 2))

class TmnxMobQciValue(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 9)

class TmnxMobQciValueOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 9)

class TmnxMobArpValue(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 15)

class TmnxMobArpValueOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 15)

class TmnxMobApn(DisplayString):
    reference = '3GPP TS 23.003 Section 9.1'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 80)

class TmnxMobApnOrZero(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 80)

class TmnxMobImsi(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class TmnxMobMsisdn(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 15)

class TmnxMobImei(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(16, 16), )
class TmnxMobNai(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 72)

class TmnxMobMcc(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TmnxMobMnc(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(2, 2), ValueSizeConstraint(3, 3), )
class TmnxMobMccOrEmpty(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(3, 3), )
class TmnxMobMncOrEmpty(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 2), ValueSizeConstraint(3, 3), )
class TmnxMobUeState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("idle", 1), ("active", 2), ("paging", 3), ("init", 4), ("suspend", 5), ("ddnDamp", 6))

class TmnxMobUeRat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("utran", 1), ("geran", 2), ("wlan", 3), ("gan", 4), ("hspa", 5), ("eutran", 6), ("ehrpd", 7), ("hrpd", 8), ("oneXrtt", 9), ("umb", 10))

class TmnxMobUeSubType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("homer", 1), ("roamer", 2), ("visitor", 3))

class TmnxMobPdnType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2), ("ipv4v6", 3))

class TmnxMobPgwSigProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("gtp", 1), ("pmip", 2))

class TmnxMobPdnSessionState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("invalid", 0), ("init", 1), ("waitPcrfResponse", 2), ("waitPgwResponse", 3), ("waitEnodebUpdate", 4), ("connected", 5), ("ulDelPending", 6), ("dlDelPending", 7), ("idleMode", 8), ("pageMode", 9), ("dlHandover", 10), ("incomingHandover", 11), ("outgoingHandover", 12), ("stateMax", 13))

class TmnxMobPdnSessionEvent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))
    namedValues = NamedValues(("sessionInvalid", 0), ("gtpCreateSessReq", 1), ("gtpUpdateBearerReq", 2), ("gtpDeleteSessReq", 3), ("gtpDeleteBearerResp", 4), ("gtpUpdateBearerResp", 5), ("gtpModifyActiveToIdle", 6), ("gtpResrcAllocCmd", 7), ("gtpModifyQosCmd", 8), ("gtpX1eNodeBTeidUpdate", 9), ("gtpX2SrcSgwDeleteSessReq", 10), ("gtpS1CreateIndirectTunnel", 11), ("dlPktRecvIndication", 12), ("dlPktNotificationAck", 13), ("dlPktNotificationFail", 14), ("pcrfSessEstResp", 15), ("pcrfSessTerminateRsp", 16), ("pcrfProvQosRules", 17), ("pmipSessResp", 18), ("pmipSessUpdate", 19), ("pmipSessDeleteRsp", 20), ("pmipSessDeleteReq", 21), ("eventMax", 22))

class TmnxMobBearerId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 15)

class TmnxMobBearerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("default", 1), ("dedicated", 2))

class TmnxMobQci(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 9)

class TmnxMobArp(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 15)

class TmnxMobSdf(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TmnxMobSdfFilter(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

class TmnxMobSdfFilterNum(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

class TmnxMobSdfRuleName(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 64)

class TmnxMobSdfFilterDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("preRel7", 0), ("downLink", 1), ("upLink", 2), ("biDir", 3))

class TmnxMobSdfFilterProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140))
    namedValues = NamedValues(("any", -1), ("ipv6HopByOpOpt", 0), ("icmp", 1), ("igmp", 2), ("ggp", 3), ("ip", 4), ("st", 5), ("tcp", 6), ("cbt", 7), ("egp", 8), ("igp", 9), ("bbnRccMon", 10), ("nvp2", 11), ("pup", 12), ("argus", 13), ("emcon", 14), ("xnet", 15), ("chaos", 16), ("udp", 17), ("mux", 18), ("dcnMeas", 19), ("hmp", 20), ("prm", 21), ("xnsIdp", 22), ("trunk1", 23), ("trunk2", 24), ("leaf1", 25), ("leaf2", 26), ("rdp", 27), ("irdp", 28), ("isoTp4", 29), ("netblt", 30), ("mfeNsp", 31), ("meritInp", 32), ("dccp", 33), ("pc3", 34), ("idpr", 35), ("xtp", 36), ("ddp", 37), ("idprCmtp", 38), ("tpplusplus", 39), ("il", 40), ("ipv6", 41), ("sdrp", 42), ("ipv6Route", 43), ("ipv6Frag", 44), ("idrp", 45), ("rsvp", 46), ("gre", 47), ("dsr", 48), ("bna", 49), ("esp", 50), ("ah", 51), ("iNlsp", 52), ("swipe", 53), ("narp", 54), ("mobile", 55), ("tlsp", 56), ("skip", 57), ("ipv6Icmp", 58), ("ipv6NoNxt", 59), ("ipv6Opts", 60), ("anyHostIntl", 61), ("cftp", 62), ("anyLocalNet", 63), ("satExpak", 64), ("kryptolan", 65), ("rvd", 66), ("ippc", 67), ("anyDFS", 68), ("satMon", 69), ("visa", 70), ("ipcv", 71), ("cpnx", 72), ("cphb", 73), ("wsn", 74), ("pvp", 75), ("brSatMon", 76), ("sunNd", 77), ("wbMon", 78), ("wbExpak", 79), ("isoIp", 80), ("vmtp", 81), ("secureVmpt", 82), ("vines", 83), ("ttp", 84), ("nsfnetIgp", 85), ("dgp", 86), ("tcf", 87), ("eiGrp", 88), ("ospfIgp", 89), ("spriteRpc", 90), ("larp", 91), ("mtp", 92), ("ax25", 93), ("ipip", 94), ("micp", 95), ("sccSp", 96), ("etherIp", 97), ("encap", 98), ("anyPEC", 99), ("gmtp", 100), ("ifmp", 101), ("pnni", 102), ("pim", 103), ("aris", 104), ("scps", 105), ("qnx", 106), ("activeNet", 107), ("ipComp", 108), ("snp", 109), ("compaqPeer", 110), ("ipxInIp", 111), ("vrrp", 112), ("pgm", 113), ("any0hop", 114), ("l2tp", 115), ("ddx", 116), ("iatp", 117), ("stp", 118), ("srp", 119), ("uti", 120), ("smp", 121), ("sm", 122), ("ptp", 123), ("isis", 124), ("fire", 125), ("crtp", 126), ("crudp", 127), ("sscopmce", 128), ("iplt", 129), ("sps", 130), ("pipe", 131), ("sctp", 132), ("fc", 133), ("rsvpE2eIgnore", 134), ("mobHeader", 135), ("udpLite", 136), ("mplsInIp", 137), ("manet", 138), ("hip", 139), ("shim6", 140))

class TmnxMobPathMgmtState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("disabled", 0), ("up", 1), ("reqTimeOut", 2), ("fault", 3), ("idle", 4), ("restart", 5))

class TmnxMobDiaPathMgmtState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("shutDown", 0), ("shuttingDown", 1), ("inactive", 2), ("active", 3))

class TmnxMobDiaDetailPathMgmtState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("error", 0), ("idle", 1), ("closed", 2), ("localShutdown", 3), ("remoteClosing", 4), ("waitConnAck", 5), ("waitCea", 6), ("open", 7), ("openCoolingDown", 8), ("waitDns", 9))

class TmnxMobGwType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("sgw", 1), ("pgw", 2), ("wlanGw", 3))

class TmnxMobChargingProfile(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TmnxMobChargingProfileOrInherit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TmnxMobAuthType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("radius", 1), ("diameter", 2))

class TmnxMobAuthUserName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("imsi", 1), ("msisdn", 2), ("pco", 3))

class TmnxMobProfGbrRate(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100000)

class TmnxMobProfMbrRate(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100000)

class TmnxMobPeerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("sgw", 1), ("pgw", 2), ("hsgw", 3))

class TmnxMobRfAcctLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pdnLevel", 1), ("qciLevel", 2))

class TmnxMobProfPolReportingLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("servId", 1), ("ratingGrp", 2))

class TmnxMobProfPolChargingMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("profChargingMtd", 0), ("online", 1), ("offline", 2), ("both", 3))

class TmnxMobProfPolMeteringMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("timeBased", 1), ("volBased", 2), ("both", 3))

class TmnxMobServerState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("na", 0), ("up", 1), ("down", 2))

class TmnxMobChargingBearerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("home", 1), ("visiting", 2), ("roaming", 3))

class TmnxMobChargingLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pdn", 1), ("bearer", 2))

class TmnxMobIpCanType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("epc3gpp", 1), ("gprs3gpp", 2))

class TmnxMobStaticPolPrecedence(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65536)

class TmnxMobStaticPolPrecedenceOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TmnxMobDualStackPref(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2), ("useCplane", 3))

class TmnxMobDfPeerId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 16)

class TmnxMobLiTarget(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class TmnxMobLiTargetType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("imsi", 1), ("msisdn", 2), ("imei", 3))

class TmnxReasContextVal(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 31)

class TmnxVdoStatInt(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("current", 1), ("interval", 2))

class TmnxVdoOutputFormat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("udp", 1), ("rtp-udp", 2))

class TmnxVdoAnalyzerAlarm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("tnc", 1), ("qos", 2), ("poa", 3))

class TmnxVdoAnalyzerAlarmStates(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(10, 10)
    fixedLength = 10

class SvcISID(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 16777215), )
class TIngPolicerId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 32)

class TIngPolicerIdOrNone(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TEgrPolicerId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 8)

class TEgrPolicerIdOrNone(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TFIRRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class TBurstSizeBytes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 134217728), )
class THSMDABurstSizeBytes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2688000), )
class THSMDAQueueBurstLimit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 1000000), )
class TClassBurstLimit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 327680), )
class TPlcrBurstSizeBytes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 4194304), )
class TBurstSizeBytesOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 134217728), )
class THSMDABurstSizeBytesOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2688000), )
class TPlcrBurstSizeBytesOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 4194304), )
class TmnxBfdSessOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("connected", 2), ("broken", 3), ("peerDetectsDown", 4), ("notConfigured", 5), ("noResources", 6))

class TmnxIngPolicerStatMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("noStats", 0), ("minimal", 1), ("offeredProfileNoCIR", 2), ("offeredTotalCIR", 3), ("offeredPrioNoCIR", 4), ("offeredProfileCIR", 5), ("offeredPrioCIR", 6), ("offeredLimitedProfileCIR", 7), ("offeredProfileCapCIR", 8), ("offeredLimitedCapCIR", 9))

class TmnxIngPolicerStatModeOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("noOverride", -1), ("noStats", 0), ("minimal", 1), ("offeredProfileNoCIR", 2), ("offeredTotalCIR", 3), ("offeredPrioNoCIR", 4), ("offeredProfileCIR", 5), ("offeredPrioCIR", 6), ("offeredLimitedProfileCIR", 7), ("offeredProfileCapCIR", 8), ("offeredLimitedCapCIR", 9))

class TmnxEgrPolicerStatMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("noStats", 0), ("minimal", 1), ("offeredProfileNoCIR", 2), ("offeredTotalCIR", 3), ("offeredProfileCIR", 4), ("offeredLimitedCapCIR", 5), ("offeredProfileCapCIR", 6))

class TmnxEgrPolicerStatModeOverride(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("noOverride", -1), ("noStats", 0), ("minimal", 1), ("offeredProfileNoCIR", 2), ("offeredTotalCIR", 3), ("offeredProfileCIR", 4), ("offeredLimitedCapCIR", 5), ("offeredProfileCapCIR", 6))

class TmnxTlsGroupId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4094)

class TSubHostId(TextualConvention, Unsigned32):
    status = 'current'

class TDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("both", 0), ("ingress", 1), ("egress", 2))

class TBurstLimit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 14000000), )
class TMacFilterType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("isid", 2), ("vid", 3))

class TmnxPwGlobalId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TmnxPwGlobalIdOrZero(TextualConvention, Unsigned32):
    status = 'current'

class TmnxPwPathHopId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 16)

class TmnxPwPathHopIdOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

class TmnxSpokeSdpId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TmnxSpokeSdpIdOrZero(TextualConvention, Unsigned32):
    status = 'current'

class TmnxMsPwPeSignaling(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("auto", 1), ("master", 2))

class TmnxLdpFECType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 128, 129, 130))
    namedValues = NamedValues(("addrWildcard", 1), ("addrPrefix", 2), ("addrHost", 3), ("vll", 128), ("vpws", 129), ("vpls", 130))

class TmnxSvcOperGrpCreationOrigin(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("manual", 1), ("mvrp", 2))

class TmnxOperGrpHoldUpTime(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 3600)

class TmnxOperGrpHoldDownTime(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 3600)

class TmnxSrrpPriorityStep(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 10)

class TmnxAiiType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("aiiType1", 1), ("aiiType2", 2))

class ServObjDesc(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 80)

class TMplsLspExpProfMapID(TPolicyID):
    status = 'current'
    subtypeSpec = TPolicyID.subtypeSpec + ValueRangeConstraint(1, 65535)

class TSysResource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 11), )
class TmnxSpbFid(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4095)

class TmnxSpbFidOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class TmnxSpbBridgePriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 15)

class TmnxSlopeMap(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("low", 1), ("high", 2), ("highLow", 3))

class TmnxCdrType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("pgwCdr", 1), ("gCdr", 2), ("eGCdr", 3))

class TmnxThresholdGroupType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("brMgmtLimit", 1), ("brMgmtCfSuccess", 2), ("brMgmtCfFailure", 3), ("brMgmtTraffic", 4), ("pathMgmt", 5), ("cpmSystem", 6), ("mgIsmSystem", 7))

class TmnxMobUeId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class TmnxMobUeIdType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("imsi", 0), ("imei", 1), ("msisdn", 2))

class TmnxMobImsiStr(DisplayString):
    reference = '3GPP TS 23.003 Numbering, addressing and identification, section 2.2 Composition of IMSI.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(9, 15), )
class TmnxVpnIpBackupFamily(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ipv4", 0), ("ipv6", 1))

class TmnxTunnelGroupId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 16)

class TmnxTunnelGroupIdOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

class TmnxMobRatingGrpState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("allowFlow", 1), ("disallowFlow", 2), ("redWebPortal", 3), ("allowResRules", 4), ("iom1stPktTrigger", 5), ("dis1stPktTrigger", 6), ("creditsToppedUp", 7), ("waitForFpt", 8))

class TmnxMobPresenceState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("absent", 0), ("present", 1))

class TmnxMobPdnGyChrgTriggerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29))
    namedValues = NamedValues(("sgsnIpAddrRecvd", 0), ("qosRecvd", 1), ("locRecvd", 2), ("ratRecvd", 3), ("qosTrfClsRecvd", 4), ("qosRlbClsRecvd", 5), ("qosDlyClsRecvd", 6), ("qosPeakThrptRecvd", 7), ("qosPrcClsRecvd", 8), ("qosMeanTrptRecvd", 9), ("qosMxBtRtUplnkRecvd", 10), ("qosMxBtRtDllnkRecvd", 11), ("qosResBerRecvd", 12), ("qosSduErrRatRecvd", 13), ("qosTransDelayRecvd", 14), ("qosTrfHndPriRecvd", 15), ("qosGrtBtRtUplnkRecvd", 16), ("qosGrtBtRtDllnkRecvd", 17), ("locMccRecvd", 18), ("locMncRecvd", 19), ("locRacRecvd", 20), ("locLacRecvd", 21), ("locCellIdRecvd", 22), ("medCompRecvd", 23), ("partcNmbRecvd", 24), ("thrldPartcNmbRecvd", 25), ("usrPartcTypeRecvd", 26), ("servCondRecvd", 27), ("servNodeRecvd", 28), ("usrCsgInfoRecvd", 29))

class TmnxMobPdnRefPointType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("s5", 1), ("s8", 2), ("gn", 3), ("s2a", 4), ("gp", 5))

class TmnxQosBytesHex(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x '
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 30)

class TSiteOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("up", 1), ("down", 2), ("outOfResource", 3))

class TmnxSpbFdbLocale(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("local", 1), ("sap", 2), ("sdp", 3), ("unknown", 4))

class TmnxSpbFdbState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("ok", 0), ("addModPending", 1), ("delPending", 2), ("sysFdbLimit", 3), ("noFateShared", 4), ("svcFdbLimit", 5), ("noUcast", 6))

class TmnxMobServRefPointType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4))
    namedValues = NamedValues(("s5", 1), ("s8", 2), ("s2a", 4))

class TmnxMobAccessType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("eps", 1), ("gprs", 2), ("non3gpp", 3))

class TmnxMobUeStrPrefix(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(4, 15)

class TmnxCdrDiagnosticAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("included", 1), ("excluded", 2))

class TmnxMplsTpGlobalID(TextualConvention, Unsigned32):
    reference = "RFC 6370, 'MPLS Transport Profile (MPLS-TP) Identifiers', Section 3, 'Uniquely Identifying an Operator - the Global_ID'."
    status = 'current'

class TmnxMplsTpNodeID(TextualConvention, Unsigned32):
    reference = "RFC 6370, 'MPLS Transport Profile (MPLS-TP) Identifiers', Section 4, 'Node and Interface Identifiers'."
    status = 'current'

class TmnxMplsTpTunnelType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("mplsTpStatic", 1))

class TmnxVwmCardType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44))
    namedValues = NamedValues(("not-provisioned", 0), ("not-equipped", 1), ("sfc1A", 2), ("sfc1B", 3), ("sfc1C", 4), ("sfc1D", 5), ("sfc1E", 6), ("sfc1F", 7), ("sfc1G", 8), ("sfc1H", 9), ("sfc2AandB", 10), ("sfc2CandD", 11), ("sfc2EandF", 12), ("sfc2GandH", 13), ("sfc4A-D", 14), ("sfc4E-H", 15), ("sfc8", 16), ("sfd8A-R", 17), ("sfd8B-R", 18), ("sfd8C-R", 19), ("sfd8D-R", 20), ("sfd4A-R", 21), ("sfd4B-R", 22), ("sfd4C-R", 23), ("sfd4D-R", 24), ("sfd4E-R", 25), ("sfd4F-R", 26), ("sfd4G-R", 27), ("sfd4H-R", 28), ("sfd2A-R", 29), ("sfd2B-R", 30), ("sfd2C-R", 31), ("sfd2D-R", 32), ("sfd2E-R", 33), ("sfd2F-R", 34), ("sfd2G-R", 35), ("sfd2H-R", 36), ("sfd2I-R", 37), ("sfd2L-R", 38), ("sfd2M-R", 39), ("sfd2N-R", 40), ("sfd2O-R", 41), ("sfd2P-R", 42), ("sfd2Q-R", 43), ("sfd2R-R", 44))

mibBuilder.exportSymbols("TIMETRA-TC-MIB", QTagFullRange=QTagFullRange, TmnxVwmCardType=TmnxVwmCardType, TRatePercent=TRatePercent, TmnxReasContextVal=TmnxReasContextVal, TNamedItemOrEmpty=TNamedItemOrEmpty, TmnxIngPolicerStatModeOverride=TmnxIngPolicerStatModeOverride, TmnxMobDualStackPref=TmnxMobDualStackPref, TEgressQPerPacketOffset=TEgressQPerPacketOffset, TMatchCriteria=TMatchCriteria, TEgrRateModType=TEgrRateModType, TmnxSubRadiusAttrType=TmnxSubRadiusAttrType, TmnxOspfInstance=TmnxOspfInstance, TCpmProtPolicyIDOrDefault=TCpmProtPolicyIDOrDefault, TmnxSpbBridgePriority=TmnxSpbBridgePriority, TmnxMobProfMbrRate=TmnxMobProfMbrRate, TmnxAppProfileStringOrEmpty=TmnxAppProfileStringOrEmpty, TmnxMplsTpGlobalID=TmnxMplsTpGlobalID, TmnxMobQciValueOrZero=TmnxMobQciValueOrZero, TmnxIPsecTunnelTemplateId=TmnxIPsecTunnelTemplateId, TmnxVRtrIDOrZero=TmnxVRtrIDOrZero, THPolVirtualScheCIRRate=THPolVirtualScheCIRRate, TPIRRateOverride=TPIRRateOverride, TmnxMobProfName=TmnxMobProfName, TFCNameOrEmpty=TFCNameOrEmpty, TmnxMobPdnType=TmnxMobPdnType, TmnxOperState=TmnxOperState, TSapIngressMeterId=TSapIngressMeterId, TSiteOperStatus=TSiteOperStatus, TDSCPValueOrNone=TDSCPValueOrNone, TmnxMobPdnSessionState=TmnxMobPdnSessionState, TmnxVPNRouteDistinguisher=TmnxVPNRouteDistinguisher, TCIRRateOverride=TCIRRateOverride, TItemScope=TItemScope, TmnxMobAuthUserName=TmnxMobAuthUserName, TmnxVdoGrpIdIndex=TmnxVdoGrpIdIndex, TDSCPName=TDSCPName, TmnxCdrDiagnosticAction=TmnxCdrDiagnosticAction, TmnxSubMgtIntDestIdOrEmpty=TmnxSubMgtIntDestIdOrEmpty, TPolicerWeight=TPolicerWeight, TLNamedItem=TLNamedItem, TPIRPercentOverride=TPIRPercentOverride, TmnxVdoGrpId=TmnxVdoGrpId, TmnxSubNasPortTypeType=TmnxSubNasPortTypeType, TmnxMobMnc=TmnxMobMnc, TmnxPppoePadoDelay=TmnxPppoePadoDelay, TEgressHsmdaCounterId=TEgressHsmdaCounterId, TmnxSlopeMap=TmnxSlopeMap, ServObjDesc=ServObjDesc, TmnxIpSecIsaOperFlags=TmnxIpSecIsaOperFlags, TMaxDecRate=TMaxDecRate, TmnxMobBufferLimit=TmnxMobBufferLimit, TPolicerRateType=TPolicerRateType, TmnxAccessLoopEncapDataLink=TmnxAccessLoopEncapDataLink, TmnxSpbFid=TmnxSpbFid, TmnxBgpRouteTarget=TmnxBgpRouteTarget, TmnxAncpString=TmnxAncpString, TBurstHundredthsOfPercent=TBurstHundredthsOfPercent, TmnxMdaQos=TmnxMdaQos, TmnxMlpppEpClass=TmnxMlpppEpClass, QTagOrZero=QTagOrZero, TCpmProtPolicyID=TCpmProtPolicyID, TItemDescription=TItemDescription, TIngressHsmdaCounterId=TIngressHsmdaCounterId, TmnxSubMgtOrgStrOrZero=TmnxSubMgtOrgStrOrZero, TmnxTunnelGroupId=TmnxTunnelGroupId, TBurstSizeBytes=TBurstSizeBytes, TmnxAdminState=TmnxAdminState, TSapEgressPolicyID=TSapEgressPolicyID, TmnxEnabledDisabled=TmnxEnabledDisabled, TSapEgrEncapGroupType=TSapEgrEncapGroupType, TmnxIgmpVersion=TmnxIgmpVersion, TmnxMobPresenceState=TmnxMobPresenceState, TDSCPNameOrEmpty=TDSCPNameOrEmpty, TmnxVdoFccServerMode=TmnxVdoFccServerMode, TmnxMobPgwSigProtocol=TmnxMobPgwSigProtocol, TmnxPortID=TmnxPortID, TmnxSubRadServAlgorithm=TmnxSubRadServAlgorithm, TmnxSubProfileString=TmnxSubProfileString, TmnxSubMgtOrgString=TmnxSubMgtOrgString, TDSCPValue=TDSCPValue, TIngressQueueId=TIngressQueueId, TmnxIgmpGroupType=TmnxIgmpGroupType, TSubHostId=TSubHostId, TAdaptationRuleOverride=TAdaptationRuleOverride, TmnxSpbFdbState=TmnxSpbFdbState, TIngressHsmdaPerPacketOffset=TIngressHsmdaPerPacketOffset, TWeight=TWeight, TmnxTunnelID=TmnxTunnelID, TProfileOrNone=TProfileOrNone, TExpSecondaryShaperClassRate=TExpSecondaryShaperClassRate, TFCType=TFCType, TMcFrQoSProfileId=TMcFrQoSProfileId, TmnxPppoeSessionType=TmnxPppoeSessionType, THsmdaPIRMRateOverride=THsmdaPIRMRateOverride, TmnxMobSdf=TmnxMobSdf, TmnxSubNasPortSuffixType=TmnxSubNasPortSuffixType, TmnxMobProfPolReportingLevel=TmnxMobProfPolReportingLevel, PYSNMP_MODULE_ID=timetraTCMIBModule, TmnxMobStaticPolPrecedence=TmnxMobStaticPolPrecedence, TPerPacketOffset=TPerPacketOffset, TmnxCustId=TmnxCustId, TmnxMulticastAddrFamily=TmnxMulticastAddrFamily, TmnxRsvpDSTEClassType=TmnxRsvpDSTEClassType, TmnxFilterProfileStringOrEmpty=TmnxFilterProfileStringOrEmpty, TTcpUdpPort=TTcpUdpPort, TmnxSubProfileStringOrEmpty=TmnxSubProfileStringOrEmpty, TmnxSlaProfileString=TmnxSlaProfileString, TmnxMobProfPolMeteringMethod=TmnxMobProfPolMeteringMethod, TmnxMobSdfRuleName=TmnxMobSdfRuleName, TmnxEgrPolicerStatModeOverride=TmnxEgrPolicerStatModeOverride, TmnxSubIdentString=TmnxSubIdentString, TmnxPwPathHopId=TmnxPwPathHopId, TQWeight=TQWeight, TmnxLdpFECType=TmnxLdpFECType, THPolPIRRateOverride=THPolPIRRateOverride, TLspExpValue=TLspExpValue, TmnxMldVersion=TmnxMldVersion, TmnxMobRatingGrpState=TmnxMobRatingGrpState, TmnxMobDiaPathMgmtState=TmnxMobDiaPathMgmtState, TmnxMobSdfFilterDirection=TmnxMobSdfFilterDirection, TmnxPwPathHopIdOrZero=TmnxPwPathHopIdOrZero, TDSCPFilterActionValue=TDSCPFilterActionValue, TmnxMobServerState=TmnxMobServerState, TPIRRatePercent=TPIRRatePercent, TmnxPppoeSessionInfoOrigin=TmnxPppoeSessionInfoOrigin, TIngPolicerIdOrNone=TIngPolicerIdOrNone, TPrecValue=TPrecValue, TLevelOrDefault=TLevelOrDefault, TSecondaryShaper10GPIRRate=TSecondaryShaper10GPIRRate, SvcISID=SvcISID, TPerPacketOffsetOvr=TPerPacketOffsetOvr, TPIRRate=TPIRRate, TmnxAsciiSpecification=TmnxAsciiSpecification, TmnxManagedRouteStatus=TmnxManagedRouteStatus, InterfaceIndex=InterfaceIndex, TFIRRate=TFIRRate, TIngHsmdaPerPacketOffsetOvr=TIngHsmdaPerPacketOffsetOvr, TmnxMobUeIdType=TmnxMobUeIdType, TQueueIdOrAll=TQueueIdOrAll, TmnxMobQueueLimit=TmnxMobQueueLimit, TmnxBgpLocalPreference=TmnxBgpLocalPreference, TEgressQueueId=TEgressQueueId, TRemarkType=TRemarkType, TIpProtocol=TIpProtocol, TCIRRate=TCIRRate, TFCName=TFCName, TLNamedItemOrEmpty=TLNamedItemOrEmpty, TmnxBgpAutonomousSystem=TmnxBgpAutonomousSystem, TmnxMobAuthType=TmnxMobAuthType, TmnxTlsGroupId=TmnxTlsGroupId, TmnxMldGroupFilterMode=TmnxMldGroupFilterMode, TOperator=TOperator, TmnxPppoeSessionId=TmnxPppoeSessionId, TmnxMobAddrScheme=TmnxMobAddrScheme, TmnxMobServRefPointType=TmnxMobServRefPointType, TIpOption=TIpOption, TPriority=TPriority, THsmdaPIRKRate=THsmdaPIRKRate, TmnxMobPathMgmtState=TmnxMobPathMgmtState, TIngressMeterId=TIngressMeterId, TmnxAiiType=TmnxAiiType, TMplsLspExpProfMapID=TMplsLspExpProfMapID, TmnxMobPdnGyChrgTriggerType=TmnxMobPdnGyChrgTriggerType, TmnxMobGwType=TmnxMobGwType, TmnxVdoAnalyzerAlarmStates=TmnxVdoAnalyzerAlarmStates, TmnxPppoeUserNameOrEmpty=TmnxPppoeUserNameOrEmpty, TBurstPercentOrDefault=TBurstPercentOrDefault, THSMDABurstSizeBytesOverride=THSMDABurstSizeBytesOverride, TBurstPercent=TBurstPercent, TmnxMobDiaRetryCount=TmnxMobDiaRetryCount, TNonZeroWeight=TNonZeroWeight, TmnxMobDfPeerId=TmnxMobDfPeerId, TmnxStatus=TmnxStatus, TmnxMobApnOrZero=TmnxMobApnOrZero, TSdpEgressPolicyID=TSdpEgressPolicyID, TmnxMobRfAcctLevel=TmnxMobRfAcctLevel, TmnxMobDiaTransTimer=TmnxMobDiaTransTimer, TmnxMobChargingBearerType=TmnxMobChargingBearerType, timetraTCMIBModule=timetraTCMIBModule, THsmdaPIRKRateOverride=THsmdaPIRKRateOverride, TSapEgrEncapGroupActionType=TSapEgrEncapGroupActionType, TmnxSubNasPortPrefixType=TmnxSubNasPortPrefixType, TPlcrBurstSizeBytes=TPlcrBurstSizeBytes, TQosQGrpInstanceIDorZero=TQosQGrpInstanceIDorZero, TmnxPwGlobalIdOrZero=TmnxPwGlobalIdOrZero, TmnxThresholdGroupType=TmnxThresholdGroupType, TmnxMobProfNameOrEmpty=TmnxMobProfNameOrEmpty, TmnxVdoGrpIdOrInherit=TmnxVdoGrpIdOrInherit, TmnxMobApn=TmnxMobApn, TmnxMobDiaPeerHost=TmnxMobDiaPeerHost, TmnxMobPdnRefPointType=TmnxMobPdnRefPointType, TNetworkPolicyID=TNetworkPolicyID, TItemMatch=TItemMatch, TItemLongDescription=TItemLongDescription, QTagFullRangeOrNone=QTagFullRangeOrNone, TMlpppQoSProfileId=TMlpppQoSProfileId, TSdpIngressPolicyID=TSdpIngressPolicyID, TIngressHsmdaCounterIdOrZero=TIngressHsmdaCounterIdOrZero, TmnxVdoStatInt=TmnxVdoStatInt, THPolPIRRate=THPolPIRRate, TmnxMobArp=TmnxMobArp, TmnxActionType=TmnxActionType, TFrameType=TFrameType, TAdaptationRule=TAdaptationRule, SdpBindId=SdpBindId, TmnxMobNode=TmnxMobNode, TTcpUdpPortOperator=TTcpUdpPortOperator, TmnxMobMccOrEmpty=TmnxMobMccOrEmpty, TmnxSrrpPriorityStep=TmnxSrrpPriorityStep, TCIRPercentOverride=TCIRPercentOverride, TmnxMobImsi=TmnxMobImsi, THsmdaSchedulerPolicyGroupId=THsmdaSchedulerPolicyGroupId, TmnxMobArpValue=TmnxMobArpValue, TClassBurstLimit=TClassBurstLimit, TmnxAccPlcyQICounters=TmnxAccPlcyQICounters, TmnxMobSdfFilter=TmnxMobSdfFilter, TmnxMobImei=TmnxMobImei, TSysResource=TSysResource, TmnxBgpPreference=TmnxBgpPreference, TmnxMobQciValue=TmnxMobQciValue, TPlcyMode=TPlcyMode, THSMDAQueueBurstLimit=THSMDAQueueBurstLimit, TmnxVcId=TmnxVcId, TmnxMobStaticPolPrecedenceOrZero=TmnxMobStaticPolPrecedenceOrZero, TEgressHsmdaPerPacketOffset=TEgressHsmdaPerPacketOffset, TPortSchedulerPIR=TPortSchedulerPIR, THPolCIRRateOverride=THPolCIRRateOverride, TQueueMode=TQueueMode, TmnxMobUeState=TmnxMobUeState, TmnxOperGrpHoldUpTime=TmnxOperGrpHoldUpTime, TQueueId=TQueueId, TmnxMobSdfFilterNum=TmnxMobSdfFilterNum, TmnxMobPeerType=TmnxMobPeerType, TmnxServId=TmnxServId, TLevel=TLevel, TmnxMobArpValueOrZero=TmnxMobArpValueOrZero, TmnxEncapVal=TmnxEncapVal, TmnxVcIdOrNone=TmnxVcIdOrNone, TmnxQosBytesHex=TmnxQosBytesHex, TNamedItem=TNamedItem, TmnxBsxAarpIdOrZero=TmnxBsxAarpIdOrZero, TTmplPolicyID=TTmplPolicyID, TmnxAccPlcyAACounters=TmnxAccPlcyAACounters, TmnxMobUeRat=TmnxMobUeRat, THsmdaWeightClass=THsmdaWeightClass, TmnxVdoIfName=TmnxVdoIfName, TmnxMobRtrAdvtLifeTime=TmnxMobRtrAdvtLifeTime, TmnxSpbFidOrZero=TmnxSpbFidOrZero, TmnxVcType=TmnxVcType, TmnxEnabledDisabledOrInherit=TmnxEnabledDisabledOrInherit, TExpSecondaryShaperPIRRate=TExpSecondaryShaperPIRRate, TmnxAccessLoopEncaps2=TmnxAccessLoopEncaps2, TmnxTunnelGroupIdOrZero=TmnxTunnelGroupIdOrZero, THsmdaPolicyIncludeQueues=THsmdaPolicyIncludeQueues)
mibBuilder.exportSymbols("TIMETRA-TC-MIB", TPIRRateOrZero=TPIRRateOrZero, TmnxMacSpecification=TmnxMacSpecification, TQGroupType=TQGroupType, TmnxAccPlcyOICounters=TmnxAccPlcyOICounters, TFCSet=TFCSet, TMacFilterType=TMacFilterType, TDEValue=TDEValue, TmnxMobMncOrEmpty=TmnxMobMncOrEmpty, TmnxBsxTransitIpPolicyId=TmnxBsxTransitIpPolicyId, TPolicyID=TPolicyID, TmnxSubAleOffsetMode=TmnxSubAleOffsetMode, TEgressHsmdaQueueId=TEgressHsmdaQueueId, TEgrHsmdaPerPacketOffsetOvr=TEgrHsmdaPerPacketOffsetOvr, TmnxRadiusServerOperState=TmnxRadiusServerOperState, TmnxMobProfGbrRate=TmnxMobProfGbrRate, TmnxIkePolicyAuthMethod=TmnxIkePolicyAuthMethod, TBWRateType=TBWRateType, THsmdaPIRMRate=THsmdaPIRMRate, TmnxVRtrMplsLspID=TmnxVRtrMplsLspID, TmnxAncpStringOrZero=TmnxAncpStringOrZero, TBurstSizeOverride=TBurstSizeOverride, THsmdaWrrWeightOverride=THsmdaWrrWeightOverride, TmnxVRtrID=TmnxVRtrID, TmnxMobNai=TmnxMobNai, TmnxMsPwPeSignaling=TmnxMsPwPeSignaling, TmnxSubRadiusVendorId=TmnxSubRadiusVendorId, TmnxMobMcc=TmnxMobMcc, TPortSchedulerCIR=TPortSchedulerCIR, TAdvCfgRate=TAdvCfgRate, THsmdaCIRKRate=THsmdaCIRKRate, THsmdaCIRMRateOverride=THsmdaCIRMRateOverride, TSapIngressPolicyID=TSapIngressPolicyID, TIngressHsmdaQueueId=TIngressHsmdaQueueId, TProfileUseDEOrNone=TProfileUseDEOrNone, TIngPolicerId=TIngPolicerId, TNetworkIngressMeterId=TNetworkIngressMeterId, TmnxBsxAarpServiceRefType=TmnxBsxAarpServiceRefType, TmnxMobUeSubType=TmnxMobUeSubType, TBurstSizeBytesOverride=TBurstSizeBytesOverride, TmnxMobGwId=TmnxMobGwId, TmnxTunnelType=TmnxTunnelType, TBurstSize=TBurstSize, TPlcyQuanta=TPlcyQuanta, THsmdaCIRKRateOverride=THsmdaCIRKRateOverride, TmnxMobLiTargetType=TmnxMobLiTargetType, BgpPeeringStatus=BgpPeeringStatus, THsmdaPolicyScheduleClass=THsmdaPolicyScheduleClass, Dot1PPriority=Dot1PPriority, TmnxMobProfPolChargingMethod=TmnxMobProfPolChargingMethod, TmnxBsxTransitIpPolicyIdOrZero=TmnxBsxTransitIpPolicyIdOrZero, ServiceOperStatus=ServiceOperStatus, Dot1PPriorityMask=Dot1PPriorityMask, TmnxMobChargingLevel=TmnxMobChargingLevel, TmnxSubAleOffset=TmnxSubAleOffset, THsmdaWeightOverride=THsmdaWeightOverride, THSMDABurstSizeBytes=THSMDABurstSizeBytes, TEntryIndicator=TEntryIndicator, TmnxDefInterDestIdSource=TmnxDefInterDestIdSource, TmnxBsxTransPrefPolicyId=TmnxBsxTransPrefPolicyId, TmnxVdoOutputFormat=TmnxVdoOutputFormat, TDirection=TDirection, TEgressHsmdaCounterIdOrZero=TEgressHsmdaCounterIdOrZero, TmnxRadiusPendingReqLimit=TmnxRadiusPendingReqLimit, TAtmTdpDescrType=TAtmTdpDescrType, THsmdaCounterIdOrZero=THsmdaCounterIdOrZero, TmnxPppNcpProtocol=TmnxPppNcpProtocol, TmnxVdoPortNumber=TmnxVdoPortNumber, THsmdaWrrWeight=THsmdaWrrWeight, TmnxSpokeSdpId=TmnxSpokeSdpId, TBurstPercentOrDefaultOverride=TBurstPercentOrDefaultOverride, TmnxMobBearerType=TmnxMobBearerType, THsmdaWeight=THsmdaWeight, TmnxIgmpGroupFilterMode=TmnxIgmpGroupFilterMode, TmnxBGPFamilyType=TmnxBGPFamilyType, TQosOverrideType=TQosOverrideType, TPolicyStatementNameOrEmpty=TPolicyStatementNameOrEmpty, TEgrPolicerIdOrNone=TEgrPolicerIdOrNone, TmnxMldGroupType=TmnxMldGroupType, TPortSchedulerPIRRate=TPortSchedulerPIRRate, TmnxEgrPolicerStatMode=TmnxEgrPolicerStatMode, TmnxMplsTpNodeID=TmnxMplsTpNodeID, TmnxSlaProfileStringOrEmpty=TmnxSlaProfileStringOrEmpty, THsmdaCounterIdOrZeroOrAll=THsmdaCounterIdOrZeroOrAll, TmnxMobImsiStr=TmnxMobImsiStr, THsmdaCIRMRate=THsmdaCIRMRate, TmnxDefSubIdSource=TmnxDefSubIdSource, TDEProfile=TDEProfile, TEntryId=TEntryId, TmnxMobBearerId=TmnxMobBearerId, TmnxVdoAnalyzerAlarm=TmnxVdoAnalyzerAlarm, TmnxSubIdentStringOrEmpty=TmnxSubIdentStringOrEmpty, TmnxPppoeUserName=TmnxPppoeUserName, TProfile=TProfile, TmnxMobChargingProfile=TmnxMobChargingProfile, TmnxAccPlcyQECounters=TmnxAccPlcyQECounters, TmnxCdrType=TmnxCdrType, TmnxSvcOperGrpCreationOrigin=TmnxSvcOperGrpCreationOrigin, TmnxSpbFdbLocale=TmnxSpbFdbLocale, TRateType=TRateType, TPriorityOrDefault=TPriorityOrDefault, TmnxAccPlcyOECounters=TmnxAccPlcyOECounters, THPolCIRRate=THPolCIRRate, TmnxMobProfIpTtl=TmnxMobProfIpTtl, THPolVirtualSchePIRRate=THPolVirtualSchePIRRate, TmnxDHCP6MsgType=TmnxDHCP6MsgType, TmnxIPsecTunnelTemplateIdOrZero=TmnxIPsecTunnelTemplateIdOrZero, TmnxMobRtrAdvtInterval=TmnxMobRtrAdvtInterval, TmnxMobSdfFilterProtocol=TmnxMobSdfFilterProtocol, TDEProfileOrDei=TDEProfileOrDei, TmnxMobAccessType=TmnxMobAccessType, QTag=QTag, TmnxAccessLoopEncaps1=TmnxAccessLoopEncaps1, TmnxMplsTpTunnelType=TmnxMplsTpTunnelType, TmnxSpokeSdpIdOrZero=TmnxSpokeSdpIdOrZero, TSapEgrEncapGrpQosPolicyIdOrZero=TSapEgrEncapGrpQosPolicyIdOrZero, TmnxMobUeId=TmnxMobUeId, TmnxMobMsisdn=TmnxMobMsisdn, TmnxBfdSessOperState=TmnxBfdSessOperState, TBurstLimit=TBurstLimit, TmnxVpnIpBackupFamily=TmnxVpnIpBackupFamily, ServiceAccessPoint=ServiceAccessPoint, TmnxDhcpOptionType=TmnxDhcpOptionType, TEgrPolicerId=TEgrPolicerId, TmnxOperGrpHoldDownTime=TmnxOperGrpHoldDownTime, TmnxMobPdnSessionEvent=TmnxMobPdnSessionEvent, TmnxMobQci=TmnxMobQci, TmnxPwGlobalId=TmnxPwGlobalId, TMeterMode=TMeterMode, TmnxMobUeStrPrefix=TmnxMobUeStrPrefix, TmnxMobLiTarget=TmnxMobLiTarget, TmnxBinarySpecification=TmnxBinarySpecification, ServiceAdminStatus=ServiceAdminStatus, TPrecValueOrNone=TPrecValueOrNone, TmnxBsxAarpId=TmnxBsxAarpId, TmnxMobChargingProfileOrInherit=TmnxMobChargingProfileOrInherit, TPlcrBurstSizeBytesOverride=TPlcrBurstSizeBytesOverride, TmnxIkePolicyOwnAuthMethod=TmnxIkePolicyOwnAuthMethod, TmnxAppProfileString=TmnxAppProfileString, TmnxStrSapId=TmnxStrSapId, TmnxTimeInSec=TmnxTimeInSec, TmnxMobDiaDetailPathMgmtState=TmnxMobDiaDetailPathMgmtState, TmnxSubMgtIntDestId=TmnxSubMgtIntDestId, IpAddressPrefixLength=IpAddressPrefixLength, TmnxMobIpCanType=TmnxMobIpCanType, TProfileOrDei=TProfileOrDei, TPriorityOrUndefined=TPriorityOrUndefined, TmnxBsxTransPrefPolicyIdOrZero=TmnxBsxTransPrefPolicyIdOrZero, TmnxIngPolicerStatMode=TmnxIngPolicerStatMode)
