#
# PySNMP MIB module Juniper-RADIUS-CLIENT-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-RADIUS-CLIENT-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:04:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Bits, IpAddress, ModuleIdentity, Gauge32, Counter64, iso, NotificationType, MibIdentifier, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Bits", "IpAddress", "ModuleIdentity", "Gauge32", "Counter64", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniRadiusClientAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35))
juniRadiusClientAgent.setRevisions(('2009-02-10 15:20', '2007-12-14 15:00', '2007-09-18 18:22', '2007-04-10 01:03', '2006-02-17 22:00', '2006-01-12 22:00', '2004-12-06 02:32', '2004-12-03 22:12', '2003-12-18 21:03', '2003-05-21 19:18', '2003-03-10 19:51', '2003-01-27 18:36', '2002-11-21 19:26', '2001-10-19 14:44', '2001-10-16 20:45', '2001-09-07 12:35',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniRadiusClientAgent.setRevisionsDescriptions(('Added rsRadiusClientIncludeIpv6AccountingInAcctStop. Added rsRadiusClientIncludeDelegatedIpv6PrefixInAcctStart, rsRadiusClientIncludeDelegatedIpv6PrefixInAcctStop, rsRadiusClientIncludeFramedIpv6PoolInAcctStart, rsRadiusClientIncludeFramedIpv6PoolInAcctStop, rsRadiusClientIncludeFramedIpv6RouteInAcctStart, rsRadiusClientIncludeFramedIpv6RouteInAcctStop, rsRadiusClientIncludeIpv6LocalInterfaceInAcctStart, rsRadiusClientIncludeIpv6LocalInterfaceInAcctStop, rsRadiusClientIncludeIpv6NdRaPrefixInAcctStart, rsRadiusClientIncludeIpv6NdRaPrefixInAcctStop, rsRadiusClientIncludeIpv6PrimaryDnsInAcctStart, rsRadiusClientIncludeIpv6PrimaryDnsInAcctStop, rsRadiusClientIncludeIpv6SecondaryDnsInAcctStart, rsRadiusClientIncludeIpv6SecondaryDnsInAcctStop, rsRadiusClientIncludeIpv6VirtualRouterInAcctStart, rsRadiusClientIncludeIpv6VirtualRouterInAcctStop.', 'Added rsRadiusClientIncludeDownStreamCalculatedQosRateInAccessReq, rsRadiusClientIncludeUpStreamCalculatedQosRateInAccessReq, rsRadiusClientIncludeDownStreamCalculatedQosRateInAcctStart, rsRadiusClientIncludeUpStreamCalculatedQosRateInAcctStart, rsRadiusClientIncludeDownStreamCalculatedQosRateInAcctStop, rsRadiusClientIncludeUpStreamCalculatedQosRateInAcctStop.', 'Added rsRadiusClientIncludeInterfaceIdInAcctStart, rsRadiusClientIncludeIpv6PrefixInAcctStart, rsRadiusClientIncludeInterfaceIdInAcctStop, rsRadiusClientIncludeIpAddrInAcctStop, rsRadiusClientIncludeIpv6PrefixInAcctStop.', 'Added rsRadiusClientIncludeL2cAccessLoopCircuitIdInAccessReq, rsRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAccessReq, rsRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAccessReq, rsRadiusClientIncludeL2cActualDataRateUstrInAccessReq, rsRadiusClientIncludeL2cActualDataRateDstrInAccessReq, rsRadiusClientIncludeL2cMinimumDataRateUstrInAccessReq, rsRadiusClientIncludeL2cMinimumDataRateDstrInAccessReq, rsRadiusClientIncludeL2cAttainDataRateUstrInAccessReq, rsRadiusClientIncludeL2cAttainDataRateDstrInAccessReq, rsRadiusClientIncludeL2cMaximumDataRateUstrInAccessReq, rsRadiusClientIncludeL2cMaximumDataRateDstrInAccessReq, rsRadiusClientIncludeL2cMinLowPowerDataRateUstrInAccessReq, rsRadiusClientIncludeL2cMinLowPowerDataRateDstrInAccessReq, rsRadiusClientIncludeL2cMaxInterleavingDelayUstrInAccessReq, rsRadiusClientIncludeL2cActInterleavingDelayUstrInAccessReq, rsRadiusClientIncludeL2cMaxInterleavingDelayDstrInAccessReq, rsRadiusClientIncludeL2cActInterleavingDelayDstrInAccessReq, rsRadiusClientIncludeL2cDslLineStateInAccessReq, rsRadiusClientIncludeL2cDslTypeInAccessReq, rsRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStart, rsRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStart, rsRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStart, rsRadiusClientIncludeL2cActualDataRateUstrInAcctStart, rsRadiusClientIncludeL2cActualDataRateDstrInAcctStart, rsRadiusClientIncludeL2cMinimumDataRateUstrInAcctStart, rsRadiusClientIncludeL2cMinimumDataRateDstrInAcctStart, rsRadiusClientIncludeL2cAttainDataRateUstrInAcctStart, rsRadiusClientIncludeL2cAttainDataRateDstrInAcctStart, rsRadiusClientIncludeL2cMaximumDataRateUstrInAcctStart, rsRadiusClientIncludeL2cMaximumDataRateDstrInAcctStart, rsRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStart, rsRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStart, rsRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStart, rsRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStart, rsRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStart, rsRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStart, rsRadiusClientIncludeL2cDslLineStateInAcctStart, rsRadiusClientIncludeL2cDslTypeInAcctStart, rsRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStop, rsRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStop, rsRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStop, rsRadiusClientIncludeL2cActualDataRateUstrInAcctStop, rsRadiusClientIncludeL2cActualDataRateDstrInAcctStop, rsRadiusClientIncludeL2cMinimumDataRateUstrInAcctStop, rsRadiusClientIncludeL2cMinimumDataRateDstrInAcctStop, rsRadiusClientIncludeL2cAttainDataRateUstrInAcctStop, rsRadiusClientIncludeL2cAttainDataRateDstrInAcctStop, rsRadiusClientIncludeL2cMaximumDataRateUstrInAcctStop, rsRadiusClientIncludeL2cMaximumDataRateDstrInAcctStop, rsRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStop, rsRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStop, rsRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStop, rsRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStop, rsRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStop, rsRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStop, rsRadiusClientIncludeL2cDslLineStateInAcctStop, rsRadiusClientIncludeL2cDslTypeInAcctStop allowing to control generation and format of decoded L2C Attributes.', 'Added new objects BRAS group to allow inclusion of DSL Forum attributes into radius requests.', 'Added new objects BRAS group to allow inclusion of L2C information, L2C up and down stream data into radius requests.', 'Added new objects BRAS group to allow inclusion of interface description into radius requests.', 'Added a new object to the BRAS group to allow override of nas-ip-address and nas-identifier from authentication router. Added new objects to the BRAS group to allow override of nas-port-id and calling-station-id with PPPoE Remote Circuit Id.', 'A new object was added to the BRAS group to indicate which RADIUS attributes should be included or excluded from RADIUS packets.', 'Added new accounting counters.', 'Added new configuration objects.', 'Replaced Unisphere names with Juniper names. Added objects to ignore attributes from the access-accept RADIUS packets. Added objects for RADIUS trap enable/disable control and detailed accounting statistics. Added notifications for available RADIUS servers.', 'Added notifications for unavailable RADIUS servers.', 'New objects were added to the BRAS group to indicate which RADIUS attributes should be included or excluded from RADIUS packets.', 'A new object was added to the BRAS group.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniRadiusClientAgent.setLastUpdated('200902101520Z')
if mibBuilder.loadTexts: juniRadiusClientAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniRadiusClientAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniRadiusClientAgent.setDescription('The agent capabilities definitions for the Remote Authentication Dial In User Service (RADIUS) Client component of the SNMP agent in the Juniper E-series family of products.')
juniRadiusClientDynamicAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1))
if mibBuilder.loadTexts: juniRadiusClientDynamicAgent.setStatus('current')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgent.setDescription('The registration group of agent capabilities for RADIUS Client application which provides complete dynamic interface support in addition to basic authentication for CLI access.')
juniRadiusClientDynamicAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV1 = juniRadiusClientDynamicAgentV1.setProductRelease('Version 1 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 1.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV1 = juniRadiusClientDynamicAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV1.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe. These capabilities became obsolete when a new object was added.')
juniRadiusClientDynamicAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV2 = juniRadiusClientDynamicAgentV2.setProductRelease('Version 2 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV2 = juniRadiusClientDynamicAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV2.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe. These capabilities became obsolete when new objects were added.')
juniRadiusClientDynamicAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV3 = juniRadiusClientDynamicAgentV3.setProductRelease('Version 3 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 3.0 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV3 = juniRadiusClientDynamicAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV3.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe. These capabilities became obsolete when new B-RAS objects were added.')
juniRadiusClientDynamicAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV4 = juniRadiusClientDynamicAgentV4.setProductRelease('Version 4 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 3.1 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV4 = juniRadiusClientDynamicAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV4.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe. These capabilities became obsolete when new objects were added.')
juniRadiusClientDynamicAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV5 = juniRadiusClientDynamicAgentV5.setProductRelease('Version 5 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 3.2 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV5 = juniRadiusClientDynamicAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV5.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe. These capabilities became obsolete when a new object was added to the BRAS group.')
juniRadiusClientDynamicAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV6 = juniRadiusClientDynamicAgentV6.setProductRelease('Version 6 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 3.3 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV6 = juniRadiusClientDynamicAgentV6.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV6.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe. These capabilities became obsolete when new objects were added to indicate which RADIUS attributes should be included or excluded from RADIUS packets.')
juniRadiusClientDynamicAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV7 = juniRadiusClientDynamicAgentV7.setProductRelease('Version 7 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 4.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV7 = juniRadiusClientDynamicAgentV7.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV7.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe. These capabilities became obsolete when notifications for unavailable RADIUS servers were added.')
juniRadiusClientDynamicAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV8 = juniRadiusClientDynamicAgentV8.setProductRelease('Version 8 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 4.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV8 = juniRadiusClientDynamicAgentV8.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV8.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe. These capabilities became obsolete when attribute-ignore objects were added to the B-RAS group and RADIUS accounting and authentication servers available traps were added.')
juniRadiusClientDynamicAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV9 = juniRadiusClientDynamicAgentV9.setProductRelease('Version 9 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV9 = juniRadiusClientDynamicAgentV9.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV9.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe. These capabilities became obsolete when new B-RAS configuration objects were added.')
juniRadiusClientDynamicAgentV10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV10 = juniRadiusClientDynamicAgentV10.setProductRelease('Version 10 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 5.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV10 = juniRadiusClientDynamicAgentV10.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV10.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe. These capabilities became obsolete when new accounting counters were added.')
juniRadiusClientDynamicAgentV11 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV11 = juniRadiusClientDynamicAgentV11.setProductRelease('Version 11 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV11 = juniRadiusClientDynamicAgentV11.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV11.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe. These capabilities became obsolete when a new B-RAS object was added.')
juniRadiusClientDynamicAgentV12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV12 = juniRadiusClientDynamicAgentV12.setProductRelease('Version 12 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  These capabilities became obsolete when a new\n        B-RAS object was added.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV12 = juniRadiusClientDynamicAgentV12.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV12.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe.')
juniRadiusClientDynamicAgentV13 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV13 = juniRadiusClientDynamicAgentV13.setProductRelease('Version 13 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 6.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV13 = juniRadiusClientDynamicAgentV13.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV13.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe.')
juniRadiusClientDynamicAgentV14 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV14 = juniRadiusClientDynamicAgentV14.setProductRelease('Version 14 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 6.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV14 = juniRadiusClientDynamicAgentV14.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV14.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe.')
juniRadiusClientDynamicAgentV15 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV15 = juniRadiusClientDynamicAgentV15.setProductRelease('Version 15 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 6.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV15 = juniRadiusClientDynamicAgentV15.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV15.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe.')
juniRadiusClientDynamicAgentV16 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV16 = juniRadiusClientDynamicAgentV16.setProductRelease('Version 16 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 7.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV16 = juniRadiusClientDynamicAgentV16.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV16.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe.')
juniRadiusClientDynamicAgentV17 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV17 = juniRadiusClientDynamicAgentV17.setProductRelease('Version 17 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 7.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV17 = juniRadiusClientDynamicAgentV17.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV17.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe.')
juniRadiusClientDynamicAgentV18 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV18 = juniRadiusClientDynamicAgentV18.setProductRelease('Version 18 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 8.1.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV18 = juniRadiusClientDynamicAgentV18.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV18.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe.')
juniRadiusClientDynamicAgentV19 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV19 = juniRadiusClientDynamicAgentV19.setProductRelease('Version 19 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 8.2.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV19 = juniRadiusClientDynamicAgentV19.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV19.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe.')
juniRadiusClientDynamicAgentV20 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 20))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV20 = juniRadiusClientDynamicAgentV20.setProductRelease('Version 20 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 9.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV20 = juniRadiusClientDynamicAgentV20.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV20.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe.')
juniRadiusClientDynamicAgentV21 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 21))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV21 = juniRadiusClientDynamicAgentV21.setProductRelease('Version 21 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 10.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV21 = juniRadiusClientDynamicAgentV21.setStatus('obsolete')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV21.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe.')
juniRadiusClientDynamicAgentV22 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 22))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV22 = juniRadiusClientDynamicAgentV22.setProductRelease('Version 22 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 10.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV22 = juniRadiusClientDynamicAgentV22.setStatus('current')
if mibBuilder.loadTexts: juniRadiusClientDynamicAgentV22.setDescription('The MIB supported by the SNMP agent for the RADIUS Client dynamic interface application in JUNOSe.')
juniRadiusClientBasicAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 2))
if mibBuilder.loadTexts: juniRadiusClientBasicAgent.setStatus('current')
if mibBuilder.loadTexts: juniRadiusClientBasicAgent.setDescription('The registration group of agent capabilities for the RADIUS Client application which only provides basic authentication for CLI access to JUNOSe.')
juniRadiusClientBasicAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientBasicAgentV1 = juniRadiusClientBasicAgentV1.setProductRelease('Version 1 of the basic authentication RADIUS Client component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientBasicAgentV1 = juniRadiusClientBasicAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniRadiusClientBasicAgentV1.setDescription('The MIB supported by the SNMP agent for the RADIUS Client basic authentication application which only supports basic authentication for remote CLI access in JUNOSe.')
mibBuilder.exportSymbols("Juniper-RADIUS-CLIENT-CONF", juniRadiusClientDynamicAgentV14=juniRadiusClientDynamicAgentV14, juniRadiusClientDynamicAgentV21=juniRadiusClientDynamicAgentV21, juniRadiusClientDynamicAgentV20=juniRadiusClientDynamicAgentV20, juniRadiusClientDynamicAgentV2=juniRadiusClientDynamicAgentV2, juniRadiusClientDynamicAgentV7=juniRadiusClientDynamicAgentV7, PYSNMP_MODULE_ID=juniRadiusClientAgent, juniRadiusClientDynamicAgentV9=juniRadiusClientDynamicAgentV9, juniRadiusClientBasicAgentV1=juniRadiusClientBasicAgentV1, juniRadiusClientDynamicAgentV4=juniRadiusClientDynamicAgentV4, juniRadiusClientDynamicAgentV11=juniRadiusClientDynamicAgentV11, juniRadiusClientDynamicAgentV19=juniRadiusClientDynamicAgentV19, juniRadiusClientDynamicAgentV12=juniRadiusClientDynamicAgentV12, juniRadiusClientDynamicAgentV6=juniRadiusClientDynamicAgentV6, juniRadiusClientDynamicAgentV15=juniRadiusClientDynamicAgentV15, juniRadiusClientDynamicAgentV10=juniRadiusClientDynamicAgentV10, juniRadiusClientDynamicAgentV1=juniRadiusClientDynamicAgentV1, juniRadiusClientDynamicAgentV5=juniRadiusClientDynamicAgentV5, juniRadiusClientDynamicAgentV8=juniRadiusClientDynamicAgentV8, juniRadiusClientBasicAgent=juniRadiusClientBasicAgent, juniRadiusClientDynamicAgentV22=juniRadiusClientDynamicAgentV22, juniRadiusClientDynamicAgentV18=juniRadiusClientDynamicAgentV18, juniRadiusClientAgent=juniRadiusClientAgent, juniRadiusClientDynamicAgentV13=juniRadiusClientDynamicAgentV13, juniRadiusClientDynamicAgentV17=juniRadiusClientDynamicAgentV17, juniRadiusClientDynamicAgentV3=juniRadiusClientDynamicAgentV3, juniRadiusClientDynamicAgent=juniRadiusClientDynamicAgent, juniRadiusClientDynamicAgentV16=juniRadiusClientDynamicAgentV16)
