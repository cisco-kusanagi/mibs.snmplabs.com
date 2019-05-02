#
# PySNMP MIB module Juniper-CBF-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-CBF-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Integer32, Counter64, ModuleIdentity, NotificationType, ObjectIdentity, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, MibIdentifier, TimeTicks, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "ModuleIdentity", "NotificationType", "ObjectIdentity", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "MibIdentifier", "TimeTicks", "Bits", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniCbfAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 48))
juniCbfAgent.setRevisions(('2002-09-06 16:54', '2001-03-29 20:23',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniCbfAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniCbfAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniCbfAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniCbfAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniCbfAgent.setDescription('The agent capabilities definitions for the Connection-Based Forwarding (CBF) protocol management component of the SNMP agent in the Juniper E-series family of products.')
juniCbfAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 48, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCbfAgentV1 = juniCbfAgentV1.setProductRelease('Version 1 of the Connection-Based Forwarding (CBF) component of the\n        JUNOSe SNMP agent.  This version of the CBF component is supported in\n        JUNOSe 3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCbfAgentV1 = juniCbfAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniCbfAgentV1.setDescription('The MIB supported by the SNMP agent for the CBF application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-CBF-CONF", juniCbfAgentV1=juniCbfAgentV1, PYSNMP_MODULE_ID=juniCbfAgent, juniCbfAgent=juniCbfAgent)
