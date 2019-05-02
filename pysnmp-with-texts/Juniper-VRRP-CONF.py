#
# PySNMP MIB module Juniper-VRRP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-VRRP-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:04:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Bits, MibIdentifier, Gauge32, TimeTicks, ObjectIdentity, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Bits", "MibIdentifier", "Gauge32", "TimeTicks", "ObjectIdentity", "IpAddress", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniVrrpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 53))
juniVrrpAgent.setRevisions(('2002-09-06 16:54', '2002-01-24 15:20',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniVrrpAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniVrrpAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniVrrpAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniVrrpAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniVrrpAgent.setDescription('The agent capabilities definitions for the Virtual Router Redundancy Protocol (VRRP) component of the SNMP agent in the Juniper E-series family of products.')
juniVrrpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 53, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniVrrpAgentV1 = juniVrrpAgentV1.setProductRelease('Version 1 of the VRRP component of the JUNOSe SNMP agent.  This version\n        of the VRRP component is supported in JUNOSe 3.4 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniVrrpAgentV1 = juniVrrpAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniVrrpAgentV1.setDescription('The MIB supported by the SNMP agent for the VRRP application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-VRRP-CONF", PYSNMP_MODULE_ID=juniVrrpAgent, juniVrrpAgentV1=juniVrrpAgentV1, juniVrrpAgent=juniVrrpAgent)
