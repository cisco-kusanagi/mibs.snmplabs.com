#
# PySNMP MIB module Juniper-Policy-Manager-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Policy-Manager-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Bits, NotificationType, Counter32, TimeTicks, MibIdentifier, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Bits", "NotificationType", "Counter32", "TimeTicks", "MibIdentifier", "Integer32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniPolicyManagerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31))
juniPolicyManagerAgent.setRevisions(('2005-08-08 18:21', '2005-02-01 15:58', '2003-10-21 19:20', '2003-08-26 12:51', '2002-09-06 16:54', '2002-08-02 12:07', '2001-09-07 15:27',))
if mibBuilder.loadTexts: juniPolicyManagerAgent.setLastUpdated('200508081821Z')
if mibBuilder.loadTexts: juniPolicyManagerAgent.setOrganization('Juniper Networks, Inc.')
juniPolicyManagerBaseAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1))
if mibBuilder.loadTexts: juniPolicyManagerBaseAgent.setStatus('current')
juniPolicyManagerBaseAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerBaseAgentV1 = juniPolicyManagerBaseAgentV1.setProductRelease('Version 1 of the Policy Manager base component of the JUNOSe SNMP\n        agent.  This version of the Policy Manager base component was supported\n        in JUNOSe 3.2 thru 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerBaseAgentV1 = juniPolicyManagerBaseAgentV1.setStatus('obsolete')
juniPolicyManagerBaseAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerBaseAgentV2 = juniPolicyManagerBaseAgentV2.setProductRelease('Version 2 of the Policy Manager base component of the JUNOSe SNMP\n        agent.  This version of the Policy Manager base component is supported\n        in JUNOSe 5.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerBaseAgentV2 = juniPolicyManagerBaseAgentV2.setStatus('obsolete')
juniPolicyManagerBaseAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerBaseAgentV3 = juniPolicyManagerBaseAgentV3.setProductRelease('Version 3 of the Policy Manager base component of the JUNOSe SNMP\n        agent.  This version of the Policy Manager base component is supported\n        in JUNOSe 6.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerBaseAgentV3 = juniPolicyManagerBaseAgentV3.setStatus('obsolete')
juniPolicyManagerBaseAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerBaseAgentV4 = juniPolicyManagerBaseAgentV4.setProductRelease('Version 4 of the Policy Manager base component of the JUNOSe SNMP\n        agent.  This version of the Policy Manager base component is supported\n        in JUNOSe 7.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerBaseAgentV4 = juniPolicyManagerBaseAgentV4.setStatus('current')
juniPolicyManagerRateLimitAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2))
if mibBuilder.loadTexts: juniPolicyManagerRateLimitAgent.setStatus('current')
juniPolicyManagerRateLimitAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerRateLimitAgentV1 = juniPolicyManagerRateLimitAgentV1.setProductRelease('Version 1 of the rate limit management subcomponent of the Policy\n        Manager component of the JUNOSe SNMP agent.  This version of the rate\n        limit policy management subcomponent was supported in JUNOSe 3.2 and\n        subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerRateLimitAgentV1 = juniPolicyManagerRateLimitAgentV1.setStatus('obsolete')
juniPolicyManagerRateLimitAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerRateLimitAgentV2 = juniPolicyManagerRateLimitAgentV2.setProductRelease('Version 2 of the rate limit management subcomponent of the Policy\n        Manager component of the JUNOSe SNMP agent.  This version of the rate\n        limit policy management subcomponent was supported in JUNOSe 4.0 thru\n        5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerRateLimitAgentV2 = juniPolicyManagerRateLimitAgentV2.setStatus('obsolete')
juniPolicyManagerRateLimitAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerRateLimitAgentV3 = juniPolicyManagerRateLimitAgentV3.setProductRelease('Version 3 of the rate limit management subcomponent of the Policy\n        Manager component of JUNOSe SNMP agent.  This version of the rate limit\n        policy management subcomponent is supported in the Juniper RX 5.3 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerRateLimitAgentV3 = juniPolicyManagerRateLimitAgentV3.setStatus('current')
juniPolicyManagerTrafficShapeAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 3))
if mibBuilder.loadTexts: juniPolicyManagerTrafficShapeAgent.setStatus('obsolete')
juniPolicyManagerTrafficShapeAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerTrafficShapeAgentV1 = juniPolicyManagerTrafficShapeAgentV1.setProductRelease('Version 1 of the traffic shape management subcomponent of the Policy\n        Manager component of the JUNOSe SNMP agent.  This version of the traffic\n        shape policy management subcomponent was supported in JUNOSe 3.2 and\n        subsequent 3.x system releases. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerTrafficShapeAgentV1 = juniPolicyManagerTrafficShapeAgentV1.setStatus('obsolete')
juniPolicyManagerLogRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 4))
if mibBuilder.loadTexts: juniPolicyManagerLogRulesAgent.setStatus('current')
juniPolicyManagerLogRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerLogRulesAgentV1 = juniPolicyManagerLogRulesAgentV1.setProductRelease('Version 1 of the log rules subcomponent of the Policy Manager component\n        of the JUNOSe SNMP agent.  This version of the log policy rules\n        subcomponent was supported in JUNOSe 3.2 thru 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerLogRulesAgentV1 = juniPolicyManagerLogRulesAgentV1.setStatus('obsolete')
juniPolicyManagerLogRulesAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 4, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerLogRulesAgentV2 = juniPolicyManagerLogRulesAgentV2.setProductRelease('Version 2 of the log rules subcomponent of the Policy Manager component\n        of the JUNOSe SNMP agent.  This version of the log policy rules\n        subcomponent is supported in JUNOSe 5.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerLogRulesAgentV2 = juniPolicyManagerLogRulesAgentV2.setStatus('current')
juniPolicyManagerNextHopRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 5))
if mibBuilder.loadTexts: juniPolicyManagerNextHopRulesAgent.setStatus('current')
juniPolicyManagerNextHopRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerNextHopRulesAgentV1 = juniPolicyManagerNextHopRulesAgentV1.setProductRelease('Version 1 of the next-hop rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the next-hop policy\n        rules subcomponent was supported in JUNOSe 3.2 thru 5.2 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerNextHopRulesAgentV1 = juniPolicyManagerNextHopRulesAgentV1.setStatus('obsolete')
juniPolicyManagerNextHopRulesAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 5, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerNextHopRulesAgentV2 = juniPolicyManagerNextHopRulesAgentV2.setProductRelease('Version 2 of the next-hop rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the next-hop policy\n        rules subcomponent is supported in JUNOSe 5.3 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerNextHopRulesAgentV2 = juniPolicyManagerNextHopRulesAgentV2.setStatus('current')
juniPolicyManagerFilterRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 6))
if mibBuilder.loadTexts: juniPolicyManagerFilterRulesAgent.setStatus('current')
juniPolicyManagerFilterRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerFilterRulesAgentV1 = juniPolicyManagerFilterRulesAgentV1.setProductRelease('Version 1 of the filter rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the filter policy\n        rules subcomponent is supported in JUNOSe 3.2 thru 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerFilterRulesAgentV1 = juniPolicyManagerFilterRulesAgentV1.setStatus('obsolete')
juniPolicyManagerFilterRulesAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 6, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerFilterRulesAgentV2 = juniPolicyManagerFilterRulesAgentV2.setProductRelease('Version 2 of the filter rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the filter policy\n        rules subcomponent is supported in JUNOSe 5.3 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerFilterRulesAgentV2 = juniPolicyManagerFilterRulesAgentV2.setStatus('current')
juniPolicyManagerNextInterfaceRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 7))
if mibBuilder.loadTexts: juniPolicyManagerNextInterfaceRulesAgent.setStatus('current')
juniPolicyManagerNextInterfaceRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 7, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerNextInterfaceRulesAgentV1 = juniPolicyManagerNextInterfaceRulesAgentV1.setProductRelease('Version 1 of the next-interface rules subcomponent of the Policy\n        Manager component of the JUNOSe SNMP agent.  This version of the\n        next-interface policy rules subcomponent was supported in JUNOSe 3.2\n        thru 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerNextInterfaceRulesAgentV1 = juniPolicyManagerNextInterfaceRulesAgentV1.setStatus('obsolete')
juniPolicyManagerNextInterfaceRulesAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 7, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerNextInterfaceRulesAgentV2 = juniPolicyManagerNextInterfaceRulesAgentV2.setProductRelease('Version 2 of the next-interface rules subcomponent of the Policy\n        Manager component of the JUNOSe SNMP agent.  This version of the\n        next-interface policy rules subcomponent is supported in JUNOSe 5.3 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerNextInterfaceRulesAgentV2 = juniPolicyManagerNextInterfaceRulesAgentV2.setStatus('current')
juniPolicyManagerMarkingRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 8))
if mibBuilder.loadTexts: juniPolicyManagerMarkingRulesAgent.setStatus('current')
juniPolicyManagerMarkingRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 8, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerMarkingRulesAgentV1 = juniPolicyManagerMarkingRulesAgentV1.setProductRelease('Version 1 of the marking rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the marking policy\n        rules subcomponent was supported in JUNOSe 3.2 thru 5.2 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerMarkingRulesAgentV1 = juniPolicyManagerMarkingRulesAgentV1.setStatus('obsolete')
juniPolicyManagerMarkingRulesAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 8, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerMarkingRulesAgentV2 = juniPolicyManagerMarkingRulesAgentV2.setProductRelease('Version 2 of the marking rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the marking policy\n        rules subcomponent is supported in JUNOSe 5.3 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerMarkingRulesAgentV2 = juniPolicyManagerMarkingRulesAgentV2.setStatus('current')
juniPolicyManagerForwardRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 9))
if mibBuilder.loadTexts: juniPolicyManagerForwardRulesAgent.setStatus('current')
juniPolicyManagerForwardRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 9, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerForwardRulesAgentV1 = juniPolicyManagerForwardRulesAgentV1.setProductRelease('Version 1 of the forward rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the forward policy\n        rules subcomponent was supported in JUNOSe 3.2 thru 5.1 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerForwardRulesAgentV1 = juniPolicyManagerForwardRulesAgentV1.setStatus('obsolete')
juniPolicyManagerForwardRulesAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 9, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerForwardRulesAgentV2 = juniPolicyManagerForwardRulesAgentV2.setProductRelease('Version 2 of the forward rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the forward policy\n        rules subcomponent was supported in JUNOSe 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerForwardRulesAgentV2 = juniPolicyManagerForwardRulesAgentV2.setStatus('obsolete')
juniPolicyManagerForwardRulesAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 9, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerForwardRulesAgentV3 = juniPolicyManagerForwardRulesAgentV3.setProductRelease('Version 3 of the forward rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the forward policy\n        rules subcomponent is supported in JUNOSe 5.3 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerForwardRulesAgentV3 = juniPolicyManagerForwardRulesAgentV3.setStatus('current')
juniPolicyManagerColorRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 10))
if mibBuilder.loadTexts: juniPolicyManagerColorRulesAgent.setStatus('current')
juniPolicyManagerColorRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 10, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerColorRulesAgentV1 = juniPolicyManagerColorRulesAgentV1.setProductRelease('Version 1 of the color rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the color policy\n        rules subcomponent was supported in JUNOSe 3.2 thru 5.2 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerColorRulesAgentV1 = juniPolicyManagerColorRulesAgentV1.setStatus('obsolete')
juniPolicyManagerColorRulesAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 10, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerColorRulesAgentV2 = juniPolicyManagerColorRulesAgentV2.setProductRelease('Version 2 of the color rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the color policy\n        rules subcomponent is supported in JUNOSe 5.3 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerColorRulesAgentV2 = juniPolicyManagerColorRulesAgentV2.setStatus('current')
juniPolicyManagerTrafficClassRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 11))
if mibBuilder.loadTexts: juniPolicyManagerTrafficClassRulesAgent.setStatus('current')
juniPolicyManagerTrafficClassRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 11, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerTrafficClassRulesAgentV1 = juniPolicyManagerTrafficClassRulesAgentV1.setProductRelease('Version 1 of the traffic class rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the traffic class\n        policy rules subcomponent was supported in JUNOSe 4.0 thru 5.2 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerTrafficClassRulesAgentV1 = juniPolicyManagerTrafficClassRulesAgentV1.setStatus('obsolete')
juniPolicyManagerTrafficClassRulesAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 11, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerTrafficClassRulesAgentV2 = juniPolicyManagerTrafficClassRulesAgentV2.setProductRelease('Version 2 of the traffic class rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the traffic class\n        policy rules subcomponent is supported in JUNOSe 5.3 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerTrafficClassRulesAgentV2 = juniPolicyManagerTrafficClassRulesAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-Policy-Manager-CONF", juniPolicyManagerAgent=juniPolicyManagerAgent, juniPolicyManagerRateLimitAgentV1=juniPolicyManagerRateLimitAgentV1, juniPolicyManagerNextHopRulesAgentV1=juniPolicyManagerNextHopRulesAgentV1, juniPolicyManagerForwardRulesAgentV3=juniPolicyManagerForwardRulesAgentV3, juniPolicyManagerRateLimitAgent=juniPolicyManagerRateLimitAgent, juniPolicyManagerColorRulesAgentV2=juniPolicyManagerColorRulesAgentV2, juniPolicyManagerColorRulesAgent=juniPolicyManagerColorRulesAgent, juniPolicyManagerMarkingRulesAgentV1=juniPolicyManagerMarkingRulesAgentV1, juniPolicyManagerNextInterfaceRulesAgentV2=juniPolicyManagerNextInterfaceRulesAgentV2, juniPolicyManagerTrafficClassRulesAgentV1=juniPolicyManagerTrafficClassRulesAgentV1, juniPolicyManagerBaseAgentV2=juniPolicyManagerBaseAgentV2, juniPolicyManagerTrafficShapeAgent=juniPolicyManagerTrafficShapeAgent, juniPolicyManagerTrafficClassRulesAgentV2=juniPolicyManagerTrafficClassRulesAgentV2, juniPolicyManagerFilterRulesAgentV2=juniPolicyManagerFilterRulesAgentV2, juniPolicyManagerLogRulesAgentV2=juniPolicyManagerLogRulesAgentV2, juniPolicyManagerForwardRulesAgent=juniPolicyManagerForwardRulesAgent, juniPolicyManagerFilterRulesAgentV1=juniPolicyManagerFilterRulesAgentV1, juniPolicyManagerMarkingRulesAgentV2=juniPolicyManagerMarkingRulesAgentV2, juniPolicyManagerRateLimitAgentV2=juniPolicyManagerRateLimitAgentV2, juniPolicyManagerForwardRulesAgentV2=juniPolicyManagerForwardRulesAgentV2, juniPolicyManagerForwardRulesAgentV1=juniPolicyManagerForwardRulesAgentV1, juniPolicyManagerNextHopRulesAgentV2=juniPolicyManagerNextHopRulesAgentV2, juniPolicyManagerBaseAgentV1=juniPolicyManagerBaseAgentV1, juniPolicyManagerBaseAgentV4=juniPolicyManagerBaseAgentV4, juniPolicyManagerNextInterfaceRulesAgentV1=juniPolicyManagerNextInterfaceRulesAgentV1, juniPolicyManagerTrafficClassRulesAgent=juniPolicyManagerTrafficClassRulesAgent, juniPolicyManagerRateLimitAgentV3=juniPolicyManagerRateLimitAgentV3, juniPolicyManagerFilterRulesAgent=juniPolicyManagerFilterRulesAgent, juniPolicyManagerBaseAgent=juniPolicyManagerBaseAgent, juniPolicyManagerBaseAgentV3=juniPolicyManagerBaseAgentV3, juniPolicyManagerMarkingRulesAgent=juniPolicyManagerMarkingRulesAgent, juniPolicyManagerNextInterfaceRulesAgent=juniPolicyManagerNextInterfaceRulesAgent, juniPolicyManagerLogRulesAgent=juniPolicyManagerLogRulesAgent, juniPolicyManagerColorRulesAgentV1=juniPolicyManagerColorRulesAgentV1, juniPolicyManagerNextHopRulesAgent=juniPolicyManagerNextHopRulesAgent, PYSNMP_MODULE_ID=juniPolicyManagerAgent, juniPolicyManagerTrafficShapeAgentV1=juniPolicyManagerTrafficShapeAgentV1, juniPolicyManagerLogRulesAgentV1=juniPolicyManagerLogRulesAgentV1)
