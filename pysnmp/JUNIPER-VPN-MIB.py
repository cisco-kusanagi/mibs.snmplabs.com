#
# PySNMP MIB module JUNIPER-VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-VPN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:49:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, iso, NotificationType, ModuleIdentity, MibIdentifier, ObjectIdentity, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, Bits, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "NotificationType", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "Bits", "Counter32", "Counter64")
StorageType, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "RowStatus", "TextualConvention", "DisplayString")
jnxVpnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 26))
jnxVpnMIB.setRevisions(('2010-10-15 00:00', '2010-08-27 00:00', '2002-04-21 21:28',))
if mibBuilder.loadTexts: jnxVpnMIB.setLastUpdated('201010150000Z')
if mibBuilder.loadTexts: jnxVpnMIB.setOrganization('IETF Provider Provisioned VPNs WG')
jnxVpnMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 26, 0))
jnxVpnMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1))
jnxVpnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 26, 2))
class JnxVpnName(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class JnxVpnType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("other", 1), ("bgpIpVpn", 2), ("bgpL2Vpn", 3), ("bgpVpls", 4), ("l2Circuit", 5), ("ldpVpls", 6), ("opticalVpn", 7), ("vpOxc", 8), ("ccc", 9), ("bgpAtmVpn", 10))

class JnxVpnIdentifierType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("none", 0), ("other", 1), ("routeDistinguisher", 2), ("routeDistinguisher0", 3), ("routeDistinguisher1", 4), ("routeDistinguisher2", 5), ("routeTarget", 6), ("routeTarget0", 7), ("routeTarget1", 8), ("routeTarget2", 9), ("vcId", 10), ("localSwitch", 11))

