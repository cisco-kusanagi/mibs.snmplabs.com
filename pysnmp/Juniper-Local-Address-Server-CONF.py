#
# PySNMP MIB module Juniper-Local-Address-Server-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Local-Address-Server-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, IpAddress, MibIdentifier, Bits, iso, Counter64, Gauge32, Integer32, Counter32, Unsigned32, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "IpAddress", "MibIdentifier", "Bits", "iso", "Counter64", "Gauge32", "Integer32", "Counter32", "Unsigned32", "TimeTicks", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniLocalAddressServerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25))
juniLocalAddressServerAgent.setRevisions(('2005-02-11 21:35', '2003-11-04 18:30', '2002-09-06 16:54', '2002-05-06 19:20', '2001-05-02 13:22',))
if mibBuilder.loadTexts: juniLocalAddressServerAgent.setLastUpdated('200502112135Z')
if mibBuilder.loadTexts: juniLocalAddressServerAgent.setOrganization('Juniper Networks, Inc.')
juniLocalAddressServerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV1 = juniLocalAddressServerAgentV1.setProductRelease('Version 1 of the Local Address Server component of the JUNOSe SNMP\n        agent.  This version of the Local Address Server component was supported\n        in JUNOSe 1.3 thru 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV1 = juniLocalAddressServerAgentV1.setStatus('obsolete')
juniLocalAddressServerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV2 = juniLocalAddressServerAgentV2.setProductRelease('Version 2 of the Local Address Server component of the JUNOSe SNMP\n        agent.  This version of the Local Address Server component was supported\n        in JUNOSe 3.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV2 = juniLocalAddressServerAgentV2.setStatus('obsolete')
juniLocalAddressServerAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV3 = juniLocalAddressServerAgentV3.setProductRelease('Version 3 of the Local Address Server component of the JUNOSe SNMP\n        agent.  This version of the Local Address Server component was supported\n        in JUNOSe 3.3 thru 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV3 = juniLocalAddressServerAgentV3.setStatus('obsolete')
juniLocalAddressServerAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV4 = juniLocalAddressServerAgentV4.setProductRelease('Version 4 of the Local Address Server component of the JUNOSe SNMP\n        agent.  This version of the Local Address Server component is supported\n        in JUNOSe 5.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV4 = juniLocalAddressServerAgentV4.setStatus('obsolete')
juniLocalAddressServerAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV5 = juniLocalAddressServerAgentV5.setProductRelease('Version 5 of the Local Address Server component of the JUNOSe SNMP\n        agent.  This version of the Local Address Server component is supported\n        in JUNOSe 6.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV5 = juniLocalAddressServerAgentV5.setStatus('obsolete')
juniLocalAddressServerAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV6 = juniLocalAddressServerAgentV6.setProductRelease('Version 6 of the Local Address Server component of the JUNOSe SNMP\n        agent.  This version of the Local Address Server component is supported\n        in JUNOSe 7.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV6 = juniLocalAddressServerAgentV6.setStatus('current')
mibBuilder.exportSymbols("Juniper-Local-Address-Server-CONF", juniLocalAddressServerAgent=juniLocalAddressServerAgent, juniLocalAddressServerAgentV2=juniLocalAddressServerAgentV2, juniLocalAddressServerAgentV3=juniLocalAddressServerAgentV3, juniLocalAddressServerAgentV6=juniLocalAddressServerAgentV6, juniLocalAddressServerAgentV4=juniLocalAddressServerAgentV4, juniLocalAddressServerAgentV1=juniLocalAddressServerAgentV1, juniLocalAddressServerAgentV5=juniLocalAddressServerAgentV5, PYSNMP_MODULE_ID=juniLocalAddressServerAgent)
