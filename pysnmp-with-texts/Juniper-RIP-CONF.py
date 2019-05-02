#
# PySNMP MIB module Juniper-RIP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-RIP-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:04:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, ObjectIdentity, Gauge32, Unsigned32, Integer32, Bits, Counter64, TimeTicks, Counter32, ModuleIdentity, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "ObjectIdentity", "Gauge32", "Unsigned32", "Integer32", "Bits", "Counter64", "TimeTicks", "Counter32", "ModuleIdentity", "iso", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniRipAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 36))
juniRipAgent.setRevisions(('2002-09-06 16:54', '2001-03-29 18:13',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniRipAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniRipAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniRipAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniRipAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniRipAgent.setDescription('The agent capabilities definitions for the Routing Information Protocol (RIP) component of the SNMP agent in the Juniper E-series family of products.')
juniRipAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 36, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRipAgentV1 = juniRipAgentV1.setProductRelease('Version 1 of the RIP component of the JUNOSe SNMP agent.  This version\n        of the RIP component is supported in JUNOSe 1.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRipAgentV1 = juniRipAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniRipAgentV1.setDescription('The MIB supported by the SNMP agent for the RIP application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-RIP-CONF", juniRipAgent=juniRipAgent, juniRipAgentV1=juniRipAgentV1, PYSNMP_MODULE_ID=juniRipAgent)
