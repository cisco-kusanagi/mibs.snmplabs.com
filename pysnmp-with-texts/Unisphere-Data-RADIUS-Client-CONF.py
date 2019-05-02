#
# PySNMP MIB module Unisphere-Data-RADIUS-Client-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-RADIUS-Client-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Unsigned32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, TimeTicks, ObjectIdentity, Integer32, ModuleIdentity, Counter32, IpAddress, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "TimeTicks", "ObjectIdentity", "Integer32", "ModuleIdentity", "Counter32", "IpAddress", "MibIdentifier", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdRadiusGeneralClientGroup2, usdRadiusGeneralClientGroup, usdRadiusAcctClientGroup, usdRadiusTunnelClientGroup, usdRadiusBrasClientGroup3, usdRadiusBrasClientGroup, usdRadiusBasicClientGroup, usdRadiusBrasClientGroup2, usdRadiusBasicClientGroup2, usdRadiusAuthClientGroup, usdRadiusBrasClientGroup5, usdRadiusBrasClientGroup4 = mibBuilder.importSymbols("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusGeneralClientGroup2", "usdRadiusGeneralClientGroup", "usdRadiusAcctClientGroup", "usdRadiusTunnelClientGroup", "usdRadiusBrasClientGroup3", "usdRadiusBrasClientGroup", "usdRadiusBasicClientGroup", "usdRadiusBrasClientGroup2", "usdRadiusBasicClientGroup2", "usdRadiusAuthClientGroup", "usdRadiusBrasClientGroup5", "usdRadiusBrasClientGroup4")
usdRadiusClientAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35))
usdRadiusClientAgent.setRevisions(('2001-10-19 14:44', '2001-10-16 20:45', '2001-09-07 12:35',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdRadiusClientAgent.setRevisionsDescriptions(('New objects were added to the BRAS group to indicate which RADIUS attributes should be included or excluded from RADIUS packets.', 'A new object was added to the BRAS group.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdRadiusClientAgent.setLastUpdated('200110191444Z')
if mibBuilder.loadTexts: usdRadiusClientAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdRadiusClientAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdRadiusClientAgent.setDescription('The agent capabilities definitions for the RADIUS Client component of the SNMP agent in the Unisphere Data Routing Switch family of products.')
usdRadiusClientDynamicAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1))
if mibBuilder.loadTexts: usdRadiusClientDynamicAgent.setStatus('current')
if mibBuilder.loadTexts: usdRadiusClientDynamicAgent.setDescription('The registration group of agent capabilities for RADIUS Client application which provides complete dynamic interface support in addition to basic authentication for CLI access.')
usdRadiusClientDynamicAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV1 = usdRadiusClientDynamicAgentV1.setProductRelease('Version 1 of the RADIUS Client dynamic interface component of the\n        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client\n        component was supported in the Unisphere RX 1.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV1 = usdRadiusClientDynamicAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdRadiusClientDynamicAgentV1.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in the Unisphere Routing Switch. These capabilities became obsolete when a new object was added.')
usdRadiusClientDynamicAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV2 = usdRadiusClientDynamicAgentV2.setProductRelease('Version 2 of the RADIUS Client dynamic interface component of the\n        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client\n        component was supported in the Unisphere RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV2 = usdRadiusClientDynamicAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdRadiusClientDynamicAgentV2.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in the Unisphere Routing Switch. These capabilities became obsolete when new objects were added.')
usdRadiusClientDynamicAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV3 = usdRadiusClientDynamicAgentV3.setProductRelease('Version 3 of the RADIUS Client dynamic interface component of the\n        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client\n        component was supported in the Unisphere RX 3.0 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV3 = usdRadiusClientDynamicAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: usdRadiusClientDynamicAgentV3.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in the Unisphere Routing Switch. These capabilities became obsolete when new B-RAS objects were added.')
usdRadiusClientDynamicAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV4 = usdRadiusClientDynamicAgentV4.setProductRelease('Version 4 of the RADIUS Client dynamic interface component of the\n        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client\n        component was supported in the Unisphere RX 3.1 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV4 = usdRadiusClientDynamicAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: usdRadiusClientDynamicAgentV4.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in the Unisphere Routing Switch. These capabilities became obsolete when new objects were added.')
usdRadiusClientDynamicAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV5 = usdRadiusClientDynamicAgentV5.setProductRelease('Version 5 of the RADIUS Client dynamic interface component of the\n        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client\n        component was supported in the Unisphere RX 3.2 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV5 = usdRadiusClientDynamicAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: usdRadiusClientDynamicAgentV5.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in the Unisphere Routing Switch. These capabilities became obsolete when a new object was added to the BRAS group.')
usdRadiusClientDynamicAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV6 = usdRadiusClientDynamicAgentV6.setProductRelease('Version 6 of the RADIUS Client dynamic interface component of the\n        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client\n        component was supported in the Unisphere RX 3.3 and subsequent RX 3.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV6 = usdRadiusClientDynamicAgentV6.setStatus('obsolete')
if mibBuilder.loadTexts: usdRadiusClientDynamicAgentV6.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in the Unisphere Routing Switch. These capabilities became obsolete when new objects were added to indicate which RADIUS attributes should be included or excluded from RADIUS packets.')
usdRadiusClientDynamicAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV7 = usdRadiusClientDynamicAgentV7.setProductRelease('Version 7 of the RADIUS Client dynamic interface component of the\n        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client\n        component is supported in the Unisphere RX 4.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV7 = usdRadiusClientDynamicAgentV7.setStatus('current')
if mibBuilder.loadTexts: usdRadiusClientDynamicAgentV7.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in the Unisphere Routing Switch.')
usdRadiusClientBasicAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 2))
if mibBuilder.loadTexts: usdRadiusClientBasicAgent.setStatus('current')
if mibBuilder.loadTexts: usdRadiusClientBasicAgent.setDescription('The registration group of agent capabilities for the RADIUS Client application which only provides basic authentication for CLI access to a Unisphere data routing switch.')
usdRadiusClientBasicAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientBasicAgentV1 = usdRadiusClientBasicAgentV1.setProductRelease('Version 1 of the basic authentication RADIUS Client component of the\n        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client\n        component is supported in the Unisphere RX 3.2 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientBasicAgentV1 = usdRadiusClientBasicAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdRadiusClientBasicAgentV1.setDescription('The MIB supported by the SNMP agent for the RADIUS Client basic authentication application which only supports basic authentication for remote CLI access in a Unisphere Data Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-RADIUS-Client-CONF", usdRadiusClientDynamicAgentV5=usdRadiusClientDynamicAgentV5, usdRadiusClientAgent=usdRadiusClientAgent, PYSNMP_MODULE_ID=usdRadiusClientAgent, usdRadiusClientDynamicAgentV4=usdRadiusClientDynamicAgentV4, usdRadiusClientDynamicAgentV6=usdRadiusClientDynamicAgentV6, usdRadiusClientBasicAgent=usdRadiusClientBasicAgent, usdRadiusClientDynamicAgentV1=usdRadiusClientDynamicAgentV1, usdRadiusClientDynamicAgentV2=usdRadiusClientDynamicAgentV2, usdRadiusClientDynamicAgent=usdRadiusClientDynamicAgent, usdRadiusClientBasicAgentV1=usdRadiusClientBasicAgentV1, usdRadiusClientDynamicAgentV3=usdRadiusClientDynamicAgentV3, usdRadiusClientDynamicAgentV7=usdRadiusClientDynamicAgentV7)
