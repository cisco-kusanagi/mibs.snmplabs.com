#
# PySNMP MIB module Juniper-PPP-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-PPP-Profile-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
juniProfileAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniProfileAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, NotificationType, ObjectIdentity, Counter32, Bits, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Gauge32, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "NotificationType", "ObjectIdentity", "Counter32", "Bits", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Gauge32", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniPppProfileAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3))
juniPppProfileAgent.setRevisions(('2009-09-18 07:24', '2009-08-10 14:23', '2007-07-12 12:15', '2005-10-19 16:26', '2003-11-03 21:32', '2003-03-13 16:47', '2002-09-06 16:54', '2002-09-03 22:38', '2002-01-25 14:10', '2002-01-16 17:58', '2002-01-08 19:43', '2001-10-17 17:10',))
if mibBuilder.loadTexts: juniPppProfileAgent.setLastUpdated('200909180724Z')
if mibBuilder.loadTexts: juniPppProfileAgent.setOrganization('Juniper Networks, Inc.')
juniPppProfileAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV1 = juniPppProfileAgentV1.setProductRelease('Version 1 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component was supported in JUNOSe 3.0 through\n        3.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV1 = juniPppProfileAgentV1.setStatus('obsolete')
juniPppProfileAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV2 = juniPppProfileAgentV2.setProductRelease('Version 2 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component was supported in JUNOSe 3.3 system\n        release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV2 = juniPppProfileAgentV2.setStatus('obsolete')
juniPppProfileAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV3 = juniPppProfileAgentV3.setProductRelease('Version 3 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component was supported in JUNOSe 3.4 and\n        subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV3 = juniPppProfileAgentV3.setStatus('obsolete')
juniPppProfileAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV4 = juniPppProfileAgentV4.setProductRelease('Version 4 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component was supported in JUNOSe 4.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV4 = juniPppProfileAgentV4.setStatus('obsolete')
juniPppProfileAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV5 = juniPppProfileAgentV5.setProductRelease('Version 5 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component was supported in JUNOSe 4.1 through\n        5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV5 = juniPppProfileAgentV5.setStatus('obsolete')
juniPppProfileAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV6 = juniPppProfileAgentV6.setProductRelease('Version 6 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component was supported in JUNOSe 5.1 and 5.2\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV6 = juniPppProfileAgentV6.setStatus('obsolete')
juniPppProfileAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV7 = juniPppProfileAgentV7.setProductRelease('Version 7 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component is supported in JUNOSe 5.3 through\n        7.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV7 = juniPppProfileAgentV7.setStatus('obsolete')
juniPppProfileAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV8 = juniPppProfileAgentV8.setProductRelease('Version 8 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component is supported in JUNOSe 7.2 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV8 = juniPppProfileAgentV8.setStatus('obsolete')
juniPppProfileAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV9 = juniPppProfileAgentV9.setProductRelease('Version 9 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component is supported in JUNOSe 7.3 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV9 = juniPppProfileAgentV9.setStatus('obsolete')
juniPppProfileAgentV10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV10 = juniPppProfileAgentV10.setProductRelease('Version 10 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component is supported in JUNOSe 11.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV10 = juniPppProfileAgentV10.setStatus('obsolete')
juniPppProfileAgentV11 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV11 = juniPppProfileAgentV11.setProductRelease('Version 11 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component is supported in JUNOSe 11.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV11 = juniPppProfileAgentV11.setStatus('current')
mibBuilder.exportSymbols("Juniper-PPP-Profile-CONF", juniPppProfileAgentV9=juniPppProfileAgentV9, juniPppProfileAgentV10=juniPppProfileAgentV10, juniPppProfileAgentV2=juniPppProfileAgentV2, juniPppProfileAgentV11=juniPppProfileAgentV11, juniPppProfileAgentV7=juniPppProfileAgentV7, juniPppProfileAgentV5=juniPppProfileAgentV5, juniPppProfileAgentV8=juniPppProfileAgentV8, juniPppProfileAgentV1=juniPppProfileAgentV1, PYSNMP_MODULE_ID=juniPppProfileAgent, juniPppProfileAgentV3=juniPppProfileAgentV3, juniPppProfileAgent=juniPppProfileAgent, juniPppProfileAgentV4=juniPppProfileAgentV4, juniPppProfileAgentV6=juniPppProfileAgentV6)
