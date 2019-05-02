#
# PySNMP MIB module Unisphere-Data-File-Transfer-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-File-Transfer-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:31:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
iso, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, Integer32, Unsigned32, IpAddress, Bits, MibIdentifier, ModuleIdentity, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "Integer32", "Unsigned32", "IpAddress", "Bits", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdFileXferGroup1, usdFileXferGroup2, usdFileXferTrapGroup = mibBuilder.importSymbols("Unisphere-Data-FILE-XFER-MIB", "usdFileXferGroup1", "usdFileXferGroup2", "usdFileXferTrapGroup")
usdFileTransferAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 15))
usdFileTransferAgent.setRevisions(('2001-03-28 13:22',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdFileTransferAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdFileTransferAgent.setLastUpdated('200103281322Z')
if mibBuilder.loadTexts: usdFileTransferAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdFileTransferAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdFileTransferAgent.setDescription('The agent capabilities definitions for the File Transfer component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdFileTransferAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 15, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFileTransferAgentV1 = usdFileTransferAgentV1.setProductRelease('Version 1 of the File Transfer component of the Unisphere Routing\n        Switch SNMP agent.  This version of the File Transfer component was\n        supported in the Unisphere RX 1.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFileTransferAgentV1 = usdFileTransferAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdFileTransferAgentV1.setDescription('The MIB supported by the SNMP agent for the File System application in the Unisphere Routing Switch. These capabilities became obsolete when remote user information was removed and router name was added.')
usdFileTransferAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 15, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFileTransferAgentV2 = usdFileTransferAgentV2.setProductRelease('Version 2 of the File Transfer component of the Unisphere Routing\n        Switch SNMP agent.  This version of the File Transfer component is\n        supported in the Unisphere RX 2.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFileTransferAgentV2 = usdFileTransferAgentV2.setStatus('current')
if mibBuilder.loadTexts: usdFileTransferAgentV2.setDescription('The MIB supported by the SNMP agent for the File System application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-File-Transfer-CONF", usdFileTransferAgent=usdFileTransferAgent, usdFileTransferAgentV2=usdFileTransferAgentV2, usdFileTransferAgentV1=usdFileTransferAgentV1, PYSNMP_MODULE_ID=usdFileTransferAgent)
