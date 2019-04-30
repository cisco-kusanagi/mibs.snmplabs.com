#
# PySNMP MIB module Unisphere-Data-Accounting-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Accounting-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acctngSelectionType, acctngFileCollectFailedAttempts, acctngFileFormat, acctngFileMinAge, acctngBasicGroup = mibBuilder.importSymbols("ACCOUNTING-CONTROL-MIB", "acctngSelectionType", "acctngFileCollectFailedAttempts", "acctngFileFormat", "acctngFileMinAge", "acctngBasicGroup")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter32, iso, MibIdentifier, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, Unsigned32, NotificationType, Gauge32, IpAddress, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "Unsigned32", "NotificationType", "Gauge32", "IpAddress", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usdAcctngBasicGroup, usdAcctngBasicGroup3, usdAcctngBasicGroup2 = mibBuilder.importSymbols("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngBasicGroup", "usdAcctngBasicGroup3", "usdAcctngBasicGroup2")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdAccountingAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 2))
usdAccountingAgent.setRevisions(('2001-11-13 20:01', '2001-11-12 15:55',))
if mibBuilder.loadTexts: usdAccountingAgent.setLastUpdated('200111132001Z')
if mibBuilder.loadTexts: usdAccountingAgent.setOrganization('Unisphere Networks, Inc.')
usdAccountingAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAccountingAgentV1 = usdAccountingAgentV1.setProductRelease('Version 1 of the Accounting component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Accounting component was supported in\n        the Unisphere RX 2.0 thru 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAccountingAgentV1 = usdAccountingAgentV1.setStatus('obsolete')
usdAccountingAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAccountingAgentV2 = usdAccountingAgentV2.setProductRelease('Version 2 of the Accounting component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Accounting component wass supported in\n        the Unisphere RX 3.2 thru 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAccountingAgentV2 = usdAccountingAgentV2.setStatus('obsolete')
usdAccountingAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 2, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAccountingAgentV3 = usdAccountingAgentV3.setProductRelease('Version 3 of the Accounting component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Accounting component is supported in\n        the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAccountingAgentV3 = usdAccountingAgentV3.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-Accounting-CONF", usdAccountingAgentV2=usdAccountingAgentV2, usdAccountingAgentV3=usdAccountingAgentV3, PYSNMP_MODULE_ID=usdAccountingAgent, usdAccountingAgentV1=usdAccountingAgentV1, usdAccountingAgent=usdAccountingAgent)
