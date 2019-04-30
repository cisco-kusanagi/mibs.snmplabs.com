#
# PySNMP MIB module Juniper-File-Transfer-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-File-Transfer-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Unsigned32, NotificationType, Gauge32, iso, MibIdentifier, IpAddress, TimeTicks, Integer32, Counter32, Bits, ModuleIdentity, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "Gauge32", "iso", "MibIdentifier", "IpAddress", "TimeTicks", "Integer32", "Counter32", "Bits", "ModuleIdentity", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniFileTransferAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 15))
juniFileTransferAgent.setRevisions(('2002-09-06 16:54', '2001-03-28 13:22',))
if mibBuilder.loadTexts: juniFileTransferAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniFileTransferAgent.setOrganization('Juniper Networks, Inc.')
juniFileTransferAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 15, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFileTransferAgentV1 = juniFileTransferAgentV1.setProductRelease('Version 1 of the File Transfer component of the JUNOSe\n        SNMP agent.  This version of the File Transfer component was supported\n        in JUNOSe 1.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFileTransferAgentV1 = juniFileTransferAgentV1.setStatus('obsolete')
juniFileTransferAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 15, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFileTransferAgentV2 = juniFileTransferAgentV2.setProductRelease('Version 2 of the File Transfer component of the JUNOSe\n        SNMP agent.  This version of the File Transfer component is supported in\n        JUNOSe 2.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFileTransferAgentV2 = juniFileTransferAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-File-Transfer-CONF", juniFileTransferAgentV1=juniFileTransferAgentV1, juniFileTransferAgentV2=juniFileTransferAgentV2, juniFileTransferAgent=juniFileTransferAgent, PYSNMP_MODULE_ID=juniFileTransferAgent)
