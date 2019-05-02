#
# PySNMP MIB module Unisphere-Data-RIP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-RIP-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
rip2PeerGroup, rip2IfConfGroup, rip2IfStatGroup, rip2GlobalGroup = mibBuilder.importSymbols("RIPv2-MIB", "rip2PeerGroup", "rip2IfConfGroup", "rip2IfStatGroup", "rip2GlobalGroup")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Unsigned32, iso, ObjectIdentity, Gauge32, TimeTicks, ModuleIdentity, Integer32, Bits, Counter64, IpAddress, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "ObjectIdentity", "Gauge32", "TimeTicks", "ModuleIdentity", "Integer32", "Bits", "Counter64", "IpAddress", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdRipAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 36))
usdRipAgent.setRevisions(('2001-03-29 18:13',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdRipAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdRipAgent.setLastUpdated('200103291813Z')
if mibBuilder.loadTexts: usdRipAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdRipAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdRipAgent.setDescription('The agent capabilities definitions for the RIP component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdRipAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 36, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRipAgentV1 = usdRipAgentV1.setProductRelease('Version 1 of the RIP component of the Unisphere Routing Switch SNMP\n        agent.  This version of the RIP component is supported in the Unisphere\n        RX 1.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRipAgentV1 = usdRipAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdRipAgentV1.setDescription('The MIB supported by the SNMP agent for the RIP application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-RIP-CONF", usdRipAgent=usdRipAgent, PYSNMP_MODULE_ID=usdRipAgent, usdRipAgentV1=usdRipAgentV1)
