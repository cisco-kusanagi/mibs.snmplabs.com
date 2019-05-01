#
# PySNMP MIB module Juniper-File-Transfer-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-File-Transfer-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Integer32, Counter32, iso, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, MibIdentifier, Counter64, NotificationType, Bits, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "iso", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "MibIdentifier", "Counter64", "NotificationType", "Bits", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniFileTransferAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 15))
juniFileTransferAgent.setRevisions(('2002-09-06 16:54', '2001-03-28 13:22',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniFileTransferAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniFileTransferAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniFileTransferAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniFileTransferAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniFileTransferAgent.setDescription('The agent capabilities definitions for the File Transfer component of the SNMP agent in the Juniper E-series family of products.')
juniFileTransferAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 15, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFileTransferAgentV1 = juniFileTransferAgentV1.setProductRelease('Version 1 of the File Transfer component of the JUNOSe\n        SNMP agent.  This version of the File Transfer component was supported\n        in JUNOSe 1.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFileTransferAgentV1 = juniFileTransferAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniFileTransferAgentV1.setDescription('The MIB supported by the SNMP agent for the File System application in JUNOSe. These capabilities became obsolete when remote user information was removed and router name was added.')
juniFileTransferAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 15, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFileTransferAgentV2 = juniFileTransferAgentV2.setProductRelease('Version 2 of the File Transfer component of the JUNOSe\n        SNMP agent.  This version of the File Transfer component is supported in\n        JUNOSe 2.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFileTransferAgentV2 = juniFileTransferAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniFileTransferAgentV2.setDescription('The MIB supported by the SNMP agent for the File System application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-File-Transfer-CONF", juniFileTransferAgentV1=juniFileTransferAgentV1, juniFileTransferAgent=juniFileTransferAgent, PYSNMP_MODULE_ID=juniFileTransferAgent, juniFileTransferAgentV2=juniFileTransferAgentV2)
