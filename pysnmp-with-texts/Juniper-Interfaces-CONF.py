#
# PySNMP MIB module Juniper-Interfaces-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Interfaces-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Unsigned32, ModuleIdentity, Gauge32, IpAddress, ObjectIdentity, TimeTicks, NotificationType, MibIdentifier, Bits, Integer32, Counter32, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Gauge32", "IpAddress", "ObjectIdentity", "TimeTicks", "NotificationType", "MibIdentifier", "Bits", "Integer32", "Counter32", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniInterfacesAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 20))
juniInterfacesAgent.setRevisions(('2004-02-04 21:38', '2003-07-16 21:38', '2002-12-16 14:43', '2001-04-27 14:24',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniInterfacesAgent.setRevisionsDescriptions(('Added mib table rsIfCountTable to count systemwide interfaces by if type.', 'IF-INVERTED-STACK-MIB: Added support for RFC 2864, the Inverted Stack Table.', 'Juniper-UNI-IF-MIB: Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniInterfacesAgent.setLastUpdated('200307162138Z')
if mibBuilder.loadTexts: juniInterfacesAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniInterfacesAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniInterfacesAgent.setDescription('The agent capabilities definitions for the Interfaces component of the SNMP agent in the Juniper E-series family of products.')
juniInterfacesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 20, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniInterfacesAgentV1 = juniInterfacesAgentV1.setProductRelease('Version 1 of the Interfaces component of the JUNOSe SNMP agent.  This\n        version of the Interfaces component was supported in JUNOSe 1.0 thru 5.0\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniInterfacesAgentV1 = juniInterfacesAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniInterfacesAgentV1.setDescription('The MIBs supported by the SNMP agent for the Interfaces application in JUNOSe. These capabilities became obsolete when support was added for the IF-INVERTED-STACK-MIB.')
juniInterfacesAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 20, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniInterfacesAgentV2 = juniInterfacesAgentV2.setProductRelease('Version 2 of the Interfaces component of the JUNOSe SNMP agent.  This\n        version of the Interfaces component is supported in JUNOSe 1.0 and\n        subsequent 2.0, 3.x, 4.x and 5.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniInterfacesAgentV2 = juniInterfacesAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniInterfacesAgentV2.setDescription('The MIBs supported by the SNMP agent for the Interfaces application in JUNOSe. These capabilities became obsolete when support was added for the ifCountTable.')
juniInterfacesAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 20, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniInterfacesAgentV3 = juniInterfacesAgentV3.setProductRelease('Version 3 of the Interfaces component of the JUNOSe SNMP agent.  This\n        version of the Interfaces component is supported in JUNOSe 1.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniInterfacesAgentV3 = juniInterfacesAgentV3.setStatus('current')
if mibBuilder.loadTexts: juniInterfacesAgentV3.setDescription('The MIBs supported by the SNMP agent for the Interfaces application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Interfaces-CONF", juniInterfacesAgent=juniInterfacesAgent, juniInterfacesAgentV1=juniInterfacesAgentV1, juniInterfacesAgentV2=juniInterfacesAgentV2, juniInterfacesAgentV3=juniInterfacesAgentV3, PYSNMP_MODULE_ID=juniInterfacesAgent)
