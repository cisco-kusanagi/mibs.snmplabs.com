#
# PySNMP MIB module Juniper-ERX-System-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-ERX-System-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
juniSystemAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniSystemAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, ObjectIdentity, Counter64, ModuleIdentity, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Gauge32, Bits, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "ObjectIdentity", "Counter64", "ModuleIdentity", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Gauge32", "Bits", "Counter32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniErxSystemAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1))
juniErxSystemAgent.setRevisions(('2003-11-24 19:53', '2003-01-28 21:48', '2002-08-19 13:17', '2002-04-01 22:32', '2001-04-13 13:03',))
if mibBuilder.loadTexts: juniErxSystemAgent.setLastUpdated('200311241953Z')
if mibBuilder.loadTexts: juniErxSystemAgent.setOrganization('Juniper Networks, Inc.')
juniErxSystemAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV1 = juniErxSystemAgentV1.setProductRelease('Version 1 of the System component of the JUNOSe SNMP agent.  This\n        version of the ERX System component was supported in the JUNOSe 1.3\n        system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV1 = juniErxSystemAgentV1.setStatus('obsolete')
juniErxSystemAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV2 = juniErxSystemAgentV2.setProductRelease('Version 2 of the System component of the JUNOSe SNMP agent.  This\n        version of the ERX System component was supported in the JUNOSe 2.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV2 = juniErxSystemAgentV2.setStatus('obsolete')
juniErxSystemAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV3 = juniErxSystemAgentV3.setProductRelease('Version 3 of the System component of the JUNOSe SNMP agent.  This\n        version of the ERX System component was supported in the JUNOSe 3.0 and\n        3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV3 = juniErxSystemAgentV3.setStatus('obsolete')
juniErxSystemAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV4 = juniErxSystemAgentV4.setProductRelease('Version 4 of the System component of the JUNOSe SNMP agent.  This\n        version of the ERX System component was supported in the JUNOSe 3.2\n        system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV4 = juniErxSystemAgentV4.setStatus('obsolete')
juniErxSystemAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV5 = juniErxSystemAgentV5.setProductRelease('Version 5 of the System component of the JUNOSe SNMP agent.  This\n        version of the ERX System component is supported in the JUNOSe 3.3 thru\n        4.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV5 = juniErxSystemAgentV5.setStatus('obsolete')
juniErxSystemAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV6 = juniErxSystemAgentV6.setProductRelease('Version 6 of the System component of the JUNOSe SNMP agent.  This\n        version of the ERX System component was supported in the JUNOSe 4.1 and\n        subsequent 4.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV6 = juniErxSystemAgentV6.setStatus('obsolete')
juniErxSystemAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV7 = juniErxSystemAgentV7.setProductRelease('Version 7 of the System component of the JUNOSe SNMP agent.  This\n        version of the ERX System component was supported in the JUNOSe 5.0 and\n        5.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV7 = juniErxSystemAgentV7.setStatus('obsolete')
juniErxSystemAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV8 = juniErxSystemAgentV8.setProductRelease('Version 8 of the System component of the JUNOSe SNMP agent.  This\n        version of the ERX System component is supported in the JUNOSe 5.2 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV8 = juniErxSystemAgentV8.setStatus('current')
mibBuilder.exportSymbols("Juniper-ERX-System-CONF", juniErxSystemAgentV8=juniErxSystemAgentV8, PYSNMP_MODULE_ID=juniErxSystemAgent, juniErxSystemAgent=juniErxSystemAgent, juniErxSystemAgentV7=juniErxSystemAgentV7, juniErxSystemAgentV4=juniErxSystemAgentV4, juniErxSystemAgentV3=juniErxSystemAgentV3, juniErxSystemAgentV6=juniErxSystemAgentV6, juniErxSystemAgentV1=juniErxSystemAgentV1, juniErxSystemAgentV5=juniErxSystemAgentV5, juniErxSystemAgentV2=juniErxSystemAgentV2)
