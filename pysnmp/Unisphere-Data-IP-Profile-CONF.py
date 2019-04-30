#
# PySNMP MIB module Unisphere-Data-IP-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-IP-Profile-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, ModuleIdentity, MibIdentifier, Unsigned32, Gauge32, Counter32, TimeTicks, NotificationType, Integer32, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "ModuleIdentity", "MibIdentifier", "Unsigned32", "Gauge32", "Counter32", "TimeTicks", "NotificationType", "Integer32", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usdProfileAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usdProfileAgents")
usdIpProfileSetMap, usdIpProfileIpAddr, usdIpProfileDeprecatedGroup, usdIpProfileDirectedBcastEnable, usdIpProfileMtu, usdIpProfileRouterName, usdIpProfileGroup2, usdIpProfileLoopback, usdIpProfileRowStatus, usdIpProfileAccessRoute, usdIpProfileIcmpRedirectEnable, usdIpProfileGroup1, usdIpProfileSrcAddrValidEnable, usdIpProfileGroup, usdIpProfileIpMask = mibBuilder.importSymbols("Unisphere-Data-IP-PROFILE-MIB", "usdIpProfileSetMap", "usdIpProfileIpAddr", "usdIpProfileDeprecatedGroup", "usdIpProfileDirectedBcastEnable", "usdIpProfileMtu", "usdIpProfileRouterName", "usdIpProfileGroup2", "usdIpProfileLoopback", "usdIpProfileRowStatus", "usdIpProfileAccessRoute", "usdIpProfileIcmpRedirectEnable", "usdIpProfileGroup1", "usdIpProfileSrcAddrValidEnable", "usdIpProfileGroup", "usdIpProfileIpMask")
usdIpProfileAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2))
usdIpProfileAgent.setRevisions(('2001-03-28 21:43',))
if mibBuilder.loadTexts: usdIpProfileAgent.setLastUpdated('200103282143Z')
if mibBuilder.loadTexts: usdIpProfileAgent.setOrganization('Unisphere Networks, Inc.')
usdIpProfileAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpProfileAgentV1 = usdIpProfileAgentV1.setProductRelease('Version 1 of the IP Profile component of the Unisphere Routing Switch\n        SNMP agent.  This version of the IP Profile Manager component was\n        supported in the Unisphere RX 1.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpProfileAgentV1 = usdIpProfileAgentV1.setStatus('obsolete')
usdIpProfileAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpProfileAgentV2 = usdIpProfileAgentV2.setProductRelease('Version 2 of the IP Profile component of the Unisphere Routing Switch\n        SNMP agent.  This version of the IP Profile Manager component was\n        supported in the Unisphere RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpProfileAgentV2 = usdIpProfileAgentV2.setStatus('obsolete')
usdIpProfileAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpProfileAgentV3 = usdIpProfileAgentV3.setProductRelease('Version 3 of the IP Profile component of the Unisphere Routing Switch\n        SNMP agent.  This version of the IP Profile Manager component is\n        supported in the Unisphere RX 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpProfileAgentV3 = usdIpProfileAgentV3.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-IP-Profile-CONF", usdIpProfileAgentV3=usdIpProfileAgentV3, usdIpProfileAgentV1=usdIpProfileAgentV1, usdIpProfileAgentV2=usdIpProfileAgentV2, usdIpProfileAgent=usdIpProfileAgent, PYSNMP_MODULE_ID=usdIpProfileAgent)
