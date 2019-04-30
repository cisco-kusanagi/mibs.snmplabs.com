#
# PySNMP MIB module Unisphere-Data-Policy-Manager-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Policy-Manager-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Gauge32, ObjectIdentity, iso, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, TimeTicks, Counter64, Integer32, Bits, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "iso", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "TimeTicks", "Counter64", "Integer32", "Bits", "Counter32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdPolicyAttachStatisticsGroup, usdForwardRulesGroup, usdPolicyIfAttachGroup, usdRateLimitGroup, usdTrafficShapeGroup, usdRateLimitGroup2, usdColorRulesGroup, usdNextInterfaceRulesGroup, usdMarkingRulesGroup, usdLogRuleGroup, usdTrafficClassRulesGroup, usdFilterRulesGroup, usdClassifierControlListGroup2, usdPolicyBaseGroup, usdNextHopRulesGroup, usdPolicyAttachProfileGroup = mibBuilder.importSymbols("Unisphere-Data-POLICY-MIB", "usdPolicyAttachStatisticsGroup", "usdForwardRulesGroup", "usdPolicyIfAttachGroup", "usdRateLimitGroup", "usdTrafficShapeGroup", "usdRateLimitGroup2", "usdColorRulesGroup", "usdNextInterfaceRulesGroup", "usdMarkingRulesGroup", "usdLogRuleGroup", "usdTrafficClassRulesGroup", "usdFilterRulesGroup", "usdClassifierControlListGroup2", "usdPolicyBaseGroup", "usdNextHopRulesGroup", "usdPolicyAttachProfileGroup")
usdPolicyManagerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31))
usdPolicyManagerAgent.setRevisions(('2002-08-02 12:07', '2001-09-07 15:27',))
if mibBuilder.loadTexts: usdPolicyManagerAgent.setLastUpdated('200208021207Z')
if mibBuilder.loadTexts: usdPolicyManagerAgent.setOrganization('Juniper Networks, Inc.')
usdPolicyManagerBaseAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1))
if mibBuilder.loadTexts: usdPolicyManagerBaseAgent.setStatus('current')
usdPolicyManagerBaseAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerBaseAgentV1 = usdPolicyManagerBaseAgentV1.setProductRelease('Version 1 of the Policy Manager base component of the Unisphere Routing\n        Switch SNMP agent.  This version of the Policy Manager base component is\n        supported in the Unisphere RX 3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerBaseAgentV1 = usdPolicyManagerBaseAgentV1.setStatus('current')
usdPolicyManagerRateLimitAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2))
if mibBuilder.loadTexts: usdPolicyManagerRateLimitAgent.setStatus('current')
usdPolicyManagerRateLimitAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerRateLimitAgentV1 = usdPolicyManagerRateLimitAgentV1.setProductRelease('Version 1 of the rate limit management subcomponent of the Policy\n        Manager component of the Unisphere Routing Switch SNMP agent.  This\n        version of the rate limit policy management subcomponent was supported\n        in the Unisphere RX 3.2 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerRateLimitAgentV1 = usdPolicyManagerRateLimitAgentV1.setStatus('obsolete')
usdPolicyManagerRateLimitAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerRateLimitAgentV2 = usdPolicyManagerRateLimitAgentV2.setProductRelease('Version 2 of the rate limit management subcomponent of the Policy\n        Manager component of the Unisphere Routing Switch SNMP agent.  This\n        version of the rate limit policy management subcomponent is supported in\n        the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerRateLimitAgentV2 = usdPolicyManagerRateLimitAgentV2.setStatus('current')
usdPolicyManagerTrafficShapeAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 3))
if mibBuilder.loadTexts: usdPolicyManagerTrafficShapeAgent.setStatus('current')
usdPolicyManagerTrafficShapeAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerTrafficShapeAgentV1 = usdPolicyManagerTrafficShapeAgentV1.setProductRelease('Version 1 of the traffic shape management subcomponent of the Policy\n        Manager component of the Unisphere Routing Switch SNMP agent.  This\n        version of the traffic shape policy management subcomponent was\n        supported in the Unisphere RX 3.2 and subsequent 3.x system releases. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerTrafficShapeAgentV1 = usdPolicyManagerTrafficShapeAgentV1.setStatus('obsolete')
usdPolicyManagerLogRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 4))
if mibBuilder.loadTexts: usdPolicyManagerLogRulesAgent.setStatus('current')
usdPolicyManagerLogRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerLogRulesAgentV1 = usdPolicyManagerLogRulesAgentV1.setProductRelease('Version 1 of the log rules subcomponent of the Policy Manager component\n        of the Unisphere Routing Switch SNMP agent.  This version of the log\n        policy rules subcomponent is supported in the Unisphere RX 3.2 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerLogRulesAgentV1 = usdPolicyManagerLogRulesAgentV1.setStatus('current')
usdPolicyManagerNextHopRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 5))
if mibBuilder.loadTexts: usdPolicyManagerNextHopRulesAgent.setStatus('current')
usdPolicyManagerNextHopRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerNextHopRulesAgentV1 = usdPolicyManagerNextHopRulesAgentV1.setProductRelease('Version 1 of the next-hop rules subcomponent of the Policy Manager\n        component of the Unisphere Routing Switch SNMP agent.  This version of\n        the next-hop policy rules subcomponent is supported in the Unisphere RX\n        3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerNextHopRulesAgentV1 = usdPolicyManagerNextHopRulesAgentV1.setStatus('current')
usdPolicyManagerFilterRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 6))
if mibBuilder.loadTexts: usdPolicyManagerFilterRulesAgent.setStatus('current')
usdPolicyManagerFilterRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerFilterRulesAgentV1 = usdPolicyManagerFilterRulesAgentV1.setProductRelease('Version 1 of the filter rules subcomponent of the Policy Manager\n        component of the Unisphere Routing Switch SNMP agent.  This version of\n        the filter policy rules subcomponent is supported in the Unisphere RX\n        3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerFilterRulesAgentV1 = usdPolicyManagerFilterRulesAgentV1.setStatus('current')
usdPolicyManagerNextInterfaceRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 7))
if mibBuilder.loadTexts: usdPolicyManagerNextInterfaceRulesAgent.setStatus('current')
usdPolicyManagerNextInterfaceRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 7, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerNextInterfaceRulesAgentV1 = usdPolicyManagerNextInterfaceRulesAgentV1.setProductRelease('Version 1 of the next-interface rules subcomponent of the Policy\n        Manager component of the Unisphere Routing Switch SNMP agent.  This\n        version of the next-interface policy rules subcomponent is supported in\n        the Unisphere RX 3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerNextInterfaceRulesAgentV1 = usdPolicyManagerNextInterfaceRulesAgentV1.setStatus('current')
usdPolicyManagerMarkingRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 8))
if mibBuilder.loadTexts: usdPolicyManagerMarkingRulesAgent.setStatus('current')
usdPolicyManagerMarkingRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 8, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerMarkingRulesAgentV1 = usdPolicyManagerMarkingRulesAgentV1.setProductRelease('Version 1 of the marking rules subcomponent of the Policy Manager\n        component of the Unisphere Routing Switch SNMP agent.  This version of\n        the marking policy rules subcomponent is supported in the Unisphere RX\n        3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerMarkingRulesAgentV1 = usdPolicyManagerMarkingRulesAgentV1.setStatus('current')
usdPolicyManagerForwardRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 9))
if mibBuilder.loadTexts: usdPolicyManagerForwardRulesAgent.setStatus('current')
usdPolicyManagerForwardRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 9, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerForwardRulesAgentV1 = usdPolicyManagerForwardRulesAgentV1.setProductRelease('Version 1 of the forward rules subcomponent of the Policy Manager\n        component of the Unisphere Routing Switch SNMP agent.  This version of\n        the forward policy rules subcomponent is supported in the Unisphere RX\n        3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerForwardRulesAgentV1 = usdPolicyManagerForwardRulesAgentV1.setStatus('current')
usdPolicyManagerColorRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 10))
if mibBuilder.loadTexts: usdPolicyManagerColorRulesAgent.setStatus('current')
usdPolicyManagerColorRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 10, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerColorRulesAgentV1 = usdPolicyManagerColorRulesAgentV1.setProductRelease('Version 1 of the color rules subcomponent of the Policy Manager\n        component of the Unisphere Routing Switch SNMP agent.  This version of\n        the color policy rules subcomponent is supported in the Unisphere RX 3.2\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerColorRulesAgentV1 = usdPolicyManagerColorRulesAgentV1.setStatus('current')
usdPolicyManagerTrafficClassRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 11))
if mibBuilder.loadTexts: usdPolicyManagerTrafficClassRulesAgent.setStatus('current')
usdPolicyManagerTrafficClassRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 11, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerTrafficClassRulesAgentV1 = usdPolicyManagerTrafficClassRulesAgentV1.setProductRelease('Version 1 of the traffic class rules subcomponent of the Policy Manager\n        component of the Unisphere Routing Switch SNMP agent.  This version of\n        the traffic class policy rules subcomponent is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerTrafficClassRulesAgentV1 = usdPolicyManagerTrafficClassRulesAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-Policy-Manager-CONF", usdPolicyManagerRateLimitAgentV1=usdPolicyManagerRateLimitAgentV1, usdPolicyManagerNextHopRulesAgentV1=usdPolicyManagerNextHopRulesAgentV1, usdPolicyManagerNextHopRulesAgent=usdPolicyManagerNextHopRulesAgent, usdPolicyManagerTrafficShapeAgent=usdPolicyManagerTrafficShapeAgent, PYSNMP_MODULE_ID=usdPolicyManagerAgent, usdPolicyManagerNextInterfaceRulesAgentV1=usdPolicyManagerNextInterfaceRulesAgentV1, usdPolicyManagerAgent=usdPolicyManagerAgent, usdPolicyManagerNextInterfaceRulesAgent=usdPolicyManagerNextInterfaceRulesAgent, usdPolicyManagerForwardRulesAgentV1=usdPolicyManagerForwardRulesAgentV1, usdPolicyManagerTrafficShapeAgentV1=usdPolicyManagerTrafficShapeAgentV1, usdPolicyManagerFilterRulesAgent=usdPolicyManagerFilterRulesAgent, usdPolicyManagerRateLimitAgentV2=usdPolicyManagerRateLimitAgentV2, usdPolicyManagerBaseAgent=usdPolicyManagerBaseAgent, usdPolicyManagerForwardRulesAgent=usdPolicyManagerForwardRulesAgent, usdPolicyManagerTrafficClassRulesAgent=usdPolicyManagerTrafficClassRulesAgent, usdPolicyManagerRateLimitAgent=usdPolicyManagerRateLimitAgent, usdPolicyManagerColorRulesAgent=usdPolicyManagerColorRulesAgent, usdPolicyManagerFilterRulesAgentV1=usdPolicyManagerFilterRulesAgentV1, usdPolicyManagerLogRulesAgent=usdPolicyManagerLogRulesAgent, usdPolicyManagerMarkingRulesAgent=usdPolicyManagerMarkingRulesAgent, usdPolicyManagerColorRulesAgentV1=usdPolicyManagerColorRulesAgentV1, usdPolicyManagerBaseAgentV1=usdPolicyManagerBaseAgentV1, usdPolicyManagerMarkingRulesAgentV1=usdPolicyManagerMarkingRulesAgentV1, usdPolicyManagerTrafficClassRulesAgentV1=usdPolicyManagerTrafficClassRulesAgentV1, usdPolicyManagerLogRulesAgentV1=usdPolicyManagerLogRulesAgentV1)
