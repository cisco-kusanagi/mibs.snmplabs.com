#
# PySNMP MIB module Juniper-RADIUS-Disconnect-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-RADIUS-Disconnect-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, Counter64, IpAddress, Integer32, TimeTicks, Unsigned32, Bits, MibIdentifier, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "IpAddress", "Integer32", "TimeTicks", "Unsigned32", "Bits", "MibIdentifier", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniRadiusDisconnectAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 63))
juniRadiusDisconnectAgent.setRevisions(('2003-01-13 21:45',))
if mibBuilder.loadTexts: juniRadiusDisconnectAgent.setLastUpdated('200301132145Z')
if mibBuilder.loadTexts: juniRadiusDisconnectAgent.setOrganization('Juniper Networks, Inc.')
juniRadiusDisconnectAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 63, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusDisconnectAgentV1 = juniRadiusDisconnectAgentV1.setProductRelease('Version 1 of the RADIUS Disconnect component of the JUNOSe SNMP agent.\n        This version of the RADIUS Disconnect component is supported in JUNOSe\n        5.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusDisconnectAgentV1 = juniRadiusDisconnectAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-RADIUS-Disconnect-CONF", juniRadiusDisconnectAgentV1=juniRadiusDisconnectAgentV1, PYSNMP_MODULE_ID=juniRadiusDisconnectAgent, juniRadiusDisconnectAgent=juniRadiusDisconnectAgent)
