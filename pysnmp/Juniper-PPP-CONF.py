#
# PySNMP MIB module Juniper-PPP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-PPP-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, Integer32, TimeTicks, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "Integer32", "TimeTicks", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniPppAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32))
juniPppAgent.setRevisions(('2010-02-09 11:06', '2009-09-18 07:24', '2009-08-10 14:23', '2008-08-27 13:18', '2007-07-12 12:15', '2005-10-19 16:26', '2004-10-01 21:41', '2003-11-03 18:32', '2003-09-24 20:11', '2003-01-28 15:47', '2002-08-30 20:36', '2002-05-09 21:03', '2002-05-08 20:25', '2001-04-10 18:23',))
if mibBuilder.loadTexts: juniPppAgent.setLastUpdated('201002091106Z')
if mibBuilder.loadTexts: juniPppAgent.setOrganization('Juniper Networks, Inc.')
juniPppAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppAgentV1 = juniPppAgentV1.setProductRelease('Version 1 of the PPP component of the JUNOSe SNMP agent.  This version\n        of the PPP component was supported in JUNOSe 2.4 thru 3.2 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppAgentV1 = juniPppAgentV1.setStatus('obsolete')
juniPppGeneralAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2))
if mibBuilder.loadTexts: juniPppGeneralAgent.setStatus('current')
juniPppGeneralAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV1 = juniPppGeneralAgentV1.setProductRelease('Version 1 of the general PPP component of the JUNOSe SNMP agent.  This\n        version of the PPP component was supported in JUNOSe 3.3 and subsequent\n        3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV1 = juniPppGeneralAgentV1.setStatus('obsolete')
juniPppGeneralAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV2 = juniPppGeneralAgentV2.setProductRelease('Version 2 of the general PPP component of the JUNOSe SNMP agent.  This\n        version of the PPP component was supported in JUNOSe 4.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV2 = juniPppGeneralAgentV2.setStatus('obsolete')
juniPppGeneralAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV3 = juniPppGeneralAgentV3.setProductRelease('Version 3 of the general PPP component of the JUNOSe SNMP agent.  This\n        version of the PPP component was supported in JUNOSe 4.1 through 5.0\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV3 = juniPppGeneralAgentV3.setStatus('obsolete')
juniPppGeneralAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV4 = juniPppGeneralAgentV4.setProductRelease('Version 4 of the general PPP component of the JUNOSe SNMP agent.  This\n        version of the PPP component was supported in JUNOSe 5.1 and subsequent\n        5.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV4 = juniPppGeneralAgentV4.setStatus('obsolete')
juniPppGeneralAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV5 = juniPppGeneralAgentV5.setProductRelease('Version 5 of the general PPP component of the JUNOSe SNMP agent.  This\n        version of the PPP component is supported in JUNOSe 6.0 throught 7.2\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV5 = juniPppGeneralAgentV5.setStatus('obsolete')
juniPppGeneralAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV6 = juniPppGeneralAgentV6.setProductRelease('Version 6 of the general PPP component of the JUNOSe SNMP agent.  This\n        version of the PPP component is supported in JUNOSe 7.3 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV6 = juniPppGeneralAgentV6.setStatus('obsolete')
juniPppGeneralAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV7 = juniPppGeneralAgentV7.setProductRelease('Version 7 of the general PPP component of the JUNOSe SNMP agent.  This\n        version of the PPP component is supported in JUNOSe 10.1 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV7 = juniPppGeneralAgentV7.setStatus('obsolete')
juniPppGeneralAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV8 = juniPppGeneralAgentV8.setProductRelease('Version 8 of the general PPP component of the JUNOSe SNMP agent.  This\n        version of the PPP component is supported in JUNOSe 11.0 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV8 = juniPppGeneralAgentV8.setStatus('obsolete')
juniPppGeneralAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV9 = juniPppGeneralAgentV9.setProductRelease('Version 9 of the general PPP component of the JUNOSe SNMP agent. This\n        version of the PPP component is supported in JUNOSe 11.2 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV9 = juniPppGeneralAgentV9.setStatus('current')
juniPppMultiLinkAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3))
if mibBuilder.loadTexts: juniPppMultiLinkAgent.setStatus('current')
juniPppMultiLinkAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV1 = juniPppMultiLinkAgentV1.setProductRelease('Version 1 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component was supported in JUNOSe 3.3 and\n        subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV1 = juniPppMultiLinkAgentV1.setStatus('obsolete')
juniPppMultiLinkAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV2 = juniPppMultiLinkAgentV2.setProductRelease('Version 2 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component was supported in JUNOSe 4.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV2 = juniPppMultiLinkAgentV2.setStatus('obsolete')
juniPppMultiLinkAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV3 = juniPppMultiLinkAgentV3.setProductRelease('Version 3 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component was supported in JUNOSe 4.1 and\n        subsequent 4.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV3 = juniPppMultiLinkAgentV3.setStatus('obsolete')
juniPppMultiLinkAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV4 = juniPppMultiLinkAgentV4.setProductRelease('Version 4 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component was supported in JUNOSe 5.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV4 = juniPppMultiLinkAgentV4.setStatus('obsolete')
juniPppMultiLinkAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV5 = juniPppMultiLinkAgentV5.setProductRelease('Version 5 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component was supported in JUNOSe 5.1 and 5.2\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV5 = juniPppMultiLinkAgentV5.setStatus('obsolete')
juniPppMultiLinkAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV6 = juniPppMultiLinkAgentV6.setProductRelease('Version 6 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component was supported in JUNOSe 5.1 and \n        subsequent 5.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV6 = juniPppMultiLinkAgentV6.setStatus('obsolete')
juniPppMultiLinkAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV7 = juniPppMultiLinkAgentV7.setProductRelease('Version 7 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component is supported in JUNOSe 6.0 through\n        7.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV7 = juniPppMultiLinkAgentV7.setStatus('obsolete')
juniPppMultiLinkAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV8 = juniPppMultiLinkAgentV8.setProductRelease('Version 8 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component is supported in JUNOSe 7.2 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV8 = juniPppMultiLinkAgentV8.setStatus('obsolete')
juniPppMultiLinkAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV9 = juniPppMultiLinkAgentV9.setProductRelease('Version 9 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component was supported in JUNOSe 7.3 and \n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV9 = juniPppMultiLinkAgentV9.setStatus('obsolete')
juniPppMultiLinkAgentV10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV10 = juniPppMultiLinkAgentV10.setProductRelease('Version 10 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component was supported in JUNOSe 11.1 and \n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV10 = juniPppMultiLinkAgentV10.setStatus('current')
mibBuilder.exportSymbols("Juniper-PPP-CONF", juniPppGeneralAgentV2=juniPppGeneralAgentV2, juniPppMultiLinkAgentV10=juniPppMultiLinkAgentV10, PYSNMP_MODULE_ID=juniPppAgent, juniPppGeneralAgentV6=juniPppGeneralAgentV6, juniPppAgentV1=juniPppAgentV1, juniPppMultiLinkAgentV7=juniPppMultiLinkAgentV7, juniPppMultiLinkAgentV4=juniPppMultiLinkAgentV4, juniPppMultiLinkAgentV8=juniPppMultiLinkAgentV8, juniPppGeneralAgentV8=juniPppGeneralAgentV8, juniPppGeneralAgentV7=juniPppGeneralAgentV7, juniPppGeneralAgentV5=juniPppGeneralAgentV5, juniPppMultiLinkAgentV3=juniPppMultiLinkAgentV3, juniPppGeneralAgentV9=juniPppGeneralAgentV9, juniPppGeneralAgentV1=juniPppGeneralAgentV1, juniPppMultiLinkAgent=juniPppMultiLinkAgent, juniPppMultiLinkAgentV6=juniPppMultiLinkAgentV6, juniPppMultiLinkAgentV1=juniPppMultiLinkAgentV1, juniPppAgent=juniPppAgent, juniPppMultiLinkAgentV5=juniPppMultiLinkAgentV5, juniPppMultiLinkAgentV9=juniPppMultiLinkAgentV9, juniPppGeneralAgent=juniPppGeneralAgent, juniPppGeneralAgentV3=juniPppGeneralAgentV3, juniPppMultiLinkAgentV2=juniPppMultiLinkAgentV2, juniPppGeneralAgentV4=juniPppGeneralAgentV4)
