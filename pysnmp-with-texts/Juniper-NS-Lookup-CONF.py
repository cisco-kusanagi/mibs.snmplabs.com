#
# PySNMP MIB module Juniper-NS-Lookup-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-NS-Lookup-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, TimeTicks, Unsigned32, ObjectIdentity, Bits, Counter64, Counter32, Integer32, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "TimeTicks", "Unsigned32", "ObjectIdentity", "Bits", "Counter64", "Counter32", "Integer32", "MibIdentifier", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniNsLookupAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 27))
juniNsLookupAgent.setRevisions(('2002-09-06 16:54', '2001-03-28 22:22',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniNsLookupAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniNsLookupAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniNsLookupAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniNsLookupAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniNsLookupAgent.setDescription('The agent capabilities definitions for the remote name server (NS) lookup component of the SNMP agent in the Juniper E-series family of products.')
juniNsLookupAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 27, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniNsLookupAgentV1 = juniNsLookupAgentV1.setProductRelease('Version 1 of the NS Lookup component of the JUNOSe SNMP agent.  This\n        version of the NS Lookup component is supported in JUNOSe 3.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniNsLookupAgentV1 = juniNsLookupAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniNsLookupAgentV1.setDescription('The MIB supported by the SNMP agent for the NS Lookup application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-NS-Lookup-CONF", juniNsLookupAgentV1=juniNsLookupAgentV1, PYSNMP_MODULE_ID=juniNsLookupAgent, juniNsLookupAgent=juniNsLookupAgent)
