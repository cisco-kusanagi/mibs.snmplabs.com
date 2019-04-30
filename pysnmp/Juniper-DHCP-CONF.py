#
# PySNMP MIB module Juniper-DHCP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DHCP-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
iso, ObjectIdentity, ModuleIdentity, Bits, Gauge32, Integer32, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, Unsigned32, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "ModuleIdentity", "Bits", "Gauge32", "Integer32", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "Unsigned32", "TimeTicks", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniDhcpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8))
juniDhcpAgent.setRevisions(('2007-01-31 20:38', '2005-11-04 19:53', '2005-05-17 19:18', '2005-12-05 21:31', '2004-11-08 16:16', '2004-01-23 16:30', '2003-09-05 19:03', '2002-12-17 16:59', '2002-05-10 19:37', '2001-03-30 18:46',))
if mibBuilder.loadTexts: juniDhcpAgent.setLastUpdated('200701312038Z')
if mibBuilder.loadTexts: juniDhcpAgent.setOrganization('Juniper Networks, Inc.')
juniDhcpRelayAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1))
if mibBuilder.loadTexts: juniDhcpRelayAgent.setStatus('current')
juniDhcpRelayAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV1 = juniDhcpRelayAgentV1.setProductRelease('Version 1 of the DHCP relay subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP relay subcomponent was supported in JUNOSe 1.3\n        thru 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV1 = juniDhcpRelayAgentV1.setStatus('obsolete')
juniDhcpRelayAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV2 = juniDhcpRelayAgentV2.setProductRelease('Version 2 of the DHCP relay subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP relay subcomponent was supported in JUNOSe 4.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV2 = juniDhcpRelayAgentV2.setStatus('obsolete')
juniDhcpRelayAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV3 = juniDhcpRelayAgentV3.setProductRelease('Version 3 of the DHCP relay subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP relay subcomponent was supported in JUNOSe 5.0\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV3 = juniDhcpRelayAgentV3.setStatus('obsolete')
juniDhcpRelayAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV4 = juniDhcpRelayAgentV4.setProductRelease('Version 4 of the DHCP relay subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP relay subcomponent is supported in JUNOSe 5.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV4 = juniDhcpRelayAgentV4.setStatus('obsolete')
juniDhcpRelayAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV5 = juniDhcpRelayAgentV5.setProductRelease('Version 5 of the DHCP relay subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP relay subcomponent is supported in JUNOSe 6.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV5 = juniDhcpRelayAgentV5.setStatus('obsolete')
juniDhcpRelayAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV6 = juniDhcpRelayAgentV6.setProductRelease('Version 6 of the DHCP relay subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP relay subcomponent is supported in JUNOSe 7.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV6 = juniDhcpRelayAgentV6.setStatus('obsolete')
juniDhcpRelayAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV7 = juniDhcpRelayAgentV7.setProductRelease('Version 7 of the DHCP relay subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP relay subcomponent is supported in JUNOSe 7.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV7 = juniDhcpRelayAgentV7.setStatus('obsolete')
juniDhcpRelayAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV8 = juniDhcpRelayAgentV8.setProductRelease('Version 8 of the DHCP relay subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP relay subcomponent is supported in JUNOSe 7.2\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV8 = juniDhcpRelayAgentV8.setStatus('obsolete')
juniDhcpRelayAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV9 = juniDhcpRelayAgentV9.setProductRelease('Version 9 of the DHCP relay subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP relay subcomponent is supported in JUNOSe 8.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV9 = juniDhcpRelayAgentV9.setStatus('current')
juniDhcpProxyAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 2))
if mibBuilder.loadTexts: juniDhcpProxyAgent.setStatus('current')
juniDhcpProxyAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpProxyAgentV1 = juniDhcpProxyAgentV1.setProductRelease('Version 1 of the DHCP proxy subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP proxy subcomponent is supported in JUNOSe 1.3\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpProxyAgentV1 = juniDhcpProxyAgentV1.setStatus('current')
juniDhcpLocalServerAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3))
if mibBuilder.loadTexts: juniDhcpLocalServerAgent.setStatus('current')
juniDhcpLocalServerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV1 = juniDhcpLocalServerAgentV1.setProductRelease('Version 1 of the DHCP local server subcomponent of JUNOSe SNMP agent.\n        This version of the DHCP local server subcomponent was supported in\n        JUNOSe 3.1 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV1 = juniDhcpLocalServerAgentV1.setStatus('obsolete')
juniDhcpLocalServerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV2 = juniDhcpLocalServerAgentV2.setProductRelease('Version 2 of the DHCP local server subcomponent of JUNOSe SNMP agent.\n        This version of the DHCP local server subcomponent was supported in\n        JUNOSe 4.0 through 5.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV2 = juniDhcpLocalServerAgentV2.setStatus('obsolete')
juniDhcpLocalServerAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV3 = juniDhcpLocalServerAgentV3.setProductRelease('Version 3 of the DHCP local server subcomponent of JUNOSe SNMP agent.\n        This version of the DHCP local server subcomponent is supported in\n        JUNOSe 5.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV3 = juniDhcpLocalServerAgentV3.setStatus('current')
juniDhcpLocalServerAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV5 = juniDhcpLocalServerAgentV5.setProductRelease('Version 5 of the DHCP local server subcomponent of JUNOSe SNMP agent.\n        This version of the DHCP local server subcomponent is supported in\n        JUNOSe 6.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV5 = juniDhcpLocalServerAgentV5.setStatus('obsolete')
juniDhcpLocalServerAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV6 = juniDhcpLocalServerAgentV6.setProductRelease('Version 6 of the DHCP local server subcomponent of JUNOSe SNMP agent.\n        This version of the DHCP local server subcomponent is supported in\n        JUNOSe 7.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV6 = juniDhcpLocalServerAgentV6.setStatus('obsolete')
juniDhcpLocalServerAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV7 = juniDhcpLocalServerAgentV7.setProductRelease('Version 7 of the DHCP local server subcomponent of JUNOSe SNMP agent.\n        This version of the DHCP local server subcomponent is supported in\n        JUNOSe 8.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV7 = juniDhcpLocalServerAgentV7.setStatus('current')
mibBuilder.exportSymbols("Juniper-DHCP-CONF", juniDhcpLocalServerAgent=juniDhcpLocalServerAgent, PYSNMP_MODULE_ID=juniDhcpAgent, juniDhcpLocalServerAgentV3=juniDhcpLocalServerAgentV3, juniDhcpRelayAgentV8=juniDhcpRelayAgentV8, juniDhcpRelayAgent=juniDhcpRelayAgent, juniDhcpRelayAgentV9=juniDhcpRelayAgentV9, juniDhcpRelayAgentV2=juniDhcpRelayAgentV2, juniDhcpRelayAgentV3=juniDhcpRelayAgentV3, juniDhcpLocalServerAgentV5=juniDhcpLocalServerAgentV5, juniDhcpRelayAgentV1=juniDhcpRelayAgentV1, juniDhcpProxyAgentV1=juniDhcpProxyAgentV1, juniDhcpLocalServerAgentV7=juniDhcpLocalServerAgentV7, juniDhcpRelayAgentV4=juniDhcpRelayAgentV4, juniDhcpLocalServerAgentV2=juniDhcpLocalServerAgentV2, juniDhcpRelayAgentV6=juniDhcpRelayAgentV6, juniDhcpRelayAgentV7=juniDhcpRelayAgentV7, juniDhcpLocalServerAgentV1=juniDhcpLocalServerAgentV1, juniDhcpLocalServerAgentV6=juniDhcpLocalServerAgentV6, juniDhcpAgent=juniDhcpAgent, juniDhcpRelayAgentV5=juniDhcpRelayAgentV5, juniDhcpProxyAgent=juniDhcpProxyAgent)
