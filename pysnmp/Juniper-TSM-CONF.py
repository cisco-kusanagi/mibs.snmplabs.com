#
# PySNMP MIB module Juniper-TSM-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-TSM-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, IpAddress, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, ObjectIdentity, TimeTicks, ModuleIdentity, Integer32, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "IpAddress", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Integer32", "MibIdentifier", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniTsmAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 67))
juniTsmAgent.setRevisions(('2003-10-27 22:50',))
if mibBuilder.loadTexts: juniTsmAgent.setLastUpdated('200310272250Z')
if mibBuilder.loadTexts: juniTsmAgent.setOrganization('Juniper Networks, Inc.')
juniTsmAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 67, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTsmAgentV1 = juniTsmAgentV1.setProductRelease('Version 1 of the Terminal Server Management (TSM) component of the\n        JUNOSe SNMP agent.  This version of the TSM component is supported in\n        JUNOSe 5.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTsmAgentV1 = juniTsmAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-TSM-CONF", juniTsmAgent=juniTsmAgent, PYSNMP_MODULE_ID=juniTsmAgent, juniTsmAgentV1=juniTsmAgentV1)
