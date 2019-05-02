#
# PySNMP MIB module DC-MASTER-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DC-MASTER-TC
# Produced by pysmi-0.3.4 at Wed May  1 11:44:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, ObjectIdentity, IpAddress, NotificationType, Unsigned32, ModuleIdentity, Counter64, Integer32, MibIdentifier, TimeTicks, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "ObjectIdentity", "IpAddress", "NotificationType", "Unsigned32", "ModuleIdentity", "Counter64", "Integer32", "MibIdentifier", "TimeTicks", "Gauge32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dcMasterTc = ModuleIdentity((1, 2, 826, 0, 1, 1578918, 5, 41, 1))
dcMasterTc.setRevisions(('2014-04-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dcMasterTc.setRevisionsDescriptions(('DCL June 2013 files with Arris changes merged in',))
if mibBuilder.loadTexts: dcMasterTc.setLastUpdated('201404220000Z')
if mibBuilder.loadTexts: dcMasterTc.setOrganization('Data Connection Ltd.')
if mibBuilder.loadTexts: dcMasterTc.setContactInfo('Postal: Data Connection Ltd. 100 Church Street Enfield Middlesex EN2 6BQ United Kingdom Tel: +44 20 83661177 E-mail: info@dataconnection.com')
if mibBuilder.loadTexts: dcMasterTc.setDescription('The set of common Textual Conventions for use in all DCL MIBs.')
class AdminStatus(TextualConvention, Integer32):
    description = 'The desired administrative state of a MIB row.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("adminStatusUp", 1), ("adminStatusDown", 2))

class OperStatus(TextualConvention, Integer32):
    description = 'The current operational state of a MIB row. This set of values is used by many Data Connection products written before 2006.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("operStatusUp", 1), ("operStatusDown", 2), ("operStatusGoingUp", 3), ("operStatusGoingDown", 4), ("operStatusActFailed", 5))

class BaseOperStatus(TextualConvention, Integer32):
    description = 'The current operational state of a MIB row. This is a complete set of values used by all Data Connection products.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("operStatusUp", 1), ("operStatusDown", 2), ("operStatusGoingUp", 3), ("operStatusGoingDown", 4), ("operStatusActFailed", 5), ("operStatusQuiescing", 6), ("operStatusNotReady", 7), ("operStatusFailed", 8), ("operStatusPrntFailed", 9), ("operStatusFailedPerm", 10), ("operStatusFailing", 11))

class NpgOperStatus(TextualConvention, Integer32):
    description = 'The current operational state of a MIB row. This set of values has been used by the Data Connection Networking Protocols Group since 2006.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 8, 10, 11))
    namedValues = NamedValues(("operStatusUp", 1), ("operStatusDown", 2), ("operStatusGoingUp", 3), ("operStatusGoingDown", 4), ("operStatusActFailed", 5), ("operStatusFailed", 8), ("operStatusFailedPerm", 10), ("operStatusFailing", 11))

class Unsigned32NonZero(TextualConvention, Unsigned32):
    description = 'A non-zero Unsigned32.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class NumericIndex(TextualConvention, Integer32):
    description = 'A numeric index value or identifier.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class NumericIndexOrZero(TextualConvention, Integer32):
    description = 'Either a numeric index value or identifier, or the value zero with a special meaning defined by the object description. Do not use this TC for MIB table index objects. Zero is not valid for such objects.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class EntityIndex(TextualConvention, Integer32):
    description = 'The HAF entity index value identifying a DC software entity. This TC is deprecated. Use NumericIndex for all indexes.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class EntityIndexOrZero(TextualConvention, Integer32):
    description = 'The HAF entity index value identifying a DC software entity, or zero which is used to indicate that the entity is not present. This TC is deprecated. Use NumericIndexOrZero for all references to indexes.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class AuthUserDataString(TextualConvention, OctetString):
    description = 'A string of user data that will be passed to the a0auth interface.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 17)

class StdAccessListListIndex(TextualConvention, Integer32):
    description = 'An arbitrary index value identifying a standard access list.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class StdAccessListListIndexOrZero(TextualConvention, Integer32):
    description = 'An arbitrary index value identifying a standard access list or zero for no access list.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class StdAccessListRuleIndex(TextualConvention, Integer32):
    description = 'An index value identifying a particular rule within a standard access list. Rules are tested in order of increasing rule index.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ExtAccessListListIndex(TextualConvention, Integer32):
    description = 'An arbitrary index value identifying an extended access list.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ExtAccessListListIndexOrZero(TextualConvention, Integer32):
    description = 'An arbitrary index value identifying an extended access list or zero for no access list.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ExtAccessListRuleIndex(TextualConvention, Integer32):
    description = 'An index value identifying a particular rule within an extended access list. Rules are tested in order of increasing rule index.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class RouteAction(TextualConvention, Integer32):
    description = 'Action to perform on receipt of a packet which matches the destination for a static route. This is one of: - forward the packet to the address specified as the next-hop address - handle the packet locally - reject [drop and send ICMP] - discard [drop but do not send ICMP] - forward the packet using a tunnel.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("routeActionLocal", 1), ("routeActionForward", 2), ("routeActionReject", 3), ("routeActionDiscard", 4), ("routeActionTunnel", 5))

class AdminDistance(TextualConvention, Integer32):
    description = 'The adminstrative distance used in prioritizing routes from different sources when selecting active routes in DC-RTM. The active route is chosen from those available routes which have the lowest associated administrative distance.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class PathType(TextualConvention, Integer32):
    description = 'Protocol-specific path type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 65536, 131072, 131073, 131074, 196608, 262144, 327680, 393216, 458752, 524288, 589824, 589825, 589826, 589827, 655360, 720896, 786432, 851968, 851969, 851970, 851971, 917504, 917505, 917506, 983040, 1048576, 1048577, 1048578, 1114112))
    namedValues = NamedValues(("pathTypeNone", 0), ("pathTypeOther", 65536), ("pathTypeConnected", 131072), ("pathTypeConfiguredLocal", 131073), ("pathTypeConfiguredConnected", 131074), ("pathTypeStatic", 196608), ("pathTypeIcmp", 262144), ("pathTypeEgp", 327680), ("pathTypePd", 393216), ("pathTypeHello", 458752), ("pathTypeRip", 524288), ("pathTypeIsisLevel1Int", 589824), ("pathTypeIsisLevel2Int", 589825), ("pathTypeIsisLevel1Ext", 589826), ("pathTypeIsisLevel2Ext", 589827), ("pathTypeEsis", 655360), ("pathTypeIgrp", 720896), ("pathTypeBbnspfigp", 786432), ("pathTypeOspfIntraArea", 851968), ("pathTypeOspfInterArea", 851969), ("pathTypeOspfType1Ext", 851970), ("pathTypeOspfType2Ext", 851971), ("pathTypeBgpInt", 917504), ("pathTypeBgpExt", 917505), ("pathTypeBgpVpn", 917506), ("pathTypeIdpr", 983040), ("pathTypeEigrp", 1048576), ("pathTypeEigrpInt", 1048577), ("pathTypeEigrpExt", 1048578), ("pathTypeDvmrp", 1114112))

class EntityProcType(TextualConvention, Integer32):
    description = 'Control plane entity component type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(553779200, 587268096, 1023475712, 1040252928, 1040318464, 1057030144, 1057095680, 1090584576, 1090650112, 1174470656, 1241579520, 1241645056))
    namedValues = NamedValues(("entityRsvp", 553779200), ("entityLdpSc", 587268096), ("entityRtm", 1023475712), ("entityOspfPm", 1040252928), ("entityOspfNm", 1040318464), ("entityIsisPm", 1057030144), ("entityIsisSdc", 1057095680), ("entityBgpRm", 1090584576), ("entityBgpNm", 1090650112), ("entityRipPm", 1174470656), ("entityOspfv3Pm", 1241579520), ("entityOspfv3Nm", 1241645056))

class InetSubAddressType(TextualConvention, Integer32):
    description = 'A value that represents a subsequent type of Internet address.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("unicast", 1), ("multicast", 2))

class BfdSessionStatus(TextualConvention, Integer32):
    description = 'The current BFD session state of a peer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("bfdSessNotRequired", 0), ("bfdSessInitial", 1), ("bfdSessActivating", 2), ("bfdSessActive", 3), ("bfdSessInactive", 4), ("bfdSessAdminDown", 5), ("bfdSessNoContact", 6))

class IgpShortcutMetricType(TextualConvention, Integer32):
    description = 'Type of metric value. This is one of: - Absolute, or fixed; the metric value defined is used as a path cost. - Relative; the metric value defined is added to an existing path cost to produce the total cost of a path. Note that, in this case, the metric value defined may be zero, positive or negative.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("metricTypeAbsolute", 1), ("metricTypeRelative", 2))

class IfOperStatus(TextualConvention, Integer32):
    description = 'The IfOperStatus as defined in RFC 2863.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7))

class MjStatus(TextualConvention, Integer32):
    description = 'The status of a Master Join.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("mjNotJoined", 1), ("mjSentAddJoin", 2), ("mjSentRegister", 3), ("mjJoinActive", 4), ("mjSentUnregister", 5), ("mjSentDelJoin", 6), ("mjFailedToAdd", 7), ("mjFailedToRegister", 8), ("mjFailingOver", 9), ("mjFailed", 10), ("mjUnavailable", 11))

class SjStatus(TextualConvention, Integer32):
    description = 'The status of a Slave Join.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("sjNotJoined", 1), ("sjJoined", 2), ("sjRcvdRegister", 3), ("sjJoinActive", 4), ("sjFailingOver", 5), ("sjFailed", 6), ("sjRcvdUnregister", 7), ("sjUnregDone", 8))

class InterfaceScope(TextualConvention, OctetString):
    description = 'The scope of an interface or interface user. When components request information about interfaces, the request includes the scope of information that the component wishes to receive. Only interfaces with matching scope are distributed to the component. This is an opaque structure that maps to an ATG_IF_SCOPE_ID. See the definition of ATG_IF_SCOPE_ID for details.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 3)

mibBuilder.exportSymbols("DC-MASTER-TC", StdAccessListListIndexOrZero=StdAccessListListIndexOrZero, BfdSessionStatus=BfdSessionStatus, ExtAccessListRuleIndex=ExtAccessListRuleIndex, NumericIndexOrZero=NumericIndexOrZero, InetSubAddressType=InetSubAddressType, PathType=PathType, InterfaceScope=InterfaceScope, EntityIndex=EntityIndex, EntityProcType=EntityProcType, MjStatus=MjStatus, IgpShortcutMetricType=IgpShortcutMetricType, SjStatus=SjStatus, EntityIndexOrZero=EntityIndexOrZero, AdminStatus=AdminStatus, StdAccessListRuleIndex=StdAccessListRuleIndex, ExtAccessListListIndexOrZero=ExtAccessListListIndexOrZero, BaseOperStatus=BaseOperStatus, Unsigned32NonZero=Unsigned32NonZero, RouteAction=RouteAction, AuthUserDataString=AuthUserDataString, StdAccessListListIndex=StdAccessListListIndex, PYSNMP_MODULE_ID=dcMasterTc, NpgOperStatus=NpgOperStatus, OperStatus=OperStatus, NumericIndex=NumericIndex, IfOperStatus=IfOperStatus, ExtAccessListListIndex=ExtAccessListListIndex, AdminDistance=AdminDistance, dcMasterTc=dcMasterTc)
