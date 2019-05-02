#
# PySNMP MIB module Juniper-Ethernet-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Ethernet-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Integer32, IpAddress, Bits, Unsigned32, iso, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ObjectIdentity, Counter64, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "Bits", "Unsigned32", "iso", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "ModuleIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniEthernetAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14))
juniEthernetAgent.setRevisions(('2003-09-29 16:18', '2002-10-01 22:10', '2002-10-01 18:02', '2002-04-05 20:33', '2001-10-25 21:36',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniEthernetAgent.setRevisionsDescriptions(('Juniper-ETHERNET-MIB: Added Ethernet interface statistics support.', 'Juniper-ETHERNET-MIB: Replaced Unisphere names with Juniper names.', 'Juniper-ETHERNET-MIB: Added MAU type and length support.', 'Juniper-ETHERNET-MIB: Added VLAN stack support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniEthernetAgent.setLastUpdated('200309291618Z')
if mibBuilder.loadTexts: juniEthernetAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniEthernetAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniEthernetAgent.setDescription('The agent capabilities definitions for the Ethernet component of the SNMP agent in the Juniper E-series family of products.')
juniEthernetAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV1 = juniEthernetAgentV1.setProductRelease('Version 1 of the Ethernet component of the JUNOSe SNMP agent.  This\n        version of the Ethernet component was supported in JUNOSe 2.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV1 = juniEthernetAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniEthernetAgentV1.setDescription('The MIBs supported by the SNMP agent for the Ethernet application in JUNOSe. These capabilities became obsolete when VLAN support was add.')
juniEthernetAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV2 = juniEthernetAgentV2.setProductRelease('Version 2 of the Ethernet component of the JUNOSe SNMP agent.  This\n        version of the Ethernet component was supported in JUNOSe 3.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV2 = juniEthernetAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniEthernetAgentV2.setDescription('The MIBs supported by the SNMP agent for the Ethernet application in JUNOSe. These capabilities became obsolete when VLAN stack support was added.')
juniEthernetAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV3 = juniEthernetAgentV3.setProductRelease('Version 3 of the Ethernet component of the JUNOSe SNMP agent.  This\n        version of the Ethernet component was supported in JUNOSe 4.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV3 = juniEthernetAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniEthernetAgentV3.setDescription('The MIBs supported by the SNMP agent for the Ethernet application in JUNOSe. These capabilities became obsolete when VLAN stack support was added.')
juniEthernetAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV4 = juniEthernetAgentV4.setProductRelease('Version 4 of the Ethernet component of the JUNOSe SNMP agent.  This\n        version of the Ethernet component was supported in JUNOSe 4.1 through\n        5.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV4 = juniEthernetAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniEthernetAgentV4.setDescription('The MIBs supported by the SNMP agent for the Ethernet application in JUNOSe. These capabilities became obsolete when Ethernet interface statistics support was added.')
juniEthernetAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV5 = juniEthernetAgentV5.setProductRelease('Version 5 of the Ethernet component of the JUNOSe SNMP agent.  This\n        version of the Ethernet component is supported in JUNOSe 5.2 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetAgentV5 = juniEthernetAgentV5.setStatus('current')
if mibBuilder.loadTexts: juniEthernetAgentV5.setDescription('The MIBs supported by the SNMP agent for the Ethernet application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Ethernet-CONF", juniEthernetAgentV3=juniEthernetAgentV3, juniEthernetAgentV2=juniEthernetAgentV2, juniEthernetAgentV4=juniEthernetAgentV4, PYSNMP_MODULE_ID=juniEthernetAgent, juniEthernetAgentV5=juniEthernetAgentV5, juniEthernetAgent=juniEthernetAgent, juniEthernetAgentV1=juniEthernetAgentV1)
