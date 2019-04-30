#
# PySNMP MIB module Unisphere-Data-CBF-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-CBF-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
IpAddress, ObjectIdentity, Counter64, NotificationType, TimeTicks, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, MibIdentifier, Counter32, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "Counter64", "NotificationType", "TimeTicks", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Counter32", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdCbfGroup, = mibBuilder.importSymbols("Unisphere-Data-CBF-MIB", "usdCbfGroup")
usdCbfAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 48))
usdCbfAgent.setRevisions(('2001-03-29 20:23',))
if mibBuilder.loadTexts: usdCbfAgent.setLastUpdated('200103292023Z')
if mibBuilder.loadTexts: usdCbfAgent.setOrganization('Unisphere Networks, Inc.')
usdCbfAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 48, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCbfAgentV1 = usdCbfAgentV1.setProductRelease('Version 1 of the Connection-Based Forwarding (CBF) component of the\n        Unisphere Routing Switch SNMP agent.  This version of the CBF component\n        is supported in the Unisphere RX 3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCbfAgentV1 = usdCbfAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-CBF-CONF", usdCbfAgent=usdCbfAgent, usdCbfAgentV1=usdCbfAgentV1, PYSNMP_MODULE_ID=usdCbfAgent)
