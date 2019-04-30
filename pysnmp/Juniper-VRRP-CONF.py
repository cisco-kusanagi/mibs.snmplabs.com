#
# PySNMP MIB module Juniper-VRRP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-VRRP-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:54:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
ModuleIdentity, TimeTicks, Gauge32, Bits, Counter32, IpAddress, Unsigned32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Gauge32", "Bits", "Counter32", "IpAddress", "Unsigned32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniVrrpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 53))
juniVrrpAgent.setRevisions(('2002-09-06 16:54', '2002-01-24 15:20',))
if mibBuilder.loadTexts: juniVrrpAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniVrrpAgent.setOrganization('Juniper Networks, Inc.')
juniVrrpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 53, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniVrrpAgentV1 = juniVrrpAgentV1.setProductRelease('Version 1 of the VRRP component of the JUNOSe SNMP agent.  This version\n        of the VRRP component is supported in JUNOSe 3.4 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniVrrpAgentV1 = juniVrrpAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-VRRP-CONF", juniVrrpAgentV1=juniVrrpAgentV1, PYSNMP_MODULE_ID=juniVrrpAgent, juniVrrpAgent=juniVrrpAgent)
