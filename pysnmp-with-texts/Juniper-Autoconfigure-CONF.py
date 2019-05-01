#
# PySNMP MIB module Juniper-Autoconfigure-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Autoconfigure-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:01:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Counter64, MibIdentifier, iso, ModuleIdentity, Counter32, ObjectIdentity, Bits, IpAddress, NotificationType, TimeTicks, Unsigned32, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "iso", "ModuleIdentity", "Counter32", "ObjectIdentity", "Bits", "IpAddress", "NotificationType", "TimeTicks", "Unsigned32", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniAutoConfAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 44))
juniAutoConfAgent.setRevisions(('2004-07-26 19:54', '2002-09-06 16:54', '2001-03-27 20:08',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniAutoConfAgent.setRevisionsDescriptions(('Added Encapsulation Type Lockout objects.', 'Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniAutoConfAgent.setLastUpdated('200407261954Z')
if mibBuilder.loadTexts: juniAutoConfAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniAutoConfAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniAutoConfAgent.setDescription('The agent capabilities definitions for the Auto-Configuration component of the SNMP agent in the Juniper E-series family of products.')
juniAutoConfAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 44, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfAgentV1 = juniAutoConfAgentV1.setProductRelease('Version 1 of the Auto-Configuration component of the JUNOSe SNMP agent.\n        This version of the Auto-Configuration component is supported in JUNOSe\n        3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfAgentV1 = juniAutoConfAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniAutoConfAgentV1.setDescription('Obsoleted MIB supported by the SNMP agent for auto-configuration capabilities in JUNOSe. This group became obsolete when encapsulation type lockout support was added.')
juniAutoConfAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 44, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfAgentV2 = juniAutoConfAgentV2.setProductRelease('Version 2 of the Auto-Configuration component of the JUNOSe SNMP agent.\n        This version of the Auto-Configuration component is supported in JUNOSe\n        7.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfAgentV2 = juniAutoConfAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniAutoConfAgentV2.setDescription('The MIB supported by the SNMP agent for auto-configuration capabilities in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Autoconfigure-CONF", juniAutoConfAgent=juniAutoConfAgent, juniAutoConfAgentV1=juniAutoConfAgentV1, PYSNMP_MODULE_ID=juniAutoConfAgent, juniAutoConfAgentV2=juniAutoConfAgentV2)
