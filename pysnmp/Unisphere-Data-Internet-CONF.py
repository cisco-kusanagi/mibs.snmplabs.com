#
# PySNMP MIB module Unisphere-Data-Internet-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Internet-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ipCidrRouteMetric3, ipCidrRouteNextHopAS, ipCidrRouteType, ipCidrRouteMetric2, ipCidrRouteMetric1, ipCidrRouteStatus, ipCidrRouteMetric4, ipCidrRouteMetric5, ipCidrRouteIfIndex, ipCidrRouteInfo, ipForwardCidrRouteGroup = mibBuilder.importSymbols("IP-FORWARD-MIB", "ipCidrRouteMetric3", "ipCidrRouteNextHopAS", "ipCidrRouteType", "ipCidrRouteMetric2", "ipCidrRouteMetric1", "ipCidrRouteStatus", "ipCidrRouteMetric4", "ipCidrRouteMetric5", "ipCidrRouteIfIndex", "ipCidrRouteInfo", "ipForwardCidrRouteGroup")
ipNetToMediaNetAddress, ipNetToMediaIfIndex, ipGroup, icmpGroup = mibBuilder.importSymbols("IP-MIB", "ipNetToMediaNetAddress", "ipNetToMediaIfIndex", "ipGroup", "icmpGroup")
ipRouteMetric5, ipRouteMetric3, ipRouteEntry, ipRouteNextHop, ipRouteType, ipRouteDest, ipRouteMetric4, ipRouteAge, ipRouteMask, ipRouteIfIndex, ipRouteMetric1, ipRouteMetric2 = mibBuilder.importSymbols("RFC1213-MIB", "ipRouteMetric5", "ipRouteMetric3", "ipRouteEntry", "ipRouteNextHop", "ipRouteType", "ipRouteDest", "ipRouteMetric4", "ipRouteAge", "ipRouteMask", "ipRouteIfIndex", "ipRouteMetric1", "ipRouteMetric2")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter32, Gauge32, Unsigned32, Counter64, NotificationType, MibIdentifier, Bits, ModuleIdentity, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "Gauge32", "Unsigned32", "Counter64", "NotificationType", "MibIdentifier", "Bits", "ModuleIdentity", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tcpGroup, = mibBuilder.importSymbols("TCP-MIB", "tcpGroup")
udpGroup, = mibBuilder.importSymbols("UDP-MIB", "udpGroup")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdHostGroup, = mibBuilder.importSymbols("Unisphere-Data-HOST-MIB", "usdHostGroup")
usdIpInterfaceGroup, usdIpRouteGroup, usdIpGlobalGroup, usdIpInterfaceGroup4, usdIpInterfaceGroup2, usdIpAddressGroup, usdIpInterfaceGroup3, usdIpAddressGroup2 = mibBuilder.importSymbols("Unisphere-Data-IP-MIB", "usdIpInterfaceGroup", "usdIpRouteGroup", "usdIpGlobalGroup", "usdIpInterfaceGroup4", "usdIpInterfaceGroup2", "usdIpAddressGroup", "usdIpInterfaceGroup3", "usdIpAddressGroup2")
usdInternetAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 21))
usdInternetAgent.setRevisions(('2002-04-03 14:04', '2002-03-26 21:46',))
if mibBuilder.loadTexts: usdInternetAgent.setLastUpdated('200204031404Z')
if mibBuilder.loadTexts: usdInternetAgent.setOrganization('Unisphere Networks, Inc.')
usdInternetAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 21, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInternetAgentV1 = usdInternetAgentV1.setProductRelease('Version 1 of the Internet component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Internet component was supported in the\n        Unisphere 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInternetAgentV1 = usdInternetAgentV1.setStatus('obsolete')
usdInternetAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 21, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInternetAgentV2 = usdInternetAgentV2.setProductRelease('Version 2 of the Internet component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Internet component was supported in the\n        Unisphere RX 3.0 and RX 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInternetAgentV2 = usdInternetAgentV2.setStatus('obsolete')
usdInternetAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 21, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInternetAgentV3 = usdInternetAgentV3.setProductRelease('Version 3 of the Internet component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Internet component was supported in the\n        Unisphere RX 3.2 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInternetAgentV3 = usdInternetAgentV3.setStatus('obsolete')
usdInternetAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 21, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInternetAgentV4 = usdInternetAgentV4.setProductRelease('Version 4 of the Internet component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Internet component is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInternetAgentV4 = usdInternetAgentV4.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-Internet-CONF", usdInternetAgentV2=usdInternetAgentV2, usdInternetAgentV3=usdInternetAgentV3, usdInternetAgent=usdInternetAgent, usdInternetAgentV4=usdInternetAgentV4, usdInternetAgentV1=usdInternetAgentV1, PYSNMP_MODULE_ID=usdInternetAgent)
