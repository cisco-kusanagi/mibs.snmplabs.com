#
# PySNMP MIB module Juniper-Frame-Relay-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Frame-Relay-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, TimeTicks, Unsigned32, Bits, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, ObjectIdentity, Gauge32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "TimeTicks", "Unsigned32", "Bits", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "ObjectIdentity", "Gauge32", "iso", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniFrameRelayAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 17))
juniFrameRelayAgent.setRevisions(('2002-09-27 15:58', '2001-04-18 19:26',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniFrameRelayAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names. Added multi-link frame relay support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniFrameRelayAgent.setLastUpdated('200209271558Z')
if mibBuilder.loadTexts: juniFrameRelayAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniFrameRelayAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniFrameRelayAgent.setDescription('The agent capabilities definitions for the Frame Relay component of the SNMP agent in the Juniper E-series family of products.')
juniFrameRelayAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 17, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFrameRelayAgentV1 = juniFrameRelayAgentV1.setProductRelease('Version 1 of the Frame Relay component of the JUNOSe SNMP agent.  This\n        version of the Frame Relay component was supported in JUNOSe 1.0 thru\n        4.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFrameRelayAgentV1 = juniFrameRelayAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniFrameRelayAgentV1.setDescription('The MIBs supported by the SNMP agent for the Frame Relay application in JUNOSe. These capabilities became obsolete when multi-link frame relay support was added.')
juniFrameRelayAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 17, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFrameRelayAgentV2 = juniFrameRelayAgentV2.setProductRelease('Version 2 of the Frame Relay component of the JUNOSe SNMP agent.  This\n        version of the Frame Relay component is supported in JUNOSe 5.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFrameRelayAgentV2 = juniFrameRelayAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniFrameRelayAgentV2.setDescription('The MIBs supported by the SNMP agent for the Frame Relay application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Frame-Relay-CONF", juniFrameRelayAgentV2=juniFrameRelayAgentV2, PYSNMP_MODULE_ID=juniFrameRelayAgent, juniFrameRelayAgentV1=juniFrameRelayAgentV1, juniFrameRelayAgent=juniFrameRelayAgent)
