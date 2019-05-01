#
# PySNMP MIB module Juniper-CLI-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-CLI-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Counter32, ObjectIdentity, Counter64, iso, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, MibIdentifier, TimeTicks, Bits, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "Counter64", "iso", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "MibIdentifier", "TimeTicks", "Bits", "ModuleIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniCliAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 6))
juniCliAgent.setRevisions(('2007-10-10 09:22', '2002-09-06 16:54', '2001-03-27 22:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniCliAgent.setRevisionsDescriptions(('Added the rsCliConfigurationTable. A script file transferred using JUNIPER-FILE-XFER-MIB can be applied using this table.', 'Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniCliAgent.setLastUpdated('200710100922Z')
if mibBuilder.loadTexts: juniCliAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniCliAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniCliAgent.setDescription('The agent capabilities definitions for the CLI component of the SNMP agent in the Juniper E-series family of products.')
juniCliAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliAgentV1 = juniCliAgentV1.setProductRelease('Version 1 of the CLI Security Management component of JUNOSe SNMP\n        agent.  This version of the CLI Security Management component is\n        supported in JUNOSe 1.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliAgentV1 = juniCliAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniCliAgentV1.setDescription('The MIB supported by the SNMP agent for the CLI Security Management application in JUNOSe.')
juniCliAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 6, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliAgentV2 = juniCliAgentV2.setProductRelease('Version 2 of the CLI component of JUNOSe SNMP agent.\n        This version of the CLI component is supported in JUNOSe 9.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliAgentV2 = juniCliAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniCliAgentV2.setDescription('The MIB supported by the JUNOSe SNMP agent for the CLI application.')
mibBuilder.exportSymbols("Juniper-CLI-CONF", juniCliAgent=juniCliAgent, juniCliAgentV2=juniCliAgentV2, PYSNMP_MODULE_ID=juniCliAgent, juniCliAgentV1=juniCliAgentV1)
