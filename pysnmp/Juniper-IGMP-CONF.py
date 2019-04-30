#
# PySNMP MIB module Juniper-IGMP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IGMP-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
TimeTicks, ModuleIdentity, iso, ObjectIdentity, Bits, Gauge32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, IpAddress, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "iso", "ObjectIdentity", "Bits", "Gauge32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "IpAddress", "Integer32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniIgmpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 19))
juniIgmpAgent.setRevisions(('2006-08-25 05:40', '2003-09-29 18:22', '2002-10-28 15:06', '2002-08-29 20:48', '2001-03-28 17:20',))
if mibBuilder.loadTexts: juniIgmpAgent.setLastUpdated('200608250540Z')
if mibBuilder.loadTexts: juniIgmpAgent.setOrganization('Juniper Networks, Inc.')
juniIgmpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 19, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV1 = juniIgmpAgentV1.setProductRelease('Version 1 of the IGMP component of the JUNOSe SNMP agent.  This version\n        of the IGMP component was supported in JUNOSe 3.0 thru 4.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV1 = juniIgmpAgentV1.setStatus('obsolete')
juniIgmpAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 19, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV2 = juniIgmpAgentV2.setProductRelease('Version 2 of the IGMP component of the JUNOSe SNMP agent.  This version\n        of the IGMP component was supported in JUNOSe 4.1 and subsequent 4.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV2 = juniIgmpAgentV2.setStatus('obsolete')
juniIgmpAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 19, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV3 = juniIgmpAgentV3.setProductRelease('Version 3 of the IGMP component of the JUNOSe SNMP agent.  This version\n        of the IGMP component was supported in JUNOSe 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV3 = juniIgmpAgentV3.setStatus('obsolete')
juniIgmpAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 19, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV4 = juniIgmpAgentV4.setProductRelease('Version 4 of the IGMP component of the JUNOSe SNMP agent.  This version\n        of the IGMP component is supported in JUNOSe 5.1 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV4 = juniIgmpAgentV4.setStatus('deprecated')
juniIgmpAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 19, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV5 = juniIgmpAgentV5.setProductRelease('Version 5 of the IGMP component of the JUNOSe SNMP agent.  This version\n        of the IGMP component is supported in JUNOSe 7.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV5 = juniIgmpAgentV5.setStatus('current')
mibBuilder.exportSymbols("Juniper-IGMP-CONF", PYSNMP_MODULE_ID=juniIgmpAgent, juniIgmpAgentV2=juniIgmpAgentV2, juniIgmpAgent=juniIgmpAgent, juniIgmpAgentV3=juniIgmpAgentV3, juniIgmpAgentV5=juniIgmpAgentV5, juniIgmpAgentV4=juniIgmpAgentV4, juniIgmpAgentV1=juniIgmpAgentV1)
