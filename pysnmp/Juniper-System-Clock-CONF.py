#
# PySNMP MIB module Juniper-System-Clock-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-System-Clock-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ObjectIdentity, TimeTicks, MibIdentifier, NotificationType, IpAddress, Bits, iso, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "MibIdentifier", "NotificationType", "IpAddress", "Bits", "iso", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "Counter32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniSysClockAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 52))
juniSysClockAgent.setRevisions(('2005-12-14 14:01', '2003-09-15 14:03', '2003-09-12 14:39', '2002-04-04 18:47',))
if mibBuilder.loadTexts: juniSysClockAgent.setLastUpdated('200512141401Z')
if mibBuilder.loadTexts: juniSysClockAgent.setOrganization('Juniper Networks, Inc.')
juniSysClockAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 52, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSysClockAgentV1 = juniSysClockAgentV1.setProductRelease('Version 1 of the system clock component of the JUNOSe SNMP agent.  This\n        version of the system clock component was supported in JUNOSe 4.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSysClockAgentV1 = juniSysClockAgentV1.setStatus('obsolete')
juniSysClockAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 52, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSysClockAgentV2 = juniSysClockAgentV2.setProductRelease('Version 2 of the system clock component of the JUNOSe SNMP agent.  This\n        version of the system clock component was supported in early JUNOSe 4.1\n        and 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSysClockAgentV2 = juniSysClockAgentV2.setStatus('obsolete')
juniSysClockAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 52, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSysClockAgentV3 = juniSysClockAgentV3.setProductRelease('Version 3 of the system clock component of the JUNOSe SNMP agent.  This\n        version of the system clock component is supported in JUNOSe 4.1.2,\n        5.0.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSysClockAgentV3 = juniSysClockAgentV3.setStatus('obsolete')
juniSysClockAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 52, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSysClockAgentV4 = juniSysClockAgentV4.setProductRelease('Version 4 of the system clock component of the JUNOSe SNMP agent.  This\n        version of the system clock component is supported in JUNOSe 7.0 and \n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSysClockAgentV4 = juniSysClockAgentV4.setStatus('current')
mibBuilder.exportSymbols("Juniper-System-Clock-CONF", juniSysClockAgentV3=juniSysClockAgentV3, juniSysClockAgent=juniSysClockAgent, juniSysClockAgentV2=juniSysClockAgentV2, PYSNMP_MODULE_ID=juniSysClockAgent, juniSysClockAgentV4=juniSysClockAgentV4, juniSysClockAgentV1=juniSysClockAgentV1)
