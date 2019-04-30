#
# PySNMP MIB module Juniper-NS-Lookup-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-NS-Lookup-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Counter32, IpAddress, ObjectIdentity, Gauge32, MibIdentifier, iso, ModuleIdentity, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Counter32", "IpAddress", "ObjectIdentity", "Gauge32", "MibIdentifier", "iso", "ModuleIdentity", "Unsigned32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniNsLookupAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 27))
juniNsLookupAgent.setRevisions(('2002-09-06 16:54', '2001-03-28 22:22',))
if mibBuilder.loadTexts: juniNsLookupAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniNsLookupAgent.setOrganization('Juniper Networks, Inc.')
juniNsLookupAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 27, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniNsLookupAgentV1 = juniNsLookupAgentV1.setProductRelease('Version 1 of the NS Lookup component of the JUNOSe SNMP agent.  This\n        version of the NS Lookup component is supported in JUNOSe 3.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniNsLookupAgentV1 = juniNsLookupAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-NS-Lookup-CONF", juniNsLookupAgent=juniNsLookupAgent, juniNsLookupAgentV1=juniNsLookupAgentV1, PYSNMP_MODULE_ID=juniNsLookupAgent)
