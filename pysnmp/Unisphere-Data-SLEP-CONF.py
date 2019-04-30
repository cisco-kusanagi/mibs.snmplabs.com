#
# PySNMP MIB module Unisphere-Data-SLEP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-SLEP-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
iso, Integer32, ModuleIdentity, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, Counter64, Unsigned32, Bits, MibIdentifier, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "ModuleIdentity", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "Counter64", "Unsigned32", "Bits", "MibIdentifier", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdSlepGroup, = mibBuilder.importSymbols("Unisphere-Data-SLEP-MIB", "usdSlepGroup")
usdSlepAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 38))
usdSlepAgent.setRevisions(('2001-03-30 14:15',))
if mibBuilder.loadTexts: usdSlepAgent.setLastUpdated('200103301415Z')
if mibBuilder.loadTexts: usdSlepAgent.setOrganization('Unisphere Networks, Inc.')
usdSlepAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 38, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSlepAgentV1 = usdSlepAgentV1.setProductRelease('Version 1 of the SLEP component of the Unisphere Routing Switch SNMP\n        agent.  This version of the SLEP component is supported in the Unisphere\n        RX 1.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSlepAgentV1 = usdSlepAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-SLEP-CONF", PYSNMP_MODULE_ID=usdSlepAgent, usdSlepAgentV1=usdSlepAgentV1, usdSlepAgent=usdSlepAgent)
