#
# PySNMP MIB module JUNIPER-VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-VPN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:00:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Counter32, Bits, TimeTicks, ObjectIdentity, Integer32, NotificationType, Gauge32, IpAddress, Unsigned32, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "Bits", "TimeTicks", "ObjectIdentity", "Integer32", "NotificationType", "Gauge32", "IpAddress", "Unsigned32", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, DisplayString, StorageType, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "StorageType", "RowStatus")
jnxVpnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 26))
jnxVpnMIB.setRevisions(('2010-10-15 00:00', '2010-08-27 00:00', '2002-04-21 21:28',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxVpnMIB.setRevisionsDescriptions(('Corrected DISPLAY-HINT for TEXTUAL-CONVENTIONs associated with a JnxVpnIdentifier.', 'Corrected related TEXTUAL-CONVENTIONs associated with a JnxVpnIdentifier.', 'A VPN MIB module that allows one to configure and monitor several types of Provider Provisioned VPNs. Initial revision.',))
if mibBuilder.loadTexts: jnxVpnMIB.setLastUpdated('201010150000Z')
if mibBuilder.loadTexts: jnxVpnMIB.setOrganization('IETF Provider Provisioned VPNs WG')
if mibBuilder.loadTexts: jnxVpnMIB.setContactInfo(' Kireeti Kompella Postal: Juniper Networks, Inc. 1194 Mathilda Ave Sunnyvale, CA 94089 Tel: +1 408 745 2000 E-mail: kireeti@juniper.net')
if mibBuilder.loadTexts: jnxVpnMIB.setDescription('Extended VPN MIB module to support VPN Identifier for locally switched L2 circuits.')
jnxVpnMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 26, 0))
jnxVpnMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1))
jnxVpnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 26, 2))
class JnxVpnName(TextualConvention, OctetString):
    description = 'Name of the VPN.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class JnxVpnType(TextualConvention, Integer32):
    description = 'Type of the VPN. The following types have been defined: bgpIpVpn: RFC 4364 VPNs; bgpL2Vpn: BGP-based Layer 2 VPNs (see draft-kompella-ppvpn-l2vpn); bgpVpls: BGP-based VPLS (see draft-kompella-ppvnp-vpls); l2Circuit: LDP-based point-to-point Layer 2 circuits (see RFC 4906); ldpVpls: LDP-based VPLS (see draft-lasserre-vkompella-ppvpn-vpls); opticalVpn: BGP-based Optical (port based) VPNs (see draft-ouldbrahim-bgpgmpls-ovpn); vpOxc: Virtual Private Optical Cross-Connect (see draft-ouldbrahim-ppvpn-vpoxc); ccc: proprietary Layer 2 circuit; bgpAtmVpn: ATM over MPLS (draft to be published).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("other", 1), ("bgpIpVpn", 2), ("bgpL2Vpn", 3), ("bgpVpls", 4), ("l2Circuit", 5), ("ldpVpls", 6), ("opticalVpn", 7), ("vpOxc", 8), ("ccc", 9), ("bgpAtmVpn", 10))

class JnxVpnIdentifierType(TextualConvention, Integer32):
    description = 'Type of the VPN Identifier. This includes Route Distinguishers, Route Targets, and VC IDs. none(0) This value MUST be used if the value of the corresponding JnxVpnIdentifier object is a zero-length string. other(1) A VPN identifier that does not match one of the types defined in this MIB. routeDistinguisher(2) A VPN identifier as defined by the JnxVpnRouteDistinguisher textual convention. routeDistinguisher0(3) A VPN identifier as defined by the JnxVpnRouteDistinguisher0 textual convention. routeDistinguisher1(4) A VPN identifier as defined by the JnxVpnRouteDistinguisher1 textual convention. routeDistinguisher2(5) A VPN identifier as defined by the JnxVpnRouteDistinguisher2 textual convention. routeTarget(6) A VPN identifier as defined by the JnxVpnRouteTarget textual convention. routeTarget0(7) A VPN identifier as defined by the JnxVpnRouteTarget0 textual convention. routeTarget1(8) A VPN identifier as defined by the JnxVpnRouteTarget1 textual convention. routeTarget2(9) A VPN identifier as defined by the JnxVpnRouteTarget2 textual convention. vcId(10) A VPN identifier as defined by the JnxVpnVCIdentifier textual convention. localSwitch(11) A VPN identifier as defined by the JnxVpnLocalSwitchIdentifier textual convention.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("none", 0), ("other", 1), ("routeDistinguisher", 2), ("routeDistinguisher0", 3), ("routeDistinguisher1", 4), ("routeDistinguisher2", 5), ("routeTarget", 6), ("routeTarget0", 7), ("routeTarget1", 8), ("routeTarget2", 9), ("vcId", 10), ("localSwitch", 11))

