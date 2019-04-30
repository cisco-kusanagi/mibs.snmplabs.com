#
# PySNMP MIB module Juniper-IP-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IP-Profile-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
juniProfileAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniProfileAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Gauge32, Integer32, iso, ObjectIdentity, NotificationType, IpAddress, Counter64, Counter32, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Gauge32", "Integer32", "iso", "ObjectIdentity", "NotificationType", "IpAddress", "Counter64", "Counter32", "Unsigned32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniIpProfileAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2))
juniIpProfileAgent.setRevisions(('2006-09-08 10:26', '2005-09-13 17:21', '2004-10-05 14:04', '2003-09-24 15:33', '2002-10-09 14:31', '2001-03-28 21:43',))
if mibBuilder.loadTexts: juniIpProfileAgent.setLastUpdated('200609081026Z')
if mibBuilder.loadTexts: juniIpProfileAgent.setOrganization('Juniper Networks, Inc.')
juniIpProfileAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV1 = juniIpProfileAgentV1.setProductRelease('Version 1 of the IP Profile component of the JUNOSe SNMP agent.  This\n        version of the IP Profile Manager component was supported in JUNOSe 1.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV1 = juniIpProfileAgentV1.setStatus('obsolete')
juniIpProfileAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV2 = juniIpProfileAgentV2.setProductRelease('Version 2 of the IP Profile component of the JUNOSe SNMP agent.  This\n        version of the IP Profile Manager component was supported in JUNOSe 2.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV2 = juniIpProfileAgentV2.setStatus('obsolete')
juniIpProfileAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV3 = juniIpProfileAgentV3.setProductRelease('Version 3 of the IP Profile component of the JUNOSe SNMP agent.  This\n        version of the IP Profile Manager component was supported in JUNOSe 3.0\n        through 4.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV3 = juniIpProfileAgentV3.setStatus('obsolete')
juniIpProfileAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV4 = juniIpProfileAgentV4.setProductRelease('Version 4 of the IP Profile component of the JUNOSe SNMP agent.  This\n        version of the IP Profile Manager component was supported in JUNOSe 5.0\n        and 5.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV4 = juniIpProfileAgentV4.setStatus('obsolete')
juniIpProfileAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV5 = juniIpProfileAgentV5.setProductRelease('Version 5 of the IP Profile component of the JUNOSe SNMP agent.  This\n        version of the IP Profile Manager component was supported in JUNOSe 5.2, 5.3, and 6.x\n        Now obsolete after IP filter options all support')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV5 = juniIpProfileAgentV5.setStatus('obsolete')
juniIpProfileAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV6 = juniIpProfileAgentV6.setProductRelease('Version 6 of the IP Profile component of the JUNOSe SNMP agent.  This\n        version of the IP Profile Manager component is supported in JUNOSe 7.0\n        and subsequent system releases. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV6 = juniIpProfileAgentV6.setStatus('obsolete')
juniIpProfileAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV7 = juniIpProfileAgentV7.setProductRelease('Version 7 of the IP Profile component of the JUNOSe SNMP agent.  This\n        version of the IP Profile Manager component is supported in JUNOSe 7.2\n        and subsequent system releases. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV7 = juniIpProfileAgentV7.setStatus('obsolete')
juniIpProfileAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV8 = juniIpProfileAgentV8.setProductRelease('Version 8 of the IP Profile component of the JUNOSe SNMP agent.  This\n        version of the IP Profile Manager component is supported in JUNOSe 8.1\n        and subsequent system releases. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV8 = juniIpProfileAgentV8.setStatus('current')
mibBuilder.exportSymbols("Juniper-IP-Profile-CONF", juniIpProfileAgent=juniIpProfileAgent, juniIpProfileAgentV4=juniIpProfileAgentV4, juniIpProfileAgentV2=juniIpProfileAgentV2, juniIpProfileAgentV6=juniIpProfileAgentV6, PYSNMP_MODULE_ID=juniIpProfileAgent, juniIpProfileAgentV1=juniIpProfileAgentV1, juniIpProfileAgentV3=juniIpProfileAgentV3, juniIpProfileAgentV7=juniIpProfileAgentV7, juniIpProfileAgentV8=juniIpProfileAgentV8, juniIpProfileAgentV5=juniIpProfileAgentV5)
