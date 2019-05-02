#
# PySNMP MIB module Juniper-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Profile-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
juniProfileAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniProfileAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Integer32, ObjectIdentity, iso, MibIdentifier, IpAddress, NotificationType, Gauge32, Counter64, Unsigned32, Counter32, ModuleIdentity, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "iso", "MibIdentifier", "IpAddress", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "Counter32", "ModuleIdentity", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniProfileManagerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1))
juniProfileManagerAgent.setRevisions(('2002-12-17 20:00', '2002-09-06 16:54', '2001-03-29 18:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniProfileManagerAgent.setRevisionsDescriptions(('Added juniProfAssignIfRangeTable and juniProfToIfRangeMapTable to extend profile assignment to interface/encapsulation/range 3-tuples.', 'Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniProfileManagerAgent.setLastUpdated('200212172000Z')
if mibBuilder.loadTexts: juniProfileManagerAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniProfileManagerAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniProfileManagerAgent.setDescription('The agent capabilities definitions for the Profile Manager component of the SNMP agent in the Juniper E-series family of products.')
juniProfileManagerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniProfileManagerAgentV1 = juniProfileManagerAgentV1.setProductRelease('Version 1 of the Profile Manager component of the JUNOSe SNMP agent.\n        This version of the Profile Manager component was supported in JUNOSe\n        1.1 thru 1.3 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniProfileManagerAgentV1 = juniProfileManagerAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniProfileManagerAgentV1.setDescription('The MIBs supported by the SNMP agent for the Profile Manager application in JUNOSe. These capabilities became obsolete when support was added for assignment of profiles to interface/ encapsulation pairs.')
juniProfileManagerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniProfileManagerAgentV2 = juniProfileManagerAgentV2.setProductRelease('Version 2 of the Profile Manager component of the JUNOSe SNMP agent.\n        This version of the Profile Manager component was supported in JUNOSe\n        2.0 thru 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniProfileManagerAgentV2 = juniProfileManagerAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniProfileManagerAgentV2.setDescription('The MIB supported by the SNMP agent for the Profile Manager application in JUNOSe. These capabilities became obsolete when support was added for assignment of profiles to interface/encapsulation/range 3-tuples.')
juniProfileManagerAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniProfileManagerAgentV3 = juniProfileManagerAgentV3.setProductRelease('Version 3 of the Profile Manager component of the JUNOSe SNMP agent.\n        This version of the Profile Manager component is supported in JUNOSe 5.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniProfileManagerAgentV3 = juniProfileManagerAgentV3.setStatus('current')
if mibBuilder.loadTexts: juniProfileManagerAgentV3.setDescription('The MIB supported by the SNMP agent for the Profile Manager application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Profile-CONF", juniProfileManagerAgentV2=juniProfileManagerAgentV2, juniProfileManagerAgentV1=juniProfileManagerAgentV1, juniProfileManagerAgentV3=juniProfileManagerAgentV3, juniProfileManagerAgent=juniProfileManagerAgent, PYSNMP_MODULE_ID=juniProfileManagerAgent)
