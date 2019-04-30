#
# PySNMP MIB module IEEE8021-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IEEE8021-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:57:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, org, Counter64, NotificationType, ObjectIdentity, ModuleIdentity, Gauge32, IpAddress, Unsigned32, MibIdentifier, Integer32, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "org", "Counter64", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Gauge32", "IpAddress", "Unsigned32", "MibIdentifier", "Integer32", "TimeTicks", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ieee8021TcMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 1))
ieee8021TcMib.setRevisions(('2014-12-15 00:00', '2012-02-15 00:00', '2011-08-23 00:00', '2011-04-06 00:00', '2011-02-27 00:00', '2008-11-18 00:00', '2008-10-15 00:00',))
if mibBuilder.loadTexts: ieee8021TcMib.setLastUpdated('201412150000Z')
if mibBuilder.loadTexts: ieee8021TcMib.setOrganization('IEEE 802.1 Working Group')
ieee802dot1mibs = MibIdentifier((1, 3, 111, 2, 802, 1, 1))
class IEEE8021PbbComponentIdentifier(TextualConvention, Unsigned32):
    reference = '12.3 l)'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IEEE8021PbbComponentIdentifierOrZero(TextualConvention, Unsigned32):
    reference = '12.3 l)'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class IEEE8021PbbServiceIdentifier(TextualConvention, Unsigned32):
    reference = '12.16.3, 12.16.5'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(256, 16777214)

class IEEE8021PbbServiceIdentifierOrUnassigned(TextualConvention, Unsigned32):
    reference = '12.16.3, 12.16.5'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(256, 16777214), )
class IEEE8021PbbIngressEgress(TextualConvention, Bits):
    reference = '12.16.3, 12.16.5'
    status = 'current'
    namedValues = NamedValues(("ingress", 0), ("egress", 1))

class IEEE8021PriorityCodePoint(TextualConvention, Integer32):
    reference = '12.6.2.6'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("codePoint8p0d", 1), ("codePoint7p1d", 2), ("codePoint6p2d", 3), ("codePoint5p3d", 4))

class IEEE8021BridgePortNumber(TextualConvention, Unsigned32):
    reference = '17.3.2.2'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class IEEE8021BridgePortNumberOrZero(TextualConvention, Unsigned32):
    reference = '17.3.2.2'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IEEE8021BridgePortType(TextualConvention, Integer32):
    reference = '40.4, 12.13.1.1, 12.13.1.2, 12.16, 12.16.1.1.3 12.16.2.1, 12.26'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("none", 1), ("customerVlanPort", 2), ("providerNetworkPort", 3), ("customerNetworkPort", 4), ("customerEdgePort", 5), ("customerBackbonePort", 6), ("virtualInstancePort", 7), ("dBridgePort", 8), ("remoteCustomerAccessPort", 9), ("stationFacingBridgePort", 10), ("uplinkAccessPort", 11), ("uplinkRelayPort", 12))

class IEEE8021VlanIndex(TextualConvention, Unsigned32):
    reference = '9.6'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 4094), ValueRangeConstraint(4096, 4294967295), )
class IEEE8021VlanIndexOrWildcard(TextualConvention, Unsigned32):
    reference = '9.6'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IEEE8021MstIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4094)

class IEEE8021ServiceSelectorType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("vlanId", 1), ("isid", 2), ("tesid", 3), ("segid", 4), ("path-tesid", 5), ("group-isid", 6), ("ieeeReserved", 7))

class IEEE8021ServiceSelectorValueOrNone(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class IEEE8021ServiceSelectorValue(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IEEE8021PortAcceptableFrameTypes(TextualConvention, Integer32):
    reference = '12.10.1.3, 12.13.3.3, 12.13.3.4'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("admitAll", 1), ("admitUntaggedAndPriority", 2), ("admitTagged", 3))

class IEEE8021PriorityValue(TextualConvention, Unsigned32):
    reference = '12.13.3.3'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class IEEE8021PbbTeProtectionGroupId(TextualConvention, Unsigned32):
    reference = '12.18.2'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 429467295)

class IEEE8021PbbTeEsp(TextualConvention, OctetString):
    reference = '3.75'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(14, 14)
    fixedLength = 14

class IEEE8021PbbTeTSidId(TextualConvention, Unsigned32):
    reference = '3.240'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 42947295)

