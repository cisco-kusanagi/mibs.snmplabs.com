#
# PySNMP MIB module Juniper-Notification-Log-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Notification-Log-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, NotificationType, TimeTicks, iso, Counter64, Gauge32, MibIdentifier, ObjectIdentity, IpAddress, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "NotificationType", "TimeTicks", "iso", "Counter64", "Gauge32", "MibIdentifier", "ObjectIdentity", "IpAddress", "Bits", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniNotificationLogAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 56))
juniNotificationLogAgent.setRevisions(('2002-09-06 16:54', '2002-03-25 18:22',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniNotificationLogAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniNotificationLogAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniNotificationLogAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniNotificationLogAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniNotificationLogAgent.setDescription('The agent capabilities definitions for the Notification Log component of the SNMP agent in the Juniper E-series family of products.')
juniNotificationLogAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 56, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniNotificationLogAgentV1 = juniNotificationLogAgentV1.setProductRelease('Version 1 of the Notification Log component of the JUNOSe SNMP agent.\n        This version of the Notification Log component is supported in JUNOSe\n        4.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniNotificationLogAgentV1 = juniNotificationLogAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniNotificationLogAgentV1.setDescription('The MIB supported by the SNMP agent for the Notification Log application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Notification-Log-CONF", PYSNMP_MODULE_ID=juniNotificationLogAgent, juniNotificationLogAgentV1=juniNotificationLogAgentV1, juniNotificationLogAgent=juniNotificationLogAgent)
