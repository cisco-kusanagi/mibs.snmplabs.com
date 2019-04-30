#
# PySNMP MIB module Unisphere-Data-RADIUS-Client-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-RADIUS-Client-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Bits, Integer32, IpAddress, iso, ObjectIdentity, Counter32, NotificationType, TimeTicks, Unsigned32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "IpAddress", "iso", "ObjectIdentity", "Counter32", "NotificationType", "TimeTicks", "Unsigned32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdRadiusGeneralClientGroup2, usdRadiusBrasClientGroup, usdRadiusBrasClientGroup2, usdRadiusBrasClientGroup5, usdRadiusTunnelClientGroup, usdRadiusBasicClientGroup, usdRadiusAuthClientGroup, usdRadiusBrasClientGroup3, usdRadiusBasicClientGroup2, usdRadiusBrasClientGroup4, usdRadiusAcctClientGroup, usdRadiusGeneralClientGroup = mibBuilder.importSymbols("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusGeneralClientGroup2", "usdRadiusBrasClientGroup", "usdRadiusBrasClientGroup2", "usdRadiusBrasClientGroup5", "usdRadiusTunnelClientGroup", "usdRadiusBasicClientGroup", "usdRadiusAuthClientGroup", "usdRadiusBrasClientGroup3", "usdRadiusBasicClientGroup2", "usdRadiusBrasClientGroup4", "usdRadiusAcctClientGroup", "usdRadiusGeneralClientGroup")
usdRadiusClientAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35))
usdRadiusClientAgent.setRevisions(('2001-10-19 14:44', '2001-10-16 20:45', '2001-09-07 12:35',))
if mibBuilder.loadTexts: usdRadiusClientAgent.setLastUpdated('200110191444Z')
if mibBuilder.loadTexts: usdRadiusClientAgent.setOrganization('Unisphere Networks, Inc.')
usdRadiusClientDynamicAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1))
if mibBuilder.loadTexts: usdRadiusClientDynamicAgent.setStatus('current')
usdRadiusClientDynamicAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV1 = usdRadiusClientDynamicAgentV1.setProductRelease('Version 1 of the RADIUS Client dynamic interface component of the\n        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client\n        component was supported in the Unisphere RX 1.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV1 = usdRadiusClientDynamicAgentV1.setStatus('obsolete')
usdRadiusClientDynamicAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV2 = usdRadiusClientDynamicAgentV2.setProductRelease('Version 2 of the RADIUS Client dynamic interface component of the\n        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client\n        component was supported in the Unisphere RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV2 = usdRadiusClientDynamicAgentV2.setStatus('obsolete')
usdRadiusClientDynamicAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV3 = usdRadiusClientDynamicAgentV3.setProductRelease('Version 3 of the RADIUS Client dynamic interface component of the\n        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client\n        component was supported in the Unisphere RX 3.0 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV3 = usdRadiusClientDynamicAgentV3.setStatus('obsolete')
usdRadiusClientDynamicAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV4 = usdRadiusClientDynamicAgentV4.setProductRelease('Version 4 of the RADIUS Client dynamic interface component of the\n        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client\n        component was supported in the Unisphere RX 3.1 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV4 = usdRadiusClientDynamicAgentV4.setStatus('obsolete')
usdRadiusClientDynamicAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV5 = usdRadiusClientDynamicAgentV5.setProductRelease('Version 5 of the RADIUS Client dynamic interface component of the\n        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client\n        component was supported in the Unisphere RX 3.2 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV5 = usdRadiusClientDynamicAgentV5.setStatus('obsolete')
usdRadiusClientDynamicAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV6 = usdRadiusClientDynamicAgentV6.setProductRelease('Version 6 of the RADIUS Client dynamic interface component of the\n        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client\n        component was supported in the Unisphere RX 3.3 and subsequent RX 3.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV6 = usdRadiusClientDynamicAgentV6.setStatus('obsolete')
usdRadiusClientDynamicAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV7 = usdRadiusClientDynamicAgentV7.setProductRelease('Version 7 of the RADIUS Client dynamic interface component of the\n        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client\n        component is supported in the Unisphere RX 4.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientDynamicAgentV7 = usdRadiusClientDynamicAgentV7.setStatus('current')
usdRadiusClientBasicAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 2))
if mibBuilder.loadTexts: usdRadiusClientBasicAgent.setStatus('current')
usdRadiusClientBasicAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientBasicAgentV1 = usdRadiusClientBasicAgentV1.setProductRelease('Version 1 of the basic authentication RADIUS Client component of the\n        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client\n        component is supported in the Unisphere RX 3.2 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRadiusClientBasicAgentV1 = usdRadiusClientBasicAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-RADIUS-Client-CONF", usdRadiusClientDynamicAgentV4=usdRadiusClientDynamicAgentV4, usdRadiusClientBasicAgent=usdRadiusClientBasicAgent, usdRadiusClientDynamicAgentV5=usdRadiusClientDynamicAgentV5, usdRadiusClientDynamicAgentV6=usdRadiusClientDynamicAgentV6, usdRadiusClientDynamicAgentV3=usdRadiusClientDynamicAgentV3, usdRadiusClientAgent=usdRadiusClientAgent, PYSNMP_MODULE_ID=usdRadiusClientAgent, usdRadiusClientDynamicAgent=usdRadiusClientDynamicAgent, usdRadiusClientDynamicAgentV1=usdRadiusClientDynamicAgentV1, usdRadiusClientBasicAgentV1=usdRadiusClientBasicAgentV1, usdRadiusClientDynamicAgentV2=usdRadiusClientDynamicAgentV2, usdRadiusClientDynamicAgentV7=usdRadiusClientDynamicAgentV7)