class IEEE8021PbbTeProtectionGroupConfigAdmin(TextualConvention, Integer32):
    reference = '26.10.3.3.5 26.10.3.3.6 26.10.3.3.7 12.18.2.3.2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("clear", 1), ("lockOutProtection", 2), ("forceSwitch", 3), ("manualSwitchToProtection", 4), ("manualSwitchToWorking", 5))

class IEEE8021PbbTeProtectionGroupActiveRequests(TextualConvention, Integer32):
    reference = '12.18.2.1.3 d)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("noRequest", 1), ("loP", 2), ("fs", 3), ("pSFH", 4), ("wSFH", 5), ("manualSwitchToProtection", 6), ("manualSwitchToWorking", 7))

class IEEE8021TeipsIpgid(TextualConvention, Unsigned32):
    reference = '12.24.1.1.3 a)'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 429467295)

class IEEE8021TeipsSegid(TextualConvention, Unsigned32):
    reference = '26.11.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 42947295)

class IEEE8021TeipsSmpid(TextualConvention, OctetString):
    reference = '26.11.1'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(14, 14)
    fixedLength = 14

class IEEE8021TeipsIpgConfigAdmin(TextualConvention, Integer32):
    reference = '12.24.2.1.3 h)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("clear", 1), ("lockOutProtection", 2), ("forceSwitch", 3), ("manualSwitchToProtection", 4), ("manualSwitchToWorking", 5))

class IEEE8021TeipsIpgConfigActiveRequests(TextualConvention, Integer32):
    reference = '12.24.2.1.3 d)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("noRequest", 1), ("loP", 2), ("fs", 3), ("pSFH", 4), ("wSFH", 5), ("manualSwitchToProtection", 6), ("manualSwitchToWorking", 7))

mibBuilder.exportSymbols("IEEE8021-TC-MIB", IEEE8021PriorityValue=IEEE8021PriorityValue, IEEE8021PbbServiceIdentifier=IEEE8021PbbServiceIdentifier, IEEE8021ServiceSelectorValue=IEEE8021ServiceSelectorValue, IEEE8021ServiceSelectorValueOrNone=IEEE8021ServiceSelectorValueOrNone, IEEE8021ServiceSelectorType=IEEE8021ServiceSelectorType, IEEE8021VlanIndexOrWildcard=IEEE8021VlanIndexOrWildcard, IEEE8021PbbTeProtectionGroupConfigAdmin=IEEE8021PbbTeProtectionGroupConfigAdmin, IEEE8021PbbTeProtectionGroupId=IEEE8021PbbTeProtectionGroupId, IEEE8021PbbComponentIdentifierOrZero=IEEE8021PbbComponentIdentifierOrZero, IEEE8021PortAcceptableFrameTypes=IEEE8021PortAcceptableFrameTypes, IEEE8021PriorityCodePoint=IEEE8021PriorityCodePoint, IEEE8021TeipsIpgid=IEEE8021TeipsIpgid, IEEE8021BridgePortNumberOrZero=IEEE8021BridgePortNumberOrZero, IEEE8021MstIdentifier=IEEE8021MstIdentifier, PYSNMP_MODULE_ID=ieee8021TcMib, IEEE8021TeipsIpgConfigActiveRequests=IEEE8021TeipsIpgConfigActiveRequests, IEEE8021PbbTeTSidId=IEEE8021PbbTeTSidId, IEEE8021VlanIndex=IEEE8021VlanIndex, IEEE8021PbbComponentIdentifier=IEEE8021PbbComponentIdentifier, IEEE8021PbbTeProtectionGroupActiveRequests=IEEE8021PbbTeProtectionGroupActiveRequests, IEEE8021TeipsIpgConfigAdmin=IEEE8021TeipsIpgConfigAdmin, IEEE8021BridgePortType=IEEE8021BridgePortType, IEEE8021PbbIngressEgress=IEEE8021PbbIngressEgress, ieee8021TcMib=ieee8021TcMib, IEEE8021PbbServiceIdentifierOrUnassigned=IEEE8021PbbServiceIdentifierOrUnassigned, IEEE8021BridgePortNumber=IEEE8021BridgePortNumber, ieee802dot1mibs=ieee802dot1mibs, IEEE8021PbbTeEsp=IEEE8021PbbTeEsp, IEEE8021TeipsSegid=IEEE8021TeipsSegid, IEEE8021TeipsSmpid=IEEE8021TeipsSmpid)
