#
# PySNMP MIB module Juniper-Interfaces-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Interfaces-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ModuleIdentity, TimeTicks, Integer32, Gauge32, MibIdentifier, Unsigned32, iso, NotificationType, Counter64, Bits, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Integer32", "Gauge32", "MibIdentifier", "Unsigned32", "iso", "NotificationType", "Counter64", "Bits", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniInterfacesAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 20))
juniInterfacesAgent.setRevisions(('2004-02-04 21:38', '2003-07-16 21:38', '2002-12-16 14:43', '2001-04-27 14:24',))
if mibBuilder.loadTexts: juniInterfacesAgent.setLastUpdated('200307162138Z')
if mibBuilder.loadTexts: juniInterfacesAgent.setOrganization('Juniper Networks, Inc.')
juniInterfacesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 20, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniInterfacesAgentV1 = juniInterfacesAgentV1.setProductRelease('Version 1 of the Interfaces component of the JUNOSe SNMP agent.  This\n        version of the Interfaces component was supported in JUNOSe 1.0 thru 5.0\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniInterfacesAgentV1 = juniInterfacesAgentV1.setStatus('current')
juniInterfacesAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 20, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniInterfacesAgentV2 = juniInterfacesAgentV2.setProductRelease('Version 2 of the Interfaces component of the JUNOSe SNMP agent.  This\n        version of the Interfaces component is supported in JUNOSe 1.0 and\n        subsequent 2.0, 3.x, 4.x and 5.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniInterfacesAgentV2 = juniInterfacesAgentV2.setStatus('obsolete')
juniInterfacesAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 20, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniInterfacesAgentV3 = juniInterfacesAgentV3.setProductRelease('Version 3 of the Interfaces component of the JUNOSe SNMP agent.  This\n        version of the Interfaces component is supported in JUNOSe 1.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniInterfacesAgentV3 = juniInterfacesAgentV3.setStatus('current')
mibBuilder.exportSymbols("Juniper-Interfaces-CONF", juniInterfacesAgentV3=juniInterfacesAgentV3, juniInterfacesAgentV2=juniInterfacesAgentV2, PYSNMP_MODULE_ID=juniInterfacesAgent, juniInterfacesAgent=juniInterfacesAgent, juniInterfacesAgentV1=juniInterfacesAgentV1)
