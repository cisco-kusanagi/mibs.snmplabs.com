#
# PySNMP MIB module Unisphere-Data-Policy-Manager-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Policy-Manager-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Integer32, Gauge32, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Bits, iso, ObjectIdentity, Counter64, Unsigned32, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Bits", "iso", "ObjectIdentity", "Counter64", "Unsigned32", "IpAddress", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdTrafficClassRulesGroup, usdTrafficShapeGroup, usdPolicyAttachStatisticsGroup, usdLogRuleGroup, usdForwardRulesGroup, usdRateLimitGroup, usdRateLimitGroup2, usdPolicyBaseGroup, usdNextHopRulesGroup, usdColorRulesGroup, usdPolicyAttachProfileGroup, usdClassifierControlListGroup2, usdNextInterfaceRulesGroup, usdMarkingRulesGroup, usdPolicyIfAttachGroup, usdFilterRulesGroup = mibBuilder.importSymbols("Unisphere-Data-POLICY-MIB", "usdTrafficClassRulesGroup", "usdTrafficShapeGroup", "usdPolicyAttachStatisticsGroup", "usdLogRuleGroup", "usdForwardRulesGroup", "usdRateLimitGroup", "usdRateLimitGroup2", "usdPolicyBaseGroup", "usdNextHopRulesGroup", "usdColorRulesGroup", "usdPolicyAttachProfileGroup", "usdClassifierControlListGroup2", "usdNextInterfaceRulesGroup", "usdMarkingRulesGroup", "usdPolicyIfAttachGroup", "usdFilterRulesGroup")
usdPolicyManagerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31))
usdPolicyManagerAgent.setRevisions(('2002-08-02 12:07', '2001-09-07 15:27',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdPolicyManagerAgent.setRevisionsDescriptions(('Added a capabilities statement for traffic class rules management. Extended rate limit profile objects. Obsoleted policy traffic shaped capabilities.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdPolicyManagerAgent.setLastUpdated('200208021207Z')
if mibBuilder.loadTexts: usdPolicyManagerAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: usdPolicyManagerAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdPolicyManagerAgent.setDescription('The agent capabilities definitions for the Policy Manager component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdPolicyManagerBaseAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1))
if mibBuilder.loadTexts: usdPolicyManagerBaseAgent.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerBaseAgent.setDescription('The basic Policy Manager component of the Policy Manager application. MIB support for each specific policy rule type can run as a subcomponent in addition to this base component.')
usdPolicyManagerBaseAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerBaseAgentV1 = usdPolicyManagerBaseAgentV1.setProductRelease('Version 1 of the Policy Manager base component of the Unisphere Routing\n        Switch SNMP agent.  This version of the Policy Manager base component is\n        supported in the Unisphere RX 3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerBaseAgentV1 = usdPolicyManagerBaseAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerBaseAgentV1.setDescription('The MIB groups supported by the SNMP agent for the base component of the Policy Manager application in the Unisphere Routing Switch.')
usdPolicyManagerRateLimitAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2))
if mibBuilder.loadTexts: usdPolicyManagerRateLimitAgent.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerRateLimitAgent.setDescription('The rate limit policy management component of the Policy Manager application. MIB support for this specific policy rule type subcomponent can run independently of the other subcomponents but requires the base component.')
usdPolicyManagerRateLimitAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerRateLimitAgentV1 = usdPolicyManagerRateLimitAgentV1.setProductRelease('Version 1 of the rate limit management subcomponent of the Policy\n        Manager component of the Unisphere Routing Switch SNMP agent.  This\n        version of the rate limit policy management subcomponent was supported\n        in the Unisphere RX 3.2 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerRateLimitAgentV1 = usdPolicyManagerRateLimitAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdPolicyManagerRateLimitAgentV1.setDescription('The MIB group supported by the SNMP agent for the rate limit policy management subcomponent of the Policy Manager application in the Unisphere Routing Switch. These capabilities became obsolete when support was added for new rate limit objects.')
usdPolicyManagerRateLimitAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerRateLimitAgentV2 = usdPolicyManagerRateLimitAgentV2.setProductRelease('Version 2 of the rate limit management subcomponent of the Policy\n        Manager component of the Unisphere Routing Switch SNMP agent.  This\n        version of the rate limit policy management subcomponent is supported in\n        the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerRateLimitAgentV2 = usdPolicyManagerRateLimitAgentV2.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerRateLimitAgentV2.setDescription('The MIB group supported by the SNMP agent for the rate limit policy management subcomponent of the Policy Manager application in the Unisphere Routing Switch.')
usdPolicyManagerTrafficShapeAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 3))
if mibBuilder.loadTexts: usdPolicyManagerTrafficShapeAgent.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerTrafficShapeAgent.setDescription('The traffic shape policy management component of the Policy Manager application. MIB support for this specific policy rule type subcomponent can run independently of the other subcomponents but requires the base component.')
usdPolicyManagerTrafficShapeAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerTrafficShapeAgentV1 = usdPolicyManagerTrafficShapeAgentV1.setProductRelease('Version 1 of the traffic shape management subcomponent of the Policy\n        Manager component of the Unisphere Routing Switch SNMP agent.  This\n        version of the traffic shape policy management subcomponent was\n        supported in the Unisphere RX 3.2 and subsequent 3.x system releases. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerTrafficShapeAgentV1 = usdPolicyManagerTrafficShapeAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdPolicyManagerTrafficShapeAgentV1.setDescription('The MIB group supported by the SNMP agent for the traffic shape policy management subcomponent of the Policy Manager application in the Unisphere Routing Switch. These capabilities became obsolete when the policy shaper capability was moved into the quality of service component.')
usdPolicyManagerLogRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 4))
if mibBuilder.loadTexts: usdPolicyManagerLogRulesAgent.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerLogRulesAgent.setDescription('The log policy rules component of the Policy Manager application. MIB support for this specific policy rule type subcomponent requires the base component but can run independently of the other subcomponents.')
usdPolicyManagerLogRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerLogRulesAgentV1 = usdPolicyManagerLogRulesAgentV1.setProductRelease('Version 1 of the log rules subcomponent of the Policy Manager component\n        of the Unisphere Routing Switch SNMP agent.  This version of the log\n        policy rules subcomponent is supported in the Unisphere RX 3.2 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerLogRulesAgentV1 = usdPolicyManagerLogRulesAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerLogRulesAgentV1.setDescription('The MIB group supported by the SNMP agent for the log policy rules subcomponent of the Policy Manager application in the Unisphere Routing Switch.')
usdPolicyManagerNextHopRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 5))
if mibBuilder.loadTexts: usdPolicyManagerNextHopRulesAgent.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerNextHopRulesAgent.setDescription('The next-hop policy rules component of the Policy Manager application. MIB support for this specific policy rule type subcomponent can run independently of the other subcomponents but requires the base component.')
usdPolicyManagerNextHopRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerNextHopRulesAgentV1 = usdPolicyManagerNextHopRulesAgentV1.setProductRelease('Version 1 of the next-hop rules subcomponent of the Policy Manager\n        component of the Unisphere Routing Switch SNMP agent.  This version of\n        the next-hop policy rules subcomponent is supported in the Unisphere RX\n        3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerNextHopRulesAgentV1 = usdPolicyManagerNextHopRulesAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerNextHopRulesAgentV1.setDescription('The MIB group supported by the SNMP agent for the next-hop policy rules subcomponent of the Policy Manager application in the Unisphere Routing Switch.')
usdPolicyManagerFilterRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 6))
if mibBuilder.loadTexts: usdPolicyManagerFilterRulesAgent.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerFilterRulesAgent.setDescription('The filter policy rules component of the Policy Manager application. MIB support for this specific policy rule type subcomponent requires the base component but can run independently of the other subcomponents.')
usdPolicyManagerFilterRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerFilterRulesAgentV1 = usdPolicyManagerFilterRulesAgentV1.setProductRelease('Version 1 of the filter rules subcomponent of the Policy Manager\n        component of the Unisphere Routing Switch SNMP agent.  This version of\n        the filter policy rules subcomponent is supported in the Unisphere RX\n        3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerFilterRulesAgentV1 = usdPolicyManagerFilterRulesAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerFilterRulesAgentV1.setDescription('The MIB group supported by the SNMP agent for the filter policy rules subcomponent of the Policy Manager application in the Unisphere Routing Switch.')
usdPolicyManagerNextInterfaceRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 7))
if mibBuilder.loadTexts: usdPolicyManagerNextInterfaceRulesAgent.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerNextInterfaceRulesAgent.setDescription('The next-interface policy rules component of the Policy Manager application. MIB support for this specific policy rule type subcomponent requires the base component but can run independently of the other subcomponents.')
usdPolicyManagerNextInterfaceRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 7, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerNextInterfaceRulesAgentV1 = usdPolicyManagerNextInterfaceRulesAgentV1.setProductRelease('Version 1 of the next-interface rules subcomponent of the Policy\n        Manager component of the Unisphere Routing Switch SNMP agent.  This\n        version of the next-interface policy rules subcomponent is supported in\n        the Unisphere RX 3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerNextInterfaceRulesAgentV1 = usdPolicyManagerNextInterfaceRulesAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerNextInterfaceRulesAgentV1.setDescription('The MIB group supported by the SNMP agent for the next-interface policy rules subcomponent of the Policy Manager application in the Unisphere Routing Switch.')
usdPolicyManagerMarkingRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 8))
if mibBuilder.loadTexts: usdPolicyManagerMarkingRulesAgent.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerMarkingRulesAgent.setDescription('The marking policy rules component of the Policy Manager application. MIB support for this specific policy rule type subcomponent requires the base component but can run independently of the other subcomponents.')
usdPolicyManagerMarkingRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 8, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerMarkingRulesAgentV1 = usdPolicyManagerMarkingRulesAgentV1.setProductRelease('Version 1 of the marking rules subcomponent of the Policy Manager\n        component of the Unisphere Routing Switch SNMP agent.  This version of\n        the marking policy rules subcomponent is supported in the Unisphere RX\n        3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerMarkingRulesAgentV1 = usdPolicyManagerMarkingRulesAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerMarkingRulesAgentV1.setDescription('The MIB group supported by the SNMP agent for the marking policy rules subcomponent of the Policy Manager application in the Unisphere Routing Switch.')
usdPolicyManagerForwardRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 9))
if mibBuilder.loadTexts: usdPolicyManagerForwardRulesAgent.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerForwardRulesAgent.setDescription('The forward policy rules component of the Policy Manager application. MIB support for this specific policy rule type subcomponent requires the base component but can run independently of the other subcomponents.')
usdPolicyManagerForwardRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 9, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerForwardRulesAgentV1 = usdPolicyManagerForwardRulesAgentV1.setProductRelease('Version 1 of the forward rules subcomponent of the Policy Manager\n        component of the Unisphere Routing Switch SNMP agent.  This version of\n        the forward policy rules subcomponent is supported in the Unisphere RX\n        3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerForwardRulesAgentV1 = usdPolicyManagerForwardRulesAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerForwardRulesAgentV1.setDescription('The MIB group supported by the SNMP agent for the forward policy rules subcomponent of the Policy Manager application in the Unisphere Routing Switch.')
usdPolicyManagerColorRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 10))
if mibBuilder.loadTexts: usdPolicyManagerColorRulesAgent.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerColorRulesAgent.setDescription('The color policy rules component of the Policy Manager application. MIB support for this specific policy rule type subcomponent requires the base component but can run independently of the other subcomponents.')
usdPolicyManagerColorRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 10, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerColorRulesAgentV1 = usdPolicyManagerColorRulesAgentV1.setProductRelease('Version 1 of the color rules subcomponent of the Policy Manager\n        component of the Unisphere Routing Switch SNMP agent.  This version of\n        the color policy rules subcomponent is supported in the Unisphere RX 3.2\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerColorRulesAgentV1 = usdPolicyManagerColorRulesAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerColorRulesAgentV1.setDescription('The MIB group supported by the SNMP agent for the color policy rules subcomponent of the Policy Manager application in the Unisphere Routing Switch.')
usdPolicyManagerTrafficClassRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 11))
if mibBuilder.loadTexts: usdPolicyManagerTrafficClassRulesAgent.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerTrafficClassRulesAgent.setDescription('The traffic class policy rules component of the Policy Manager application. MIB support for this specific policy rule type subcomponent requires the base component but can run independently of the other subcomponents.')
usdPolicyManagerTrafficClassRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 11, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerTrafficClassRulesAgentV1 = usdPolicyManagerTrafficClassRulesAgentV1.setProductRelease('Version 1 of the traffic class rules subcomponent of the Policy Manager\n        component of the Unisphere Routing Switch SNMP agent.  This version of\n        the traffic class policy rules subcomponent is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPolicyManagerTrafficClassRulesAgentV1 = usdPolicyManagerTrafficClassRulesAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdPolicyManagerTrafficClassRulesAgentV1.setDescription('The MIB group supported by the SNMP agent for the traffic class policy rules subcomponent of the Policy Manager application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-Policy-Manager-CONF", PYSNMP_MODULE_ID=usdPolicyManagerAgent, usdPolicyManagerFilterRulesAgentV1=usdPolicyManagerFilterRulesAgentV1, usdPolicyManagerNextInterfaceRulesAgentV1=usdPolicyManagerNextInterfaceRulesAgentV1, usdPolicyManagerRateLimitAgent=usdPolicyManagerRateLimitAgent, usdPolicyManagerLogRulesAgent=usdPolicyManagerLogRulesAgent, usdPolicyManagerForwardRulesAgentV1=usdPolicyManagerForwardRulesAgentV1, usdPolicyManagerColorRulesAgent=usdPolicyManagerColorRulesAgent, usdPolicyManagerRateLimitAgentV1=usdPolicyManagerRateLimitAgentV1, usdPolicyManagerTrafficShapeAgent=usdPolicyManagerTrafficShapeAgent, usdPolicyManagerColorRulesAgentV1=usdPolicyManagerColorRulesAgentV1, usdPolicyManagerBaseAgentV1=usdPolicyManagerBaseAgentV1, usdPolicyManagerFilterRulesAgent=usdPolicyManagerFilterRulesAgent, usdPolicyManagerAgent=usdPolicyManagerAgent, usdPolicyManagerBaseAgent=usdPolicyManagerBaseAgent, usdPolicyManagerNextHopRulesAgentV1=usdPolicyManagerNextHopRulesAgentV1, usdPolicyManagerNextInterfaceRulesAgent=usdPolicyManagerNextInterfaceRulesAgent, usdPolicyManagerForwardRulesAgent=usdPolicyManagerForwardRulesAgent, usdPolicyManagerMarkingRulesAgent=usdPolicyManagerMarkingRulesAgent, usdPolicyManagerNextHopRulesAgent=usdPolicyManagerNextHopRulesAgent, usdPolicyManagerTrafficClassRulesAgent=usdPolicyManagerTrafficClassRulesAgent, usdPolicyManagerLogRulesAgentV1=usdPolicyManagerLogRulesAgentV1, usdPolicyManagerRateLimitAgentV2=usdPolicyManagerRateLimitAgentV2, usdPolicyManagerMarkingRulesAgentV1=usdPolicyManagerMarkingRulesAgentV1, usdPolicyManagerTrafficShapeAgentV1=usdPolicyManagerTrafficShapeAgentV1, usdPolicyManagerTrafficClassRulesAgentV1=usdPolicyManagerTrafficClassRulesAgentV1)
