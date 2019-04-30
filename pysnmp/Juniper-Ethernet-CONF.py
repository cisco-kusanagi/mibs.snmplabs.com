#
# PySNMP MIB module Juniper-Ethernet-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Ethernet-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, Gauge32, ModuleIdentity, ObjectIdentity, Integer32, iso, Counter32, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Integer32", "iso", "Counter32", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniEthernetAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14))
juniEthernetAgent.setRevisions(('2003-09-29 16:18', '2002-10-01 22:10', '2002-10-01 18:02', '2002-04-05 20:33', '2001-10-25 21:36',))
if mibBuilder.loadTexts: juniEthernetAgent.setLastUpdated('200309291618Z')
if mibBuilder.loadTexts: juniEthernetAgent.setOrganization('Juniper Networks, Inc.')
juniEthernetAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV1 = juniEthernetAgentV1.setProductRelease('Version 1 of the Ethernet component of the JUNOSe SNMP agent.  This\n        version of the Ethernet component was supported in JUNOSe 2.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV1 = juniEthernetAgentV1.setStatus('obsolete')
juniEthernetAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV2 = juniEthernetAgentV2.setProductRelease('Version 2 of the Ethernet component of the JUNOSe SNMP agent.  This\n        version of the Ethernet component was supported in JUNOSe 3.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV2 = juniEthernetAgentV2.setStatus('obsolete')
juniEthernetAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV3 = juniEthernetAgentV3.setProductRelease('Version 3 of the Ethernet component of the JUNOSe SNMP agent.  This\n        version of the Ethernet component was supported in JUNOSe 4.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV3 = juniEthernetAgentV3.setStatus('obsolete')
juniEthernetAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV4 = juniEthernetAgentV4.setProductRelease('Version 4 of the Ethernet component of the JUNOSe SNMP agent.  This\n        version of the Ethernet component was supported in JUNOSe 4.1 through\n        5.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV4 = juniEthernetAgentV4.setStatus('obsolete')
juniEthernetAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV5 = juniEthernetAgentV5.setProductRelease('Version 5 of the Ethernet component of the JUNOSe SNMP agent.  This\n        version of the Ethernet component is supported in JUNOSe 5.2 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV5 = juniEthernetAgentV5.setStatus('current')
mibBuilder.exportSymbols("Juniper-Ethernet-CONF", juniEthernetAgentV1=juniEthernetAgentV1, juniEthernetAgentV2=juniEthernetAgentV2, PYSNMP_MODULE_ID=juniEthernetAgent, juniEthernetAgentV5=juniEthernetAgentV5, juniEthernetAgentV4=juniEthernetAgentV4, juniEthernetAgentV3=juniEthernetAgentV3, juniEthernetAgent=juniEthernetAgent)
