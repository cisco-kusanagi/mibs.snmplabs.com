#
# PySNMP MIB module IEEE8021-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IEEE8021-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:13:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, org, iso, MibIdentifier, ModuleIdentity, Unsigned32, Integer32, Gauge32, IpAddress, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "org", "iso", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Integer32", "Gauge32", "IpAddress", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ieee8021TcMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 1))
ieee8021TcMib.setRevisions(('2014-12-15 00:00', '2012-02-15 00:00', '2011-08-23 00:00', '2011-04-06 00:00', '2011-02-27 00:00', '2008-11-18 00:00', '2008-10-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ieee8021TcMib.setRevisionsDescriptions(('Published as part of IEEE Std 802.1Q 2014 revision. Cross references updated and corrected. Updating of definition of IEEE8021PbbIngressEgress New identifier types for new SPBM MA types', 'Modified IEEE8021BridgePortType textual convention to include stationFacingBridgePort, uplinkAccessPort, and uplinkRelayPort types.', 'Modified textual conventions to support the IEEE 802.1 MIBs for PBB-TE Infrastructure Protection Switching.', 'Modified textual conventions to support Remote Customer Service Interfaces.', 'Minor edits to contact information etc. as part of 2011 revision of IEEE Std 802.1Q.', 'Added textual conventions needed to support the IEEE 802.1 MIBs for PBB-TE. Additionally, some textual conventions were modified for the same reason.', 'Initial version.',))
if mibBuilder.loadTexts: ieee8021TcMib.setLastUpdated('201412150000Z')
if mibBuilder.loadTexts: ieee8021TcMib.setOrganization('IEEE 802.1 Working Group')
if mibBuilder.loadTexts: ieee8021TcMib.setContactInfo(' WG-URL: http://grouper.ieee.org/groups/802/1/index.html WG-EMail: stds-802-1@ieee.org Contact: IEEE 802.1 Working Group Chair Postal: C/O IEEE 802.1 Working Group IEEE Standards Association 445 Hoes Lane P.O. Box 1331 Piscataway NJ 08855-1331 USA E-mail: STDS-802-1-L@LISTSERV.IEEE.ORG')
if mibBuilder.loadTexts: ieee8021TcMib.setDescription('Textual conventions used throughout the various IEEE 802.1 MIB modules. Unless otherwise indicated, the references in this MIB module are to IEEE Std 802.1Q-2014. Copyright (C) IEEE (2014). This version of this MIB module is part of IEEE Std 802.1Q; see the draft itself for full legal notices.')
ieee802dot1mibs = MibIdentifier((1, 3, 111, 2, 802, 1, 1))
class IEEE8021PbbComponentIdentifier(TextualConvention, Unsigned32):
    reference = '12.3 l)'
    description = 'The component identifier is used to distinguish between the multiple virtual Bridge instances within a PB or PBB. Each virtual Bridge instance is called a component. In simple situations where there is only a single component the default value is 1. The component is identified by a component identifier unique within the BEB and by a MAC address unique within the PBBN. Each component is associated with a Backbone Edge Bridge (BEB) Configuration managed object.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IEEE8021PbbComponentIdentifierOrZero(TextualConvention, Unsigned32):
    reference = '12.3 l)'
    description = "The component identifier is used to distinguish between the multiple virtual Bridge instances within a PB or PBB. In simple situations where there is only a single component the default value is 1. The component is identified by a component identifier unique within the BEB and by a MAC address unique within the PBBN. Each component is associated with a Backbone Edge Bridge (BEB) Configuration managed object. The special value '0' means 'no component identifier'. When this TC is used as the SYNTAX of an object, that object must specify the exact meaning for this value."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class IEEE8021PbbServiceIdentifier(TextualConvention, Unsigned32):
    reference = '12.16.3, 12.16.5'
    description = 'The service instance identifier is used at the Customer Backbone Port of a PBB to distinguish a service instance (Local-SID). If the Local-SID field is supported, it is used to perform a bidirectional 1:1 mapping between the Backbone I-SID and the Local-SID. If the Local-SID field is not supported, the Local-SID value is the same as the Backbone I-SID value.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(256, 16777214)

class IEEE8021PbbServiceIdentifierOrUnassigned(TextualConvention, Unsigned32):
    reference = '12.16.3, 12.16.5'
    description = 'The service instance identifier is used at the Customer Backbone Port of a PBB to distinguish a service instance (Local-SID). If the Local-SID field is supported, it is used to perform a bidirectional 1:1 mapping between the Backbone I-SID and the Local-SID. If the Local-SID field is not supported, the Local-SID value is the same as the Backbone I-SID value. The special value of 1 indicates an unassigned I-SID.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(256, 16777214), )
class IEEE8021PbbIngressEgress(TextualConvention, Bits):
    reference = '12.16.3, 12.16.5'
    description = 'A 2 bit selector which determines if frames on this VIP may ingress to the PBBN but not egress the PBBN, egress to the PBBN but not ingress the PBBN, or both ingress and egress the PBBN.'
    status = 'current'
    namedValues = NamedValues(("ingress", 0), ("egress", 1))

class IEEE8021PriorityCodePoint(TextualConvention, Integer32):
    reference = '12.6.2.6'
    description = 'Bridge ports may encode or decode the PCP value of the frames that traverse the port. This textual convention names the possible encoding and decoding schemes that the port may use. The priority and drop_eligible parameters are encoded in the Priority Code Point (PCP) field of the VLAN tag using the Priority Code Point Encoding Table for the Port, and they are decoded from the PCP using the Priority Code Point Decoding Table.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("codePoint8p0d", 1), ("codePoint7p1d", 2), ("codePoint6p2d", 3), ("codePoint5p3d", 4))

class IEEE8021BridgePortNumber(TextualConvention, Unsigned32):
    reference = '17.3.2.2'
    description = 'An integer that uniquely identifies a Bridge Port, as specified in 17.3.2.2. This value is used within the spanning tree protocol to identify this port to neighbor Bridges.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class IEEE8021BridgePortNumberOrZero(TextualConvention, Unsigned32):
    reference = '17.3.2.2'
    description = 'An integer that uniquely identifies a Bridge Port. The value 0 means no port number, and this must be clarified in the DESCRIPTION clause of any object defined using this TEXTUAL-CONVENTION.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IEEE8021BridgePortType(TextualConvention, Integer32):
    reference = '40.4, 12.13.1.1, 12.13.1.2, 12.16, 12.16.1.1.3 12.16.2.1, 12.26'
    description = "A port type. The possible port types are: customerVlanPort(2) - Indicates a port is a C-tag aware port of an enterprise VLAN aware Bridge. providerNetworkPort(3) - Indicates a port is an S-tag aware port of a Provider Bridge or Backbone Edge Bridge used for connections within a PBN or PBBN. customerNetworkPort(4) - Indicates a port is an S-tag aware port of a Provider Bridge or Backbone Edge Bridge used for connections to the exterior of a PBN or PBBN. customerEdgePort(5) - Indicates a port is a C-tag aware port of a Provider Bridge used for connections to the exterior of a PBN or PBBN. customerBackbonePort(6) - Indicates a port is a I-tag aware port of a Backbone Edge Bridge's B-component. virtualInstancePort(7) - Indicates a port is a virtual S-tag aware port within a Backbone Edge Bridge's I-component which is responsible for handling S-tagged traffic for a specific backbone service instance. dBridgePort(8) - Indicates a port is a VLAN-unaware member of an 802.1D Bridge. remoteCustomerAccessPort (9) - Indicates a port is an S-tag aware port of a Provider Bridge used for connections to remote customer interface LANs through another PBN. stationFacingBridgePort (10) - Indicates a port of a Bridge that supports the EVB status parameters (40.4) with an EVBMode parameter value of EVB Bridge. uplinkAccessPort (11) - Indicates a port on a Port-mapping S-VLAN component that connects an EVB Bridge with an EVB station. uplinkRelayPort (12) - Indicates a port of an edge relay that supports the EVB status parameters (40.4) with an EVBMode parameter value of EVB station."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("none", 1), ("customerVlanPort", 2), ("providerNetworkPort", 3), ("customerNetworkPort", 4), ("customerEdgePort", 5), ("customerBackbonePort", 6), ("virtualInstancePort", 7), ("dBridgePort", 8), ("remoteCustomerAccessPort", 9), ("stationFacingBridgePort", 10), ("uplinkAccessPort", 11), ("uplinkRelayPort", 12))

class IEEE8021VlanIndex(TextualConvention, Unsigned32):
    reference = '9.6'
    description = 'A value used to index per-VLAN tables: values of 0 and 4095 are not permitted. If the value is between 1 and 4094 inclusive, it represents an IEEE 802.1Q VLAN-ID with global scope within a given bridged domain (see VlanId textual convention). If the value is greater than 4095, then it represents a VLAN with scope local to the particular agent, i.e., one without a global VLAN-ID assigned to it. Such VLANs are outside the scope of IEEE 802.1Q, but it is convenient to be able to manage them in the same way using this MIB.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 4094), ValueRangeConstraint(4096, 4294967295), )
class IEEE8021VlanIndexOrWildcard(TextualConvention, Unsigned32):
    reference = '9.6'
    description = "A value used to index per-VLAN tables. The value 0 is not permitted, while the value 4095 represents a 'wildcard' value. An object whose SYNTAX is IEEE8021VlanIndexOrWildcard must specify in its DESCRIPTION the specific meaning of the wildcard value. If the value is between 1 and 4094 inclusive, it represents an IEEE 802.1Q VLAN-ID with global scope within a given bridged domain (see VlanId textual convention). If the value is greater than 4095, then it represents a VLAN with scope local to the particular agent, i.e., one without a global VLAN-ID assigned to it. Such VLANs are outside the scope of IEEE 802.1Q, but it is convenient to be able to manage them in the same way using this MIB."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IEEE8021MstIdentifier(TextualConvention, Unsigned32):
    description = 'In an MSTP Bridge, an MSTID, i.e., a value used to identify a spanning tree (or MST) instance. In the PBB-TE environment the value 4094 is used to identify VIDs managed by the PBB-TE procedures.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4094)

class IEEE8021ServiceSelectorType(TextualConvention, Integer32):
    description = 'A value that represents a type (and thereby the format) of a IEEE8021ServiceSelectorValue. The value can be one of the following: ieeeReserved(0) Reserved for definition by IEEE 802.1 recommend to not use zero unless absolutely needed. vlanId(1) 12-Bit identifier as described in IEEE802.1Q. isid(2) 24-Bit identifier as described in IEEE802.1ah. tesid(3) 32 Bit identifier as described below. segid(4) 32 Bit identifier as described below. path-tesid(5) 32 Bit identifier as described below. group-isid(6) 24 Bit identifier as described below. ieeeReserved(7) Reserved for definition by IEEE 802.1 To support future extensions, the IEEE8021ServiceSelectorType textual convention SHOULD NOT be subtyped in object type definitions. It MAY be subtyped in compliance statements in order to require only a subset of these address types for a compliant implementation. The tesid is used as a service selector for MAs that are present in Bridges that implement PBB-TE functionality. A selector of this type is interpreted as a 32 bit unsigned value of type IEEE8021PbbTeTSidId. This type is used to index the ieee8021PbbTeTeSiEspTable to find the ESPs which comprise the TE Service Instance named by this TE-SID value. The segid is used as a service selector for MAs that are present in Bridges that implement IPS functionality. A selector of this type is interpreted as a 32 bit unsigned value of type IEEE8021TeipsSegid. This type is used to index the Ieee8021TeipsSegTable to find the SMPs which comprise the Infrastructure Segment named by this segid value. The path-tesid is used as a service selector for SPBM path MAs. A selector of this type is interpreted as a 32 bit unsigned value corresponding to the MA index dot1agCfmMaIndex. This type is used to index the dot1agCfmMepSpbmEspTable to find the ESPs which comprise the SPBM path associated with an SPBM path MA. The group-isid is used as a service selector for SPBM group MAs. A selector of this type is interpreted as a 24 bit unsigned value corresponding to the I-SID associated with an SPBM group MA. Implementations MUST ensure that IEEE8021ServiceSelectorType objects and any dependent objects (e.g., IEEE8021ServiceSelectorValue objects) are consistent. An inconsistentValue error MUST be generated if an attempt to change an IEEE8021ServiceSelectorType object would, for example, lead to an undefined IEEE8021ServiceSelectorValue value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("vlanId", 1), ("isid", 2), ("tesid", 3), ("segid", 4), ("path-tesid", 5), ("group-isid", 6), ("ieeeReserved", 7))

class IEEE8021ServiceSelectorValueOrNone(TextualConvention, Unsigned32):
    description = "An integer that uniquely identifies a generic MAC Service, or none. Examples of service selectors are a VLAN-ID (IEEE 802.1Q) and an I-SID (IEEE 802.1ah). An IEEE8021ServiceSelectorValueOrNone value is always interpreted within the context of an IEEE8021ServiceSelectorType value. Every usage of the IEEE8021ServiceSelectorValueOrNone textual convention is required to specify the IEEE8021ServiceSelectorType object that provides the context. It is suggested that the IEEE8021ServiceSelectorType object be logically registered before the object(s) that use the IEEE8021ServiceSelectorValueOrNone textual convention, if they appear in the same logical row. The value of an IEEE8021ServiceSelectorValueOrNone object must always be consistent with the value of the associated IEEE8021ServiceSelectorType object. Attempts to set an IEEE8021ServiceSelectorValueOrNone object to a value inconsistent with the associated IEEE8021ServiceSelectorType must fail with an inconsistentValue error. The special value of zero is used to indicate that no service selector is present or used. This can be used in any situation where an object or a table entry MUST either refer to a specific service, or not make a selection. Note that a MIB object that is defined using this TEXTUAL-CONVENTION SHOULD clarify the meaning of 'no service' (i.e., the special value 0), as well as the maximum value (i.e., 4094, for a VLAN ID)."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class IEEE8021ServiceSelectorValue(TextualConvention, Unsigned32):
    description = 'An integer that uniquely identifies a generic MAC Service. Examples of service selectors are a VLAN-ID (IEEE 802.1Q) and an I-SID (IEEE 802.1ah). An IEEE8021ServiceSelectorValue value is always interpreted within the context of an IEEE8021ServiceSelectorType value. Every usage of the IEEE8021ServiceSelectorValue textual convention is required to specify the IEEE8021ServiceSelectorType object that provides the context. It is suggested that the IEEE8021ServiceSelectorType object be logically registered before the object(s) that use the IEEE8021ServiceSelectorValue textual convention, if they appear in the same logical row. The value of an IEEE8021ServiceSelectorValue object must always be consistent with the value of the associated IEEE8021ServiceSelectorType object. Attempts to set an IEEE8021ServiceSelectorValue object to a value inconsistent with the associated IEEE8021ServiceSelectorType must fail with an inconsistentValue error. Note that a MIB object that is defined using this TEXTUAL-CONVENTION SHOULD clarify the maximum value (i.e., 4094, for a VLAN ID).'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IEEE8021PortAcceptableFrameTypes(TextualConvention, Integer32):
    reference = '12.10.1.3, 12.13.3.3, 12.13.3.4'
    description = 'Acceptable frame types on a port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("admitAll", 1), ("admitUntaggedAndPriority", 2), ("admitTagged", 3))

class IEEE8021PriorityValue(TextualConvention, Unsigned32):
    reference = '12.13.3.3'
    description = 'An 802.1Q user priority value.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class IEEE8021PbbTeProtectionGroupId(TextualConvention, Unsigned32):
    reference = '12.18.2'
    description = 'The PbbTeProtectionGroupId identifier is used to distinguish protection group instances present in the B Component of an IB-BEB.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 429467295)

class IEEE8021PbbTeEsp(TextualConvention, OctetString):
    reference = '3.75'
    description = 'This textual convention is used to represent the logical components that comprise the 3-tuple that identifies an Ethernet Switched Path. The 3-tuple consists of a destination MAC address, a source MAC address and a VID. Bytes (1..6) of this textual convention contain the ESP-MAC-DA, bytes (7..12) contain the ESP-MAC-SA, and bytes (13..14) contain the ESP-VID.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(14, 14)
    fixedLength = 14

class IEEE8021PbbTeTSidId(TextualConvention, Unsigned32):
    reference = '3.240'
    description = 'This textual convention is used to represent an identifier that refers to a TE Service Instance. Note that, internally a TE-SID is implementation dependent. This textual convention defines the external representation of TE-SID values.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 42947295)

class IEEE8021PbbTeProtectionGroupConfigAdmin(TextualConvention, Integer32):
    reference = '26.10.3.3.5 26.10.3.3.6 26.10.3.3.7 12.18.2.3.2'
    description = 'This textual convention is used to represent administrative commands that can be issued to a protection group. The value noAdmin(1) is used to indicate that no administrative action is to be performed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("clear", 1), ("lockOutProtection", 2), ("forceSwitch", 3), ("manualSwitchToProtection", 4), ("manualSwitchToWorking", 5))

class IEEE8021PbbTeProtectionGroupActiveRequests(TextualConvention, Integer32):
    reference = '12.18.2.1.3 d)'
    description = 'This textual convention is used to represent the status of active requests within a protection group.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("noRequest", 1), ("loP", 2), ("fs", 3), ("pSFH", 4), ("wSFH", 5), ("manualSwitchToProtection", 6), ("manualSwitchToWorking", 7))

class IEEE8021TeipsIpgid(TextualConvention, Unsigned32):
    reference = '12.24.1.1.3 a)'
    description = 'The TEIPS IPG identifier is used to distinguish IPG instances present in a PBB.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 429467295)

class IEEE8021TeipsSegid(TextualConvention, Unsigned32):
    reference = '26.11.1'
    description = 'This textual convention is used to represent an identifier that refers to an Infrastructure Segment. Note that, internally a SEG-ID implementation dependent. This textual convention defines the external representation of SEG-ID values.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 42947295)

class IEEE8021TeipsSmpid(TextualConvention, OctetString):
    reference = '26.11.1'
    description = 'This textual convention is used to represent the logical components that comprise the 3-tuple that identifies a Segment Monitoring Path (SMP). The 3-tuple consists of a destination MAC address, a source MAC address and a VID. Bytes (1..6) of this textual convention contain the SMP-MAC-DA, bytes (7..12) contain the SMP-MAC-SA, and bytes (13..14) contain the SMP-VID.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(14, 14)
    fixedLength = 14

class IEEE8021TeipsIpgConfigAdmin(TextualConvention, Integer32):
    reference = '12.24.2.1.3 h)'
    description = 'This textual convention is used to represent administrative commands that can be issued to an IPG. The value clear(1) is used to indicate that no administrative action is to be performed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("clear", 1), ("lockOutProtection", 2), ("forceSwitch", 3), ("manualSwitchToProtection", 4), ("manualSwitchToWorking", 5))

class IEEE8021TeipsIpgConfigActiveRequests(TextualConvention, Integer32):
    reference = '12.24.2.1.3 d)'
    description = 'This textual convention is used to represent the status of active requests within an IPG.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("noRequest", 1), ("loP", 2), ("fs", 3), ("pSFH", 4), ("wSFH", 5), ("manualSwitchToProtection", 6), ("manualSwitchToWorking", 7))

mibBuilder.exportSymbols("IEEE8021-TC-MIB", IEEE8021BridgePortNumber=IEEE8021BridgePortNumber, IEEE8021ServiceSelectorValue=IEEE8021ServiceSelectorValue, IEEE8021PortAcceptableFrameTypes=IEEE8021PortAcceptableFrameTypes, IEEE8021TeipsSegid=IEEE8021TeipsSegid, IEEE8021PbbIngressEgress=IEEE8021PbbIngressEgress, IEEE8021BridgePortType=IEEE8021BridgePortType, IEEE8021PriorityValue=IEEE8021PriorityValue, IEEE8021TeipsIpgid=IEEE8021TeipsIpgid, IEEE8021PbbTeProtectionGroupConfigAdmin=IEEE8021PbbTeProtectionGroupConfigAdmin, IEEE8021VlanIndexOrWildcard=IEEE8021VlanIndexOrWildcard, IEEE8021TeipsIpgConfigActiveRequests=IEEE8021TeipsIpgConfigActiveRequests, ieee8021TcMib=ieee8021TcMib, IEEE8021PbbServiceIdentifier=IEEE8021PbbServiceIdentifier, IEEE8021ServiceSelectorValueOrNone=IEEE8021ServiceSelectorValueOrNone, IEEE8021VlanIndex=IEEE8021VlanIndex, IEEE8021ServiceSelectorType=IEEE8021ServiceSelectorType, IEEE8021PbbTeProtectionGroupActiveRequests=IEEE8021PbbTeProtectionGroupActiveRequests, IEEE8021MstIdentifier=IEEE8021MstIdentifier, IEEE8021PbbServiceIdentifierOrUnassigned=IEEE8021PbbServiceIdentifierOrUnassigned, IEEE8021PbbTeEsp=IEEE8021PbbTeEsp, IEEE8021PbbComponentIdentifier=IEEE8021PbbComponentIdentifier, IEEE8021PbbTeTSidId=IEEE8021PbbTeTSidId, IEEE8021TeipsSmpid=IEEE8021TeipsSmpid, PYSNMP_MODULE_ID=ieee8021TcMib, IEEE8021PbbTeProtectionGroupId=IEEE8021PbbTeProtectionGroupId, ieee802dot1mibs=ieee802dot1mibs, IEEE8021PriorityCodePoint=IEEE8021PriorityCodePoint, IEEE8021TeipsIpgConfigAdmin=IEEE8021TeipsIpgConfigAdmin, IEEE8021PbbComponentIdentifierOrZero=IEEE8021PbbComponentIdentifierOrZero, IEEE8021BridgePortNumberOrZero=IEEE8021BridgePortNumberOrZero)
