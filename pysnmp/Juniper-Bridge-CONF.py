#
# PySNMP MIB module Juniper-Bridge-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Bridge-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, ModuleIdentity, IpAddress, Gauge32, Unsigned32, NotificationType, TimeTicks, Bits, MibIdentifier, Counter64, Integer32, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Gauge32", "Unsigned32", "NotificationType", "TimeTicks", "Bits", "MibIdentifier", "Counter64", "Integer32", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniBridgeAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 60))
juniBridgeAgent.setRevisions(('2003-09-30 13:03', '2002-10-02 15:29',))
if mibBuilder.loadTexts: juniBridgeAgent.setLastUpdated('200309301303Z')
if mibBuilder.loadTexts: juniBridgeAgent.setOrganization('Juniper Networks, Inc.')
juniBridgeAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 60, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgeAgentV1 = juniBridgeAgentV1.setProductRelease('Version 1 of the Bridge component of the JUNOSe SNMP agent.  This\n        version of the Bridge component is supported in the Juniper JUNOSe 5.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgeAgentV1 = juniBridgeAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-Bridge-CONF", juniBridgeAgentV1=juniBridgeAgentV1, PYSNMP_MODULE_ID=juniBridgeAgent, juniBridgeAgent=juniBridgeAgent)
