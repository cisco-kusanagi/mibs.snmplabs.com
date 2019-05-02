#
# PySNMP MIB module Juniper-SSC-Client-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-SSC-Client-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:04:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Bits, Integer32, Counter32, NotificationType, IpAddress, Counter64, Unsigned32, iso, ModuleIdentity, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Counter32", "NotificationType", "IpAddress", "Counter64", "Unsigned32", "iso", "ModuleIdentity", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniSscClientAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41))
juniSscClientAgent.setRevisions(('2003-11-18 21:11', '2002-09-06 16:54', '2001-09-19 20:29', '2001-03-30 15:18',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniSscClientAgent.setRevisionsDescriptions(('Obsoleted token and added discover scalar statistics.', 'Replaced Unisphere names with Juniper names.', 'Add version number object.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniSscClientAgent.setLastUpdated('200311182111Z')
if mibBuilder.loadTexts: juniSscClientAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniSscClientAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniSscClientAgent.setDescription('The agent capabilities definitions for the Service Selection Center (SSC) Client component of the SNMP agent in the Juniper E-series family of products.')
juniSscClientAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSscClientAgentV1 = juniSscClientAgentV1.setProductRelease('Version 1 of the SSC Client component of the JUNOSe SNMP agent.  This\n        version of the SSC Client component was supported in JUNOSe 2.0 thru 3.0\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSscClientAgentV1 = juniSscClientAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniSscClientAgentV1.setDescription('The MIB supported by the SNMP agent for the SSC Client application in JUNOSe. These capabilities became obsolete when DHCP-LS, Web and SSC support objects were added to the MIB.')
juniSscClientAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSscClientAgentV2 = juniSscClientAgentV2.setProductRelease('Version 2 of the SSC Client component of the JUNOSe SNMP agent.  This\n        version of the SSC Client component was supported in JUNOSe 3.1 and\n        subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSscClientAgentV2 = juniSscClientAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniSscClientAgentV2.setDescription('The MIB supported by the SNMP agent for the SSC Client application in JUNOSe. These capabilities became obsolete when the version number object was added to the MIB.')
juniSscClientAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSscClientAgentV3 = juniSscClientAgentV3.setProductRelease('Version 3 of the SSC Client component of the JUNOSe SNMP agent.  This\n        version of the SSC Client component was supported in JUNOSe 4.0 through\n        5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSscClientAgentV3 = juniSscClientAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniSscClientAgentV3.setDescription('The MIB supported by the SNMP agent for the SSC Client application in JUNOSe. These capabilities became obsolete when token scalar statistics were obsoleted and discover scalar statistics were added.')
juniSscClientAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSscClientAgentV4 = juniSscClientAgentV4.setProductRelease('Version 4 of the SSC Client component of the JUNOSe SNMP agent.  This\n        version of the SSC Client component is supported in JUNOSe 5.3 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSscClientAgentV4 = juniSscClientAgentV4.setStatus('current')
if mibBuilder.loadTexts: juniSscClientAgentV4.setDescription('The MIB supported by the SNMP agent for the SSC Client application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-SSC-Client-CONF", juniSscClientAgentV1=juniSscClientAgentV1, juniSscClientAgentV2=juniSscClientAgentV2, juniSscClientAgentV4=juniSscClientAgentV4, PYSNMP_MODULE_ID=juniSscClientAgent, juniSscClientAgent=juniSscClientAgent, juniSscClientAgentV3=juniSscClientAgentV3)
