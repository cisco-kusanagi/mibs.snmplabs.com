#
# PySNMP MIB module Unisphere-Data-Internet-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Internet-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:31:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ipCidrRouteType, ipCidrRouteMetric4, ipCidrRouteMetric2, ipForwardCidrRouteGroup, ipCidrRouteMetric5, ipCidrRouteIfIndex, ipCidrRouteInfo, ipCidrRouteNextHopAS, ipCidrRouteStatus, ipCidrRouteMetric3, ipCidrRouteMetric1 = mibBuilder.importSymbols("IP-FORWARD-MIB", "ipCidrRouteType", "ipCidrRouteMetric4", "ipCidrRouteMetric2", "ipForwardCidrRouteGroup", "ipCidrRouteMetric5", "ipCidrRouteIfIndex", "ipCidrRouteInfo", "ipCidrRouteNextHopAS", "ipCidrRouteStatus", "ipCidrRouteMetric3", "ipCidrRouteMetric1")
ipNetToMediaIfIndex, ipGroup, icmpGroup, ipNetToMediaNetAddress = mibBuilder.importSymbols("IP-MIB", "ipNetToMediaIfIndex", "ipGroup", "icmpGroup", "ipNetToMediaNetAddress")
ipRouteEntry, ipRouteMetric2, ipRouteDest, ipRouteAge, ipRouteMetric5, ipRouteIfIndex, ipRouteMask, ipRouteMetric3, ipRouteMetric1, ipRouteType, ipRouteMetric4, ipRouteNextHop = mibBuilder.importSymbols("RFC1213-MIB", "ipRouteEntry", "ipRouteMetric2", "ipRouteDest", "ipRouteAge", "ipRouteMetric5", "ipRouteIfIndex", "ipRouteMask", "ipRouteMetric3", "ipRouteMetric1", "ipRouteType", "ipRouteMetric4", "ipRouteNextHop")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Integer32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, Counter64, Bits, Unsigned32, IpAddress, ModuleIdentity, TimeTicks, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "Counter64", "Bits", "Unsigned32", "IpAddress", "ModuleIdentity", "TimeTicks", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tcpGroup, = mibBuilder.importSymbols("TCP-MIB", "tcpGroup")
udpGroup, = mibBuilder.importSymbols("UDP-MIB", "udpGroup")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdHostGroup, = mibBuilder.importSymbols("Unisphere-Data-HOST-MIB", "usdHostGroup")
usdIpAddressGroup, usdIpInterfaceGroup3, usdIpInterfaceGroup4, usdIpAddressGroup2, usdIpGlobalGroup, usdIpRouteGroup, usdIpInterfaceGroup2, usdIpInterfaceGroup = mibBuilder.importSymbols("Unisphere-Data-IP-MIB", "usdIpAddressGroup", "usdIpInterfaceGroup3", "usdIpInterfaceGroup4", "usdIpAddressGroup2", "usdIpGlobalGroup", "usdIpRouteGroup", "usdIpInterfaceGroup2", "usdIpInterfaceGroup")
usdInternetAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 21))
usdInternetAgent.setRevisions(('2002-04-03 14:04', '2002-03-26 21:46',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdInternetAgent.setRevisionsDescriptions(('Obsoleted the QoS related objects in the Unisphere-Data-IP-MIB.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdInternetAgent.setLastUpdated('200204031404Z')
if mibBuilder.loadTexts: usdInternetAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdInternetAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdInternetAgent.setDescription('The agent capabilities definitions for the basic layer 3 and 4 Internet component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdInternetAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 21, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInternetAgentV1 = usdInternetAgentV1.setProductRelease('Version 1 of the Internet component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Internet component was supported in the\n        Unisphere 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInternetAgentV1 = usdInternetAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdInternetAgentV1.setDescription('The MIBs supported by the SNMP agent for the Internet application in the Unisphere Routing Switch. These capabilities became obsolete when the IP global objects were added to the Unisphere-Data-IP-MIB.')
usdInternetAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 21, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInternetAgentV2 = usdInternetAgentV2.setProductRelease('Version 2 of the Internet component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Internet component was supported in the\n        Unisphere RX 3.0 and RX 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInternetAgentV2 = usdInternetAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdInternetAgentV2.setDescription('The MIBs supported by the SNMP agent for the Internet application in the Unisphere Routing Switch. These capabilities became obsolete when support was added for the RFC1213-MIB.ipRouteTable and the Unisphere-Data-IP-MIB.rsIpIfAssocTable.')
usdInternetAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 21, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInternetAgentV3 = usdInternetAgentV3.setProductRelease('Version 3 of the Internet component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Internet component was supported in the\n        Unisphere RX 3.2 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInternetAgentV3 = usdInternetAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: usdInternetAgentV3.setDescription('The MIBs supported by the SNMP agent for the Internet application in the Unisphere Routing Switch. These capabilities became obsolete when the QoS related objects in the Unisphere-Data-IP-MIB were obsoleted.')
usdInternetAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 21, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInternetAgentV4 = usdInternetAgentV4.setProductRelease('Version 4 of the Internet component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Internet component is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInternetAgentV4 = usdInternetAgentV4.setStatus('current')
if mibBuilder.loadTexts: usdInternetAgentV4.setDescription('The MIBs supported by the SNMP agent for the Internet application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-Internet-CONF", usdInternetAgent=usdInternetAgent, usdInternetAgentV1=usdInternetAgentV1, usdInternetAgentV2=usdInternetAgentV2, PYSNMP_MODULE_ID=usdInternetAgent, usdInternetAgentV4=usdInternetAgentV4, usdInternetAgentV3=usdInternetAgentV3)
