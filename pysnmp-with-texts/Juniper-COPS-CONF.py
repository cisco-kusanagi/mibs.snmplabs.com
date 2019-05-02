#
# PySNMP MIB module Juniper-COPS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-COPS-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, NotificationType, MibIdentifier, Counter32, ObjectIdentity, Unsigned32, Counter64, Gauge32, Bits, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "NotificationType", "MibIdentifier", "Counter32", "ObjectIdentity", "Unsigned32", "Counter64", "Gauge32", "Bits", "iso", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniCopsAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 7))
juniCopsAgent.setRevisions(('2002-09-06 16:54', '2002-01-14 19:36', '2001-03-27 22:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniCopsAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'Added support for the local address and transport router name objects.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniCopsAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniCopsAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniCopsAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniCopsAgent.setDescription('The agent capabilities definitions for the Common Open Policy Service (COPS) Protocol management component of the SNMP agent in the Juniper E-series family of products.')
juniCopsAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 7, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCopsAgentV1 = juniCopsAgentV1.setProductRelease('Version 1 of the COPS component of the JUNOSe SNMP agent.  This version\n        of the COPS component was supported in JUNOSe 2.x and 3.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCopsAgentV1 = juniCopsAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniCopsAgentV1.setDescription('The MIB supported by the SNMP agent for the COPS application in JUNOSe. These capabilities became obsolete when the local address and transport router name objects were add.')
juniCopsAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 7, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCopsAgentV2 = juniCopsAgentV2.setProductRelease('Version 2 of the COPS component of the JUNOSe SNMP agent.  This version\n        of the COPS component is supported in JUNOSe 4.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCopsAgentV2 = juniCopsAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniCopsAgentV2.setDescription('The MIB supported by the SNMP agent for the COPS application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-COPS-CONF", juniCopsAgent=juniCopsAgent, juniCopsAgentV1=juniCopsAgentV1, juniCopsAgentV2=juniCopsAgentV2, PYSNMP_MODULE_ID=juniCopsAgent)
