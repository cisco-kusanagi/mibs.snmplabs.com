#
# PySNMP MIB module Juniper-Local-Address-Server-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Local-Address-Server-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Integer32, ModuleIdentity, TimeTicks, iso, Gauge32, ObjectIdentity, Unsigned32, IpAddress, Counter64, Counter32, NotificationType, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "TimeTicks", "iso", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter64", "Counter32", "NotificationType", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniLocalAddressServerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25))
juniLocalAddressServerAgent.setRevisions(('2005-02-11 21:35', '2003-11-04 18:30', '2002-09-06 16:54', '2002-05-06 19:20', '2001-05-02 13:22',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniLocalAddressServerAgent.setRevisionsDescriptions(('Added support for rsAddressSharedPoolTable, update agent to version 6.', 'Juniper-ADDRESS-POOL-MIB: Added support for address pool aliases.', 'Juniper-ADDRESS-POOL-MIB: Replaced Unisphere names with Juniper names.', 'Juniper-ADDRESS-POOL-MIB: Added support for address pools with multiple address ranges.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniLocalAddressServerAgent.setLastUpdated('200502112135Z')
if mibBuilder.loadTexts: juniLocalAddressServerAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniLocalAddressServerAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniLocalAddressServerAgent.setDescription('The agent capabilities definitions for the Local Address Server component of the SNMP agent in the Juniper E-series family of products.')
juniLocalAddressServerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV1 = juniLocalAddressServerAgentV1.setProductRelease('Version 1 of the Local Address Server component of the JUNOSe SNMP\n        agent.  This version of the Local Address Server component was supported\n        in JUNOSe 1.3 thru 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV1 = juniLocalAddressServerAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniLocalAddressServerAgentV1.setDescription('The MIB supported by the SNMP agent for the Local Address Server application in JUNOSe. These capabilities became obsolete when pool exhaustion variables and notifications were added.')
juniLocalAddressServerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV2 = juniLocalAddressServerAgentV2.setProductRelease('Version 2 of the Local Address Server component of the JUNOSe SNMP\n        agent.  This version of the Local Address Server component was supported\n        in JUNOSe 3.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV2 = juniLocalAddressServerAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniLocalAddressServerAgentV2.setDescription('The MIB supported by the SNMP agent for the Local Address Server application in JUNOSe. These capabilities became obsolete when support was added for address pools with multiple address ranges.')
juniLocalAddressServerAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV3 = juniLocalAddressServerAgentV3.setProductRelease('Version 3 of the Local Address Server component of the JUNOSe SNMP\n        agent.  This version of the Local Address Server component was supported\n        in JUNOSe 3.3 thru 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV3 = juniLocalAddressServerAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniLocalAddressServerAgentV3.setDescription('The MIB supported by the SNMP agent for the Local Address Server application in JUNOSe. These capabilities became obsolete when support was added for address pool aliases.')
juniLocalAddressServerAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV4 = juniLocalAddressServerAgentV4.setProductRelease('Version 4 of the Local Address Server component of the JUNOSe SNMP\n        agent.  This version of the Local Address Server component is supported\n        in JUNOSe 5.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV4 = juniLocalAddressServerAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniLocalAddressServerAgentV4.setDescription('The MIB supported by the SNMP agent for the Local Address Server application in JUNOSe. These capabilities became obsolete when support was added for next PoolProfile index.')
juniLocalAddressServerAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV5 = juniLocalAddressServerAgentV5.setProductRelease('Version 5 of the Local Address Server component of the JUNOSe SNMP\n        agent.  This version of the Local Address Server component is supported\n        in JUNOSe 6.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV5 = juniLocalAddressServerAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniLocalAddressServerAgentV5.setDescription('The MIB supported by the SNMP agent for the Local Address Server application in JUNOSe.')
juniLocalAddressServerAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV6 = juniLocalAddressServerAgentV6.setProductRelease('Version 6 of the Local Address Server component of the JUNOSe SNMP\n        agent.  This version of the Local Address Server component is supported\n        in JUNOSe 7.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLocalAddressServerAgentV6 = juniLocalAddressServerAgentV6.setStatus('current')
if mibBuilder.loadTexts: juniLocalAddressServerAgentV6.setDescription('The MIB supported by the SNMP agent for the Local Address Server application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Local-Address-Server-CONF", juniLocalAddressServerAgentV5=juniLocalAddressServerAgentV5, juniLocalAddressServerAgent=juniLocalAddressServerAgent, juniLocalAddressServerAgentV6=juniLocalAddressServerAgentV6, juniLocalAddressServerAgentV1=juniLocalAddressServerAgentV1, juniLocalAddressServerAgentV3=juniLocalAddressServerAgentV3, PYSNMP_MODULE_ID=juniLocalAddressServerAgent, juniLocalAddressServerAgentV2=juniLocalAddressServerAgentV2, juniLocalAddressServerAgentV4=juniLocalAddressServerAgentV4)
