#
# PySNMP MIB module Unisphere-Data-IS-IS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-IS-IS-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:31:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Integer32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Gauge32, iso, TimeTicks, ObjectIdentity, IpAddress, Unsigned32, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Gauge32", "iso", "TimeTicks", "ObjectIdentity", "IpAddress", "Unsigned32", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdIsisSystemMgmtGroup2, usdIsisCircuitMgmtGroup, usdIsisCircuitMgmtGroup2, usdIsisSystemMgmtGroup = mibBuilder.importSymbols("Unisphere-Data-ISIS-MIB", "usdIsisSystemMgmtGroup2", "usdIsisCircuitMgmtGroup", "usdIsisCircuitMgmtGroup2", "usdIsisSystemMgmtGroup")
usdIsisAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 23))
usdIsisAgent.setRevisions(('2002-04-04 20:37', '2001-04-24 19:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdIsisAgent.setRevisionsDescriptions(('Added MPLS support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdIsisAgent.setLastUpdated('200204042037Z')
if mibBuilder.loadTexts: usdIsisAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdIsisAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdIsisAgent.setDescription('The agent capabilities definitions for the intermediate system to intermediate system (IS-IS) protocol management component of the SNMP agent in the Unisphere Data Routing Switch family of products.')
usdIsisAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 23, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIsisAgentV1 = usdIsisAgentV1.setProductRelease('Version 1 of the IS-IS component of the Unisphere Routing Switch SNMP\n        agent.  This version of the IS-IS component was supported in the\n        Unisphere RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIsisAgentV1 = usdIsisAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdIsisAgentV1.setDescription('The MIB supported by the SNMP agent for the intermediate system to intermediate system (IS-IS) protocol application in the Unisphere Routing Switch. These capabilities became obsolete when the usdIsisCircState object was added.')
usdIsisAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 23, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIsisAgentV2 = usdIsisAgentV2.setProductRelease('Version 2 of the IS-IS component of the Unisphere Routing Switch SNMP\n        agent.  This version of the IS-IS component was supported in the\n        Unisphere RX 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIsisAgentV2 = usdIsisAgentV2.setStatus('current')
if mibBuilder.loadTexts: usdIsisAgentV2.setDescription('The MIB supported by the SNMP agent for the intermediate system to intermediate system (IS-IS) protocol application in the Unisphere Routing Switch. These capabilities became obsolete when MPLS support was added.')
usdIsisAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 23, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIsisAgentV3 = usdIsisAgentV3.setProductRelease('Version 3 of the IS-IS component of the Unisphere Routing Switch SNMP\n        agent.  This version of the IS-IS component is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIsisAgentV3 = usdIsisAgentV3.setStatus('current')
if mibBuilder.loadTexts: usdIsisAgentV3.setDescription('The MIB supported by the SNMP agent for the intermediate system to intermediate system (IS-IS) protocol application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-IS-IS-CONF", usdIsisAgentV2=usdIsisAgentV2, usdIsisAgentV3=usdIsisAgentV3, PYSNMP_MODULE_ID=usdIsisAgent, usdIsisAgent=usdIsisAgent, usdIsisAgentV1=usdIsisAgentV1)
