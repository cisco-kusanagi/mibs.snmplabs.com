#
# PySNMP MIB module Juniper-Log-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Log-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
IpAddress, Gauge32, MibIdentifier, NotificationType, TimeTicks, iso, Unsigned32, ModuleIdentity, Integer32, Counter32, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "MibIdentifier", "NotificationType", "TimeTicks", "iso", "Unsigned32", "ModuleIdentity", "Integer32", "Counter32", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniLogAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 26))
juniLogAgent.setRevisions(('2002-09-06 16:54', '2001-03-28 22:07',))
if mibBuilder.loadTexts: juniLogAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniLogAgent.setOrganization('Juniper Networks, Inc.')
juniLogAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 26, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLogAgentV1 = juniLogAgentV1.setProductRelease('Version 1 of the logging managment component of the JUNOSe SNMP agent.\n        This version of the logging managment component was supported in JUNOSe\n        1.3 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLogAgentV1 = juniLogAgentV1.setStatus('obsolete')
juniLogAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 26, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLogAgentV2 = juniLogAgentV2.setProductRelease('Version 2 of the logging managment component of the JUNOSe SNMP agent.\n        This version of the logging managment component is supported in JUNOSe\n        2.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLogAgentV2 = juniLogAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-Log-CONF", PYSNMP_MODULE_ID=juniLogAgent, juniLogAgentV2=juniLogAgentV2, juniLogAgent=juniLogAgent, juniLogAgentV1=juniLogAgentV1)