class JnxVpnIdentifier(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class JnxVpnRouteDistinguisher(TextualConvention, OctetString):
    reference = 'BGP/MPLS VPNs, RFC 4364.'
    status = 'current'
    displayHint = '1x:1x:1x:1x:1x:1x:1x:1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JnxVpnRouteDistinguisher0(TextualConvention, OctetString):
    reference = 'BGP/MPLS VPNs, RFC 4364.'
    status = 'current'
    displayHint = '2x-2d:4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JnxVpnRouteDistinguisher1(TextualConvention, OctetString):
    reference = 'BGP/MPLS VPNs, RFC 4364.'
    status = 'current'
    displayHint = '2x-1d.1d.1d.1d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JnxVpnRouteDistinguisher2(TextualConvention, OctetString):
    reference = 'BGP/MPLS VPNs, RFC 4364.'
    status = 'current'
    displayHint = '2x-4d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JnxVpnRouteTarget(TextualConvention, OctetString):
    reference = 'BGP Extended Communities Attribute, RFC 4360.'
    status = 'current'
    displayHint = '1x:1x:1x:1x:1x:1x:1x:1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JnxVpnRouteTarget0(TextualConvention, OctetString):
    reference = 'BGP Extended Communities Attribute, RFC 4360.'
    status = 'current'
    displayHint = '2x-4d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JnxVpnRouteTarget1(TextualConvention, OctetString):
    reference = 'BGP Extended Communities Attribute, RFC 4360.'
    status = 'current'
    displayHint = '2x-1d.1d.1d.1d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JnxVpnRouteTarget2(TextualConvention, OctetString):
    reference = 'BGP Extended Communities Attribute, RFC 4360.'
    status = 'current'
    displayHint = '2x-2d:4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JnxVpnVCIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d.1d:4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JnxVpnMultiplexor(TextualConvention, Unsigned32):
    status = 'current'

class JnxVpnLocalSwitchIdentifier(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 256)

jnxVpnInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1))
jnxVpnConfiguredVpns = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnConfiguredVpns.setStatus('current')
jnxVpnActiveVpns = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnActiveVpns.setStatus('current')
jnxVpnNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnNextIfIndex.setStatus('current')
jnxVpnNextPwIndex = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnNextPwIndex.setStatus('current')
jnxVpnNextRTIndex = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnNextRTIndex.setStatus('current')
jnxVpnTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2), )
if mibBuilder.loadTexts: jnxVpnTable.setStatus('current')
jnxVpnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnName"))
if mibBuilder.loadTexts: jnxVpnEntry.setStatus('current')
jnxVpnType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 1), JnxVpnType())
if mibBuilder.loadTexts: jnxVpnType.setStatus('current')
jnxVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 2), JnxVpnName())
if mibBuilder.loadTexts: jnxVpnName.setStatus('current')
jnxVpnRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 3), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRowStatus.setStatus('current')
jnxVpnStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnStorageType.setStatus('current')
jnxVpnDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnDescription.setStatus('current')
jnxVpnIdentifierType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 6), JnxVpnIdentifierType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIdentifierType.setStatus('current')
jnxVpnIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 7), JnxVpnIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIdentifier.setStatus('current')
jnxVpnConfiguredSites = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnConfiguredSites.setStatus('current')
jnxVpnActiveSites = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnActiveSites.setStatus('current')
jnxVpnLocalAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnLocalAddresses.setStatus('current')
jnxVpnTotalAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnTotalAddresses.setStatus('current')
jnxVpnAge = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnAge.setStatus('current')
jnxVpnIfTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3), )
if mibBuilder.loadTexts: jnxVpnIfTable.setStatus('current')
jnxVpnIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnIfVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnIfVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnIfIndex"))
if mibBuilder.loadTexts: jnxVpnIfEntry.setStatus('current')
jnxVpnIfVpnType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 1), JnxVpnType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxVpnIfVpnType.setStatus('current')
jnxVpnIfVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 2), JnxVpnName()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxVpnIfVpnName.setStatus('current')
jnxVpnIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxVpnIfIndex.setStatus('current')
jnxVpnIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfRowStatus.setStatus('current')
jnxVpnIfStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 5), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfStorageType.setStatus('current')
jnxVpnIfAssociatedPw = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfAssociatedPw.setStatus('current')
jnxVpnIfProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 20, 21, 22, 23, 24, 25, 26, 129, 130))).clone(namedValues=NamedValues(("other", 0), ("frameRelay", 1), ("atmAal5", 2), ("atmCell", 3), ("ethernetVlan", 4), ("ethernet", 5), ("ciscoHdlc", 6), ("ppp", 7), ("cem", 8), ("atmVcc", 9), ("atmVpc", 10), ("vpls", 11), ("ipInterworking", 12), ("snapInterworking", 13), ("frameRelayPort", 15), ("satope1", 17), ("satopt1", 18), ("static", 20), ("rip", 21), ("ospf", 22), ("bgp", 23), ("satope3", 24), ("satopt3", 25), ("cesop", 26), ("atmTrunkNNI", 129), ("atmTrunkUNI", 130)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfProtocol.setStatus('current')
jnxVpnIfInBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfInBandwidth.setStatus('current')
jnxVpnIfOutBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfOutBandwidth.setStatus('current')
jnxVpnIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 0), ("noLocalInterface", 1), ("disabled", 2), ("encapsulationMismatch", 3), ("down", 4), ("up", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnIfStatus.setStatus('current')
jnxVpnPwTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4), )
if mibBuilder.loadTexts: jnxVpnPwTable.setStatus('current')
jnxVpnPwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"))
if mibBuilder.loadTexts: jnxVpnPwEntry.setStatus('current')
jnxVpnPwVpnType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 1), JnxVpnType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxVpnPwVpnType.setStatus('current')
jnxVpnPwVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 2), JnxVpnName()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxVpnPwVpnName.setStatus('current')
jnxVpnPwIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxVpnPwIndex.setStatus('current')
jnxVpnPwRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwRowStatus.setStatus('current')
jnxVpnPwStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 5), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwStorageType.setStatus('current')
jnxVpnPwAssociatedInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwAssociatedInterface.setStatus('current')
jnxVpnPwLocalSiteId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwLocalSiteId.setStatus('current')
jnxVpnPwRemoteSiteId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwRemoteSiteId.setStatus('current')
jnxVpnRemotePeIdAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 9), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRemotePeIdAddrType.setStatus('current')
jnxVpnRemotePeIdAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 10), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRemotePeIdAddress.setStatus('current')
jnxVpnPwTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("static", 1), ("gre", 2), ("l2tpv3", 3), ("ipSec", 4), ("ldp", 5), ("rsvpTe", 6), ("crLdp", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwTunnelType.setStatus('current')
jnxVpnPwTunnelName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwTunnelName.setStatus('current')
jnxVpnPwReceiveDemux = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 13), JnxVpnMultiplexor()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwReceiveDemux.setStatus('current')
jnxVpnPwTransmitDemux = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 14), JnxVpnMultiplexor()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwTransmitDemux.setStatus('current')
jnxVpnPwStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("down", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwStatus.setStatus('current')
jnxVpnPwTunnelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("down", 1), ("testing", 2), ("up", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwTunnelStatus.setStatus('current')
jnxVpnPwRemoteSiteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("outOfRange", 1), ("down", 2), ("up", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwRemoteSiteStatus.setStatus('current')
jnxVpnPwTimeUp = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 18), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwTimeUp.setStatus('current')
jnxVpnPwTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwTransitions.setStatus('current')
jnxVpnPwLastTransition = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 20), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwLastTransition.setStatus('current')
jnxVpnPwPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwPacketsSent.setStatus('current')
jnxVpnPwOctetsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwOctetsSent.setStatus('current')
jnxVpnPwPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwPacketsReceived.setStatus('current')
jnxVpnPwOctetsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwOctetsReceived.setStatus('current')
jnxVpnPwLRPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwLRPacketsSent.setStatus('current')
jnxVpnPwLROctetsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwLROctetsSent.setStatus('current')
jnxVpnPwLRPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwLRPacketsReceived.setStatus('current')
jnxVpnPwLROctetsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnPwLROctetsReceived.setStatus('current')
jnxVpnRTTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5), )
if mibBuilder.loadTexts: jnxVpnRTTable.setStatus('current')
jnxVpnRTEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnRTVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnRTVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnRTIndex"))
if mibBuilder.loadTexts: jnxVpnRTEntry.setStatus('current')
jnxVpnRTVpnType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 1), JnxVpnType())
if mibBuilder.loadTexts: jnxVpnRTVpnType.setStatus('current')
jnxVpnRTVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 2), JnxVpnName())
if mibBuilder.loadTexts: jnxVpnRTVpnName.setStatus('current')
jnxVpnRTIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 3), Unsigned32())
if mibBuilder.loadTexts: jnxVpnRTIndex.setStatus('current')
jnxVpnRTRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRTRowStatus.setStatus('current')
jnxVpnRTStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 5), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRTStorageType.setStatus('current')
jnxVpnRTType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 6), JnxVpnIdentifierType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRTType.setStatus('current')
jnxVpnRT = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 7), JnxVpnIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRT.setStatus('current')
jnxVpnRTFunction = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("import", 1), ("export", 2), ("both", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVpnRTFunction.setStatus('current')
jnxVpnIfUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 26, 0, 1)).setObjects(("JUNIPER-VPN-MIB", "jnxVpnIfVpnType"), ("JUNIPER-VPN-MIB", "jnxVpnIfVpnName"), ("JUNIPER-VPN-MIB", "jnxVpnIfIndex"))
if mibBuilder.loadTexts: jnxVpnIfUp.setStatus('current')
jnxVpnIfDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 26, 0, 2)).setObjects(("JUNIPER-VPN-MIB", "jnxVpnIfVpnType"), ("JUNIPER-VPN-MIB", "jnxVpnIfVpnName"), ("JUNIPER-VPN-MIB", "jnxVpnIfIndex"))
if mibBuilder.loadTexts: jnxVpnIfDown.setStatus('current')
jnxVpnPwUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 26, 0, 3)).setObjects(("JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), ("JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), ("JUNIPER-VPN-MIB", "jnxVpnPwIndex"))
if mibBuilder.loadTexts: jnxVpnPwUp.setStatus('current')
jnxVpnPwDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 26, 0, 4)).setObjects(("JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), ("JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), ("JUNIPER-VPN-MIB", "jnxVpnPwIndex"))
if mibBuilder.loadTexts: jnxVpnPwDown.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-VPN-MIB", jnxVpnAge=jnxVpnAge, jnxVpnTotalAddresses=jnxVpnTotalAddresses, jnxVpnPwUp=jnxVpnPwUp, jnxVpnPwTimeUp=jnxVpnPwTimeUp, jnxVpnPwTunnelName=jnxVpnPwTunnelName, JnxVpnRouteTarget2=JnxVpnRouteTarget2, jnxVpnRowStatus=jnxVpnRowStatus, PYSNMP_MODULE_ID=jnxVpnMIB, jnxVpnPwVpnName=jnxVpnPwVpnName, jnxVpnStorageType=jnxVpnStorageType, jnxVpnIfVpnType=jnxVpnIfVpnType, jnxVpnConfiguredVpns=jnxVpnConfiguredVpns, jnxVpnPwLRPacketsReceived=jnxVpnPwLRPacketsReceived, jnxVpnPwRemoteSiteStatus=jnxVpnPwRemoteSiteStatus, jnxVpnTable=jnxVpnTable, jnxVpnRTTable=jnxVpnRTTable, jnxVpnIfUp=jnxVpnIfUp, JnxVpnVCIdentifier=JnxVpnVCIdentifier, jnxVpnPwOctetsReceived=jnxVpnPwOctetsReceived, jnxVpnMIB=jnxVpnMIB, jnxVpnPwTunnelType=jnxVpnPwTunnelType, jnxVpnPwTunnelStatus=jnxVpnPwTunnelStatus, jnxVpnConfiguredSites=jnxVpnConfiguredSites, JnxVpnType=JnxVpnType, JnxVpnRouteTarget=JnxVpnRouteTarget, jnxVpnRTVpnName=jnxVpnRTVpnName, jnxVpnRemotePeIdAddrType=jnxVpnRemotePeIdAddrType, jnxVpnActiveSites=jnxVpnActiveSites, jnxVpnPwAssociatedInterface=jnxVpnPwAssociatedInterface, JnxVpnRouteDistinguisher1=JnxVpnRouteDistinguisher1, jnxVpnPwStorageType=jnxVpnPwStorageType, jnxVpnRTIndex=jnxVpnRTIndex, JnxVpnRouteDistinguisher2=JnxVpnRouteDistinguisher2, JnxVpnName=JnxVpnName, jnxVpnIfVpnName=jnxVpnIfVpnName, jnxVpnIfOutBandwidth=jnxVpnIfOutBandwidth, jnxVpnPwLROctetsReceived=jnxVpnPwLROctetsReceived, jnxVpnIfStatus=jnxVpnIfStatus, jnxVpnPwVpnType=jnxVpnPwVpnType, JnxVpnMultiplexor=JnxVpnMultiplexor, jnxVpnRTStorageType=jnxVpnRTStorageType, jnxVpnRTType=jnxVpnRTType, JnxVpnRouteTarget0=JnxVpnRouteTarget0, jnxVpnInfo=jnxVpnInfo, jnxVpnPwLastTransition=jnxVpnPwLastTransition, jnxVpnName=jnxVpnName, jnxVpnMibObjects=jnxVpnMibObjects, jnxVpnPwTransmitDemux=jnxVpnPwTransmitDemux, jnxVpnIfEntry=jnxVpnIfEntry, jnxVpnPwReceiveDemux=jnxVpnPwReceiveDemux, jnxVpnPwDown=jnxVpnPwDown, jnxVpnIfAssociatedPw=jnxVpnIfAssociatedPw, jnxVpnType=jnxVpnType, jnxVpnIfDown=jnxVpnIfDown, jnxVpnRTVpnType=jnxVpnRTVpnType, jnxVpnPwIndex=jnxVpnPwIndex, jnxVpnPwTransitions=jnxVpnPwTransitions, jnxVpnPwStatus=jnxVpnPwStatus, jnxVpnRTEntry=jnxVpnRTEntry, jnxVpnActiveVpns=jnxVpnActiveVpns, jnxVpnPwLocalSiteId=jnxVpnPwLocalSiteId, jnxVpnIfProtocol=jnxVpnIfProtocol, jnxVpnPwRemoteSiteId=jnxVpnPwRemoteSiteId, jnxVpnMIBNotifications=jnxVpnMIBNotifications, JnxVpnRouteDistinguisher=JnxVpnRouteDistinguisher, jnxVpnNextIfIndex=jnxVpnNextIfIndex, JnxVpnRouteDistinguisher0=JnxVpnRouteDistinguisher0, jnxVpnPwLRPacketsSent=jnxVpnPwLRPacketsSent, JnxVpnIdentifier=JnxVpnIdentifier, jnxVpnNextPwIndex=jnxVpnNextPwIndex, jnxVpnIdentifierType=jnxVpnIdentifierType, jnxVpnRTRowStatus=jnxVpnRTRowStatus, jnxVpnLocalAddresses=jnxVpnLocalAddresses, jnxVpnIdentifier=jnxVpnIdentifier, jnxVpnIfTable=jnxVpnIfTable, jnxVpnPwPacketsSent=jnxVpnPwPacketsSent, jnxVpnNextRTIndex=jnxVpnNextRTIndex, jnxVpnIfInBandwidth=jnxVpnIfInBandwidth, jnxVpnDescription=jnxVpnDescription, jnxVpnPwEntry=jnxVpnPwEntry, JnxVpnLocalSwitchIdentifier=JnxVpnLocalSwitchIdentifier, jnxVpnPwLROctetsSent=jnxVpnPwLROctetsSent, jnxVpnPwTable=jnxVpnPwTable, jnxVpnMIBConformance=jnxVpnMIBConformance, jnxVpnEntry=jnxVpnEntry, jnxVpnIfStorageType=jnxVpnIfStorageType, jnxVpnIfIndex=jnxVpnIfIndex, jnxVpnIfRowStatus=jnxVpnIfRowStatus, jnxVpnRT=jnxVpnRT, jnxVpnRTFunction=jnxVpnRTFunction, jnxVpnPwOctetsSent=jnxVpnPwOctetsSent, JnxVpnIdentifierType=JnxVpnIdentifierType, JnxVpnRouteTarget1=JnxVpnRouteTarget1, jnxVpnPwPacketsReceived=jnxVpnPwPacketsReceived, jnxVpnPwRowStatus=jnxVpnPwRowStatus, jnxVpnRemotePeIdAddress=jnxVpnRemotePeIdAddress)
