#
# PySNMP MIB module Juniper-TSM-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-TSM-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:04:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibIdentifier, TimeTicks, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Integer32, Gauge32, Unsigned32, Counter64, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "TimeTicks", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Integer32", "Gauge32", "Unsigned32", "Counter64", "Bits", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniTsmAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 67))
juniTsmAgent.setRevisions(('2003-10-27 22:50',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniTsmAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: juniTsmAgent.setLastUpdated('200310272250Z')
if mibBuilder.loadTexts: juniTsmAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniTsmAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniTsmAgent.setDescription('The agent capabilities definitions for the Terminal Server Management (TSM) component of the SNMP agent in the Juniper E-series family of products.')
juniTsmAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 67, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTsmAgentV1 = juniTsmAgentV1.setProductRelease('Version 1 of the Terminal Server Management (TSM) component of the\n        JUNOSe SNMP agent.  This version of the TSM component is supported in\n        JUNOSe 5.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTsmAgentV1 = juniTsmAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniTsmAgentV1.setDescription('The MIB supported by the JUNOSe SNMP agent for the TSM application.')
mibBuilder.exportSymbols("Juniper-TSM-CONF", PYSNMP_MODULE_ID=juniTsmAgent, juniTsmAgent=juniTsmAgent, juniTsmAgentV1=juniTsmAgentV1)
