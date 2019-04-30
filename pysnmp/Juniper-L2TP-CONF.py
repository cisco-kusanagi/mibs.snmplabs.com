#
# PySNMP MIB module Juniper-L2TP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-L2TP-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter32, iso, MibIdentifier, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Gauge32, TimeTicks, NotificationType, Integer32, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "MibIdentifier", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Gauge32", "TimeTicks", "NotificationType", "Integer32", "Unsigned32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniL2tpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24))
juniL2tpAgent.setRevisions(('2005-09-16 15:58', '2005-07-28 22:00', '2005-02-17 02:24', '2004-09-02 23:47', '2004-05-04 14:31', '2004-03-08 18:04', '2004-03-08 18:04', '2003-02-13 21:12', '2003-02-12 21:03', '2003-02-07 22:26', '2001-10-17 16:03', '2001-10-17 14:21',))
if mibBuilder.loadTexts: juniL2tpAgent.setLastUpdated('200509161558Z')
if mibBuilder.loadTexts: juniL2tpAgent.setOrganization('Juniper Networks, Inc.')
juniL2tpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV1 = juniL2tpAgentV1.setProductRelease('Version 1 of the L2TP component of the JUNOSe SNMP agent.  This version\n        of the L2TP component was supported in JUNOSe 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV1 = juniL2tpAgentV1.setStatus('obsolete')
juniL2tpAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV2 = juniL2tpAgentV2.setProductRelease('Version 2 of the L2TP component of the JUNOSe SNMP agent.  This version\n        of the L2TP component was supported in JUNOSe 3.0 and 3.1 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV2 = juniL2tpAgentV2.setStatus('obsolete')
juniL2tpAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV3 = juniL2tpAgentV3.setProductRelease('Version 3 of the L2TP component of the JUNOSe SNMP agent.  This version\n        of the L2TP component was supported in JUNOSe 3.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV3 = juniL2tpAgentV3.setStatus('obsolete')
juniL2tpAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV4 = juniL2tpAgentV4.setProductRelease('Version 4 of the L2TP component of the JUNOSe SNMP agent.  This version\n        of the L2TP component was supported in JUNOSe 3.3 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV4 = juniL2tpAgentV4.setStatus('obsolete')
juniL2tpAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV5 = juniL2tpAgentV5.setProductRelease('Version 5 of the L2TP component of the JUNOSe SNMP agent.  This version\n        of the L2TP component was supported in JUNOSe 3.4 thru 4.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV5 = juniL2tpAgentV5.setStatus('obsolete')
juniL2tpAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV6 = juniL2tpAgentV6.setProductRelease('Version 6 of the L2TP component of the JUNOSe SNMP agent.  This version\n        of the L2TP component was supported in JUNOSe 4.1 and subsequent 4.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV6 = juniL2tpAgentV6.setStatus('obsolete')
juniL2tpAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV7 = juniL2tpAgentV7.setProductRelease('Version 7 of the L2TP component of the JUNOSe SNMP agent.  This version\n        of the L2TP component was supported in JUNOSe 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV7 = juniL2tpAgentV7.setStatus('obsolete')
juniL2tpAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV8 = juniL2tpAgentV8.setProductRelease('Version 8 of the L2TP component of the JUNOSe SNMP agent.  This version\n        of the L2TP component was supported in JUNOSe 5.1 and 5.1 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV8 = juniL2tpAgentV8.setStatus('obsolete')
juniL2tpAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV9 = juniL2tpAgentV9.setProductRelease('Version 9 of the L2TP component of the JUNOSe SNMP agent.  This version\n        of the L2TP component is supported in JUNOSe 5.3 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV9 = juniL2tpAgentV9.setStatus('obsolete')
juniL2tpAgentV10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV10 = juniL2tpAgentV10.setProductRelease('Version 10 of the L2TP component of the JUNOSe SNMP agent.  This version\n        of the L2TP component is supported in JUNOSe 6.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV10 = juniL2tpAgentV10.setStatus('obsolete')
juniL2tpAgentV11 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV11 = juniL2tpAgentV11.setProductRelease('Version 11 of the L2TP component of the JUNOSe SNMP agent.  This version\n        of the L2TP component is supported in JUNOSe 7.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV11 = juniL2tpAgentV11.setStatus('obsolete')
juniL2tpAgentV12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV12 = juniL2tpAgentV12.setProductRelease('Version 12 of the L2TP component of the JUNOSe SNMP agent.  This\n        version of the L2TP component is supported in JUNOSe 7.1 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV12 = juniL2tpAgentV12.setStatus('obsolete')
juniL2tpAgentV13 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV13 = juniL2tpAgentV13.setProductRelease('Version 13 of the L2TP component of the JUNOSe SNMP agent.  This\n        version of the L2TP component is supported in JUNOSe Kyoto and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV13 = juniL2tpAgentV13.setStatus('current')
juniL2tpAgentV14 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV14 = juniL2tpAgentV14.setProductRelease('Version 14 of the L2TP component of the JUNOSe SNMP agent.  This\n        version of the L2TP component is supported in JUNOSe 8.0 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpAgentV14 = juniL2tpAgentV14.setStatus('current')
mibBuilder.exportSymbols("Juniper-L2TP-CONF", juniL2tpAgentV2=juniL2tpAgentV2, juniL2tpAgentV3=juniL2tpAgentV3, juniL2tpAgentV13=juniL2tpAgentV13, juniL2tpAgentV10=juniL2tpAgentV10, juniL2tpAgentV5=juniL2tpAgentV5, juniL2tpAgentV1=juniL2tpAgentV1, juniL2tpAgentV4=juniL2tpAgentV4, PYSNMP_MODULE_ID=juniL2tpAgent, juniL2tpAgentV6=juniL2tpAgentV6, juniL2tpAgentV7=juniL2tpAgentV7, juniL2tpAgent=juniL2tpAgent, juniL2tpAgentV8=juniL2tpAgentV8, juniL2tpAgentV12=juniL2tpAgentV12, juniL2tpAgentV14=juniL2tpAgentV14, juniL2tpAgentV9=juniL2tpAgentV9, juniL2tpAgentV11=juniL2tpAgentV11)