class JnxVpnIdentifier(TextualConvention, OctetString):
    description = 'Syntax for a VPN identifier. A VPN Identifier is always interpreted within the context of an jnxVpnIdentifierType value. The jnxVpnIdentifierType object which defines the context must be registered immediately before the object which uses the VpnIdentifier textual convention. In other words, the object identifiers for the jnxVpnIdentifierType object and the jnxVpnIdentifier object MUST have the same length and the last sub-identifier of the jnxVpnIdentifierType object MUST be 1 less than the last sub-identifier of the jnxVpnIdentifier object.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class JnxVpnRouteDistinguisher(TextualConvention, OctetString):
    reference = 'BGP/MPLS VPNs, RFC 4364.'
    description = 'Represents a Generic Route Distinguisher.'
    status = 'current'
    displayHint = '1x:1x:1x:1x:1x:1x:1x:1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JnxVpnRouteDistinguisher0(TextualConvention, OctetString):
    reference = 'BGP/MPLS VPNs, RFC 4364.'
    description = 'Represents a Type 0 Route Distinguisher.'
    status = 'current'
    displayHint = '2x-2d:4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JnxVpnRouteDistinguisher1(TextualConvention, OctetString):
    reference = 'BGP/MPLS VPNs, RFC 4364.'
    description = 'Represents a Type 1 Route Distinguisher.'
    status = 'current'
    displayHint = '2x-1d.1d.1d.1d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JnxVpnRouteDistinguisher2(TextualConvention, OctetString):
    reference = 'BGP/MPLS VPNs, RFC 4364.'
    description = 'Represents a Type 2 Route Distinguisher.'
    status = 'current'
    displayHint = '2x-4d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JnxVpnRouteTarget(TextualConvention, OctetString):
    reference = 'BGP Extended Communities Attribute, RFC 4360.'
    description = 'Represents a Generic Route Target.'
    status = 'current'
    displayHint = '1x:1x:1x:1x:1x:1x:1x:1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JnxVpnRouteTarget0(TextualConvention, OctetString):
    reference = 'BGP Extended Communities Attribute, RFC 4360.'
    description = 'Represents a Type 00 Route Target.'
    status = 'current'
    displayHint = '2x-4d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JnxVpnRouteTarget1(TextualConvention, OctetString):
    reference = 'BGP Extended Communities Attribute, RFC 4360.'
    description = 'Represents a Type 01 Route Target.'
    status = 'current'
    displayHint = '2x-1d.1d.1d.1d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JnxVpnRouteTarget2(TextualConvention, OctetString):
    reference = 'BGP Extended Communities Attribute, RFC 4360.'
    description = 'Represents a Type 02 Route Target.'
    status = 'current'
    displayHint = '2x-2d:4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JnxVpnVCIdentifier(TextualConvention, OctetString):
    description = 'Represents a PE ID, VC ID pair. The PE ID is the Router ID of the remote PE. The VC ID follows the description given in draft-martini-l2circuit-trans.'
    status = 'current'
    displayHint = '1d.1d.1d.1d:4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JnxVpnMultiplexor(TextualConvention, Unsigned32):
    description = 'Syntax for a VPN multiplexor/demultiplexor within a Pseudo-Wire Tunnel.'
    status = 'current'

class JnxVpnLocalSwitchIdentifier(TextualConvention, OctetString):
    description = 'The string representing the name of two interfaces that are being locally switched separated by a colon.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 256)

jnxVpnInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1))
jnxVpnConfiguredVpns = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnConfiguredVpns.setStatus('current')
if mibBuilder.loadTexts: jnxVpnConfiguredVpns.setDescription('Number of configured VPNs.')
jnxVpnActiveVpns = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnActiveVpns.setStatus('current')
if mibBuilder.loadTexts: jnxVpnActiveVpns.setDescription('Number of active VPNs.')
jnxVpnNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnNextIfIndex.setStatus('current')
if mibBuilder.loadTexts: jnxVpnNextIfIndex.setDescription('Next free VPN interface index.')
jnxVpnNextPwIndex = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnNextPwIndex.setStatus('current')
if mibBuilder.loadTexts: jnxVpnNextPwIndex.setDescription('Next free Pseudo-Wire index.')
jnxVpnNextRTIndex = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnNextRTIndex.setStatus('current')
if mibBuilder.loadTexts: jnxVpnNextRTIndex.setDescription('Next free Route Target index.')
jnxVpnTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2), )
if mibBuilder.loadTexts: jnxVpnTable.setStatus('current')
if mibBuilder.loadTexts: jnxVpnTable.setDescription('Table of Configured VPNs.')
jnxVpnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnName"))
if mibBuilder.loadTexts: jnxVpnEntry.setStatus('current')
if mibBuilder.loadTexts: jnxVpnEntry.setDescription('Entry containing information about a particular VPN.')
jnxVpnType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 1), JnxVpnType())
if mibBuilder.loadTexts: jnxVpnType.setStatus('current')
if mibBuilder.loadTexts: jnxVpnType.setDescription('Type of the VPN.')
jnxVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 2), JnxVpnName())
if mibBuilder.loadTexts: jnxVpnName.setStatus('current')
if mibBuilder.loadTexts: jnxVpnName.setDescription("Name of the VPN. This should ideally be unique in the Service Provider's domain; at a minimum, it MUST be unique per Provider Edge router.")
jnxVpnRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 3), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRowStatus.setStatus('current')
if mibBuilder.loadTexts: jnxVpnRowStatus.setDescription('This variable is used to create, modify, and/or delete a row in this table.')
jnxVpnStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnStorageType.setStatus('current')
if mibBuilder.loadTexts: jnxVpnStorageType.setDescription('This variable indicates the storage type for this object.')
jnxVpnDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnDescription.setStatus('current')
if mibBuilder.loadTexts: jnxVpnDescription.setDescription('String describing the VPN.')
jnxVpnIdentifierType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 6), JnxVpnIdentifierType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIdentifierType.setStatus('current')
if mibBuilder.loadTexts: jnxVpnIdentifierType.setDescription('Type of the following JnxVpnIdentifier.')
jnxVpnIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 7), JnxVpnIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIdentifier.setStatus('current')
if mibBuilder.loadTexts: jnxVpnIdentifier.setDescription('In the case of BGP VPNs, this is the Route Distinguisher for the VPN. In the case of LDP VPNs, this is the VC ID for the circuit. A value of all zeros indicates that the neither a Route Distinguisher nor a VC ID is configured for the VPN.')
jnxVpnConfiguredSites = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnConfiguredSites.setStatus('current')
if mibBuilder.loadTexts: jnxVpnConfiguredSites.setDescription('The number of sites configured in the VPN. Must be set to zero if not applicable.')
jnxVpnActiveSites = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnActiveSites.setStatus('current')
if mibBuilder.loadTexts: jnxVpnActiveSites.setDescription('The number of active sites (i.e., sites whose state is active) in the VPN.')
jnxVpnLocalAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnLocalAddresses.setStatus('current')
if mibBuilder.loadTexts: jnxVpnLocalAddresses.setDescription('The number of addresses learned from the CE device.')
jnxVpnTotalAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnTotalAddresses.setStatus('current')
if mibBuilder.loadTexts: jnxVpnTotalAddresses.setDescription('The total number of addresses in the VPN RIB.')
jnxVpnAge = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnAge.setStatus('current')
if mibBuilder.loadTexts: jnxVpnAge.setDescription('The age (i.e., time from creation till now) of this VPN in hundredths of a second.')
jnxVpnIfTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3), )
if mibBuilder.loadTexts: jnxVpnIfTable.setStatus('current')
if mibBuilder.loadTexts: jnxVpnIfTable.setDescription('Table of VPN Interfaces.')
jnxVpnIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnIfVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnIfVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnIfIndex"))
if mibBuilder.loadTexts: jnxVpnIfEntry.setStatus('current')
if mibBuilder.loadTexts: jnxVpnIfEntry.setDescription('Entry containing information about a particular VPN interface.')
jnxVpnIfVpnType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 1), JnxVpnType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxVpnIfVpnType.setStatus('current')
if mibBuilder.loadTexts: jnxVpnIfVpnType.setDescription('Type of the VPN to which this interface belongs.')
jnxVpnIfVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 2), JnxVpnName()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxVpnIfVpnName.setStatus('current')
if mibBuilder.loadTexts: jnxVpnIfVpnName.setDescription('Name of the VPN to which this interface belongs.')
jnxVpnIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxVpnIfIndex.setStatus('current')
if mibBuilder.loadTexts: jnxVpnIfIndex.setDescription('The index of this interface in the VPN. Each interface in the VPN is given a unique index. The RowStatus says whether a given interface (i.e., a row in this table) is valid or not. Note: this index MUST NOT be zero.')
jnxVpnIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfRowStatus.setStatus('current')
if mibBuilder.loadTexts: jnxVpnIfRowStatus.setDescription('This variable is used to create, modify, and/or delete a row in this table.')
jnxVpnIfStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 5), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfStorageType.setStatus('current')
if mibBuilder.loadTexts: jnxVpnIfStorageType.setDescription('This variable indicates the storage type for this object.')
jnxVpnIfAssociatedPw = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfAssociatedPw.setStatus('current')
if mibBuilder.loadTexts: jnxVpnIfAssociatedPw.setDescription('Index of associated Pseudo-wire, if any, in which case the index MUST be non-zero. If none, then this index MUST be zero.')
jnxVpnIfProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 20, 21, 22, 23, 24, 25, 26, 129, 130))).clone(namedValues=NamedValues(("other", 0), ("frameRelay", 1), ("atmAal5", 2), ("atmCell", 3), ("ethernetVlan", 4), ("ethernet", 5), ("ciscoHdlc", 6), ("ppp", 7), ("cem", 8), ("atmVcc", 9), ("atmVpc", 10), ("vpls", 11), ("ipInterworking", 12), ("snapInterworking", 13), ("frameRelayPort", 15), ("satope1", 17), ("satopt1", 18), ("static", 20), ("rip", 21), ("ospf", 22), ("bgp", 23), ("satope3", 24), ("satopt3", 25), ("cesop", 26), ("atmTrunkNNI", 129), ("atmTrunkUNI", 130)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfProtocol.setStatus('current')
if mibBuilder.loadTexts: jnxVpnIfProtocol.setDescription('Protocol running over this VPN interface. The values up to 10 are taken from draft-martini-l2circuit-trans-mpls-08.txt; the value for vpls is taken from draft-lasserre-vkompella-ppvpn-vpls-01.txt. The values from 20-23 are used when the VPN is a Layer 3 VPN.')
jnxVpnIfInBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfInBandwidth.setStatus('current')
if mibBuilder.loadTexts: jnxVpnIfInBandwidth.setDescription('Maximum bandwidth that the CE connected over this VPN i/f can send to the PE, in Kilo (i.e., 1000) Bytes per second. A value of zero means there is no configured maximum.')
jnxVpnIfOutBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfOutBandwidth.setStatus('current')
if mibBuilder.loadTexts: jnxVpnIfOutBandwidth.setDescription('Maximum bandwidth that the PE can send to the CE over this VPN interface, in Kilo (i.e., 1000) Bytes per second. A value of zero means there is no configured maximum.')
jnxVpnIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 0), ("noLocalInterface", 1), ("disabled", 2), ("encapsulationMismatch", 3), ("down", 4), ("up", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfStatus.setStatus('current')
if mibBuilder.loadTexts: jnxVpnIfStatus.setDescription('Status of this interface.')
jnxVpnPwTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4), )
if mibBuilder.loadTexts: jnxVpnPwTable.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwTable.setDescription('Table of Pseudo-Wire Connections.')
jnxVpnPwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"))
if mibBuilder.loadTexts: jnxVpnPwEntry.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwEntry.setDescription('Entry containing information about a particular VPN.')
jnxVpnPwVpnType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 1), JnxVpnType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxVpnPwVpnType.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwVpnType.setDescription('The type of the VPN to which this Pseudo-Wire belongs.')
jnxVpnPwVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 2), JnxVpnName()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxVpnPwVpnName.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwVpnName.setDescription('The name of the VPN to which this Pseudo-Wire belongs.')
jnxVpnPwIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxVpnPwIndex.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwIndex.setDescription('The index of this Pseudo-Wire in the VPN. Each Pseudo Wire in the VPN is given a unique index. The RowStatus says whether a given Pseudo Wire (i.e., a row in this table) is valid or not. Note: this index MUST NOT be zero.')
jnxVpnPwRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwRowStatus.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwRowStatus.setDescription('This variable is used to create, modify, and/or delete a row in this table.')
jnxVpnPwStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 5), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwStorageType.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwStorageType.setDescription('This variable indicates the storage type for this object.')
jnxVpnPwAssociatedInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwAssociatedInterface.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwAssociatedInterface.setDescription('The VPN index of the interface associated with this Pseudo Wire, if any. If there is no interface associated with this Pseudo Wire, a value of zero is to be returned.')
jnxVpnPwLocalSiteId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwLocalSiteId.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwLocalSiteId.setDescription('The local site identifier for this Pseudo-Wire. If there is no local site identifier, a value of zero is to be returned.')
jnxVpnPwRemoteSiteId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwRemoteSiteId.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwRemoteSiteId.setDescription('The remote site (i.e., the site at the other end of this Pseudo-Wire) identifier. If there is no remote site identifier, a value of zero is to be returned.')
jnxVpnRemotePeIdAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 9), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRemotePeIdAddrType.setStatus('current')
if mibBuilder.loadTexts: jnxVpnRemotePeIdAddrType.setDescription('The type of address assigned to the remote PE.')
jnxVpnRemotePeIdAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 10), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRemotePeIdAddress.setStatus('current')
if mibBuilder.loadTexts: jnxVpnRemotePeIdAddress.setDescription('The address of the remote PE, i.e., the router at the other end of the Pseudo-Wire.')
jnxVpnPwTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("static", 1), ("gre", 2), ("l2tpv3", 3), ("ipSec", 4), ("ldp", 5), ("rsvpTe", 6), ("crLdp", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwTunnelType.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwTunnelType.setDescription('The type of the tunnel over which the Pseudo-Wire is carried. If several Pseudo-Wires can be carried in one tunnel, each Pseudo-Wire is identified by the multiplexor/ demultiplexor within this tunnel.')
jnxVpnPwTunnelName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwTunnelName.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwTunnelName.setDescription('The name of the Tunnel over which this Pseudo-Wire is carried, if any.')
jnxVpnPwReceiveDemux = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 13), JnxVpnMultiplexor()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwReceiveDemux.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwReceiveDemux.setDescription('The value of the demultiplexor that identifies received packets as belonging to this Pseudo-Wire, if any.')
jnxVpnPwTransmitDemux = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 14), JnxVpnMultiplexor()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwTransmitDemux.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwTransmitDemux.setDescription('The value of the demultiplexor that identifies transmitted packets as belonging to this Pseudo-Wire, if any.')
jnxVpnPwStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("down", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwStatus.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwStatus.setDescription('Status of the Pseudo-Wire.')
jnxVpnPwTunnelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("down", 1), ("testing", 2), ("up", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwTunnelStatus.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwTunnelStatus.setDescription('Status of the PE-to-PE tunnel over which the Pseudo- Wire is carried.')
jnxVpnPwRemoteSiteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("outOfRange", 1), ("down", 2), ("up", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwRemoteSiteStatus.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwRemoteSiteStatus.setDescription('Status of the interface at the remote end of the Pseudo-Wire.')
jnxVpnPwTimeUp = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 18), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwTimeUp.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwTimeUp.setDescription('The total time in hundredths of a second that this Pseudo-Wire has been operational.')
jnxVpnPwTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwTransitions.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwTransitions.setDescription('The number of state transitions (up -> down and down -> up) this Tunnel has undergone.')
jnxVpnPwLastTransition = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 20), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwLastTransition.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwLastTransition.setDescription('The time in hundredths of a second since the last transition occurred on this Tunnel.')
jnxVpnPwPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwPacketsSent.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwPacketsSent.setDescription('The number of packets that have been sent over this Pseudo-Wire.')
jnxVpnPwOctetsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwOctetsSent.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwOctetsSent.setDescription('The number of octets that have been sent over this Pseudo-Wire.')
jnxVpnPwPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwPacketsReceived.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwPacketsReceived.setDescription('The number of packets that have been received over this Pseudo-Wire.')
jnxVpnPwOctetsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwOctetsReceived.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwOctetsReceived.setDescription('The number of octets that have been received over this Pseudo-Wire.')
jnxVpnPwLRPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwLRPacketsSent.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwLRPacketsSent.setDescription('The number of packets that have been sent over this Pseudo-Wire.')
jnxVpnPwLROctetsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwLROctetsSent.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwLROctetsSent.setDescription('The number of octets that have been sent over this Pseudo-Wire.')
jnxVpnPwLRPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwLRPacketsReceived.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwLRPacketsReceived.setDescription('The number of packets that have been received over this Pseudo-Wire.')
jnxVpnPwLROctetsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwLROctetsReceived.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwLROctetsReceived.setDescription('The number of octets that have been received over this Pseudo-Wire.')
jnxVpnRTTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5), )
if mibBuilder.loadTexts: jnxVpnRTTable.setStatus('current')
if mibBuilder.loadTexts: jnxVpnRTTable.setDescription('Table of Route Targets for a VPN.')
jnxVpnRTEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnRTVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnRTVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnRTIndex"))
if mibBuilder.loadTexts: jnxVpnRTEntry.setStatus('current')
if mibBuilder.loadTexts: jnxVpnRTEntry.setDescription('Entry containing information about a particular VPN.')
jnxVpnRTVpnType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 1), JnxVpnType())
if mibBuilder.loadTexts: jnxVpnRTVpnType.setStatus('current')
if mibBuilder.loadTexts: jnxVpnRTVpnType.setDescription('The type of the VPN for which this list of Route Targets are defined.')
jnxVpnRTVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 2), JnxVpnName())
if mibBuilder.loadTexts: jnxVpnRTVpnName.setStatus('current')
if mibBuilder.loadTexts: jnxVpnRTVpnName.setDescription('The name of the VPN for which this list of Route Targets are defined.')
jnxVpnRTIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 3), Unsigned32())
if mibBuilder.loadTexts: jnxVpnRTIndex.setStatus('current')
if mibBuilder.loadTexts: jnxVpnRTIndex.setDescription('The index within the list of Route Targets that specifies individual Route Targets that define the VPN. Note: this index MUST NOT be zero.')
jnxVpnRTRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRTRowStatus.setStatus('current')
if mibBuilder.loadTexts: jnxVpnRTRowStatus.setDescription('This variable is used to create, modify, and/or delete a row in this table.')
jnxVpnRTStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 5), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRTStorageType.setStatus('current')
if mibBuilder.loadTexts: jnxVpnRTStorageType.setDescription('This variable indicates the storage type for this object.')
jnxVpnRTType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 6), JnxVpnIdentifierType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRTType.setStatus('current')
if mibBuilder.loadTexts: jnxVpnRTType.setDescription("Type of the following Route Target. This can one of 'routeTarget[012]' or 'none'.")
jnxVpnRT = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 7), JnxVpnIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRT.setStatus('current')
if mibBuilder.loadTexts: jnxVpnRT.setDescription("Route Target for the VPN. If the jnxVpnRTType is 'none', this value should be all zeros.")
jnxVpnRTFunction = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("import", 1), ("export", 2), ("both", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRTFunction.setStatus('current')
if mibBuilder.loadTexts: jnxVpnRTFunction.setDescription('The route target export distribution type.')
jnxVpnIfUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 26, 0, 1)).setObjects(("JUNIPER-VPN-MIB", "jnxVpnIfVpnType"), ("JUNIPER-VPN-MIB", "jnxVpnIfVpnName"), ("JUNIPER-VPN-MIB", "jnxVpnIfIndex"))
if mibBuilder.loadTexts: jnxVpnIfUp.setStatus('current')
if mibBuilder.loadTexts: jnxVpnIfUp.setDescription("A jnxVpnIfUp notification is generated when the interface with index jnxVpnIfIndex belonging to the VPN named jnxVpnIfVpnName of type jnxVpnIfVpnType transitions out of the 'down' state.")
jnxVpnIfDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 26, 0, 2)).setObjects(("JUNIPER-VPN-MIB", "jnxVpnIfVpnType"), ("JUNIPER-VPN-MIB", "jnxVpnIfVpnName"), ("JUNIPER-VPN-MIB", "jnxVpnIfIndex"))
if mibBuilder.loadTexts: jnxVpnIfDown.setStatus('current')
if mibBuilder.loadTexts: jnxVpnIfDown.setDescription("A jnxVpnIfDown notification is generated when the interface with index jnxVpnIfIndex belonging to the VPN named jnxVpnIfVpnName of type jnxVpnIfVpnType transitions to the 'down' state.")
jnxVpnPwUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 26, 0, 3)).setObjects(("JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), ("JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), ("JUNIPER-VPN-MIB", "jnxVpnPwIndex"))
if mibBuilder.loadTexts: jnxVpnPwUp.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwUp.setDescription("A jnxVpnPwUp notification is generated when the Pseudo-Wire with index jnxVpnPwIndex belonging to the VPN named jnxVpnPwVpnName of type jnxVpnPwVpnType transitions out of the 'down' state.")
jnxVpnPwDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 26, 0, 4)).setObjects(("JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), ("JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), ("JUNIPER-VPN-MIB", "jnxVpnPwIndex"))
if mibBuilder.loadTexts: jnxVpnPwDown.setStatus('current')
if mibBuilder.loadTexts: jnxVpnPwDown.setDescription("A jnxVpnPwDown notification is generated when the Pseudo-Wire with index jnxVpnPwIndex belonging to the VPN named jnxVpnPwVpnName of type jnxVpnPwVpnType transitions to the 'down' state.")
mibBuilder.exportSymbols("JUNIPER-VPN-MIB", jnxVpnTable=jnxVpnTable, JnxVpnRouteTarget0=JnxVpnRouteTarget0, JnxVpnRouteTarget2=JnxVpnRouteTarget2, jnxVpnPwPacketsSent=jnxVpnPwPacketsSent, JnxVpnLocalSwitchIdentifier=JnxVpnLocalSwitchIdentifier, jnxVpnPwRemoteSiteStatus=jnxVpnPwRemoteSiteStatus, JnxVpnRouteDistinguisher0=JnxVpnRouteDistinguisher0, jnxVpnIfAssociatedPw=jnxVpnIfAssociatedPw, jnxVpnPwVpnType=jnxVpnPwVpnType, JnxVpnRouteTarget1=JnxVpnRouteTarget1, jnxVpnPwLastTransition=jnxVpnPwLastTransition, jnxVpnPwTunnelName=jnxVpnPwTunnelName, jnxVpnActiveVpns=jnxVpnActiveVpns, jnxVpnRTTable=jnxVpnRTTable, jnxVpnIfIndex=jnxVpnIfIndex, jnxVpnIfStatus=jnxVpnIfStatus, jnxVpnIfOutBandwidth=jnxVpnIfOutBandwidth, jnxVpnIfInBandwidth=jnxVpnIfInBandwidth, jnxVpnStorageType=jnxVpnStorageType, jnxVpnIfVpnType=jnxVpnIfVpnType, jnxVpnPwRowStatus=jnxVpnPwRowStatus, jnxVpnPwPacketsReceived=jnxVpnPwPacketsReceived, jnxVpnPwTransitions=jnxVpnPwTransitions, jnxVpnRTRowStatus=jnxVpnRTRowStatus, jnxVpnNextIfIndex=jnxVpnNextIfIndex, jnxVpnIfRowStatus=jnxVpnIfRowStatus, jnxVpnPwStorageType=jnxVpnPwStorageType, JnxVpnIdentifier=JnxVpnIdentifier, jnxVpnLocalAddresses=jnxVpnLocalAddresses, jnxVpnIfUp=jnxVpnIfUp, jnxVpnIfDown=jnxVpnIfDown, jnxVpnMibObjects=jnxVpnMibObjects, jnxVpnPwLocalSiteId=jnxVpnPwLocalSiteId, JnxVpnIdentifierType=JnxVpnIdentifierType, jnxVpnType=jnxVpnType, jnxVpnPwVpnName=jnxVpnPwVpnName, jnxVpnRTVpnName=jnxVpnRTVpnName, JnxVpnRouteDistinguisher2=JnxVpnRouteDistinguisher2, jnxVpnPwTunnelStatus=jnxVpnPwTunnelStatus, jnxVpnMIB=jnxVpnMIB, jnxVpnPwOctetsSent=jnxVpnPwOctetsSent, JnxVpnRouteTarget=JnxVpnRouteTarget, jnxVpnEntry=jnxVpnEntry, jnxVpnTotalAddresses=jnxVpnTotalAddresses, jnxVpnRTFunction=jnxVpnRTFunction, jnxVpnPwLRPacketsSent=jnxVpnPwLRPacketsSent, jnxVpnInfo=jnxVpnInfo, jnxVpnIfEntry=jnxVpnIfEntry, jnxVpnRemotePeIdAddress=jnxVpnRemotePeIdAddress, jnxVpnPwLRPacketsReceived=jnxVpnPwLRPacketsReceived, jnxVpnMIBNotifications=jnxVpnMIBNotifications, jnxVpnPwTunnelType=jnxVpnPwTunnelType, jnxVpnPwOctetsReceived=jnxVpnPwOctetsReceived, JnxVpnMultiplexor=JnxVpnMultiplexor, jnxVpnRTStorageType=jnxVpnRTStorageType, JnxVpnVCIdentifier=JnxVpnVCIdentifier, jnxVpnName=jnxVpnName, jnxVpnPwDown=jnxVpnPwDown, JnxVpnRouteDistinguisher1=JnxVpnRouteDistinguisher1, jnxVpnDescription=jnxVpnDescription, jnxVpnIdentifierType=jnxVpnIdentifierType, jnxVpnRemotePeIdAddrType=jnxVpnRemotePeIdAddrType, jnxVpnRTVpnType=jnxVpnRTVpnType, JnxVpnType=JnxVpnType, jnxVpnMIBConformance=jnxVpnMIBConformance, jnxVpnPwRemoteSiteId=jnxVpnPwRemoteSiteId, jnxVpnConfiguredVpns=jnxVpnConfiguredVpns, jnxVpnAge=jnxVpnAge, jnxVpnPwEntry=jnxVpnPwEntry, jnxVpnPwTimeUp=jnxVpnPwTimeUp, jnxVpnPwAssociatedInterface=jnxVpnPwAssociatedInterface, jnxVpnPwTable=jnxVpnPwTable, jnxVpnRTType=jnxVpnRTType, jnxVpnIfStorageType=jnxVpnIfStorageType, jnxVpnIfProtocol=jnxVpnIfProtocol, PYSNMP_MODULE_ID=jnxVpnMIB, jnxVpnNextRTIndex=jnxVpnNextRTIndex, jnxVpnRowStatus=jnxVpnRowStatus, JnxVpnRouteDistinguisher=JnxVpnRouteDistinguisher, jnxVpnPwIndex=jnxVpnPwIndex, jnxVpnNextPwIndex=jnxVpnNextPwIndex, jnxVpnConfiguredSites=jnxVpnConfiguredSites, JnxVpnName=JnxVpnName, jnxVpnRTEntry=jnxVpnRTEntry, jnxVpnPwReceiveDemux=jnxVpnPwReceiveDemux, jnxVpnPwStatus=jnxVpnPwStatus, jnxVpnRT=jnxVpnRT, jnxVpnPwLROctetsSent=jnxVpnPwLROctetsSent, jnxVpnPwUp=jnxVpnPwUp, jnxVpnRTIndex=jnxVpnRTIndex, jnxVpnIdentifier=jnxVpnIdentifier, jnxVpnIfTable=jnxVpnIfTable, jnxVpnIfVpnName=jnxVpnIfVpnName, jnxVpnPwTransmitDemux=jnxVpnPwTransmitDemux, jnxVpnPwLROctetsReceived=jnxVpnPwLROctetsReceived, jnxVpnActiveSites=jnxVpnActiveSites)
