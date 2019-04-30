#
# PySNMP MIB module Juniper-V35-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-V35-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:54:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Bits, Counter32, iso, NotificationType, Gauge32, Counter64, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, ModuleIdentity, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "iso", "NotificationType", "Gauge32", "Counter64", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "ModuleIdentity", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniV35Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 54))
juniV35Agent.setRevisions(('2002-09-06 16:54', '2002-01-25 21:43',))
if mibBuilder.loadTexts: juniV35Agent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniV35Agent.setOrganization('Juniper Networks, Inc.')
juniV35AgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 54, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniV35AgentV1 = juniV35AgentV1.setProductRelease('Version 1 of the X.21/V.35 component of the JUNOSe SNMP agent.  This\n        version of the X.21/V.35 component is supported in JUNOSe 4.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniV35AgentV1 = juniV35AgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-V35-CONF", juniV35Agent=juniV35Agent, PYSNMP_MODULE_ID=juniV35Agent, juniV35AgentV1=juniV35AgentV1)
