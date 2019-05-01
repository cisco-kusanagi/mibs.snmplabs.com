#
# PySNMP MIB module Juniper-Packet-Mirror-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Packet-Mirror-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Integer32, TimeTicks, iso, ModuleIdentity, NotificationType, Counter64, MibIdentifier, Bits, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "TimeTicks", "iso", "ModuleIdentity", "NotificationType", "Counter64", "MibIdentifier", "Bits", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniPacketMirrorAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 72))
juniPacketMirrorAgent.setRevisions(('2005-06-30 18:13',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniPacketMirrorAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: juniPacketMirrorAgent.setLastUpdated('200506301813Z')
if mibBuilder.loadTexts: juniPacketMirrorAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniPacketMirrorAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniPacketMirrorAgent.setDescription('The agent capabilities definitions for the Packet Mirror component of the SNMP agent in the Juniper E-series family of products.')
juniPacketMirrorAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 72, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPacketMirrorAgentV1 = juniPacketMirrorAgentV1.setProductRelease('Version 1 of the Packet Mirror component of the JUNOSe SNMP agent.\n        This version of the Packet Mirror component is supported in JUNOSe 6.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPacketMirrorAgentV1 = juniPacketMirrorAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniPacketMirrorAgentV1.setDescription('The MIB supported by the JUNOSe SNMP agent for the Packet Mirror application.')
mibBuilder.exportSymbols("Juniper-Packet-Mirror-CONF", juniPacketMirrorAgent=juniPacketMirrorAgent, PYSNMP_MODULE_ID=juniPacketMirrorAgent, juniPacketMirrorAgentV1=juniPacketMirrorAgentV1)
