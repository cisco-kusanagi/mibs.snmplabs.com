#
# PySNMP MIB module Unisphere-Data-SMDS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-SMDS-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, TimeTicks, Counter32, Counter64, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Bits, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "TimeTicks", "Counter32", "Counter64", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Bits", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdSmdsGroup2, usdSmdsGroup = mibBuilder.importSymbols("Unisphere-Data-SMDS-MIB", "usdSmdsGroup2", "usdSmdsGroup")
usdSmdsAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 46))
usdSmdsAgent.setRevisions(('2001-09-20 14:57', '2001-03-30 14:30',))
if mibBuilder.loadTexts: usdSmdsAgent.setLastUpdated('200109201457Z')
if mibBuilder.loadTexts: usdSmdsAgent.setOrganization('Unisphere Networks, Inc.')
usdSmdsAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 46, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSmdsAgentV1 = usdSmdsAgentV1.setProductRelease('Version 1 of the Switched Multimegabit Data Service (SMDS) management\n        component of the Unisphere Routing Switch SNMP agent.  This version of\n        the SMDS component was supported in the Unisphere RX 3.1 thru 3.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSmdsAgentV1 = usdSmdsAgentV1.setStatus('obsolete')
usdSmdsAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 46, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSmdsAgentV2 = usdSmdsAgentV2.setProductRelease('Version 2 of the Switched Multimegabit Data Service (SMDS) management\n        component of the Unisphere Routing Switch SNMP agent.  This version of\n        the SMDS component is supported in the Unisphere RX 4.0 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSmdsAgentV2 = usdSmdsAgentV2.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-SMDS-CONF", PYSNMP_MODULE_ID=usdSmdsAgent, usdSmdsAgentV2=usdSmdsAgentV2, usdSmdsAgentV1=usdSmdsAgentV1, usdSmdsAgent=usdSmdsAgent)
