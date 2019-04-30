#
# PySNMP MIB module Juniper-PIM-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-PIM-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
ObjectIdentity, ModuleIdentity, Counter64, Unsigned32, MibIdentifier, iso, Counter32, NotificationType, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "Counter64", "Unsigned32", "MibIdentifier", "iso", "Counter32", "NotificationType", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniPimAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 29))
juniPimAgent.setRevisions(('2002-09-06 16:54', '2001-11-15 22:38',))
if mibBuilder.loadTexts: juniPimAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniPimAgent.setOrganization('Juniper Networks, Inc.')
juniPimAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 29, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPimAgentV1 = juniPimAgentV1.setProductRelease('Version 1 of the PIM component of the JUNOSe SNMP agent.  This version\n        of the PIM component is supported in JUNOSe 3.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPimAgentV1 = juniPimAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-PIM-CONF", PYSNMP_MODULE_ID=juniPimAgent, juniPimAgentV1=juniPimAgentV1, juniPimAgent=juniPimAgent)
