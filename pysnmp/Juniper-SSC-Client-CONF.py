#
# PySNMP MIB module Juniper-SSC-Client-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-SSC-Client-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
IpAddress, Gauge32, NotificationType, Unsigned32, Counter32, MibIdentifier, Counter64, ObjectIdentity, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "NotificationType", "Unsigned32", "Counter32", "MibIdentifier", "Counter64", "ObjectIdentity", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniSscClientAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41))
juniSscClientAgent.setRevisions(('2003-11-18 21:11', '2002-09-06 16:54', '2001-09-19 20:29', '2001-03-30 15:18',))
if mibBuilder.loadTexts: juniSscClientAgent.setLastUpdated('200311182111Z')
if mibBuilder.loadTexts: juniSscClientAgent.setOrganization('Juniper Networks, Inc.')
juniSscClientAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSscClientAgentV1 = juniSscClientAgentV1.setProductRelease('Version 1 of the SSC Client component of the JUNOSe SNMP agent.  This\n        version of the SSC Client component was supported in JUNOSe 2.0 thru 3.0\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSscClientAgentV1 = juniSscClientAgentV1.setStatus('obsolete')
juniSscClientAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSscClientAgentV2 = juniSscClientAgentV2.setProductRelease('Version 2 of the SSC Client component of the JUNOSe SNMP agent.  This\n        version of the SSC Client component was supported in JUNOSe 3.1 and\n        subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSscClientAgentV2 = juniSscClientAgentV2.setStatus('obsolete')
juniSscClientAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSscClientAgentV3 = juniSscClientAgentV3.setProductRelease('Version 3 of the SSC Client component of the JUNOSe SNMP agent.  This\n        version of the SSC Client component was supported in JUNOSe 4.0 through\n        5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSscClientAgentV3 = juniSscClientAgentV3.setStatus('obsolete')
juniSscClientAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSscClientAgentV4 = juniSscClientAgentV4.setProductRelease('Version 4 of the SSC Client component of the JUNOSe SNMP agent.  This\n        version of the SSC Client component is supported in JUNOSe 5.3 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSscClientAgentV4 = juniSscClientAgentV4.setStatus('current')
mibBuilder.exportSymbols("Juniper-SSC-Client-CONF", juniSscClientAgentV3=juniSscClientAgentV3, juniSscClientAgent=juniSscClientAgent, PYSNMP_MODULE_ID=juniSscClientAgent, juniSscClientAgentV4=juniSscClientAgentV4, juniSscClientAgentV2=juniSscClientAgentV2, juniSscClientAgentV1=juniSscClientAgentV1)
