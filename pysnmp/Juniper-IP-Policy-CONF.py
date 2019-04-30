#
# PySNMP MIB module Juniper-IP-Policy-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IP-Policy-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Gauge32, iso, Counter64, TimeTicks, Bits, Integer32, ModuleIdentity, ObjectIdentity, Counter32, IpAddress, Unsigned32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "Counter64", "TimeTicks", "Bits", "Integer32", "ModuleIdentity", "ObjectIdentity", "Counter32", "IpAddress", "Unsigned32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniIpPolicyAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22))
juniIpPolicyAgent.setRevisions(('2003-02-05 14:58', '2002-09-06 16:54', '2001-05-01 20:13',))
if mibBuilder.loadTexts: juniIpPolicyAgent.setLastUpdated('200302051458Z')
if mibBuilder.loadTexts: juniIpPolicyAgent.setOrganization('Juniper Networks, Inc.')
juniIpPolicyAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpPolicyAgentV1 = juniIpPolicyAgentV1.setProductRelease('Version 1 of the IP Policy component of the JUNOSe SNMP agent.  This\n        version of the IP Policy component was supported in JUNOSe 1.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpPolicyAgentV1 = juniIpPolicyAgentV1.setStatus('obsolete')
juniIpPolicyAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpPolicyAgentV2 = juniIpPolicyAgentV2.setProductRelease('Version 2 of the IP Policy component of the JUNOSe SNMP agent.  This\n        version of the IP Policy component was supported in JUNOSe 2.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpPolicyAgentV2 = juniIpPolicyAgentV2.setStatus('obsolete')
juniIpPolicyAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpPolicyAgentV3 = juniIpPolicyAgentV3.setProductRelease('Version 3 of the IP Policy component of the JUNOSe SNMP agent.  This\n        version of the IP Policy component was supported in JUNOSe 3.0 thru 5.0\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpPolicyAgentV3 = juniIpPolicyAgentV3.setStatus('obsolete')
juniIpPolicyAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpPolicyAgentV4 = juniIpPolicyAgentV4.setProductRelease('Version 4 of the IP Policy component of the JUNOSe SNMP agent.  This\n        version of the IP Policy component is supported in JUNOSe 5.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpPolicyAgentV4 = juniIpPolicyAgentV4.setStatus('current')
mibBuilder.exportSymbols("Juniper-IP-Policy-CONF", juniIpPolicyAgentV3=juniIpPolicyAgentV3, juniIpPolicyAgentV1=juniIpPolicyAgentV1, juniIpPolicyAgentV4=juniIpPolicyAgentV4, juniIpPolicyAgent=juniIpPolicyAgent, PYSNMP_MODULE_ID=juniIpPolicyAgent, juniIpPolicyAgentV2=juniIpPolicyAgentV2)
