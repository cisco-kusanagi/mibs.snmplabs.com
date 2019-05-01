#
# PySNMP MIB module Juniper-SLEP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-SLEP-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:04:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, NotificationType, iso, MibIdentifier, Gauge32, Unsigned32, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "NotificationType", "iso", "MibIdentifier", "Gauge32", "Unsigned32", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniSlepAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 38))
juniSlepAgent.setRevisions(('2003-09-10 21:27', '2002-12-23 20:40', '2001-03-30 14:15',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniSlepAgent.setRevisionsDescriptions(('Added version 2 capabilities.', 'Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniSlepAgent.setLastUpdated('200309102127Z')
if mibBuilder.loadTexts: juniSlepAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniSlepAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniSlepAgent.setDescription('The agent capabilities definitions for the Serial Line Encapsulation Protocol (SLEP) component of the SNMP agent in the Juniper E-series family of products.')
juniSlepAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 38, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSlepAgentV1 = juniSlepAgentV1.setProductRelease('Version 1 of the SLEP component of the JUNOSe SNMP agent.  This version\n        of the SLEP component was supported in JUNOSe 1.3 thru 3.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSlepAgentV1 = juniSlepAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniSlepAgentV1.setDescription('The MIB supported by the SNMP agent for the SLEP application in JUNOSe. These capabilities became obsolete when down-when-looped control support was added.')
juniSlepAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 38, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSlepAgentV2 = juniSlepAgentV2.setProductRelease('Version 2 of the SLEP component of the JUNOSe SNMP agent.  This version\n        of the SLEP component is supported in JUNOSe 3.1 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSlepAgentV2 = juniSlepAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniSlepAgentV2.setDescription('The MIB supported by the SNMP agent for the SLEP application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-SLEP-CONF", juniSlepAgent=juniSlepAgent, juniSlepAgentV2=juniSlepAgentV2, PYSNMP_MODULE_ID=juniSlepAgent, juniSlepAgentV1=juniSlepAgentV1)
