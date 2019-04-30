#
# PySNMP MIB module Juniper-RADIUS-Proxy-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-RADIUS-Proxy-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, Integer32, ObjectIdentity, Unsigned32, Gauge32, Bits, ModuleIdentity, MibIdentifier, iso, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "Integer32", "ObjectIdentity", "Unsigned32", "Gauge32", "Bits", "ModuleIdentity", "MibIdentifier", "iso", "NotificationType", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniRadiusProxyAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 68))
juniRadiusProxyAgent.setRevisions(('2004-01-23 19:16',))
if mibBuilder.loadTexts: juniRadiusProxyAgent.setLastUpdated('200401231916Z')
if mibBuilder.loadTexts: juniRadiusProxyAgent.setOrganization('Juniper Networks, Inc.')
juniRadiusProxyAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 68, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusProxyAgentV1 = juniRadiusProxyAgentV1.setProductRelease('Version 1 of the RADIUS Proxy component of the JUNOSe SNMP agent.  This\n        version of the RADIUS Proxy component is supported in JUNOSe 6.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusProxyAgentV1 = juniRadiusProxyAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-RADIUS-Proxy-CONF", juniRadiusProxyAgent=juniRadiusProxyAgent, PYSNMP_MODULE_ID=juniRadiusProxyAgent, juniRadiusProxyAgentV1=juniRadiusProxyAgentV1)
