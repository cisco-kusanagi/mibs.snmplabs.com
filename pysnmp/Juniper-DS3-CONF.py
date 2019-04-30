#
# PySNMP MIB module Juniper-DS3-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DS3-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Counter64, Bits, TimeTicks, Integer32, NotificationType, ModuleIdentity, IpAddress, Counter32, Gauge32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "Integer32", "NotificationType", "ModuleIdentity", "IpAddress", "Counter32", "Gauge32", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniDs3Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11))
juniDs3Agent.setRevisions(('2003-09-29 21:05', '2003-01-30 19:08', '2003-01-30 16:37', '2002-08-27 18:48', '2001-04-18 19:41',))
if mibBuilder.loadTexts: juniDs3Agent.setLastUpdated('200309292105Z')
if mibBuilder.loadTexts: juniDs3Agent.setOrganization('Juniper Networks, Inc.')
juniDs3AgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV1 = juniDs3AgentV1.setProductRelease('Version 1 of the DS3 component of the JUNOSe SNMP agent.  This version\n        of the DS3 component was supported in JUNOSe 1.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV1 = juniDs3AgentV1.setStatus('obsolete')
juniDs3AgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV2 = juniDs3AgentV2.setProductRelease('Version 2 of the DS3 component of the JUNOSe SNMP agent.  This version\n        of the DS3 component was supported in JUNOSe 1.1 thru JUNOSe 2.5 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV2 = juniDs3AgentV2.setStatus('obsolete')
juniDs3AgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV3 = juniDs3AgentV3.setProductRelease('Version 3 of the DS3 component of the JUNOSe SNMP agent.  This version\n        of the DS3 component was supported in JUNOSe 2.6 and subsequent JUNOSe\n        2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV3 = juniDs3AgentV3.setStatus('obsolete')
juniDs3AgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV4 = juniDs3AgentV4.setProductRelease('Version 4 of the DS3 component of the JUNOSe SNMP agent.  This version\n        of the DS3 component was supported in JUNOSe 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV4 = juniDs3AgentV4.setStatus('obsolete')
juniDs3AgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV5 = juniDs3AgentV5.setProductRelease('Version 5 of the DS3 component of the JUNOSe SNMP agent.  This version\n        of the DS3 component was supported in JUNOSe 4.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV5 = juniDs3AgentV5.setStatus('obsolete')
juniDs3AgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV6 = juniDs3AgentV6.setProductRelease('Version 6 of the DS3 component of the JUNOSe SNMP agent.  This version\n        of the DS3 component is supported in JUNOSe 4.1 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV6 = juniDs3AgentV6.setStatus('current')
mibBuilder.exportSymbols("Juniper-DS3-CONF", juniDs3Agent=juniDs3Agent, juniDs3AgentV5=juniDs3AgentV5, juniDs3AgentV2=juniDs3AgentV2, juniDs3AgentV6=juniDs3AgentV6, juniDs3AgentV3=juniDs3AgentV3, PYSNMP_MODULE_ID=juniDs3Agent, juniDs3AgentV1=juniDs3AgentV1, juniDs3AgentV4=juniDs3AgentV4)
