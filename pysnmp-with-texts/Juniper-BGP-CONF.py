#
# PySNMP MIB module Juniper-BGP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-BGP-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:01:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, Counter64, iso, Unsigned32, TimeTicks, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, NotificationType, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "Counter64", "iso", "Unsigned32", "TimeTicks", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "NotificationType", "ModuleIdentity", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniBgpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4))
juniBgpAgent.setRevisions(('2007-05-11 05:17', '2003-12-18 15:28', '2003-12-18 14:27', '2003-07-09 21:35', '2002-11-06 16:33', '2002-09-05 12:56', '2002-09-04 17:56', '2002-03-01 17:51', '2002-01-23 13:16', '2001-12-04 16:09', '2001-12-03 18:48',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniBgpAgent.setRevisionsDescriptions(('Juniper-BGP-MIB: Added support for BGP conditional advertisement', 'Juniper-BGP-MIB: Added support for route-map option in default-information originate and neighbor ... default-originate. Added support for IP profiles and IP service-profiles to be used by BGP when creating IP dynamic interfaces over MPLS tunnels. BGP4-V2-MIB-JUNIPER: Implemented an experimental version of the Internet draft BGP4 MIB extentions (version 2) based on draft-ietf-idr-bgp4-mibv2-03.txt.', "Juniper-BGP-MIB: Added support for send-label. Added support for carrier's carrier feature for BGP/MPLS VPN. Added support for reconvergence after loss of MPLS next-hop.", 'Juniper-BGP-MIB: Added support for maximum-paths eiBGP. Added support for bgpIpV6. Replaced VRF distance objects with address family distance objects. Changed default values for VRF maximum paths. Obsoleted storage heap size objects. Added support for leaked flag attribute of the BGP route.', 'Juniper-BGP-MIB: Replaced Unisphere names with Juniper names. Added support for neighbor site-of-origin and peer leniency.', 'Juniper-BGP-MIB: Added support for four-octet AS-numbers, dynamic capability negotiation, iBGP multipath, confederation peers filter-list, and peer and peer-group address family maximum prefix strict flags. Replaced Route MPLS label object with separate in and out objects. Deprecated support for two-octet AS-numbers. Obsoleted rsBgpEqualCostLimit.', 'BGP4-MIB: Added full support for RFC1657 and draft-ietf-idr-bgp4-mib-07. Juniper-BGP-MIB: Added support for BGP internal redistribute. Obsoleted juniBgpStorageInitialHistoryRoutePoolSize and juniBgpStorageMaxHistoryRoutePoolSize. Added the ability to unconfigure BGP attributes from the MIB.', 'Juniper-BGP-MIB: Added support for adding unicast BGP routes into a multicast view.', 'Juniper-BGP-MIB: Added support for peer and peer-group local-as.', 'Juniper-BGP-MIB: Replaced the BGP route congiguration group with new tables containing the original route destination as an additional index.', 'The initial release of this management information module. Juniper-BGP-MIB: Added support for BGP default IPv4 unicast.',))
if mibBuilder.loadTexts: juniBgpAgent.setLastUpdated('200705110517Z')
if mibBuilder.loadTexts: juniBgpAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniBgpAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniBgpAgent.setDescription('The agent capabilities definitions for the BGP component of the SNMP agent in the Juniper E-series family of products.')
juniBgpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV1 = juniBgpAgentV1.setProductRelease('Version 1 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 3.0 and 3.1 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV1 = juniBgpAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniBgpAgentV1.setDescription('The MIB supported by the SNMP agent for the BGP application in JUNOSe. These capabilities became obsolete when a new object was added to the general configuration group.')
juniBgpAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV2 = juniBgpAgentV2.setProductRelease('Version 2 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 3.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV2 = juniBgpAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniBgpAgentV2.setDescription('The MIB supported by the SNMP agent for the BGP application in JUNOSe. These capabilities became obsolete when the BGP route congiguration group was replaced with new tables containing the original route destination as an additional index.')
juniBgpAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV3 = juniBgpAgentV3.setProductRelease('Version 3 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 3.3 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV3 = juniBgpAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniBgpAgentV3.setDescription('The MIB supported by the SNMP agent for the BGP application in JUNOSe. These capabilities became obsolete when the peer and peer-group local-as support was added.')
juniBgpAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV4 = juniBgpAgentV4.setProductRelease('Version 4 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 3.4 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV4 = juniBgpAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniBgpAgentV4.setDescription('The MIB supported by the SNMP agent for the BGP application in JUNOSe. These capabilities became obsolete when support was added for adding unicast BGP routes into a multicast view.')
juniBgpAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV5 = juniBgpAgentV5.setProductRelease('Version 5 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 3.5 and subseguent 3.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV5 = juniBgpAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniBgpAgentV5.setDescription('The MIB supported by the SNMP agent for the BGP application in JUNOSe. These capabilities became obsolete when support was added for the standard BGP4-MIB and for BGP internal redistribute.')
juniBgpAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV6 = juniBgpAgentV6.setProductRelease('Version 6 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 4.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV6 = juniBgpAgentV6.setStatus('obsolete')
if mibBuilder.loadTexts: juniBgpAgentV6.setDescription('The MIBs supported by the SNMP agent for the BGP application in JUNOSe. These capabilities became obsolete when support was added to the Juniper-BGP-MIB for four-octet AS-numbers, dynamic capability negotiation, iBGP multipath and confederation peers filter-list.')
juniBgpAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV7 = juniBgpAgentV7.setProductRelease('Version 7 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 4.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV7 = juniBgpAgentV7.setStatus('obsolete')
if mibBuilder.loadTexts: juniBgpAgentV7.setDescription('The MIBs supported by the SNMP agent for the BGP application in JUNOSe. These capabilities became obsolete when support was added to the Juniper-BGP-MIB for neighbor site-of-origin and peer leniency.')
juniBgpAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV8 = juniBgpAgentV8.setProductRelease('Version 8 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV8 = juniBgpAgentV8.setStatus('obsolete')
if mibBuilder.loadTexts: juniBgpAgentV8.setDescription('The MIBs supported by the SNMP agent for the BGP application in JUNOSe. These capabilities became obsolete when support was added to the Juniper-BGP-MIB for several new features.')
juniBgpAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV9 = juniBgpAgentV9.setProductRelease('Version 9 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 5.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV9 = juniBgpAgentV9.setStatus('obsolete')
if mibBuilder.loadTexts: juniBgpAgentV9.setDescription("The MIBs supported by the SNMP agent for the BGP application in JUNOSe. These capabilities became obsolete when support was added to the Juniper-BGP-MIB for send-label, carrier's carrier feature for BGP/MPLS VPN and reconvergence after loss of MPLS next-hop.")
juniBgpAgentV10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV10 = juniBgpAgentV10.setProductRelease('Version 10 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV10 = juniBgpAgentV10.setStatus('obsolete')
if mibBuilder.loadTexts: juniBgpAgentV10.setDescription('The MIBs supported by the SNMP agent for the BGP application in JUNOSe. These capabilities became obsolete when support was added to the Juniper-BGP-MIB for route-map option in default-information originate and neighbor ... default-originate, and when support was added for the new dynamic capability negotiation draft.')
juniBgpAgentV11 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV11 = juniBgpAgentV11.setProductRelease('Version 11 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component is supported in JUNOSe 5.3 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV11 = juniBgpAgentV11.setStatus('obsolete')
if mibBuilder.loadTexts: juniBgpAgentV11.setDescription('The MIB supported by the SNMP agent for the BGP application in JUNOSe. These capabilities became obsolete when support was added to the Juniper-BGP-MIB for BGP conditional advertisement.')
juniBgpAgentV12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV12 = juniBgpAgentV12.setProductRelease('Version 12 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component is supported in JUNOSe 9.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV12 = juniBgpAgentV12.setStatus('current')
if mibBuilder.loadTexts: juniBgpAgentV12.setDescription('The MIB supported by the SNMP agent for the BGP application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-BGP-CONF", juniBgpAgentV9=juniBgpAgentV9, juniBgpAgentV2=juniBgpAgentV2, juniBgpAgentV10=juniBgpAgentV10, juniBgpAgentV3=juniBgpAgentV3, juniBgpAgentV1=juniBgpAgentV1, juniBgpAgentV6=juniBgpAgentV6, juniBgpAgentV8=juniBgpAgentV8, juniBgpAgent=juniBgpAgent, juniBgpAgentV7=juniBgpAgentV7, juniBgpAgentV11=juniBgpAgentV11, juniBgpAgentV12=juniBgpAgentV12, PYSNMP_MODULE_ID=juniBgpAgent, juniBgpAgentV5=juniBgpAgentV5, juniBgpAgentV4=juniBgpAgentV4)
