#
# PySNMP MIB module Juniper-SNMP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-SNMP-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Integer32, Bits, TimeTicks, Counter64, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, ObjectIdentity, Gauge32, iso, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "TimeTicks", "Counter64", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "Gauge32", "iso", "Unsigned32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniSnmpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39))
juniSnmpAgent.setRevisions(('2003-03-10 20:27', '2002-09-06 16:54', '2002-08-20 13:29', '2002-08-14 19:23', '2001-10-16 13:44', '2001-04-13 15:44',))
if mibBuilder.loadTexts: juniSnmpAgent.setLastUpdated('200303102027Z')
if mibBuilder.loadTexts: juniSnmpAgent.setOrganization('Juniper Networks, Inc.')
juniSnmpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV1 = juniSnmpAgentV1.setProductRelease('Version 1 of the SNMP entity component of the JUNOSe SNMP agent.  This\n        version of the SNMP entity component was supported in JUNOSe 1.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV1 = juniSnmpAgentV1.setStatus('obsolete')
juniSnmpAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV2 = juniSnmpAgentV2.setProductRelease('Version 2 of the SNMP entity component of the JUNOSe SNMP agent.  This\n        version of the SNMP entity component was supported in JUNOSe 2.0 thru\n        2.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV2 = juniSnmpAgentV2.setStatus('obsolete')
juniSnmpAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV3 = juniSnmpAgentV3.setProductRelease('Version 3 of the SNMP entity component of the JUNOSe SNMP agent.  This\n        version of the SNMP entity component was supported in JUNOSe 2.3 thru\n        3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV3 = juniSnmpAgentV3.setStatus('obsolete')
juniSnmpAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV4 = juniSnmpAgentV4.setProductRelease('Version 4 of the SNMP entity component of the JUNOSe SNMP agent.  This\n        version of the SNMP entity component was supported in JUNOSe 3.2 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV4 = juniSnmpAgentV4.setStatus('obsolete')
juniSnmpAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV5 = juniSnmpAgentV5.setProductRelease('Version 5 of the SNMP entity component of the JUNOSe SNMP agent.  This\n        version of the SNMP entity component was supported in JUNOSe 3.3 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV5 = juniSnmpAgentV5.setStatus('obsolete')
juniSnmpAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV6 = juniSnmpAgentV6.setProductRelease('Version 6 of the SNMP entity component of the JUNOSe SNMP agent.  This\n        version of the SNMP entity component was supported in JUNOSe 3.4 thru\n        4.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV6 = juniSnmpAgentV6.setStatus('obsolete')
juniSnmpAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV7 = juniSnmpAgentV7.setProductRelease('Version 7 of the SNMP entity component of the JUNOSe SNMP\n        agent.  This version of the SNMP entity component is supported in the\n        JUNOSe 4.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV7 = juniSnmpAgentV7.setStatus('obsolete')
juniSnmpAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV8 = juniSnmpAgentV8.setProductRelease('Version 8 of the SNMP entity component of the JUNOSe SNMP agent.  This\n        version of the SNMP entity component is supported in JUNOSe 5.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV8 = juniSnmpAgentV8.setStatus('obsolete')
juniSnmpAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV9 = juniSnmpAgentV9.setProductRelease('Version 9 of the SNMP entity component of the JUNOSe SNMP agent.  This\n        version of the SNMP entity component is supported in JUNOSe 9.3 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV9 = juniSnmpAgentV9.setStatus('obsolete')
juniSnmpAgentV10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV10 = juniSnmpAgentV10.setProductRelease('Version 10 of the SNMP entity component of the JUNOSe SNMP agent.  This\n        version of the SNMP entity component is supported in JUNOSe 10.2 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV10 = juniSnmpAgentV10.setStatus('current')
mibBuilder.exportSymbols("Juniper-SNMP-CONF", juniSnmpAgentV9=juniSnmpAgentV9, juniSnmpAgentV2=juniSnmpAgentV2, juniSnmpAgentV1=juniSnmpAgentV1, PYSNMP_MODULE_ID=juniSnmpAgent, juniSnmpAgentV7=juniSnmpAgentV7, juniSnmpAgentV4=juniSnmpAgentV4, juniSnmpAgentV8=juniSnmpAgentV8, juniSnmpAgent=juniSnmpAgent, juniSnmpAgentV6=juniSnmpAgentV6, juniSnmpAgentV10=juniSnmpAgentV10, juniSnmpAgentV5=juniSnmpAgentV5, juniSnmpAgentV3=juniSnmpAgentV3)
