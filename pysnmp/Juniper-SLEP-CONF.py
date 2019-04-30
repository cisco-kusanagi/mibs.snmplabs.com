#
# PySNMP MIB module Juniper-SLEP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-SLEP-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Counter32, ObjectIdentity, MibIdentifier, ModuleIdentity, Bits, Gauge32, Counter64, iso, IpAddress, Integer32, Unsigned32, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Bits", "Gauge32", "Counter64", "iso", "IpAddress", "Integer32", "Unsigned32", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniSlepAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 38))
juniSlepAgent.setRevisions(('2003-09-10 21:27', '2002-12-23 20:40', '2001-03-30 14:15',))
if mibBuilder.loadTexts: juniSlepAgent.setLastUpdated('200309102127Z')
if mibBuilder.loadTexts: juniSlepAgent.setOrganization('Juniper Networks, Inc.')
juniSlepAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 38, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSlepAgentV1 = juniSlepAgentV1.setProductRelease('Version 1 of the SLEP component of the JUNOSe SNMP agent.  This version\n        of the SLEP component was supported in JUNOSe 1.3 thru 3.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSlepAgentV1 = juniSlepAgentV1.setStatus('current')
juniSlepAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 38, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSlepAgentV2 = juniSlepAgentV2.setProductRelease('Version 2 of the SLEP component of the JUNOSe SNMP agent.  This version\n        of the SLEP component is supported in JUNOSe 3.1 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSlepAgentV2 = juniSlepAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-SLEP-CONF", juniSlepAgentV1=juniSlepAgentV1, juniSlepAgent=juniSlepAgent, PYSNMP_MODULE_ID=juniSlepAgent, juniSlepAgentV2=juniSlepAgentV2)
