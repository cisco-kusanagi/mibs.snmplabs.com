#
# PySNMP MIB module Juniper-CBF-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-CBF-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
IpAddress, MibIdentifier, Counter32, ModuleIdentity, Counter64, Unsigned32, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, TimeTicks, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Counter32", "ModuleIdentity", "Counter64", "Unsigned32", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "TimeTicks", "NotificationType", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniCbfAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 48))
juniCbfAgent.setRevisions(('2002-09-06 16:54', '2001-03-29 20:23',))
if mibBuilder.loadTexts: juniCbfAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniCbfAgent.setOrganization('Juniper Networks, Inc.')
juniCbfAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 48, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCbfAgentV1 = juniCbfAgentV1.setProductRelease('Version 1 of the Connection-Based Forwarding (CBF) component of the\n        JUNOSe SNMP agent.  This version of the CBF component is supported in\n        JUNOSe 3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCbfAgentV1 = juniCbfAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-CBF-CONF", juniCbfAgentV1=juniCbfAgentV1, juniCbfAgent=juniCbfAgent, PYSNMP_MODULE_ID=juniCbfAgent)
