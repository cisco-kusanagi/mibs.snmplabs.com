#
# PySNMP MIB module Unisphere-Data-Autoconfigure-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Autoconfigure-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Gauge32, Integer32, Counter32, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Unsigned32, MibIdentifier, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Gauge32", "Integer32", "Counter32", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usdAutoConfGroup, = mibBuilder.importSymbols("Unisphere-Data-AUTOCONFIGURE-MIB", "usdAutoConfGroup")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdAutoConfAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 44))
usdAutoConfAgent.setRevisions(('2001-03-27 20:08',))
if mibBuilder.loadTexts: usdAutoConfAgent.setLastUpdated('200103272008Z')
if mibBuilder.loadTexts: usdAutoConfAgent.setOrganization('Unisphere Networks, Inc.')
usdAutoConfAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 44, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAutoConfAgentV1 = usdAutoConfAgentV1.setProductRelease('Version 1 of the Auto-Configuration component of the Unisphere Routing\n        Switch SNMP agent.  This version of the Auto-Configuration component is\n        supported in the Unisphere RX 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAutoConfAgentV1 = usdAutoConfAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-Autoconfigure-CONF", usdAutoConfAgentV1=usdAutoConfAgentV1, usdAutoConfAgent=usdAutoConfAgent, PYSNMP_MODULE_ID=usdAutoConfAgent)
