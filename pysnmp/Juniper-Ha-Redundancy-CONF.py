#
# PySNMP MIB module Juniper-Ha-Redundancy-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Ha-Redundancy-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, Gauge32, Integer32, ObjectIdentity, MibIdentifier, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Bits, Counter32, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "Integer32", "ObjectIdentity", "MibIdentifier", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Bits", "Counter32", "Unsigned32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniHaRedundancyAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 69))
juniHaRedundancyAgent.setRevisions(('2004-02-02 16:46',))
if mibBuilder.loadTexts: juniHaRedundancyAgent.setLastUpdated('200402021646Z')
if mibBuilder.loadTexts: juniHaRedundancyAgent.setOrganization('Juniper Networks, Inc.')
juniHaRedundancyAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 69, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHaRedundancyAgentV1 = juniHaRedundancyAgentV1.setProductRelease('Version 1 of the Ha Redundancy component of the JUNOSe SNMP agent.\n        This version of the Ha Redundancy component is supported in JUNOSe 6.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHaRedundancyAgentV1 = juniHaRedundancyAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-Ha-Redundancy-CONF", PYSNMP_MODULE_ID=juniHaRedundancyAgent, juniHaRedundancyAgent=juniHaRedundancyAgent, juniHaRedundancyAgentV1=juniHaRedundancyAgentV1)
