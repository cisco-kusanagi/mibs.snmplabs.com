#
# PySNMP MIB module Juniper-Packet-Mirror-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Packet-Mirror-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Bits, ObjectIdentity, MibIdentifier, IpAddress, Counter64, iso, Gauge32, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter64", "iso", "Gauge32", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "Counter32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniPacketMirrorAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 72))
juniPacketMirrorAgent.setRevisions(('2005-06-30 18:13',))
if mibBuilder.loadTexts: juniPacketMirrorAgent.setLastUpdated('200506301813Z')
if mibBuilder.loadTexts: juniPacketMirrorAgent.setOrganization('Juniper Networks, Inc.')
juniPacketMirrorAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 72, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPacketMirrorAgentV1 = juniPacketMirrorAgentV1.setProductRelease('Version 1 of the Packet Mirror component of the JUNOSe SNMP agent.\n        This version of the Packet Mirror component is supported in JUNOSe 6.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPacketMirrorAgentV1 = juniPacketMirrorAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-Packet-Mirror-CONF", PYSNMP_MODULE_ID=juniPacketMirrorAgent, juniPacketMirrorAgentV1=juniPacketMirrorAgentV1, juniPacketMirrorAgent=juniPacketMirrorAgent)
