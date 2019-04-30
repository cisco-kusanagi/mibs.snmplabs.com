#
# PySNMP MIB module Juniper-RADIUS-CLIENT-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-RADIUS-CLIENT-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Gauge32, IpAddress, Integer32, iso, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, Counter64, Unsigned32, ModuleIdentity, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "Integer32", "iso", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "Counter64", "Unsigned32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniRadiusClientAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35))
juniRadiusClientAgent.setRevisions(('2009-02-10 15:20', '2007-12-14 15:00', '2007-09-18 18:22', '2007-04-10 01:03', '2006-02-17 22:00', '2006-01-12 22:00', '2004-12-06 02:32', '2004-12-03 22:12', '2003-12-18 21:03', '2003-05-21 19:18', '2003-03-10 19:51', '2003-01-27 18:36', '2002-11-21 19:26', '2001-10-19 14:44', '2001-10-16 20:45', '2001-09-07 12:35',))
if mibBuilder.loadTexts: juniRadiusClientAgent.setLastUpdated('200902101520Z')
if mibBuilder.loadTexts: juniRadiusClientAgent.setOrganization('Juniper Networks, Inc.')
juniRadiusClientDynamicAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1))
if mibBuilder.loadTexts: juniRadiusClientDynamicAgent.setStatus('current')
juniRadiusClientDynamicAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV1 = juniRadiusClientDynamicAgentV1.setProductRelease('Version 1 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 1.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV1 = juniRadiusClientDynamicAgentV1.setStatus('obsolete')
juniRadiusClientDynamicAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV2 = juniRadiusClientDynamicAgentV2.setProductRelease('Version 2 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV2 = juniRadiusClientDynamicAgentV2.setStatus('obsolete')
juniRadiusClientDynamicAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV3 = juniRadiusClientDynamicAgentV3.setProductRelease('Version 3 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 3.0 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV3 = juniRadiusClientDynamicAgentV3.setStatus('obsolete')
juniRadiusClientDynamicAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV4 = juniRadiusClientDynamicAgentV4.setProductRelease('Version 4 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 3.1 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV4 = juniRadiusClientDynamicAgentV4.setStatus('obsolete')
juniRadiusClientDynamicAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV5 = juniRadiusClientDynamicAgentV5.setProductRelease('Version 5 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 3.2 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV5 = juniRadiusClientDynamicAgentV5.setStatus('obsolete')
juniRadiusClientDynamicAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV6 = juniRadiusClientDynamicAgentV6.setProductRelease('Version 6 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 3.3 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV6 = juniRadiusClientDynamicAgentV6.setStatus('obsolete')
juniRadiusClientDynamicAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV7 = juniRadiusClientDynamicAgentV7.setProductRelease('Version 7 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 4.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV7 = juniRadiusClientDynamicAgentV7.setStatus('obsolete')
juniRadiusClientDynamicAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV8 = juniRadiusClientDynamicAgentV8.setProductRelease('Version 8 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 4.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV8 = juniRadiusClientDynamicAgentV8.setStatus('obsolete')
juniRadiusClientDynamicAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV9 = juniRadiusClientDynamicAgentV9.setProductRelease('Version 9 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV9 = juniRadiusClientDynamicAgentV9.setStatus('obsolete')
juniRadiusClientDynamicAgentV10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV10 = juniRadiusClientDynamicAgentV10.setProductRelease('Version 10 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 5.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV10 = juniRadiusClientDynamicAgentV10.setStatus('obsolete')
juniRadiusClientDynamicAgentV11 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV11 = juniRadiusClientDynamicAgentV11.setProductRelease('Version 11 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component was\n        supported in JUNOSe 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV11 = juniRadiusClientDynamicAgentV11.setStatus('obsolete')
juniRadiusClientDynamicAgentV12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV12 = juniRadiusClientDynamicAgentV12.setProductRelease('Version 12 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  These capabilities became obsolete when a new\n        B-RAS object was added.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV12 = juniRadiusClientDynamicAgentV12.setStatus('obsolete')
juniRadiusClientDynamicAgentV13 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV13 = juniRadiusClientDynamicAgentV13.setProductRelease('Version 13 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 6.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV13 = juniRadiusClientDynamicAgentV13.setStatus('obsolete')
juniRadiusClientDynamicAgentV14 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV14 = juniRadiusClientDynamicAgentV14.setProductRelease('Version 14 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 6.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV14 = juniRadiusClientDynamicAgentV14.setStatus('obsolete')
juniRadiusClientDynamicAgentV15 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV15 = juniRadiusClientDynamicAgentV15.setProductRelease('Version 15 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 6.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV15 = juniRadiusClientDynamicAgentV15.setStatus('obsolete')
juniRadiusClientDynamicAgentV16 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV16 = juniRadiusClientDynamicAgentV16.setProductRelease('Version 16 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 7.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV16 = juniRadiusClientDynamicAgentV16.setStatus('obsolete')
juniRadiusClientDynamicAgentV17 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV17 = juniRadiusClientDynamicAgentV17.setProductRelease('Version 17 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 7.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV17 = juniRadiusClientDynamicAgentV17.setStatus('obsolete')
juniRadiusClientDynamicAgentV18 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV18 = juniRadiusClientDynamicAgentV18.setProductRelease('Version 18 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 8.1.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV18 = juniRadiusClientDynamicAgentV18.setStatus('obsolete')
juniRadiusClientDynamicAgentV19 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV19 = juniRadiusClientDynamicAgentV19.setProductRelease('Version 19 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 8.2.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV19 = juniRadiusClientDynamicAgentV19.setStatus('obsolete')
juniRadiusClientDynamicAgentV20 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 20))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV20 = juniRadiusClientDynamicAgentV20.setProductRelease('Version 20 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 9.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV20 = juniRadiusClientDynamicAgentV20.setStatus('obsolete')
juniRadiusClientDynamicAgentV21 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 21))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV21 = juniRadiusClientDynamicAgentV21.setProductRelease('Version 21 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 10.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV21 = juniRadiusClientDynamicAgentV21.setStatus('obsolete')
juniRadiusClientDynamicAgentV22 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 22))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV22 = juniRadiusClientDynamicAgentV22.setProductRelease('Version 22 of the RADIUS Client dynamic interface component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 10.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientDynamicAgentV22 = juniRadiusClientDynamicAgentV22.setStatus('current')
juniRadiusClientBasicAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 2))
if mibBuilder.loadTexts: juniRadiusClientBasicAgent.setStatus('current')
juniRadiusClientBasicAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientBasicAgentV1 = juniRadiusClientBasicAgentV1.setProductRelease('Version 1 of the basic authentication RADIUS Client component of the\n        JUNOSe SNMP agent.  This version of the RADIUS Client component is\n        supported in JUNOSe 3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusClientBasicAgentV1 = juniRadiusClientBasicAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-RADIUS-CLIENT-CONF", juniRadiusClientDynamicAgentV1=juniRadiusClientDynamicAgentV1, juniRadiusClientDynamicAgentV21=juniRadiusClientDynamicAgentV21, juniRadiusClientDynamicAgentV10=juniRadiusClientDynamicAgentV10, juniRadiusClientDynamicAgentV22=juniRadiusClientDynamicAgentV22, juniRadiusClientDynamicAgentV4=juniRadiusClientDynamicAgentV4, juniRadiusClientDynamicAgentV6=juniRadiusClientDynamicAgentV6, juniRadiusClientDynamicAgentV20=juniRadiusClientDynamicAgentV20, juniRadiusClientBasicAgentV1=juniRadiusClientBasicAgentV1, juniRadiusClientDynamicAgentV12=juniRadiusClientDynamicAgentV12, juniRadiusClientDynamicAgentV7=juniRadiusClientDynamicAgentV7, juniRadiusClientDynamicAgentV15=juniRadiusClientDynamicAgentV15, juniRadiusClientAgent=juniRadiusClientAgent, juniRadiusClientDynamicAgentV11=juniRadiusClientDynamicAgentV11, juniRadiusClientDynamicAgentV2=juniRadiusClientDynamicAgentV2, juniRadiusClientDynamicAgentV13=juniRadiusClientDynamicAgentV13, juniRadiusClientDynamicAgentV18=juniRadiusClientDynamicAgentV18, juniRadiusClientDynamicAgentV17=juniRadiusClientDynamicAgentV17, juniRadiusClientDynamicAgentV19=juniRadiusClientDynamicAgentV19, juniRadiusClientBasicAgent=juniRadiusClientBasicAgent, juniRadiusClientDynamicAgentV9=juniRadiusClientDynamicAgentV9, juniRadiusClientDynamicAgentV14=juniRadiusClientDynamicAgentV14, juniRadiusClientDynamicAgent=juniRadiusClientDynamicAgent, juniRadiusClientDynamicAgentV5=juniRadiusClientDynamicAgentV5, PYSNMP_MODULE_ID=juniRadiusClientAgent, juniRadiusClientDynamicAgentV16=juniRadiusClientDynamicAgentV16, juniRadiusClientDynamicAgentV8=juniRadiusClientDynamicAgentV8, juniRadiusClientDynamicAgentV3=juniRadiusClientDynamicAgentV3)
