#
# PySNMP MIB module Juniper-DS1-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DS1-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ObjectIdentity, Bits, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, MibIdentifier, ModuleIdentity, Integer32, TimeTicks, IpAddress, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Integer32", "TimeTicks", "IpAddress", "Counter32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniDs1Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 10))
juniDs1Agent.setRevisions(('2003-09-25 15:23', '2003-01-31 17:15', '2003-01-31 16:37', '2002-05-13 16:34', '2001-03-29 20:36',))
if mibBuilder.loadTexts: juniDs1Agent.setLastUpdated('200309251523Z')
if mibBuilder.loadTexts: juniDs1Agent.setOrganization('Juniper Networks, Inc.')
juniDs1AgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV1 = juniDs1AgentV1.setProductRelease('Version 1 of the DS1 component of the JUNOSe SNMP agent.  This version\n        of the DS1 component was supported in JUNOSe 1.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV1 = juniDs1AgentV1.setStatus('obsolete')
juniDs1AgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV2 = juniDs1AgentV2.setProductRelease('Version 2 of the DS1 component of the JUNOSe SNMP agent.  This version\n        of the DS1 component was supported in JUNOSe 1.1 thru JUNOSe 2.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV2 = juniDs1AgentV2.setStatus('obsolete')
juniDs1AgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV3 = juniDs1AgentV3.setProductRelease('Version 3 of the DS1 component of the JUNOSe SNMP agent.  This version\n        of the DS1 component was supported in JUNOSe 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV3 = juniDs1AgentV3.setStatus('obsolete')
juniDs1AgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV4 = juniDs1AgentV4.setProductRelease('Version 4 of the DS1 component of the JUNOSe SNMP agent.  This version\n        of the DS1 component was supported in JUNOSe 4.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV4 = juniDs1AgentV4.setStatus('obsolete')
juniDs1AgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV5 = juniDs1AgentV5.setProductRelease('Version 5 of the DS1 component of the JUNOSe SNMP agent.  This version\n        of the DS1 component is supported in JUNOSe 4.1 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV5 = juniDs1AgentV5.setStatus('current')
mibBuilder.exportSymbols("Juniper-DS1-CONF", PYSNMP_MODULE_ID=juniDs1Agent, juniDs1AgentV3=juniDs1AgentV3, juniDs1AgentV4=juniDs1AgentV4, juniDs1Agent=juniDs1Agent, juniDs1AgentV5=juniDs1AgentV5, juniDs1AgentV1=juniDs1AgentV1, juniDs1AgentV2=juniDs1AgentV2)
