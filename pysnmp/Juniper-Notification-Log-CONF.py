#
# PySNMP MIB module Juniper-Notification-Log-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Notification-Log-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, Counter32, IpAddress, TimeTicks, iso, MibIdentifier, Counter64, Gauge32, Unsigned32, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Counter32", "IpAddress", "TimeTicks", "iso", "MibIdentifier", "Counter64", "Gauge32", "Unsigned32", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniNotificationLogAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 56))
juniNotificationLogAgent.setRevisions(('2002-09-06 16:54', '2002-03-25 18:22',))
if mibBuilder.loadTexts: juniNotificationLogAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniNotificationLogAgent.setOrganization('Juniper Networks, Inc.')
juniNotificationLogAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 56, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniNotificationLogAgentV1 = juniNotificationLogAgentV1.setProductRelease('Version 1 of the Notification Log component of the JUNOSe SNMP agent.\n        This version of the Notification Log component is supported in JUNOSe\n        4.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniNotificationLogAgentV1 = juniNotificationLogAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-Notification-Log-CONF", PYSNMP_MODULE_ID=juniNotificationLogAgent, juniNotificationLogAgent=juniNotificationLogAgent, juniNotificationLogAgentV1=juniNotificationLogAgentV1)
