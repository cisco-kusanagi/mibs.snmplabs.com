#
# PySNMP MIB module Unisphere-Data-File-Transfer-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-File-Transfer-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter32, NotificationType, Bits, ObjectIdentity, Gauge32, IpAddress, ModuleIdentity, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "Bits", "ObjectIdentity", "Gauge32", "IpAddress", "ModuleIdentity", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "Unsigned32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdFileXferGroup2, usdFileXferGroup1, usdFileXferTrapGroup = mibBuilder.importSymbols("Unisphere-Data-FILE-XFER-MIB", "usdFileXferGroup2", "usdFileXferGroup1", "usdFileXferTrapGroup")
usdFileTransferAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 15))
usdFileTransferAgent.setRevisions(('2001-03-28 13:22',))
if mibBuilder.loadTexts: usdFileTransferAgent.setLastUpdated('200103281322Z')
if mibBuilder.loadTexts: usdFileTransferAgent.setOrganization('Unisphere Networks, Inc.')
usdFileTransferAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 15, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFileTransferAgentV1 = usdFileTransferAgentV1.setProductRelease('Version 1 of the File Transfer component of the Unisphere Routing\n        Switch SNMP agent.  This version of the File Transfer component was\n        supported in the Unisphere RX 1.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFileTransferAgentV1 = usdFileTransferAgentV1.setStatus('obsolete')
usdFileTransferAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 15, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFileTransferAgentV2 = usdFileTransferAgentV2.setProductRelease('Version 2 of the File Transfer component of the Unisphere Routing\n        Switch SNMP agent.  This version of the File Transfer component is\n        supported in the Unisphere RX 2.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFileTransferAgentV2 = usdFileTransferAgentV2.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-File-Transfer-CONF", usdFileTransferAgent=usdFileTransferAgent, PYSNMP_MODULE_ID=usdFileTransferAgent, usdFileTransferAgentV1=usdFileTransferAgentV1, usdFileTransferAgentV2=usdFileTransferAgentV2)
