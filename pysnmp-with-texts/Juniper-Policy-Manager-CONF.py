#
# PySNMP MIB module Juniper-Policy-Manager-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Policy-Manager-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Bits, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, Unsigned32, ObjectIdentity, TimeTicks, IpAddress, iso, MibIdentifier, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "Unsigned32", "ObjectIdentity", "TimeTicks", "IpAddress", "iso", "MibIdentifier", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniPolicyManagerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31))
juniPolicyManagerAgent.setRevisions(('2005-08-08 18:21', '2005-02-01 15:58', '2003-10-21 19:20', '2003-08-26 12:51', '2002-09-06 16:54', '2002-08-02 12:07', '2001-09-07 15:27',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniPolicyManagerAgent.setRevisionsDescriptions(('Add support for ATM Cell Mode configuration.', 'Add attachment statistics preserve attribute.', 'Juniper-POLICY-MIB: Policy precedence enhancements. Route class policy feature support.', 'Juniper-POLICY-MIB: Added new forward rules data objects.', 'Juniper-POLICY-MIB: Replaced Unisphere names with Juniper names.', 'Juniper-POLICY-MIB: Added a capabilities statement for traffic class rules management. Extended rate limit profile objects. Obsoleted policy traffic shaped capabilities.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniPolicyManagerAgent.setLastUpdated('200508081821Z')
if mibBuilder.loadTexts: juniPolicyManagerAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniPolicyManagerAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniPolicyManagerAgent.setDescription('The agent capabilities definitions for the Policy Manager component of the SNMP agent in the Juniper E-series family of products.')
juniPolicyManagerBaseAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1))
if mibBuilder.loadTexts: juniPolicyManagerBaseAgent.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerBaseAgent.setDescription('The basic Policy Manager component of the Policy Manager application. MIB support for each specific policy rule type can run as a subcomponent in addition to this base component.')
juniPolicyManagerBaseAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerBaseAgentV1 = juniPolicyManagerBaseAgentV1.setProductRelease('Version 1 of the Policy Manager base component of the JUNOSe SNMP\n        agent.  This version of the Policy Manager base component was supported\n        in JUNOSe 3.2 thru 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerBaseAgentV1 = juniPolicyManagerBaseAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniPolicyManagerBaseAgentV1.setDescription('The MIB groups supported by the SNMP agent for the base component of the Policy Manager application in JUNOSe. These capabilities became obsolete when support was added to separate precedence from policy rule and apply it to classifier groups within a policy list.')
juniPolicyManagerBaseAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerBaseAgentV2 = juniPolicyManagerBaseAgentV2.setProductRelease('Version 2 of the Policy Manager base component of the JUNOSe SNMP\n        agent.  This version of the Policy Manager base component is supported\n        in JUNOSe 5.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerBaseAgentV2 = juniPolicyManagerBaseAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniPolicyManagerBaseAgentV2.setDescription('The MIB groups supported by the SNMP agent for the base component of the Policy Manager application in JUNOSe. These capabilities became obsolete when support was added for client based policy sharing.')
juniPolicyManagerBaseAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerBaseAgentV3 = juniPolicyManagerBaseAgentV3.setProductRelease('Version 3 of the Policy Manager base component of the JUNOSe SNMP\n        agent.  This version of the Policy Manager base component is supported\n        in JUNOSe 6.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerBaseAgentV3 = juniPolicyManagerBaseAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniPolicyManagerBaseAgentV3.setDescription('The MIB groups supported by the SNMP agent for the base component of the Policy Manager application in JUNOSe. These capabilities became obsolete when support was added to allow consideration for ATM cell tax when calculating statistics and rate limiting.')
juniPolicyManagerBaseAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerBaseAgentV4 = juniPolicyManagerBaseAgentV4.setProductRelease('Version 4 of the Policy Manager base component of the JUNOSe SNMP\n        agent.  This version of the Policy Manager base component is supported\n        in JUNOSe 7.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerBaseAgentV4 = juniPolicyManagerBaseAgentV4.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerBaseAgentV4.setDescription('The MIB groups supported by the SNMP agent for the base component of the Policy Manager application in JUNOSe.')
juniPolicyManagerRateLimitAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2))
if mibBuilder.loadTexts: juniPolicyManagerRateLimitAgent.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerRateLimitAgent.setDescription('The rate limit policy management component of the Policy Manager application. MIB support for this specific policy rule type subcomponent can run independently of the other subcomponents but requires the base component.')
juniPolicyManagerRateLimitAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerRateLimitAgentV1 = juniPolicyManagerRateLimitAgentV1.setProductRelease('Version 1 of the rate limit management subcomponent of the Policy\n        Manager component of the JUNOSe SNMP agent.  This version of the rate\n        limit policy management subcomponent was supported in JUNOSe 3.2 and\n        subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerRateLimitAgentV1 = juniPolicyManagerRateLimitAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniPolicyManagerRateLimitAgentV1.setDescription('The MIB group supported by the SNMP agent for the rate limit policy management subcomponent of the Policy Manager application in JUNOSe. These capabilities became obsolete when support was added for new rate limit objects.')
juniPolicyManagerRateLimitAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerRateLimitAgentV2 = juniPolicyManagerRateLimitAgentV2.setProductRelease('Version 2 of the rate limit management subcomponent of the Policy\n        Manager component of the JUNOSe SNMP agent.  This version of the rate\n        limit policy management subcomponent was supported in JUNOSe 4.0 thru\n        5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerRateLimitAgentV2 = juniPolicyManagerRateLimitAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniPolicyManagerRateLimitAgentV2.setDescription('The MIB group supported by the SNMP agent for the rate limit policy management subcomponent of the Policy Manager application in JUNOSe. These capabilities became obsolete when support was added to separate precedence from policy rule and apply it to classifier groups within a policy list.')
juniPolicyManagerRateLimitAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerRateLimitAgentV3 = juniPolicyManagerRateLimitAgentV3.setProductRelease('Version 3 of the rate limit management subcomponent of the Policy\n        Manager component of JUNOSe SNMP agent.  This version of the rate limit\n        policy management subcomponent is supported in the Juniper RX 5.3 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerRateLimitAgentV3 = juniPolicyManagerRateLimitAgentV3.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerRateLimitAgentV3.setDescription('The MIB group supported by the SNMP agent for the rate limit policy management subcomponent of the Policy Manager application in JUNOSe.')
juniPolicyManagerTrafficShapeAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 3))
if mibBuilder.loadTexts: juniPolicyManagerTrafficShapeAgent.setStatus('obsolete')
if mibBuilder.loadTexts: juniPolicyManagerTrafficShapeAgent.setDescription('The traffic shape policy management component of the Policy Manager application. MIB support for this specific policy rule type subcomponent can run independently of the other subcomponents but requires the base component.')
juniPolicyManagerTrafficShapeAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerTrafficShapeAgentV1 = juniPolicyManagerTrafficShapeAgentV1.setProductRelease('Version 1 of the traffic shape management subcomponent of the Policy\n        Manager component of the JUNOSe SNMP agent.  This version of the traffic\n        shape policy management subcomponent was supported in JUNOSe 3.2 and\n        subsequent 3.x system releases. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerTrafficShapeAgentV1 = juniPolicyManagerTrafficShapeAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniPolicyManagerTrafficShapeAgentV1.setDescription('The MIB group supported by the SNMP agent for the traffic shape policy management subcomponent of the Policy Manager application in JUNOSe. These capabilities became obsolete when the policy shaper capability was moved into the quality of service component.')
juniPolicyManagerLogRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 4))
if mibBuilder.loadTexts: juniPolicyManagerLogRulesAgent.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerLogRulesAgent.setDescription('The log policy rules component of the Policy Manager application. MIB support for this specific policy rule type subcomponent requires the base component but can run independently of the other subcomponents.')
juniPolicyManagerLogRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerLogRulesAgentV1 = juniPolicyManagerLogRulesAgentV1.setProductRelease('Version 1 of the log rules subcomponent of the Policy Manager component\n        of the JUNOSe SNMP agent.  This version of the log policy rules\n        subcomponent was supported in JUNOSe 3.2 thru 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerLogRulesAgentV1 = juniPolicyManagerLogRulesAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniPolicyManagerLogRulesAgentV1.setDescription('The MIB group supported by the SNMP agent for the log policy rules subcomponent of the Policy Manager application in JUNOSe. These capabilities became obsolete when support was added to separate precedence from policy rule and apply it to classifier groups within a policy list.')
juniPolicyManagerLogRulesAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 4, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerLogRulesAgentV2 = juniPolicyManagerLogRulesAgentV2.setProductRelease('Version 2 of the log rules subcomponent of the Policy Manager component\n        of the JUNOSe SNMP agent.  This version of the log policy rules\n        subcomponent is supported in JUNOSe 5.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerLogRulesAgentV2 = juniPolicyManagerLogRulesAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerLogRulesAgentV2.setDescription('The MIB group supported by the SNMP agent for the log policy rules subcomponent of the Policy Manager application in JUNOSe.')
juniPolicyManagerNextHopRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 5))
if mibBuilder.loadTexts: juniPolicyManagerNextHopRulesAgent.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerNextHopRulesAgent.setDescription('The next-hop policy rules component of the Policy Manager application. MIB support for this specific policy rule type subcomponent can run independently of the other subcomponents but requires the base component.')
juniPolicyManagerNextHopRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerNextHopRulesAgentV1 = juniPolicyManagerNextHopRulesAgentV1.setProductRelease('Version 1 of the next-hop rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the next-hop policy\n        rules subcomponent was supported in JUNOSe 3.2 thru 5.2 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerNextHopRulesAgentV1 = juniPolicyManagerNextHopRulesAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniPolicyManagerNextHopRulesAgentV1.setDescription('The MIB group supported by the SNMP agent for the next-hop policy rules subcomponent of the Policy Manager application in JUNOSe. These capabilities became obsolete when support was added to separate precedence from policy rule and apply it to classifier groups within a policy list.')
juniPolicyManagerNextHopRulesAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 5, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerNextHopRulesAgentV2 = juniPolicyManagerNextHopRulesAgentV2.setProductRelease('Version 2 of the next-hop rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the next-hop policy\n        rules subcomponent is supported in JUNOSe 5.3 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerNextHopRulesAgentV2 = juniPolicyManagerNextHopRulesAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerNextHopRulesAgentV2.setDescription('The MIB group supported by the SNMP agent for the next-hop policy rules subcomponent of the Policy Manager application in the JUNOSe.')
juniPolicyManagerFilterRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 6))
if mibBuilder.loadTexts: juniPolicyManagerFilterRulesAgent.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerFilterRulesAgent.setDescription('The filter policy rules component of the Policy Manager application. MIB support for this specific policy rule type subcomponent requires the base component but can run independently of the other subcomponents.')
juniPolicyManagerFilterRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerFilterRulesAgentV1 = juniPolicyManagerFilterRulesAgentV1.setProductRelease('Version 1 of the filter rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the filter policy\n        rules subcomponent is supported in JUNOSe 3.2 thru 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerFilterRulesAgentV1 = juniPolicyManagerFilterRulesAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniPolicyManagerFilterRulesAgentV1.setDescription('The MIB group supported by the SNMP agent for the filter policy rules subcomponent of the Policy Manager application in JUNOSe. These capabilities became obsolete when support was added to separate precedence from policy rule and apply it to classifier groups within a policy list.')
juniPolicyManagerFilterRulesAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 6, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerFilterRulesAgentV2 = juniPolicyManagerFilterRulesAgentV2.setProductRelease('Version 2 of the filter rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the filter policy\n        rules subcomponent is supported in JUNOSe 5.3 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerFilterRulesAgentV2 = juniPolicyManagerFilterRulesAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerFilterRulesAgentV2.setDescription('The MIB group supported by the SNMP agent for the filter policy rules subcomponent of the Policy Manager application in the JUNOSe.')
juniPolicyManagerNextInterfaceRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 7))
if mibBuilder.loadTexts: juniPolicyManagerNextInterfaceRulesAgent.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerNextInterfaceRulesAgent.setDescription('The next-interface policy rules component of the Policy Manager application. MIB support for this specific policy rule type subcomponent requires the base component but can run independently of the other subcomponents.')
juniPolicyManagerNextInterfaceRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 7, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerNextInterfaceRulesAgentV1 = juniPolicyManagerNextInterfaceRulesAgentV1.setProductRelease('Version 1 of the next-interface rules subcomponent of the Policy\n        Manager component of the JUNOSe SNMP agent.  This version of the\n        next-interface policy rules subcomponent was supported in JUNOSe 3.2\n        thru 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerNextInterfaceRulesAgentV1 = juniPolicyManagerNextInterfaceRulesAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniPolicyManagerNextInterfaceRulesAgentV1.setDescription('The MIB group supported by the SNMP agent for the next-interface policy rules subcomponent of the Policy Manager application in JUNOSe. These capabilities became obsolete when support was added to separate precedence from policy rule and apply it to classifier groups within a policy list.')
juniPolicyManagerNextInterfaceRulesAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 7, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerNextInterfaceRulesAgentV2 = juniPolicyManagerNextInterfaceRulesAgentV2.setProductRelease('Version 2 of the next-interface rules subcomponent of the Policy\n        Manager component of the JUNOSe SNMP agent.  This version of the\n        next-interface policy rules subcomponent is supported in JUNOSe 5.3 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerNextInterfaceRulesAgentV2 = juniPolicyManagerNextInterfaceRulesAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerNextInterfaceRulesAgentV2.setDescription('The MIB group supported by the SNMP agent for the next-interface policy rules subcomponent of the Policy Manager application in JUNOSe.')
juniPolicyManagerMarkingRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 8))
if mibBuilder.loadTexts: juniPolicyManagerMarkingRulesAgent.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerMarkingRulesAgent.setDescription('The marking policy rules component of the Policy Manager application. MIB support for this specific policy rule type subcomponent requires the base component but can run independently of the other subcomponents.')
juniPolicyManagerMarkingRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 8, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerMarkingRulesAgentV1 = juniPolicyManagerMarkingRulesAgentV1.setProductRelease('Version 1 of the marking rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the marking policy\n        rules subcomponent was supported in JUNOSe 3.2 thru 5.2 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerMarkingRulesAgentV1 = juniPolicyManagerMarkingRulesAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniPolicyManagerMarkingRulesAgentV1.setDescription('The MIB group supported by the SNMP agent for the marking policy rules subcomponent of the Policy Manager application in JUNOSe. These capabilities became obsolete when support was added to separate precedence from policy rule and apply it to classifier groups within a policy list.')
juniPolicyManagerMarkingRulesAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 8, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerMarkingRulesAgentV2 = juniPolicyManagerMarkingRulesAgentV2.setProductRelease('Version 2 of the marking rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the marking policy\n        rules subcomponent is supported in JUNOSe 5.3 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerMarkingRulesAgentV2 = juniPolicyManagerMarkingRulesAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerMarkingRulesAgentV2.setDescription('The MIB group supported by the SNMP agent for the marking policy rules subcomponent of the Policy Manager application in JUNOSe.')
juniPolicyManagerForwardRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 9))
if mibBuilder.loadTexts: juniPolicyManagerForwardRulesAgent.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerForwardRulesAgent.setDescription('The forward policy rules component of the Policy Manager application. MIB support for this specific policy rule type subcomponent requires the base component but can run independently of the other subcomponents.')
juniPolicyManagerForwardRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 9, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerForwardRulesAgentV1 = juniPolicyManagerForwardRulesAgentV1.setProductRelease('Version 1 of the forward rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the forward policy\n        rules subcomponent was supported in JUNOSe 3.2 thru 5.1 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerForwardRulesAgentV1 = juniPolicyManagerForwardRulesAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniPolicyManagerForwardRulesAgentV1.setDescription('The MIB group supported by the SNMP agent for the forward policy rules subcomponent of the Policy Manager application in JUNOSe. These capabilities became obsolete when support was added for new forward rules objects.')
juniPolicyManagerForwardRulesAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 9, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerForwardRulesAgentV2 = juniPolicyManagerForwardRulesAgentV2.setProductRelease('Version 2 of the forward rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the forward policy\n        rules subcomponent was supported in JUNOSe 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerForwardRulesAgentV2 = juniPolicyManagerForwardRulesAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniPolicyManagerForwardRulesAgentV2.setDescription('The MIB group supported by the SNMP agent for the forward policy rules subcomponent of the Policy Manager application in JUNOSe. These capabilities became obsolete when support was added to separate precedence from policy rule and apply it to classifier groups within a policy list.')
juniPolicyManagerForwardRulesAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 9, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerForwardRulesAgentV3 = juniPolicyManagerForwardRulesAgentV3.setProductRelease('Version 3 of the forward rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the forward policy\n        rules subcomponent is supported in JUNOSe 5.3 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerForwardRulesAgentV3 = juniPolicyManagerForwardRulesAgentV3.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerForwardRulesAgentV3.setDescription('The MIB group supported by the SNMP agent for the forward policy rules subcomponent of the Policy Manager application in JUNOSe.')
juniPolicyManagerColorRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 10))
if mibBuilder.loadTexts: juniPolicyManagerColorRulesAgent.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerColorRulesAgent.setDescription('The color policy rules component of the Policy Manager application. MIB support for this specific policy rule type subcomponent requires the base component but can run independently of the other subcomponents.')
juniPolicyManagerColorRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 10, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerColorRulesAgentV1 = juniPolicyManagerColorRulesAgentV1.setProductRelease('Version 1 of the color rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the color policy\n        rules subcomponent was supported in JUNOSe 3.2 thru 5.2 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerColorRulesAgentV1 = juniPolicyManagerColorRulesAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniPolicyManagerColorRulesAgentV1.setDescription('The MIB group supported by the SNMP agent for the color policy rules subcomponent of the Policy Manager application in JUNOSe. These capabilities became obsolete when support was added to separate precedence from policy rule and apply it to classifier groups within a policy list.')
juniPolicyManagerColorRulesAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 10, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerColorRulesAgentV2 = juniPolicyManagerColorRulesAgentV2.setProductRelease('Version 2 of the color rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the color policy\n        rules subcomponent is supported in JUNOSe 5.3 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerColorRulesAgentV2 = juniPolicyManagerColorRulesAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerColorRulesAgentV2.setDescription('The MIB group supported by the SNMP agent for the color policy rules subcomponent of the Policy Manager application in JUNOSe.')
juniPolicyManagerTrafficClassRulesAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 11))
if mibBuilder.loadTexts: juniPolicyManagerTrafficClassRulesAgent.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerTrafficClassRulesAgent.setDescription('The traffic class policy rules component of the Policy Manager application. MIB support for this specific policy rule type subcomponent requires the base component but can run independently of the other subcomponents.')
juniPolicyManagerTrafficClassRulesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 11, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerTrafficClassRulesAgentV1 = juniPolicyManagerTrafficClassRulesAgentV1.setProductRelease('Version 1 of the traffic class rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the traffic class\n        policy rules subcomponent was supported in JUNOSe 4.0 thru 5.2 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerTrafficClassRulesAgentV1 = juniPolicyManagerTrafficClassRulesAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniPolicyManagerTrafficClassRulesAgentV1.setDescription('The MIB group supported by the SNMP agent for the traffic class policy rules subcomponent of the Policy Manager application in JUNOSe. These capabilities became obsolete when support was added to separate precedence from policy rule and apply it to classifier groups within a policy list.')
juniPolicyManagerTrafficClassRulesAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 11, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerTrafficClassRulesAgentV2 = juniPolicyManagerTrafficClassRulesAgentV2.setProductRelease('Version 2 of the traffic class rules subcomponent of the Policy Manager\n        component of the JUNOSe SNMP agent.  This version of the traffic class\n        policy rules subcomponent is supported in JUNOSe 5.3 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPolicyManagerTrafficClassRulesAgentV2 = juniPolicyManagerTrafficClassRulesAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniPolicyManagerTrafficClassRulesAgentV2.setDescription('The MIB group supported by the SNMP agent for the traffic class policy rules subcomponent of the Policy Manager application in the JUNOSe.')
mibBuilder.exportSymbols("Juniper-Policy-Manager-CONF", juniPolicyManagerTrafficClassRulesAgentV2=juniPolicyManagerTrafficClassRulesAgentV2, juniPolicyManagerRateLimitAgentV2=juniPolicyManagerRateLimitAgentV2, juniPolicyManagerLogRulesAgentV1=juniPolicyManagerLogRulesAgentV1, juniPolicyManagerBaseAgentV4=juniPolicyManagerBaseAgentV4, juniPolicyManagerRateLimitAgent=juniPolicyManagerRateLimitAgent, juniPolicyManagerFilterRulesAgentV1=juniPolicyManagerFilterRulesAgentV1, juniPolicyManagerNextInterfaceRulesAgent=juniPolicyManagerNextInterfaceRulesAgent, juniPolicyManagerForwardRulesAgent=juniPolicyManagerForwardRulesAgent, juniPolicyManagerFilterRulesAgent=juniPolicyManagerFilterRulesAgent, juniPolicyManagerMarkingRulesAgent=juniPolicyManagerMarkingRulesAgent, juniPolicyManagerBaseAgentV3=juniPolicyManagerBaseAgentV3, juniPolicyManagerNextHopRulesAgentV2=juniPolicyManagerNextHopRulesAgentV2, juniPolicyManagerFilterRulesAgentV2=juniPolicyManagerFilterRulesAgentV2, juniPolicyManagerRateLimitAgentV1=juniPolicyManagerRateLimitAgentV1, juniPolicyManagerMarkingRulesAgentV2=juniPolicyManagerMarkingRulesAgentV2, juniPolicyManagerMarkingRulesAgentV1=juniPolicyManagerMarkingRulesAgentV1, juniPolicyManagerColorRulesAgentV1=juniPolicyManagerColorRulesAgentV1, juniPolicyManagerBaseAgentV1=juniPolicyManagerBaseAgentV1, juniPolicyManagerLogRulesAgentV2=juniPolicyManagerLogRulesAgentV2, juniPolicyManagerForwardRulesAgentV1=juniPolicyManagerForwardRulesAgentV1, juniPolicyManagerForwardRulesAgentV3=juniPolicyManagerForwardRulesAgentV3, juniPolicyManagerTrafficShapeAgent=juniPolicyManagerTrafficShapeAgent, juniPolicyManagerTrafficClassRulesAgent=juniPolicyManagerTrafficClassRulesAgent, juniPolicyManagerNextInterfaceRulesAgentV1=juniPolicyManagerNextInterfaceRulesAgentV1, juniPolicyManagerColorRulesAgent=juniPolicyManagerColorRulesAgent, juniPolicyManagerForwardRulesAgentV2=juniPolicyManagerForwardRulesAgentV2, juniPolicyManagerTrafficShapeAgentV1=juniPolicyManagerTrafficShapeAgentV1, juniPolicyManagerColorRulesAgentV2=juniPolicyManagerColorRulesAgentV2, juniPolicyManagerAgent=juniPolicyManagerAgent, juniPolicyManagerNextHopRulesAgentV1=juniPolicyManagerNextHopRulesAgentV1, juniPolicyManagerNextInterfaceRulesAgentV2=juniPolicyManagerNextInterfaceRulesAgentV2, PYSNMP_MODULE_ID=juniPolicyManagerAgent, juniPolicyManagerNextHopRulesAgent=juniPolicyManagerNextHopRulesAgent, juniPolicyManagerLogRulesAgent=juniPolicyManagerLogRulesAgent, juniPolicyManagerBaseAgentV2=juniPolicyManagerBaseAgentV2, juniPolicyManagerRateLimitAgentV3=juniPolicyManagerRateLimitAgentV3, juniPolicyManagerTrafficClassRulesAgentV1=juniPolicyManagerTrafficClassRulesAgentV1, juniPolicyManagerBaseAgent=juniPolicyManagerBaseAgent)
