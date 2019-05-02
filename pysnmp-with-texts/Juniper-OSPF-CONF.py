#
# PySNMP MIB module Juniper-OSPF-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-OSPF-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
MibIdentifier, Integer32, ModuleIdentity, iso, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, Counter32, NotificationType, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "ModuleIdentity", "iso", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "Counter32", "NotificationType", "Counter64", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniOspfAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 28))
juniOspfAgent.setRevisions(('2002-09-06 16:54', '2001-12-06 15:12', '2001-03-29 13:34',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniOspfAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'New objects were added to the Juniper-OSPF-MIB juniOspfBasicGroup2.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniOspfAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniOspfAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniOspfAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniOspfAgent.setDescription('The agent capabilities definitions for the Open Shortest Path First (OSPF) routing protocol component of the SNMP agent in the Juniper E-series family of products.')
juniOspfAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 28, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniOspfAgentV1 = juniOspfAgentV1.setProductRelease('Version 1 of the OSPF component of the JUNOSe SNMP agent.  This version\n        of the OSPF component was supported in JUNOSe 2.x and 3.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniOspfAgentV1 = juniOspfAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniOspfAgentV1.setDescription('The MIBs supported by the SNMP agent for the OSPF application in JUNOSe. These capabilities became obsolete when new objects were added to the juniOspfBasicGroup.')
juniOspfAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 28, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniOspfAgentV2 = juniOspfAgentV2.setProductRelease('Version 2 of the OSPF component of the JUNOSe SNMP agent.  This version\n        of the OSPF component is supported in JUNOSe 4.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniOspfAgentV2 = juniOspfAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniOspfAgentV2.setDescription('The MIBs supported by the SNMP agent for the OSPF application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-OSPF-CONF", juniOspfAgentV1=juniOspfAgentV1, PYSNMP_MODULE_ID=juniOspfAgent, juniOspfAgentV2=juniOspfAgentV2, juniOspfAgent=juniOspfAgent)
