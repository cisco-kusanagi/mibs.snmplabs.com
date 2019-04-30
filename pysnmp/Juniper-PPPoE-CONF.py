#
# PySNMP MIB module Juniper-PPPoE-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-PPPoE-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Gauge32, Counter32, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, ObjectIdentity, TimeTicks, MibIdentifier, Unsigned32, NotificationType, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Unsigned32", "NotificationType", "iso", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniPppoeAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33))
juniPppoeAgent.setRevisions(('2008-11-27 10:23', '2005-08-03 20:58', '2005-07-13 11:40', '2004-06-14 20:48', '2003-03-10 18:48', '2002-12-23 19:41', '2002-10-01 18:37', '2002-08-19 15:14', '2001-06-19 14:27', '2001-04-02 19:21',))
if mibBuilder.loadTexts: juniPppoeAgent.setLastUpdated('200811271023Z')
if mibBuilder.loadTexts: juniPppoeAgent.setOrganization('Juniper Networks, Inc.')
juniPppoeAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV1 = juniPppoeAgentV1.setProductRelease('Version 1 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component was supported in JUNOSe 3.0 thru 3.2.2\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV1 = juniPppoeAgentV1.setStatus('obsolete')
juniPppoeAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV2 = juniPppoeAgentV2.setProductRelease('Version 2 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component was supported in JUNOSe 3.2.3 through 3.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV2 = juniPppoeAgentV2.setStatus('obsolete')
juniPppoeAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV3 = juniPppoeAgentV3.setProductRelease('Version 3 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component was supported in JUNOSe 4.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV3 = juniPppoeAgentV3.setStatus('obsolete')
juniPppoeAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV4 = juniPppoeAgentV4.setProductRelease('Version 4 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component was supported in JUNOSe 4.1 through 5.0\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV4 = juniPppoeAgentV4.setStatus('obsolete')
juniPppoeAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV5 = juniPppoeAgentV5.setProductRelease('Version 5 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component was supported in JUNOSe 5.1 through 7.0\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV5 = juniPppoeAgentV5.setStatus('obsolete')
juniPppoeAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV6 = juniPppoeAgentV6.setProductRelease('Version 6 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component is supported in JUNOSe 7.0 system\n        release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV6 = juniPppoeAgentV6.setStatus('obsolete')
juniPppoeAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV7 = juniPppoeAgentV7.setProductRelease('Version 7 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component is supported in JUNOSe 7.0.1 through 7.1\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV7 = juniPppoeAgentV7.setStatus('obsolete')
juniPppoeAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV8 = juniPppoeAgentV8.setProductRelease('Version 8 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component is supported in JUNOSe 7.2 through 9.3 \n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV8 = juniPppoeAgentV8.setStatus('obsolete')
juniPppoeAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV9 = juniPppoeAgentV9.setProductRelease('Version 9 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component is supported in JUNOSe 10.1 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV9 = juniPppoeAgentV9.setStatus('current')
mibBuilder.exportSymbols("Juniper-PPPoE-CONF", juniPppoeAgentV1=juniPppoeAgentV1, PYSNMP_MODULE_ID=juniPppoeAgent, juniPppoeAgentV5=juniPppoeAgentV5, juniPppoeAgent=juniPppoeAgent, juniPppoeAgentV2=juniPppoeAgentV2, juniPppoeAgentV6=juniPppoeAgentV6, juniPppoeAgentV8=juniPppoeAgentV8, juniPppoeAgentV4=juniPppoeAgentV4, juniPppoeAgentV7=juniPppoeAgentV7, juniPppoeAgentV3=juniPppoeAgentV3, juniPppoeAgentV9=juniPppoeAgentV9)
