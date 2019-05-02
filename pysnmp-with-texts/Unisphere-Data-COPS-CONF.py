#
# PySNMP MIB module Unisphere-Data-COPS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-COPS-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:30:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Bits, iso, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, Gauge32, Counter64, MibIdentifier, TimeTicks, Integer32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "Gauge32", "Counter64", "MibIdentifier", "TimeTicks", "Integer32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdCopsProtocolGroup2, usdCopsProtocolGroup = mibBuilder.importSymbols("Unisphere-Data-COPS-MIB", "usdCopsProtocolGroup2", "usdCopsProtocolGroup")
usdCopsAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 7))
usdCopsAgent.setRevisions(('2002-01-14 19:36', '2001-03-27 22:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdCopsAgent.setRevisionsDescriptions(('Added support for the local address and transport router name objects.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdCopsAgent.setLastUpdated('200201141936Z')
if mibBuilder.loadTexts: usdCopsAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdCopsAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdCopsAgent.setDescription('The agent capabilities definitions for the Common Open Policy Service (COPS) Protocol management component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdCopsAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 7, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCopsAgentV1 = usdCopsAgentV1.setProductRelease('Version 1 of the COPS component of the Unisphere Routing Switch SNMP\n        agent.  This version of the COPS component was supported in the\n        Unisphere RX 2.x and 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCopsAgentV1 = usdCopsAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdCopsAgentV1.setDescription('The MIB supported by the SNMP agent for the COPS application in the Unisphere Routing Switch. These capabilities became obsolete when the local address and transport router name objects were add.')
usdCopsAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 7, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCopsAgentV2 = usdCopsAgentV2.setProductRelease('Version 2 of the COPS component of the Unisphere Routing Switch SNMP\n        agent.  This version of the COPS component is supported in the Unisphere\n        RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCopsAgentV2 = usdCopsAgentV2.setStatus('current')
if mibBuilder.loadTexts: usdCopsAgentV2.setDescription('The MIB supported by the SNMP agent for the COPS application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-COPS-CONF", usdCopsAgentV2=usdCopsAgentV2, PYSNMP_MODULE_ID=usdCopsAgent, usdCopsAgent=usdCopsAgent, usdCopsAgentV1=usdCopsAgentV1)
