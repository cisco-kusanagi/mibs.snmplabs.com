#
# PySNMP MIB module Juniper-AAA-Server-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-AAA-Server-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:01:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
TimeTicks, iso, Integer32, Gauge32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, IpAddress, ObjectIdentity, Counter32, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Integer32", "Gauge32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "IpAddress", "ObjectIdentity", "Counter32", "Bits", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniAaaServerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1))
juniAaaServerAgent.setRevisions(('2008-10-24 09:16', '2008-09-04 10:34', '2008-06-05 03:48', '2007-10-23 19:34', '2007-10-04 01:33', '2007-07-31 19:34', '2006-08-02 18:34', '2006-04-26 18:52', '2005-09-16 15:58', '2005-03-24 18:37', '2004-12-14 18:37', '2004-12-03 22:12', '2004-05-20 21:33', '2004-07-26 17:02', '2003-03-07 20:51', '2002-12-02 18:44', '2002-08-16 15:10', '2002-05-13 19:32', '2002-01-03 20:30', '2001-09-18 21:13', '2001-04-10 14:02',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniAaaServerAgent.setRevisionsDescriptions(('Added rsAaaDelegatedIpv6PrefixAsDhcpv6DelegatedPrefix and rsAaaFramedIpv6PrefixAsIpv6NdRaPrefix to the rsAaaAssignGeneral object.', 'Added rsAaaAssignDomainBackupPoolName to the rsAaaAssignDomain object.', 'Added rsAaaMonitorIngressTrafficOnly to the rsAaaTimeoutGeneral object.', 'Added rsAaaAssignDomainTunnelSubscriberAuthentication for enable or disable suberscriber to authenticate with configured authentication server when there are tunnel configurations under the domain', 'Added rsAaaAssignDomainAuthRouterName, rsAaaAssignDomainIpRouterName, rsAaaAssignDomainRouterName is deprecated and becomes read-only.', 'Added rsAaaServiceAcctInterval for the default service accounting interval; added rsAaaUserAcctInterval for the default user accounting interval; changed rsAaaAcctInterval to set both rsAaaServiceAcctInterval, and rsAaaUserAcctInterval; get of rsAaaAcctInterval only returns the rsAaaUserAcctInterval value', 'Added new values to rsAaaAssignTunnelCallingNumberFormat. Added rsAaaAssignTunnelCallingNumberFormatFallback ', 'Added rsAaaAssignQosDownstreamRate object to the rsAaaBrasGroup.', 'A new object was added to the tunnel group and domain map.', 'Added rsAAASubscriberExtTable support.', 'Added tunnel group support.', 'Added rsAaaLocalAuthUser, rsAaaLocalAuthUserDb, and rsAaaLocalAuthUserDbAssoc groups to support local authentication. Added broadcast accounting support: rsAaaAcctBcastServerGroupTable, rsAaaAcctBcastServerGroupName, rsAaaOutgoingBcastAcctRequests and rsAaaIncomingBcastAcctResponses.', 'Updates to tunnel server and bras agents.', 'Added new states to RsSubscriberState. Added realm and domain parse direction. Added rsAaaAuthMethodsTable and rsAaaAcctMethodsTable.', 'Added support for IPv6.', 'Replaced Unisphere names with Juniper names. Added PADN support.', 'Added new B-RAS and tunnel objects.', 'Added new B-RAS and accounting objects.', 'Added support for subscriber-per-interface-location monitoring.', 'Separated out optional capabilities. Added the subscriber and capabilities groups.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniAaaServerAgent.setLastUpdated('200810240916Z')
if mibBuilder.loadTexts: juniAaaServerAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniAaaServerAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniAaaServerAgent.setDescription('The agent capabilities definitions for the Authentication, Authorization and Accounting (AAA) Server component of the SNMP agent in the Juniper E-series family of products.')
juniAaaServerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV1 = juniAaaServerAgentV1.setProductRelease('Version 1 of the AAA Server component of the JUNOSe SNMP agent.  This\n        version was supported in JUNOSe 1.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV1 = juniAaaServerAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerAgentV1.setDescription('The MIB supported by the SNMP agent for the AAA Server application in JUNOSe. These capabilities became obsolete when new objects were added.')
juniAaaServerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV2 = juniAaaServerAgentV2.setProductRelease('Version 2 of the AAA Server component of the JUNOSe SNMP agent.  This\n        version was supported in JUNOSe 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV2 = juniAaaServerAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerAgentV2.setDescription('The MIB supported by the SNMP agent for the AAA Server application in JUNOSe. These capabilities became obsolete when new objects were added and new groupings were defined.')
juniAaaServerAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV3 = juniAaaServerAgentV3.setProductRelease('Version 3 of the AAA Server component of the JUNOSe SNMP agent.  This\n        version was supported in JUNOSe 3.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV3 = juniAaaServerAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerAgentV3.setDescription('The MIB supported by the SNMP agent for the AAA Server application in JUNOSe. These capabilities became obsolete when the juniAaaAssignDomainStripDomain object was added to the B-RAS group.')
juniAaaServerAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV4 = juniAaaServerAgentV4.setProductRelease('Version 4 of the AAA Server component of the JUNOSe SNMP\n        agent.  This version was supported in JUNOSe 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV4 = juniAaaServerAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerAgentV4.setDescription('The MIB supported by the SNMP agent for the AAA Server application in JUNOSe. These capabilities became obsolete when new assignment delimiter objects were added to the B-RAS group.')
juniAaaServerAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV5 = juniAaaServerAgentV5.setProductRelease('Version 5 of the AAA Server component of the JUNOSe SNMP agent.  This\n        version was supported in JUNOSe 3.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV5 = juniAaaServerAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerAgentV5.setDescription('The MIB supported by the SNMP agent for the AAA Server application in JUNOSe. These capabilities became obsolete when the groups were separated into multiple statements and the subscriber and capabilties groups were added.')
juniAaaServerBaseAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 6))
if mibBuilder.loadTexts: juniAaaServerBaseAgent.setStatus('current')
if mibBuilder.loadTexts: juniAaaServerBaseAgent.setDescription('The registration group of agent capabilities for the basic AAA Server management.')
juniAaaServerBaseAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBaseAgentV1 = juniAaaServerBaseAgentV1.setProductRelease('Version 1 of the basic AAA Server component of the JUNOSe SNMP agent.\n        This version is supported in JUNOSe 3.3 through 5.2.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBaseAgentV1 = juniAaaServerBaseAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerBaseAgentV1.setDescription('Obsolete MIB groups supported by the SNMP agent for the basic AAA Server application in JUNOSe. These capabilities became obsolete when a new accounting object was added.')
juniAaaServerBaseAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 6, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBaseAgentV2 = juniAaaServerBaseAgentV2.setProductRelease('Version 2 of the basic AAA Server component of the JUNOSe SNMP agent.\n        This version is supported in JUNOSe 5.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBaseAgentV2 = juniAaaServerBaseAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerBaseAgentV2.setDescription('The MIB groups supported by the SNMP agent for the basic AAA Server application in JUNOSe.')
juniAaaServerBaseAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 6, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBaseAgentV3 = juniAaaServerBaseAgentV3.setProductRelease('Version 3 of the basic AAA Server component of the JUNOSe SNMP agent.\n        This version is supported in JUNOSe 6.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBaseAgentV3 = juniAaaServerBaseAgentV3.setStatus('current')
if mibBuilder.loadTexts: juniAaaServerBaseAgentV3.setDescription('The MIB groups supported by the SNMP agent for the basic AAA Server application in JUNOSe.')
juniAaaServerBrasAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7))
if mibBuilder.loadTexts: juniAaaServerBrasAgent.setStatus('current')
if mibBuilder.loadTexts: juniAaaServerBrasAgent.setDescription('The registration group of agent capabilities for AAA Server B-RAS management.')
juniAaaServerBrasAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV1 = juniAaaServerBrasAgentV1.setProductRelease('Version 1 of the B-RAS option of the AAA Server component of the JUNOSe\n        SNMP agent.  This version was supported in JUNOSe 3.3 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV1 = juniAaaServerBrasAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerBrasAgentV1.setDescription('The MIB groups supported by the SNMP agent for the B-RAS option of the AAA Server application in JUNOSe. These capabilities became obsolete when support was added for monitoring subscriber information by interface location.')
juniAaaServerBrasAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV2 = juniAaaServerBrasAgentV2.setProductRelease('Version 2 of the B-RAS option of the AAA Server component of the JUNOSe\n        SNMP agent.  This version was supported in JUNOSe 3.4 and subsequent 3.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV2 = juniAaaServerBrasAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerBrasAgentV2.setDescription('The MIB groups supported by the SNMP agent for the B-RAS option of the AAA Server application in JUNOSe. These capabilities became obsolete when new B-RAS objects were added.')
juniAaaServerBrasAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV3 = juniAaaServerBrasAgentV3.setProductRelease('Version 3 of the B-RAS option of the AAA Server component of the JUNOSe\n        SNMP agent.  This version was supported in JUNOSe 4.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV3 = juniAaaServerBrasAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerBrasAgentV3.setDescription('The MIB groups supported by the SNMP agent for the B-RAS option of the AAA Server application in JUNOSe. These capabilities became obsolete when a new B-RAS object was added.')
juniAaaServerBrasAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV4 = juniAaaServerBrasAgentV4.setProductRelease('Version 4 of the B-RAS option of the AAA Server component of the JUNOSe\n        SNMP agent.  This version was supported in JUNOSe 4.1 and subsequent 4.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV4 = juniAaaServerBrasAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerBrasAgentV4.setDescription('The MIB groups supported by the SNMP agent for the B-RAS option of the AAA Server application in JUNOSe. These capabilities became obsolete when PADN support was added.')
juniAaaServerBrasAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV5 = juniAaaServerBrasAgentV5.setProductRelease('Version 5 of the B-RAS option of the AAA Server component of the JUNOSe\n        SNMP agent.  This version was supported in JUNOSe 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV5 = juniAaaServerBrasAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerBrasAgentV5.setDescription('The MIB groups supported by the SNMP agent for the B-RAS option of the AAA Server application in JUNOSe.')
juniAaaServerBrasAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV6 = juniAaaServerBrasAgentV6.setProductRelease('Version 6 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 5.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV6 = juniAaaServerBrasAgentV6.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerBrasAgentV6.setDescription('The MIB groups supported by the SNMP agent for the B-RAS option of the AAA Server application in JUNOSe.')
juniAaaServerBrasAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV7 = juniAaaServerBrasAgentV7.setProductRelease('Version 7 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 5.3\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV7 = juniAaaServerBrasAgentV7.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerBrasAgentV7.setDescription('The MIB groups supported by the SNMP agent for the B-RAS option of the AAA Server application in JUNOSe.')
juniAaaServerBrasAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV8 = juniAaaServerBrasAgentV8.setProductRelease('Obsolete Version 8 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 6.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV8 = juniAaaServerBrasAgentV8.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerBrasAgentV8.setDescription('The MIB groups supported by the SNMP agent for the B-RAS option of the AAA Server application in JUNOSe.')
juniAaaServerBrasAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV9 = juniAaaServerBrasAgentV9.setProductRelease('Obsolete Version 9 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 7.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV9 = juniAaaServerBrasAgentV9.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerBrasAgentV9.setDescription('The MIB groups supported by the SNMP agent for the B-RAS option of the AAA Server application in JUNOSe.')
juniAaaServerBrasAgentV10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV10 = juniAaaServerBrasAgentV10.setProductRelease('Obsolete Version 10 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 7.3\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV10 = juniAaaServerBrasAgentV10.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerBrasAgentV10.setDescription('The MIB groups supported by the SNMP agent for the B-RAS option of the AAA Server application in JUNOSe.')
juniAaaServerBrasAgentV11 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV11 = juniAaaServerBrasAgentV11.setProductRelease('Obsolete Version 11 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 8.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV11 = juniAaaServerBrasAgentV11.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerBrasAgentV11.setDescription('The MIB groups supported by the SNMP agent for the B-RAS option of the AAA Server application in JUNOSe.')
juniAaaServerBrasAgentV12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV12 = juniAaaServerBrasAgentV12.setProductRelease('Version 12 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 9.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV12 = juniAaaServerBrasAgentV12.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerBrasAgentV12.setDescription('The MIB groups supported by the SNMP agent for the B-RAS option of the AAA Server application in JUNOSe.')
juniAaaServerBrasAgentV13 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV13 = juniAaaServerBrasAgentV13.setProductRelease('Version 13 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 9.3\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV13 = juniAaaServerBrasAgentV13.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerBrasAgentV13.setDescription('The MIB groups supported by the SNMP agent for the B-RAS option of the AAA Server application in JUNOSe.')
juniAaaServerBrasAgentV14 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV14 = juniAaaServerBrasAgentV14.setProductRelease('Version 14 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 10.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV14 = juniAaaServerBrasAgentV14.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerBrasAgentV14.setDescription('The MIB groups supported by the SNMP agent for the B-RAS option of the AAA Server application in JUNOSe.')
juniAaaServerBrasAgentV15 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV15 = juniAaaServerBrasAgentV15.setProductRelease('Version 15 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 10.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV15 = juniAaaServerBrasAgentV15.setStatus('current')
if mibBuilder.loadTexts: juniAaaServerBrasAgentV15.setDescription('The MIB groups supported by the SNMP agent for the B-RAS option of the AAA Server application in JUNOSe.')
juniAaaServerTunnelAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8))
if mibBuilder.loadTexts: juniAaaServerTunnelAgent.setStatus('current')
if mibBuilder.loadTexts: juniAaaServerTunnelAgent.setDescription('The registration group of agent capabilities for AAA Server tunneling management.')
juniAaaServerTunnelAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV1 = juniAaaServerTunnelAgentV1.setProductRelease('Version 1 of the tunneling option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version was supported in JUNOSe 3.3 through 4.0\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV1 = juniAaaServerTunnelAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerTunnelAgentV1.setDescription('The MIB group supported by the SNMP agent for the tunneling option of the AAA Server application in JUNOSe. These capabilities became obsolete when a new tunnel object was added.')
juniAaaServerTunnelAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV2 = juniAaaServerTunnelAgentV2.setProductRelease('Version 2 of the tunneling option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 4.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV2 = juniAaaServerTunnelAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerTunnelAgentV2.setDescription('The MIB group supported by the SNMP agent for the tunneling option of the AAA Server application in JUNOSe. These capabilities became obsolete when a new tunnel object was added.')
juniAaaServerTunnelAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV3 = juniAaaServerTunnelAgentV3.setProductRelease('Version 3 of the tunneling option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 6.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV3 = juniAaaServerTunnelAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerTunnelAgentV3.setDescription('The MIB group supported by the SNMP agent for the tunneling option of the AAA Server application in JUNOSe.')
juniAaaServerTunnelAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV4 = juniAaaServerTunnelAgentV4.setProductRelease('Version 4 of the tunneling option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 7.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV4 = juniAaaServerTunnelAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerTunnelAgentV4.setDescription('The MIB group supported by the SNMP agent for the tunneling option of the AAA Server application in JUNOSe.')
juniAaaServerTunnelAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV5 = juniAaaServerTunnelAgentV5.setProductRelease('Version 5 of the tunneling option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 8.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV5 = juniAaaServerTunnelAgentV5.setStatus('current')
if mibBuilder.loadTexts: juniAaaServerTunnelAgentV5.setDescription('The MIB group supported by the SNMP agent for the tunneling option of the AAA Server application in JUNOSe.')
juniAaaServerAccountingAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9))
if mibBuilder.loadTexts: juniAaaServerAccountingAgent.setStatus('current')
if mibBuilder.loadTexts: juniAaaServerAccountingAgent.setDescription('The registration group of agent capabilities for AAA Server accounting management.')
juniAaaServerAccountingAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV1 = juniAaaServerAccountingAgentV1.setProductRelease('Version 1 of the accounting option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version was supported in JUNOSe 3.3 and\n        subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV1 = juniAaaServerAccountingAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerAccountingAgentV1.setDescription('The MIB group supported by the SNMP agent for the accounting option of the AAA Server application in JUNOSe. These capabilities became obsolete when a new accounting object was added.')
juniAaaServerAccountingAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV2 = juniAaaServerAccountingAgentV2.setProductRelease('Version 2 of the accounting option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 4.0 through\n        5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV2 = juniAaaServerAccountingAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerAccountingAgentV2.setDescription('Obsolete MIB group supported by the SNMP agent for the accounting option of the AAA Server application in JUNOSe. These capabilities became obsolete when a new accounting object was added.')
juniAaaServerAccountingAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV3 = juniAaaServerAccountingAgentV3.setProductRelease('Version 3 of the accounting option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 5.3 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV3 = juniAaaServerAccountingAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerAccountingAgentV3.setDescription('The MIB group supported by the SNMP agent for the accounting option of the AAA Server application in JUNOSe.')
juniAaaServerAccountingAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV4 = juniAaaServerAccountingAgentV4.setProductRelease('Version 4 of the accounting option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 6.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV4 = juniAaaServerAccountingAgentV4.setStatus('current')
if mibBuilder.loadTexts: juniAaaServerAccountingAgentV4.setDescription('The MIB group supported by the SNMP agent for the accounting option of the AAA Server application in JUNOSe.')
juniAaaServerAccountingAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV5 = juniAaaServerAccountingAgentV5.setProductRelease('Version 5 of the accounting option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 9.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV5 = juniAaaServerAccountingAgentV5.setStatus('current')
if mibBuilder.loadTexts: juniAaaServerAccountingAgentV5.setDescription('The MIB group supported by the SNMP agent for the accounting option of the AAA Server application in JUNOSe.')
juniAaaServerAddressAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 10))
if mibBuilder.loadTexts: juniAaaServerAddressAgent.setStatus('current')
if mibBuilder.loadTexts: juniAaaServerAddressAgent.setDescription('The registration group of agent capabilities for AAA Server address assignment management.')
juniAaaServerAddressAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 10, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAddressAgentV1 = juniAaaServerAddressAgentV1.setProductRelease('Version 1 of the address assignment option of the AAA Server component\n        of the JUNOSe SNMP agent.  This version was supported in JUNOSe 3.3\n        through 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAddressAgentV1 = juniAaaServerAddressAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniAaaServerAddressAgentV1.setDescription('The MIB group supported by the SNMP agent for the address assignment option of the AAA Server application in JUNOSe. These capabilities became obsolete when IPv6 support was added.')
juniAaaServerAddressAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 10, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAddressAgentV2 = juniAaaServerAddressAgentV2.setProductRelease('Version 2 of the address assignment option of the AAA Server component\n        of the JUNOSe SNMP agent.  This version is supported in JUNOSe 5.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAddressAgentV2 = juniAaaServerAddressAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniAaaServerAddressAgentV2.setDescription('The MIB group supported by the SNMP agent for the address assignment option of the AAA Server application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-AAA-Server-CONF", juniAaaServerAccountingAgentV3=juniAaaServerAccountingAgentV3, juniAaaServerBaseAgentV1=juniAaaServerBaseAgentV1, juniAaaServerTunnelAgent=juniAaaServerTunnelAgent, juniAaaServerBrasAgentV10=juniAaaServerBrasAgentV10, juniAaaServerAccountingAgent=juniAaaServerAccountingAgent, juniAaaServerBrasAgentV14=juniAaaServerBrasAgentV14, juniAaaServerTunnelAgentV3=juniAaaServerTunnelAgentV3, juniAaaServerBrasAgentV2=juniAaaServerBrasAgentV2, juniAaaServerBrasAgentV5=juniAaaServerBrasAgentV5, juniAaaServerAccountingAgentV5=juniAaaServerAccountingAgentV5, juniAaaServerBrasAgentV1=juniAaaServerBrasAgentV1, juniAaaServerAgentV3=juniAaaServerAgentV3, juniAaaServerBrasAgentV6=juniAaaServerBrasAgentV6, juniAaaServerBrasAgentV4=juniAaaServerBrasAgentV4, juniAaaServerAddressAgent=juniAaaServerAddressAgent, PYSNMP_MODULE_ID=juniAaaServerAgent, juniAaaServerBrasAgentV13=juniAaaServerBrasAgentV13, juniAaaServerBrasAgent=juniAaaServerBrasAgent, juniAaaServerTunnelAgentV2=juniAaaServerTunnelAgentV2, juniAaaServerAgentV2=juniAaaServerAgentV2, juniAaaServerAgentV1=juniAaaServerAgentV1, juniAaaServerAccountingAgentV1=juniAaaServerAccountingAgentV1, juniAaaServerAccountingAgentV4=juniAaaServerAccountingAgentV4, juniAaaServerBaseAgentV2=juniAaaServerBaseAgentV2, juniAaaServerBrasAgentV12=juniAaaServerBrasAgentV12, juniAaaServerBaseAgentV3=juniAaaServerBaseAgentV3, juniAaaServerTunnelAgentV1=juniAaaServerTunnelAgentV1, juniAaaServerBrasAgentV8=juniAaaServerBrasAgentV8, juniAaaServerAgentV5=juniAaaServerAgentV5, juniAaaServerBrasAgentV9=juniAaaServerBrasAgentV9, juniAaaServerBaseAgent=juniAaaServerBaseAgent, juniAaaServerAddressAgentV1=juniAaaServerAddressAgentV1, juniAaaServerBrasAgentV7=juniAaaServerBrasAgentV7, juniAaaServerAgent=juniAaaServerAgent, juniAaaServerAgentV4=juniAaaServerAgentV4, juniAaaServerBrasAgentV15=juniAaaServerBrasAgentV15, juniAaaServerAccountingAgentV2=juniAaaServerAccountingAgentV2, juniAaaServerBrasAgentV11=juniAaaServerBrasAgentV11, juniAaaServerTunnelAgentV4=juniAaaServerTunnelAgentV4, juniAaaServerAddressAgentV2=juniAaaServerAddressAgentV2, juniAaaServerBrasAgentV3=juniAaaServerBrasAgentV3, juniAaaServerTunnelAgentV5=juniAaaServerTunnelAgentV5)
