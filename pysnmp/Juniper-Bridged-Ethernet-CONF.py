#
# PySNMP MIB module Juniper-Bridged-Ethernet-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Bridged-Ethernet-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Integer32, Unsigned32, TimeTicks, iso, Bits, NotificationType, IpAddress, MibIdentifier, Gauge32, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "TimeTicks", "iso", "Bits", "NotificationType", "IpAddress", "MibIdentifier", "Gauge32", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniBridgedEthernetAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 5))
juniBridgedEthernetAgent.setRevisions(('2002-09-06 16:54', '2001-03-30 16:45',))
if mibBuilder.loadTexts: juniBridgedEthernetAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniBridgedEthernetAgent.setOrganization('Juniper Networks, Inc.')
juniBridgedEthernetAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgedEthernetAgentV1 = juniBridgedEthernetAgentV1.setProductRelease('Version 1 of the Bridged Ethernet component of the JUNOSe SNMP agent.\n        This version of the Bridged Ethernet component is supported in JUNOSe\n        2.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgedEthernetAgentV1 = juniBridgedEthernetAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-Bridged-Ethernet-CONF", PYSNMP_MODULE_ID=juniBridgedEthernetAgent, juniBridgedEthernetAgent=juniBridgedEthernetAgent, juniBridgedEthernetAgentV1=juniBridgedEthernetAgentV1)
