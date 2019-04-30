#
# PySNMP MIB module Juniper-AAA-Server-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-AAA-Server-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:50:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Counter32, MibIdentifier, NotificationType, Unsigned32, IpAddress, Counter64, Bits, iso, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "NotificationType", "Unsigned32", "IpAddress", "Counter64", "Bits", "iso", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniAaaServerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1))
juniAaaServerAgent.setRevisions(('2008-10-24 09:16', '2008-09-04 10:34', '2008-06-05 03:48', '2007-10-23 19:34', '2007-10-04 01:33', '2007-07-31 19:34', '2006-08-02 18:34', '2006-04-26 18:52', '2005-09-16 15:58', '2005-03-24 18:37', '2004-12-14 18:37', '2004-12-03 22:12', '2004-05-20 21:33', '2004-07-26 17:02', '2003-03-07 20:51', '2002-12-02 18:44', '2002-08-16 15:10', '2002-05-13 19:32', '2002-01-03 20:30', '2001-09-18 21:13', '2001-04-10 14:02',))
if mibBuilder.loadTexts: juniAaaServerAgent.setLastUpdated('200810240916Z')
if mibBuilder.loadTexts: juniAaaServerAgent.setOrganization('Juniper Networks, Inc.')
juniAaaServerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV1 = juniAaaServerAgentV1.setProductRelease('Version 1 of the AAA Server component of the JUNOSe SNMP agent.  This\n        version was supported in JUNOSe 1.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV1 = juniAaaServerAgentV1.setStatus('obsolete')
juniAaaServerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV2 = juniAaaServerAgentV2.setProductRelease('Version 2 of the AAA Server component of the JUNOSe SNMP agent.  This\n        version was supported in JUNOSe 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV2 = juniAaaServerAgentV2.setStatus('obsolete')
juniAaaServerAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV3 = juniAaaServerAgentV3.setProductRelease('Version 3 of the AAA Server component of the JUNOSe SNMP agent.  This\n        version was supported in JUNOSe 3.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV3 = juniAaaServerAgentV3.setStatus('obsolete')
juniAaaServerAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV4 = juniAaaServerAgentV4.setProductRelease('Version 4 of the AAA Server component of the JUNOSe SNMP\n        agent.  This version was supported in JUNOSe 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV4 = juniAaaServerAgentV4.setStatus('obsolete')
juniAaaServerAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV5 = juniAaaServerAgentV5.setProductRelease('Version 5 of the AAA Server component of the JUNOSe SNMP agent.  This\n        version was supported in JUNOSe 3.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAgentV5 = juniAaaServerAgentV5.setStatus('obsolete')
juniAaaServerBaseAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 6))
if mibBuilder.loadTexts: juniAaaServerBaseAgent.setStatus('current')
juniAaaServerBaseAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBaseAgentV1 = juniAaaServerBaseAgentV1.setProductRelease('Version 1 of the basic AAA Server component of the JUNOSe SNMP agent.\n        This version is supported in JUNOSe 3.3 through 5.2.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBaseAgentV1 = juniAaaServerBaseAgentV1.setStatus('obsolete')
juniAaaServerBaseAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 6, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBaseAgentV2 = juniAaaServerBaseAgentV2.setProductRelease('Version 2 of the basic AAA Server component of the JUNOSe SNMP agent.\n        This version is supported in JUNOSe 5.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBaseAgentV2 = juniAaaServerBaseAgentV2.setStatus('obsolete')
juniAaaServerBaseAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 6, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBaseAgentV3 = juniAaaServerBaseAgentV3.setProductRelease('Version 3 of the basic AAA Server component of the JUNOSe SNMP agent.\n        This version is supported in JUNOSe 6.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBaseAgentV3 = juniAaaServerBaseAgentV3.setStatus('current')
juniAaaServerBrasAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7))
if mibBuilder.loadTexts: juniAaaServerBrasAgent.setStatus('current')
juniAaaServerBrasAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV1 = juniAaaServerBrasAgentV1.setProductRelease('Version 1 of the B-RAS option of the AAA Server component of the JUNOSe\n        SNMP agent.  This version was supported in JUNOSe 3.3 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV1 = juniAaaServerBrasAgentV1.setStatus('obsolete')
juniAaaServerBrasAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV2 = juniAaaServerBrasAgentV2.setProductRelease('Version 2 of the B-RAS option of the AAA Server component of the JUNOSe\n        SNMP agent.  This version was supported in JUNOSe 3.4 and subsequent 3.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV2 = juniAaaServerBrasAgentV2.setStatus('obsolete')
juniAaaServerBrasAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV3 = juniAaaServerBrasAgentV3.setProductRelease('Version 3 of the B-RAS option of the AAA Server component of the JUNOSe\n        SNMP agent.  This version was supported in JUNOSe 4.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV3 = juniAaaServerBrasAgentV3.setStatus('obsolete')
juniAaaServerBrasAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV4 = juniAaaServerBrasAgentV4.setProductRelease('Version 4 of the B-RAS option of the AAA Server component of the JUNOSe\n        SNMP agent.  This version was supported in JUNOSe 4.1 and subsequent 4.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV4 = juniAaaServerBrasAgentV4.setStatus('obsolete')
juniAaaServerBrasAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV5 = juniAaaServerBrasAgentV5.setProductRelease('Version 5 of the B-RAS option of the AAA Server component of the JUNOSe\n        SNMP agent.  This version was supported in JUNOSe 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV5 = juniAaaServerBrasAgentV5.setStatus('obsolete')
juniAaaServerBrasAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV6 = juniAaaServerBrasAgentV6.setProductRelease('Version 6 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 5.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV6 = juniAaaServerBrasAgentV6.setStatus('obsolete')
juniAaaServerBrasAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV7 = juniAaaServerBrasAgentV7.setProductRelease('Version 7 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 5.3\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV7 = juniAaaServerBrasAgentV7.setStatus('obsolete')
juniAaaServerBrasAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV8 = juniAaaServerBrasAgentV8.setProductRelease('Obsolete Version 8 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 6.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV8 = juniAaaServerBrasAgentV8.setStatus('obsolete')
juniAaaServerBrasAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV9 = juniAaaServerBrasAgentV9.setProductRelease('Obsolete Version 9 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 7.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV9 = juniAaaServerBrasAgentV9.setStatus('obsolete')
juniAaaServerBrasAgentV10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV10 = juniAaaServerBrasAgentV10.setProductRelease('Obsolete Version 10 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 7.3\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV10 = juniAaaServerBrasAgentV10.setStatus('obsolete')
juniAaaServerBrasAgentV11 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV11 = juniAaaServerBrasAgentV11.setProductRelease('Obsolete Version 11 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 8.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV11 = juniAaaServerBrasAgentV11.setStatus('obsolete')
juniAaaServerBrasAgentV12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV12 = juniAaaServerBrasAgentV12.setProductRelease('Version 12 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 9.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV12 = juniAaaServerBrasAgentV12.setStatus('obsolete')
juniAaaServerBrasAgentV13 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV13 = juniAaaServerBrasAgentV13.setProductRelease('Version 13 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 9.3\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV13 = juniAaaServerBrasAgentV13.setStatus('obsolete')
juniAaaServerBrasAgentV14 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV14 = juniAaaServerBrasAgentV14.setProductRelease('Version 14 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 10.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV14 = juniAaaServerBrasAgentV14.setStatus('obsolete')
juniAaaServerBrasAgentV15 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV15 = juniAaaServerBrasAgentV15.setProductRelease('Version 15 of the B-RAS option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 10.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerBrasAgentV15 = juniAaaServerBrasAgentV15.setStatus('current')
juniAaaServerTunnelAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8))
if mibBuilder.loadTexts: juniAaaServerTunnelAgent.setStatus('current')
juniAaaServerTunnelAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV1 = juniAaaServerTunnelAgentV1.setProductRelease('Version 1 of the tunneling option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version was supported in JUNOSe 3.3 through 4.0\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV1 = juniAaaServerTunnelAgentV1.setStatus('obsolete')
juniAaaServerTunnelAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV2 = juniAaaServerTunnelAgentV2.setProductRelease('Version 2 of the tunneling option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 4.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV2 = juniAaaServerTunnelAgentV2.setStatus('obsolete')
juniAaaServerTunnelAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV3 = juniAaaServerTunnelAgentV3.setProductRelease('Version 3 of the tunneling option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 6.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV3 = juniAaaServerTunnelAgentV3.setStatus('obsolete')
juniAaaServerTunnelAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV4 = juniAaaServerTunnelAgentV4.setProductRelease('Version 4 of the tunneling option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 7.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV4 = juniAaaServerTunnelAgentV4.setStatus('obsolete')
juniAaaServerTunnelAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV5 = juniAaaServerTunnelAgentV5.setProductRelease('Version 5 of the tunneling option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 8.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerTunnelAgentV5 = juniAaaServerTunnelAgentV5.setStatus('current')
juniAaaServerAccountingAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9))
if mibBuilder.loadTexts: juniAaaServerAccountingAgent.setStatus('current')
juniAaaServerAccountingAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV1 = juniAaaServerAccountingAgentV1.setProductRelease('Version 1 of the accounting option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version was supported in JUNOSe 3.3 and\n        subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV1 = juniAaaServerAccountingAgentV1.setStatus('obsolete')
juniAaaServerAccountingAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV2 = juniAaaServerAccountingAgentV2.setProductRelease('Version 2 of the accounting option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 4.0 through\n        5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV2 = juniAaaServerAccountingAgentV2.setStatus('obsolete')
juniAaaServerAccountingAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV3 = juniAaaServerAccountingAgentV3.setProductRelease('Version 3 of the accounting option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 5.3 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV3 = juniAaaServerAccountingAgentV3.setStatus('obsolete')
juniAaaServerAccountingAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV4 = juniAaaServerAccountingAgentV4.setProductRelease('Version 4 of the accounting option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 6.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV4 = juniAaaServerAccountingAgentV4.setStatus('current')
juniAaaServerAccountingAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV5 = juniAaaServerAccountingAgentV5.setProductRelease('Version 5 of the accounting option of the AAA Server component of the\n        JUNOSe SNMP agent.  This version is supported in JUNOSe 9.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAccountingAgentV5 = juniAaaServerAccountingAgentV5.setStatus('current')
juniAaaServerAddressAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 10))
if mibBuilder.loadTexts: juniAaaServerAddressAgent.setStatus('current')
juniAaaServerAddressAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 10, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAddressAgentV1 = juniAaaServerAddressAgentV1.setProductRelease('Version 1 of the address assignment option of the AAA Server component\n        of the JUNOSe SNMP agent.  This version was supported in JUNOSe 3.3\n        through 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAddressAgentV1 = juniAaaServerAddressAgentV1.setStatus('obsolete')
juniAaaServerAddressAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 10, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAddressAgentV2 = juniAaaServerAddressAgentV2.setProductRelease('Version 2 of the address assignment option of the AAA Server component\n        of the JUNOSe SNMP agent.  This version is supported in JUNOSe 5.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAaaServerAddressAgentV2 = juniAaaServerAddressAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-AAA-Server-CONF", juniAaaServerBrasAgentV13=juniAaaServerBrasAgentV13, juniAaaServerAddressAgentV1=juniAaaServerAddressAgentV1, juniAaaServerAccountingAgentV2=juniAaaServerAccountingAgentV2, juniAaaServerAgentV2=juniAaaServerAgentV2, juniAaaServerBrasAgentV7=juniAaaServerBrasAgentV7, juniAaaServerAddressAgentV2=juniAaaServerAddressAgentV2, PYSNMP_MODULE_ID=juniAaaServerAgent, juniAaaServerBrasAgentV8=juniAaaServerBrasAgentV8, juniAaaServerAgentV1=juniAaaServerAgentV1, juniAaaServerBrasAgentV9=juniAaaServerBrasAgentV9, juniAaaServerBaseAgent=juniAaaServerBaseAgent, juniAaaServerAgentV3=juniAaaServerAgentV3, juniAaaServerBaseAgentV1=juniAaaServerBaseAgentV1, juniAaaServerBrasAgentV10=juniAaaServerBrasAgentV10, juniAaaServerAccountingAgentV4=juniAaaServerAccountingAgentV4, juniAaaServerTunnelAgentV2=juniAaaServerTunnelAgentV2, juniAaaServerBrasAgentV14=juniAaaServerBrasAgentV14, juniAaaServerBrasAgentV6=juniAaaServerBrasAgentV6, juniAaaServerBrasAgentV2=juniAaaServerBrasAgentV2, juniAaaServerBrasAgentV11=juniAaaServerBrasAgentV11, juniAaaServerBrasAgentV1=juniAaaServerBrasAgentV1, juniAaaServerBaseAgentV3=juniAaaServerBaseAgentV3, juniAaaServerAddressAgent=juniAaaServerAddressAgent, juniAaaServerAccountingAgentV1=juniAaaServerAccountingAgentV1, juniAaaServerBrasAgentV15=juniAaaServerBrasAgentV15, juniAaaServerAgent=juniAaaServerAgent, juniAaaServerBrasAgent=juniAaaServerBrasAgent, juniAaaServerBaseAgentV2=juniAaaServerBaseAgentV2, juniAaaServerTunnelAgentV3=juniAaaServerTunnelAgentV3, juniAaaServerAccountingAgent=juniAaaServerAccountingAgent, juniAaaServerTunnelAgentV5=juniAaaServerTunnelAgentV5, juniAaaServerAccountingAgentV5=juniAaaServerAccountingAgentV5, juniAaaServerBrasAgentV3=juniAaaServerBrasAgentV3, juniAaaServerTunnelAgentV1=juniAaaServerTunnelAgentV1, juniAaaServerAgentV5=juniAaaServerAgentV5, juniAaaServerBrasAgentV4=juniAaaServerBrasAgentV4, juniAaaServerBrasAgentV12=juniAaaServerBrasAgentV12, juniAaaServerTunnelAgent=juniAaaServerTunnelAgent, juniAaaServerTunnelAgentV4=juniAaaServerTunnelAgentV4, juniAaaServerAccountingAgentV3=juniAaaServerAccountingAgentV3, juniAaaServerBrasAgentV5=juniAaaServerBrasAgentV5, juniAaaServerAgentV4=juniAaaServerAgentV4)
