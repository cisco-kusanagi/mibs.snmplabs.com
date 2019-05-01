#
# PySNMP MIB module Unisphere-Data-IP-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-IP-Profile-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:31:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
TimeTicks, IpAddress, NotificationType, Counter32, Unsigned32, Gauge32, Bits, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "NotificationType", "Counter32", "Unsigned32", "Gauge32", "Bits", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "iso", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usdProfileAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usdProfileAgents")
usdIpProfileDeprecatedGroup, usdIpProfileIpMask, usdIpProfileDirectedBcastEnable, usdIpProfileSetMap, usdIpProfileGroup, usdIpProfileGroup1, usdIpProfileIpAddr, usdIpProfileSrcAddrValidEnable, usdIpProfileRouterName, usdIpProfileIcmpRedirectEnable, usdIpProfileAccessRoute, usdIpProfileMtu, usdIpProfileLoopback, usdIpProfileRowStatus, usdIpProfileGroup2 = mibBuilder.importSymbols("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileDeprecatedGroup", "usdIpProfileIpMask", "usdIpProfileDirectedBcastEnable", "usdIpProfileSetMap", "usdIpProfileGroup", "usdIpProfileGroup1", "usdIpProfileIpAddr", "usdIpProfileSrcAddrValidEnable", "usdIpProfileRouterName", "usdIpProfileIcmpRedirectEnable", "usdIpProfileAccessRoute", "usdIpProfileMtu", "usdIpProfileLoopback", "usdIpProfileRowStatus", "usdIpProfileGroup2")
usdIpProfileAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2))
usdIpProfileAgent.setRevisions(('2001-03-28 21:43',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdIpProfileAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdIpProfileAgent.setLastUpdated('200103282143Z')
if mibBuilder.loadTexts: usdIpProfileAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdIpProfileAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdIpProfileAgent.setDescription('The agent capabilities definitions for the IP Profile Manager component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdIpProfileAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpProfileAgentV1 = usdIpProfileAgentV1.setProductRelease('Version 1 of the IP Profile component of the Unisphere Routing Switch\n        SNMP agent.  This version of the IP Profile Manager component was\n        supported in the Unisphere RX 1.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpProfileAgentV1 = usdIpProfileAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdIpProfileAgentV1.setDescription('The MIB supported by the SNMP agent for the IP Profile Manager application in the Unisphere Routing Switch. These capabilities became obsolete when the profile loopback object changed.')
usdIpProfileAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpProfileAgentV2 = usdIpProfileAgentV2.setProductRelease('Version 2 of the IP Profile component of the Unisphere Routing Switch\n        SNMP agent.  This version of the IP Profile Manager component was\n        supported in the Unisphere RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpProfileAgentV2 = usdIpProfileAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdIpProfileAgentV2.setDescription('The MIB supported by the SNMP agent for the IP Profile Manager application in the Unisphere Routing Switch. These capabilities became obsolete when rsIpProfileRowStatus was deprecate and the rsIpProfileSetMap and rsIpProfileSrcAddrValidEnable objects were added.')
usdIpProfileAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpProfileAgentV3 = usdIpProfileAgentV3.setProductRelease('Version 3 of the IP Profile component of the Unisphere Routing Switch\n        SNMP agent.  This version of the IP Profile Manager component is\n        supported in the Unisphere RX 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpProfileAgentV3 = usdIpProfileAgentV3.setStatus('current')
if mibBuilder.loadTexts: usdIpProfileAgentV3.setDescription('The MIB supported by the SNMP agent for the IP Profile Manager application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-IP-Profile-CONF", usdIpProfileAgentV1=usdIpProfileAgentV1, usdIpProfileAgentV3=usdIpProfileAgentV3, usdIpProfileAgent=usdIpProfileAgent, usdIpProfileAgentV2=usdIpProfileAgentV2, PYSNMP_MODULE_ID=usdIpProfileAgent)
