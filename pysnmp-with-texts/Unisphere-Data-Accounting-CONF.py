#
# PySNMP MIB module Unisphere-Data-Accounting-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Accounting-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:30:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acctngFileCollectFailedAttempts, acctngFileMinAge, acctngFileFormat, acctngSelectionType, acctngBasicGroup = mibBuilder.importSymbols("ACCOUNTING-CONTROL-MIB", "acctngFileCollectFailedAttempts", "acctngFileMinAge", "acctngFileFormat", "acctngSelectionType", "acctngBasicGroup")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, ObjectIdentity, Unsigned32, IpAddress, Integer32, Gauge32, MibIdentifier, TimeTicks, Counter32, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "ObjectIdentity", "Unsigned32", "IpAddress", "Integer32", "Gauge32", "MibIdentifier", "TimeTicks", "Counter32", "Counter64", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usdAcctngBasicGroup3, usdAcctngBasicGroup, usdAcctngBasicGroup2 = mibBuilder.importSymbols("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngBasicGroup3", "usdAcctngBasicGroup", "usdAcctngBasicGroup2")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdAccountingAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 2))
usdAccountingAgent.setRevisions(('2001-11-13 20:01', '2001-11-12 15:55',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdAccountingAgent.setRevisionsDescriptions(('Added support for selection policy name and type objects.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdAccountingAgent.setLastUpdated('200111132001Z')
if mibBuilder.loadTexts: usdAccountingAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdAccountingAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdAccountingAgent.setDescription('The agent capabilities definitions for the Accounting component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdAccountingAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAccountingAgentV1 = usdAccountingAgentV1.setProductRelease('Version 1 of the Accounting component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Accounting component was supported in\n        the Unisphere RX 2.0 thru 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAccountingAgentV1 = usdAccountingAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdAccountingAgentV1.setDescription('The MIBs supported by the SNMP agent for the Accounting application in the Unisphere Routing Switch. These capabilities became obsolete when the usdAcctngSelectionSubtreeType object was deprecated.')
usdAccountingAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAccountingAgentV2 = usdAccountingAgentV2.setProductRelease('Version 2 of the Accounting component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Accounting component wass supported in\n        the Unisphere RX 3.2 thru 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAccountingAgentV2 = usdAccountingAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdAccountingAgentV2.setDescription('The MIBs supported by the SNMP agent for the Accounting application in the Unisphere Routing Switch. These capabilities became obsolete when support was added to the Unisphere-Data-ACCOUNTING-MIB for selection policy name and type objects.')
usdAccountingAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 2, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAccountingAgentV3 = usdAccountingAgentV3.setProductRelease('Version 3 of the Accounting component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Accounting component is supported in\n        the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAccountingAgentV3 = usdAccountingAgentV3.setStatus('current')
if mibBuilder.loadTexts: usdAccountingAgentV3.setDescription('The MIBs supported by the SNMP agent for the Accounting application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-Accounting-CONF", usdAccountingAgentV2=usdAccountingAgentV2, usdAccountingAgentV1=usdAccountingAgentV1, usdAccountingAgent=usdAccountingAgent, PYSNMP_MODULE_ID=usdAccountingAgent, usdAccountingAgentV3=usdAccountingAgentV3)
