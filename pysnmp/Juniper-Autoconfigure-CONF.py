#
# PySNMP MIB module Juniper-Autoconfigure-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Autoconfigure-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, TimeTicks, ModuleIdentity, Gauge32, ObjectIdentity, Counter64, IpAddress, Integer32, iso, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "TimeTicks", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Counter64", "IpAddress", "Integer32", "iso", "MibIdentifier", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniAutoConfAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 44))
juniAutoConfAgent.setRevisions(('2004-07-26 19:54', '2002-09-06 16:54', '2001-03-27 20:08',))
if mibBuilder.loadTexts: juniAutoConfAgent.setLastUpdated('200407261954Z')
if mibBuilder.loadTexts: juniAutoConfAgent.setOrganization('Juniper Networks, Inc.')
juniAutoConfAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 44, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfAgentV1 = juniAutoConfAgentV1.setProductRelease('Version 1 of the Auto-Configuration component of the JUNOSe SNMP agent.\n        This version of the Auto-Configuration component is supported in JUNOSe\n        3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfAgentV1 = juniAutoConfAgentV1.setStatus('obsolete')
juniAutoConfAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 44, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfAgentV2 = juniAutoConfAgentV2.setProductRelease('Version 2 of the Auto-Configuration component of the JUNOSe SNMP agent.\n        This version of the Auto-Configuration component is supported in JUNOSe\n        7.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfAgentV2 = juniAutoConfAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-Autoconfigure-CONF", PYSNMP_MODULE_ID=juniAutoConfAgent, juniAutoConfAgentV2=juniAutoConfAgentV2, juniAutoConfAgent=juniAutoConfAgent, juniAutoConfAgentV1=juniAutoConfAgentV1)
