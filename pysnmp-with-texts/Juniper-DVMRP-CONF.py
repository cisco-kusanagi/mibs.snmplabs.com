#
# PySNMP MIB module Juniper-DVMRP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DVMRP-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Unsigned32, Integer32, IpAddress, iso, Counter64, ObjectIdentity, Counter32, Bits, Gauge32, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Unsigned32", "Integer32", "IpAddress", "iso", "Counter64", "ObjectIdentity", "Counter32", "Bits", "Gauge32", "NotificationType", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniDvmrpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 12))
juniDvmrpAgent.setRevisions(('2003-01-16 21:01', '2001-11-30 20:24',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniDvmrpAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names. Added support for unicast routing and the interface announce list name.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniDvmrpAgent.setLastUpdated('200301162101Z')
if mibBuilder.loadTexts: juniDvmrpAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniDvmrpAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniDvmrpAgent.setDescription('The agent capabilities definitions for the DVMRP component of the SNMP agent in the Juniper E-series family of products.')
juniDvmrpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 12, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDvmrpAgentV1 = juniDvmrpAgentV1.setProductRelease('Version 1 of the DVMRP component of the JUNOSe SNMP agent.  This\n        version of the DVMRP component was supported in JUNOSe 3.0 thru 4.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDvmrpAgentV1 = juniDvmrpAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniDvmrpAgentV1.setDescription('The MIBs supported by the SNMP agent for the DVMRP application in JUNOSe. These capabilities became obsolete when new objects were added to the Juniper-DVMRP-MIB.')
juniDvmrpAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 12, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDvmrpAgentV2 = juniDvmrpAgentV2.setProductRelease('Version 2 of the DVMRP component of the JUNOSe SNMP agent.  This\n        version of the DVMRP component is supported in JUNOSe 5.0 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDvmrpAgentV2 = juniDvmrpAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniDvmrpAgentV2.setDescription('The MIBs supported by the SNMP agent for the DVMRP application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-DVMRP-CONF", juniDvmrpAgentV1=juniDvmrpAgentV1, juniDvmrpAgentV2=juniDvmrpAgentV2, juniDvmrpAgent=juniDvmrpAgent, PYSNMP_MODULE_ID=juniDvmrpAgent)
