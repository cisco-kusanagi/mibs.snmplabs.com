#
# PySNMP MIB module Juniper-Agents (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Agents
# Produced by pysmi-0.3.4 at Wed May  1 14:01:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
juniAgentCapability, = mibBuilder.importSymbols("Juniper-UNI-SMI", "juniAgentCapability")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, iso, Integer32, Gauge32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, IpAddress, ObjectIdentity, Counter32, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Integer32", "Gauge32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "IpAddress", "ObjectIdentity", "Counter32", "Bits", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniAgents = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2))
juniAgents.setRevisions(('2008-01-07 11:12', '2006-10-18 14:36', '2006-07-22 07:26', '2006-03-29 18:03', '2006-01-01 00:00', '2005-06-30 18:03', '2004-06-23 17:41', '2004-06-08 15:39', '2003-10-03 18:35', '2003-05-08 17:44', '2003-05-02 18:18', '2003-04-29 14:14', '2003-04-23 13:56', '2002-01-24 15:23', '2001-04-13 17:16',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniAgents.setRevisionsDescriptions(('Added module OID for MPLS FTN MIB agent capabilities.', 'Added module OID for LDP MIB agent capabilities.', 'Added module OID for MobileIpv4 agent capabilities.', 'Added module OID for MPLS-TE MIB agent capabilities.', 'Added module OID for Dos Protection and Dos Protection Platform agent capabilities.', 'Added module OID for Packet Mirror agent capabilities.', 'Updated the comments for juniMplsAgent: added support for MPLS-LSR-STD-MIB.', 'Added module OIDs for the generic E-series system MIB, the RADIUS Proxy MIB and the RADIUS Initiated Request MIB agent capabilities. Obsoleted some objects in the enterprise MPLS MIB.', 'Added module OIDs for the Event Manager, IPsec Tunnel, Internet Key Exchange (IKE), and Tunnel Server Manager (TSM) MIB Agent capabilities.', 'Added module OIDs for the ATM 1483 Profile, IPv6 Profile, and DHCPv6 MIB agent capabilities.', 'Replaced Unisphere names with Juniper names. Added module OIDs for the bridge, bridging manager, L2TP dialout, and RADIUS Disconnect MIB agent capabilities.', 'Added module OIDs for the multicast router, notification logging and TACACS+ client MIB agent capabilities.', 'Added module OIDs for the QoS manager, MPLS, system clock and X.21/V.35 MIB agent capabilities. Obsoleted L2F MIB.', 'Added module OID for the VRRP MIB agent capabilities.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniAgents.setLastUpdated('200801071112Z')
if mibBuilder.loadTexts: juniAgents.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniAgents.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniAgents.setDescription('The agent capabilities definition identifiers for the Juniper Networks E-series products. This is the top-level object identifier registry for SNMP modules containing agent capabilities definitions.')
juniAaaServerAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1))
juniAccountingAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 2))
juniAtmAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3))
juniBgpAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4))
juniBridgedEthernetAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 5))
juniCliAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 6))
juniCopsAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 7))
juniDhcpAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8))
juniDnsAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 9))
juniDs1Agent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 10))
juniDs3Agent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11))
juniDvmrpAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 12))
juniEntityAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 13))
juniEthernetAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14))
juniFileTransferAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 15))
juniFractionalT1Agent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 16))
juniFrameRelayAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 17))
juniHdlcAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18))
juniIgmpAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 19))
juniInterfacesAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 20))
juniInternetAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 21))
juniIpPolicyAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22))
juniIsisAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 23))
juniL2tpAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24))
juniLocalAddressServerAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25))
juniLogAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 26))
juniNsLookupAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 27))
juniOspfAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 28))
juniPimAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 29))
juniPingAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 30))
juniPolicyManagerAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31))
juniPppAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32))
juniPppoeAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33))
juniProfileAgents = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34))
if mibBuilder.loadTexts: juniProfileAgents.setStatus('current')
if mibBuilder.loadTexts: juniProfileAgents.setDescription('The group of Agent Capabilities modules that are deal with profile management.')
juniProfileManagerAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1))
juniIpProfileAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2))
juniPppProfileAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3))
juniPppoeProfileAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4))
juniIpv6ProfileAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 5))
juniAtm1483ProfileAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 6))
juniHttpProfileAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 7))
juniRadiusClientAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35))
juniRipAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 36))
juniRouterAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37))
juniSlepAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 38))
juniSnmpAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39))
juniSonetAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40))
juniSscClientAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41))
juniSystemAgents = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42))
if mibBuilder.loadTexts: juniSystemAgents.setStatus('current')
if mibBuilder.loadTexts: juniSystemAgents.setDescription('The root object identifier under which are registered the platform- specific SNMP modules containing the AGENT-CAPABILITIES definitions for the system components of the Juniper E-series family of products.')
juniErxSystemAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1))
juniSystemAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 2))
juniTraceRouteAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 43))
juniAutoConfAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 44))
juniSubscriberAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 45))
juniSmdsAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 46))
juniIpTunnelAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 47))
juniCbfAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 48))
juniL2fAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 49))
juniQosManagerAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 50))
juniMplsAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51))
juniSysClockAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 52))
juniVrrpAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 53))
juniV35Agent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 54))
juniMRouterAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 55))
juniNotificationLogAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 56))
juniTacacsPlusClientAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 57))
juniL2tpDialoutAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 59))
juniBridgeAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 60))
juniBridgingMgrAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 61))
juniEventManagerAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 62))
juniRadiusDisconnectAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 63))
juniDhcpv6Agent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 64))
juniIpsecTunnelAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 65))
juniIkeAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 66))
juniTsmAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 67))
juniRadiusProxyAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 68))
juniHaRedundancyAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 69))
juniRadiusRequestAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 70))
juniLicenseMgrAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 71))
juniPacketMirrorAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 72))
juniVpnmibAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 73))
juniHttpAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 74))
juniBfdmibAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 75))
juniDosProtectionAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 76))
juniDosProtectionPlatformAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 77))
juniMplsteAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 78))
juniMplsLdpAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 79))
juniMobileIpv4HaAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 80))
juniFtnMgrAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 81))
mibBuilder.exportSymbols("Juniper-Agents", juniSmdsAgent=juniSmdsAgent, juniL2tpDialoutAgent=juniL2tpDialoutAgent, juniNotificationLogAgent=juniNotificationLogAgent, juniErxSystemAgent=juniErxSystemAgent, juniPppoeAgent=juniPppoeAgent, juniIsisAgent=juniIsisAgent, juniMplsLdpAgent=juniMplsLdpAgent, juniQosManagerAgent=juniQosManagerAgent, juniPingAgent=juniPingAgent, juniL2tpAgent=juniL2tpAgent, juniSnmpAgent=juniSnmpAgent, juniBridgedEthernetAgent=juniBridgedEthernetAgent, juniIpTunnelAgent=juniIpTunnelAgent, juniVpnmibAgent=juniVpnmibAgent, juniTsmAgent=juniTsmAgent, juniIpProfileAgent=juniIpProfileAgent, juniAutoConfAgent=juniAutoConfAgent, juniFileTransferAgent=juniFileTransferAgent, juniAtm1483ProfileAgent=juniAtm1483ProfileAgent, juniRadiusClientAgent=juniRadiusClientAgent, juniBridgeAgent=juniBridgeAgent, juniPolicyManagerAgent=juniPolicyManagerAgent, juniHaRedundancyAgent=juniHaRedundancyAgent, juniHttpAgent=juniHttpAgent, juniHttpProfileAgent=juniHttpProfileAgent, juniAaaServerAgent=juniAaaServerAgent, juniPppoeProfileAgent=juniPppoeProfileAgent, juniRadiusDisconnectAgent=juniRadiusDisconnectAgent, juniSlepAgent=juniSlepAgent, juniInterfacesAgent=juniInterfacesAgent, juniDnsAgent=juniDnsAgent, juniSysClockAgent=juniSysClockAgent, juniBfdmibAgent=juniBfdmibAgent, juniProfileManagerAgent=juniProfileManagerAgent, juniFtnMgrAgent=juniFtnMgrAgent, juniInternetAgent=juniInternetAgent, juniIkeAgent=juniIkeAgent, juniCopsAgent=juniCopsAgent, juniPimAgent=juniPimAgent, juniOspfAgent=juniOspfAgent, juniIgmpAgent=juniIgmpAgent, juniDosProtectionAgent=juniDosProtectionAgent, juniDosProtectionPlatformAgent=juniDosProtectionPlatformAgent, juniRadiusRequestAgent=juniRadiusRequestAgent, juniPacketMirrorAgent=juniPacketMirrorAgent, juniRipAgent=juniRipAgent, juniPppAgent=juniPppAgent, juniRouterAgent=juniRouterAgent, juniMplsteAgent=juniMplsteAgent, juniSystemAgent=juniSystemAgent, juniSubscriberAgent=juniSubscriberAgent, juniCliAgent=juniCliAgent, juniFractionalT1Agent=juniFractionalT1Agent, juniAgents=juniAgents, juniAtmAgent=juniAtmAgent, juniBgpAgent=juniBgpAgent, juniLogAgent=juniLogAgent, juniDs1Agent=juniDs1Agent, juniMplsAgent=juniMplsAgent, juniLicenseMgrAgent=juniLicenseMgrAgent, juniLocalAddressServerAgent=juniLocalAddressServerAgent, juniSonetAgent=juniSonetAgent, juniNsLookupAgent=juniNsLookupAgent, juniTacacsPlusClientAgent=juniTacacsPlusClientAgent, juniEthernetAgent=juniEthernetAgent, juniEntityAgent=juniEntityAgent, juniDs3Agent=juniDs3Agent, juniDhcpv6Agent=juniDhcpv6Agent, juniAccountingAgent=juniAccountingAgent, juniVrrpAgent=juniVrrpAgent, juniV35Agent=juniV35Agent, juniMobileIpv4HaAgent=juniMobileIpv4HaAgent, juniCbfAgent=juniCbfAgent, juniSscClientAgent=juniSscClientAgent, juniDvmrpAgent=juniDvmrpAgent, juniSystemAgents=juniSystemAgents, juniFrameRelayAgent=juniFrameRelayAgent, juniIpv6ProfileAgent=juniIpv6ProfileAgent, juniIpsecTunnelAgent=juniIpsecTunnelAgent, juniDhcpAgent=juniDhcpAgent, juniL2fAgent=juniL2fAgent, juniProfileAgents=juniProfileAgents, juniMRouterAgent=juniMRouterAgent, juniBridgingMgrAgent=juniBridgingMgrAgent, juniRadiusProxyAgent=juniRadiusProxyAgent, juniPppProfileAgent=juniPppProfileAgent, juniHdlcAgent=juniHdlcAgent, PYSNMP_MODULE_ID=juniAgents, juniEventManagerAgent=juniEventManagerAgent, juniIpPolicyAgent=juniIpPolicyAgent, juniTraceRouteAgent=juniTraceRouteAgent)
